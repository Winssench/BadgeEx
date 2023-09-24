"""
Author: Omar CHICHAOUI
Date: September 24, 2023
Description: This is a Python script to verify badges.
"""
from PIL import Image, ImageDraw

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
        img = Image.open(image_path)

        # Verify size (512x512)
        if img.size != (512, 512):
            return "Image size is not 512x512"


        # Check if the non-transparent pixels are within a circle
   

        # Color analysis (define your criteria for "happy" colors)
        # You can use the Image.getpixel() method to analyze individual pixels

        return "Badge is valid"

    except Exception as e:
        return f"Error: {str(e)}"



invalid_image = 'invalid_badge.png'
# Verify an invalid badge image
result_invalid = verify_badge(invalid_image)
print(f"Verification result for {invalid_image}: {result_invalid}")
