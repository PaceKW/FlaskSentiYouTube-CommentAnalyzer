document.addEventListener('DOMContentLoaded', function() {
    const sentimentCounts = {{ sentiment_counts|tojson }};
    console.log(sentimentCounts); // Debugging
    const ctx = document.getElementById('sentimentChart').getContext('2d');

    const sentimentChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(sentimentCounts),
            datasets: [{
                label: 'Jumlah Komentar',
                data: Object.values(sentimentCounts),
                backgroundColor: ['#66b3ff', '#99ff99', '#ff9999'],
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
