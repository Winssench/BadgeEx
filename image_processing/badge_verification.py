from PIL import Image, ImageDraw
import numpy as np

"""
Author: Omar CHICHAOUI
Date: September 24, 2023
Description: This is a Python script to verify badges.
"""


def is_pastel_color(rgb):
    """
    Check if an RGB color is within the pastel color range.

    Parameters:
        rgb (tuple): A tuple containing three integers representing the RGB values (red, green, blue)
                     of the color to be checked.

    Returns:
        bool: True if the color is pastel; False otherwise.

    This function checks if the given RGB color is within the pastel color range (considered to give positive feeling)
    typically characterized by having high values for all three color channels (red, green, blue).
    """
    # Check if the RGB color is within the pastel range
    r, g, b = rgb
    return r >= 200 and g >= 200 and b >= 200

def get_median_color(image):
    """
    Calculate the median color of an image.

    Parameters:
        image (PIL.Image.Image): The input image for which the median color will be calculated.

    Returns:
        tuple: A tuple containing the RGB values of the median color.

    This function calculates the median color of the provided image by averaging the RGB values
    of all the pixels in the image.

    """
    # Get a list of all pixel colors in the image
    pixels = list(image.getdata())

    # Calculate the median color
    num_pixels = len(pixels)
    r_median = sum(pixel[0] for pixel in pixels) // num_pixels
    g_median = sum(pixel[1] for pixel in pixels) // num_pixels
    b_median = sum(pixel[2] for pixel in pixels) // num_pixels

    return (r_median, g_median, b_median)

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

            mask_colors = []
            # Check if there are any non-transparent pixels outside the circle on the original image
            for x in range(512):
                for y in range(512):
                    pixel = img.getpixel((x, y))
                    alpha = pixel[3]
                    if alpha != 0 and mask.getpixel((x, y)) == 0:
                        return "Non-transparent pixels are not within a circle"
                    if alpha != 0 and mask.getpixel((x, y)) != 0:
                        mask_colors.append(pixel[:3])

            # Calculate the median color of pixels inside the circular mask
            if mask_colors:
                median_color = np.median(mask_colors, axis=0)
                
                # Check if the median color is pastel
                if not is_pastel_color(median_color):
                    return "Colors are not pastel"

            return "Badge is valid"


    except Exception as e:
        return f"Error: {str(e)}"