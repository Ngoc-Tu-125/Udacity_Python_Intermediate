"""Web application to generate meme."""

import random
import os
import requests
from flask import Flask, render_template, request

from meme_generation.meme_engine import MemeEngine
from quote_engine.ingestor import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes = []

    for file in quote_files:
        quotes += Ingestor.parse(file)

    images_path = "./_data/photos/dog/"

    # images within the images images_path directory
    imgs = []

    for file in os.listdir(images_path):
        if file.endswith('.jpg'):
            imgs.append(os.path.join(images_path, file))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    if not request.form["image_url"]:
        return render_template('meme_form.html')

    image_url = request.form["image_url"]

    try:
        reader = requests.get(image_url, timeout=5, verify=False)
        tmp_image = 'tmp_image.jpg'
        with open(tmp_image, 'wb') as img:
            img.write(reader.content)

        quote_body = request.form["body"]
        author = request.form["author"]

        path = meme.make_meme(tmp_image, quote_body, author)

        os.remove(tmp_image)

        return render_template('meme.html', path=path)
    except:
        return render_template('meme_error.html')


if __name__ == "__main__":
    app.run()
