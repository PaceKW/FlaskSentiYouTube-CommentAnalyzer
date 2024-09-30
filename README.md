# YouTube Comments Sentiment Analysis with Flask and SentiWordNet

## Example/GIF Demonstration
![Demo GIF](images/Demo.gif)

## Description
This project is a **YouTube Comment Sentiment Analysis** application developed using **Flask** and **NLTK**. The application analyzes the sentiment of comments on YouTube videos and provides insights into viewer opinions.

## Features
- Extracts comments from YouTube videos using the **YouTube API**.
- Analyzes sentiment of comments (Positive, Negative, Neutral) using **SentiWordNet**.
- User-friendly interface built with **Bootstrap** for responsiveness and elegance.
- Visualizes sentiment analysis results with **Chart.js**.

## Technologies Used
- **Flask**: A lightweight WSGI web application framework.
- **NLTK**: Natural Language Toolkit for text processing.
- **SentiWordNet**: For sentiment analysis of words.
- **google-api-python-client**: To interact with the YouTube API.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Chart.js**: For visualizing data.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create a virtual environment (if you haven't already):
    ```bash
    python -m venv .venv
    ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a ```.env``` file in the root directory and add your YouTube API key:
    ```bash
    API_KEY=your_youtube_api_key
    ```

## Usage
Run the application:
```bash
flask run
```
Visit `http://127.0.0.1:5000` in your web browser.

