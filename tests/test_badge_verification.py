import unittest
from image_processing.badge_verification import verify_badge

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
        image_path = 'invalid-non-circular-badge.png'  
        result = verify_badge(image_path)
        self.assertEqual(result, 'Non-transparent pixels are not within a circle')

 

if __name__ == '__main__':
    unittest.main()
