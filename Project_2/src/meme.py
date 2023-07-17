"""Meme generation by CLI."""

import os
import random
import argparse

from quote_engine.quote_model import QuoteModel
from quote_engine.ingestor import Ingestor
from meme_generation.meme_engine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


def parse_arguments() -> argparse.Namespace:
    """Parse arguments from CLI."""
    # Create the argument parser
    parser = argparse.ArgumentParser()

    # Add the optional arguments
    parser.add_argument("--body", help="string quote body")
    parser.add_argument("--author", help="string quote author")
    parser.add_argument("--path", help="image path")

    cl_args = parser.parse_args()

    return cl_args


if __name__ == "__main__":
    args = parse_arguments()
    print(generate_meme(args.path, args.body, args.author))
