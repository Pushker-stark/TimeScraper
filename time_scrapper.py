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
        # print(soup)
        title=soup.find_all(attrs={'class':'most-popular-feed__item-headline'})
        links=soup.find_all('a').href
        print(title)
        print(links)
        
        return jsonify(stories)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
