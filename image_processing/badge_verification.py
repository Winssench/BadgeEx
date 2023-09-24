"""
Author: Omar CHICHAOUI
Date: September 24, 2023
Description: This is a Python script to verify badges.
"""
from PIL import Image, ImageDraw
import numpy as np



def is_pastel_color(rgb):
    # Check if the RGB color is within the pastel range
    r, g, b = rgb
    return r >= 200 and g >= 200 and b >= 200

def verify_badge(image_path):
    """
    Verify a badge image.

    Parameters:
        image_path (str): The path to the badge image file to be verified.

    Returns:
        str: A string describing the verification result.

    This function verifies the specified badge image to ensure it meets certain criteria.
    - `image_path` should be the path to the badge image file you want to verify.

    The function returns a string describing the verification result, which can be one of the following:
    - "Image size is not 512x512" if the image size is incorrect.

    Example:
    result = verify_badge("valid-badge.png")
    print(result)  # Outputs: "Badge is valid"
    """

    try:
        # Open the image
        with Image.open(image_path) as img:
        
            # Verify size (512x512)
            if img.size != (512, 512):
                return "Image size is not 512x512"

            # Create a mask for the circular region

            mask = Image.new('L', img.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 512, 512), fill=255)

            # Check if there are any non-transparent pixels outside the circle on the original image
            for x in range(512):
                for y in range(512):
                    pixel = img.getpixel((x, y))
                    alpha = pixel[3]
                    if alpha != 0 and mask.getpixel((x, y)) == 0:
                        return "Non-transparent pixels are not within a circle"
                    if alpha != 0 and not is_pastel_color(pixel[:3]):
                        return "Colors are not pastel"

            return "Badge is valid"


    except Exception as e:
        return f"Error: {str(e)}"