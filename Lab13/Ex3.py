# Create a Flask app to retrieve memes from website

from flask import Flask, render_template, request, redirect, url_for

import requests

url = "https://meme-api.com/gimme/wholesomememes"

app = Flask(__name__)
@app.route('/')

def home():
    response = requests.request("GET", url)
    data = response.json()
    meme_url = data["url"]
    title = data["title"]
    subreddit = data["subreddit"]

    # Fix: ensure full URL
    post_link = data["postLink"]

    return render_template(
        'memes.html',
        meme_url=meme_url,
        title=title,
        post_link=post_link,
        subreddit=subreddit
    )

if __name__ == "__main__":
    app.run(debug=True)