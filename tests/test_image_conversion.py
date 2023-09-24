import unittest
from image_processing.image_conversion import create_mask, change_image_shape
from PIL import Image
import os
import numpy as np

"""
Author: Omar CHICHAOUI
email: omar.chichaoui@gmail.com
Date: September 24, 2023
"""

class TestImageManipulation(unittest.TestCase):

    def test_create_mask(self):
        # Test the create_mask function
        size = (100, 100)
        circle_mask = create_mask('circle', size)
        self.assertIsInstance(circle_mask, Image.Image)

        square_mask = create_mask('square', size)
        self.assertIsInstance(square_mask, Image.Image)

        triangle_mask = create_mask('triangle', size)
        self.assertIsInstance(triangle_mask, Image.Image)

    def test_change_image_shape(self):
        # Test the change_image_shape function
        input_image_path = "./test_resources/output_files/dummy-badge.png"

        # Test changing the shape to a circle
        output_path_circle = change_image_shape(input_image_path, 'circle')
        self.assertTrue(os.path.exists(output_path_circle))

        # Test changing the shape to a square
        output_path_square = change_image_shape(input_image_path, 'square')
        self.assertTrue(os.path.exists(output_path_square))

        # Test changing the shape to a triangle
        output_path_triangle = change_image_shape(input_image_path, 'triangle')
        self.assertTrue(os.path.exists(output_path_triangle))

        # Clean up test files
        # os.remove(input_image_path)
        # os.remove(output_path_circle)
        # os.remove(output_path_square)
        # os.remove(output_path_triangle)

if __name__ == '__main__':
    unittest.main()