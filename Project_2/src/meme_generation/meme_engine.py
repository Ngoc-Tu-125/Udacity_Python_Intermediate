"""Meme Engine."""

import os
import random
import textwrap
from PIL import Image, ImageFont, ImageDraw
from utils.exceptions import ImagePathError, SizeImageError


class MemeEngine:
    """Meme Engine defination."""

    def __init__(self, out_dir: str) -> None:
        """Init."""
        self.out_dir = out_dir
        self.count = 0
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

    def make_meme(
            self, img: str, body: str, quote_author: str, width: int = 500
            ) -> str:
        """Make meme."""
        # output file
        self.count = random.choice(range(0, 10000000))
        out_file = os.path.join(
            self.out_dir, 'meme_' + str(self.count) + '.jpg'
        )
        # Read image
        try:
            with Image.open(img) as image:
                # Get origin image size
                or_img_width, or_img_height = image.size
                height = 0
                if width <= 500:
                    height = int((width / or_img_width) * or_img_height)
                else:
                    raise SizeImageError('Width of image less than 500')

                # Resize image
                image = image.resize((width, height))

                # Set font size of txt
                font_size = int(height / 15)
                # Set position of txt
                x_pos = random.choice(range(0, int(width/5)))
                y_pos = random.choice(range(0, int(height/5)))
                # Draw meme
                font_txt = ImageFont.truetype("./_data/arial.ttf", font_size)
                draw_meme = ImageDraw.Draw(image)
                # Just about 30 character in a line
                wrapped_body = textwrap.fill(body, width=35)
                multi_line_needed = 1 + len(body)/35
                draw_meme.text(
                    (x_pos, y_pos),
                    wrapped_body,
                    font=font_txt,
                    fill=(0, 0, 0)
                )
                draw_meme.text(
                    (x_pos*1.5, y_pos+multi_line_needed*font_size),
                    ' - ' + quote_author,
                    font=font_txt,
                    fill=(0, 0, 0)
                )

                # Save image
                image.save(out_file)
        except ImagePathError:
            raise ImagePathError("Image path wrong!")

        return out_file
