import re
import nltk
from flask import Flask, render_template, request
from googleapiclient.discovery import build
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from dotenv import load_dotenv
import os

# Unduh data yang diperlukan dari NLTK
nltk.download('wordnet')
nltk.download('sentiwordnet')

# Memuat variabel lingkungan dari file .env
load_dotenv()

app = Flask(__name__)

# Mengambil API Key dari variabel lingkungan
api_key = os.getenv('API_KEY')

# Membangun objek YouTube
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_id(url):
    # Regex untuk mengekstrak video ID dari URL YouTube
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', url)
    return match.group(1) if match else None

def get_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText',
        maxResults=100
    )
    response = request.execute()

    for item in response.get('items', []):
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments

def get_sentiment_score(word):
    synsets = wn.synsets(word)
    score = 0.0
    count = 0

    for synset in synsets:
        senti_synset = swn.senti_synset(synset.name())
        score += senti_synset.pos_score() - senti_synset.neg_score()
        count += 1

    return score / count if count > 0 else 0

def analyze_sentiment(comment):
    words = comment.split()
    total_score = 0

    for word in words:
        score = get_sentiment_score(word)
        total_score += score
        
    if total_score > 0:
        return 'Positif'
    elif total_score < 0:
        return 'Negatif'
    else:
        return 'Netral'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = get_video_id(video_url)
        
        if not video_id:
            return render_template('index.html', analyzed_comments=None, sentiment_counts=None)

        comments = get_comments(video_id)

        # Hitung jumlah komentar berdasarkan label
        sentiment_counts = {'Positif': 0, 'Negatif': 0, 'Netral': 0}
        analyzed_comments = [(comment, analyze_sentiment(comment)) for comment in comments]

        for _, label in analyzed_comments:
            sentiment_counts[label] += 1

        return render_template('index.html', analyzed_comments=analyzed_comments, sentiment_counts=sentiment_counts, video_id=video_id)

    return render_template('index.html', analyzed_comments=None, sentiment_counts=None)

if __name__ == '__main__':
    app.run(debug=True)
