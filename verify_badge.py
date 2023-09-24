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
            mask.save("sakoch.png")

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



    

#invalid_image = 'violation4.png'

#result_invalid = verify_badge(invalid_image)
#print(f"Verification result for {invalid_image}: {result_invalid}")





# Example usage
input_image_path = "leo_512x512.png"  # Replace with the path to your input image
output_image_path_circle = change_image_shape(input_image_path, 'circle')
output_image_path_square = change_image_shape(input_image_path, 'triangle')

print(f"Circle shape transformation saved as: {output_image_path_circle}")
print(f"Square shape transformation saved as: {output_image_path_square}")





