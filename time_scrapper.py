from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getTimeStories', methods=['GET'])
def get_time_stories():
    try:
        url = 'https://time.com'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        stories = []
        
        anchors = soup.find_all('a', attrs={'data-article-id': True})
        
        for anchor in anchors:
            link = anchor['href']
            title = anchor.find('h3', class_='most-popular-feed__item-headline').get_text(strip=True)
            stories.append({'title': title, 'link': link})

        print(stories)
        return jsonify(stories)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
