"""
Author: Omar CHICHAOUI
Date: September 24, 2023
Description: This is a Python script to verify badges.
"""
from PIL import Image, ImageDraw
import numpy as np


def create_mask(shape, size):
    # Create a mask image based on the specified shape
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    
    if shape == 'circle':
        # Draw a circular mask
        draw.ellipse((0, 0, size[0], size[1]), fill=255)
    elif shape == 'square':
        # Draw a square mask
        draw.rectangle((0, 0, size[0], size[1]), fill=255)
    elif shape == 'triangle':
        # Draw a triangular mask
        draw.polygon([(0, size[1]), (size[0] / 2, 0), (size[0], size[1])], fill=255)
    
    return mask


def change_image_shape(input_image_path, shape):
    """
    Change the shape of an image using a mask.

    Parameters:
        input_image_path (str): The path to the input image.
        shape (str): The desired shape ('circle' or 'square').

    Returns:
        str: The path to the transformed image.
    """
    try:
        # should be able to handle a wide range of image formats supported by the Pillow (PIL) 
        # for more information https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
        img = Image.open(input_image_path)
        
        # Create a mask based on the specified shape
        mask = create_mask(shape, img.size)

        # Apply the mask to the input image
        result = Image.new("RGBA", img.size)
        result.paste(img, mask=mask)

        # Define the output path and save the transformed image
        output_image_path = input_image_path.replace(".png", f"_{shape}_transformed.png")
        result.save(output_image_path)

        return output_image_path

    except Exception as e:
        return f"Error: {str(e)}"