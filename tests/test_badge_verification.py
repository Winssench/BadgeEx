import unittest
from image_processing.badge_verification import verify_badge


"""
Author: Omar CHICHAOUI
email: omar.chichaoui@gmail.com
Date: September 24, 2023
"""

class TestVerificationBadge(unittest.TestCase):

    def test_valid_badge(self):
        # Test verification of a valid badge
        image_path = './test_resources/input_files/valid-badge.png'
        result = verify_badge(image_path)
        self.assertEqual(result, 'Badge is valid')

    
    def test_invalid_badge_size(self):
        # Test verification of an image with incorrect size
        image_path = './test_resources/input_files/invalid_badge_size.png'
        result = verify_badge(image_path)
        self.assertEqual(result, 'Image size is not 512x512')

    
    def test_invalid_badge_non_circular(self):
        # Test verification of an image with non-transparent pixels outside the circle
        image_path = './test_resources/input_files/invalid-non-circular-badge.png'  
        result = verify_badge(image_path)
        self.assertEqual(result, 'Non-transparent pixels are not within a circle')


    def test_invalid_color_pastel(self):
        # Test verification of an image with non-transparent pixels outside the circle
        image_path = './test_resources/input_files/invalid_colors.png'  
        result = verify_badge(image_path)
        self.assertEqual(result, 'Colors are not pastel')
 

if __name__ == '__main__':
    unittest.main()
