"""
Steganography Message Extractor
Extracts hidden messages from images using various steganography techniques
"""

from PIL import Image
import os
import sys
from typing import Optional, Tuple
import io


class SteganographyExtractor:
    """Extract hidden messages from images using LSB (Least Significant Bit) steganography"""
    
    def __init__(self, image_path: str):
        """
        Initialize the extractor with an image file
        
        Args:
            image_path: Path to the image file
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.pixels = self.image.load()
        self.width, self.height = self.image.size
        
    def extract_lsb_message(self) -> Optional[str]:
        """
        Extract hidden message using LSB (Least Significant Bit) technique
        
        Returns:
            Extracted message or None if no message found
        """
        binary_string = ""
        
        # Convert image to RGB if necessary
        if self.image.mode != 'RGB':
            self.image = self.image.convert('RGB')
            self.pixels = self.image.load()
        
        # Extract LSB from each pixel's RGB values
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = self.pixels[x, y][:3]
                
                # Extract LSB from each color channel
                binary_string += str(r & 1)
                binary_string += str(g & 1)
                binary_string += str(b & 1)
        
        # Convert binary string to text
        message = self._binary_to_text(binary_string)
        return message if message else None
    
    def _binary_to_text(self, binary_string: str) -> str:
        """
        Convert binary string to readable text
        
        Args:
            binary_string: Binary string to convert
            
        Returns:
            Decoded text message
        """
        message = ""
        
        # Process 8 bits at a time
        for i in range(0, len(binary_string) - 7, 8):
            byte = binary_string[i:i+8]
            char_code = int(byte, 2)
            
            # Stop at null terminator or non-printable characters
            if char_code == 0:
                break
            
            # Only include printable ASCII characters
            if 32 <= char_code <= 126 or char_code in [9, 10, 13]:
                message += chr(char_code)
            else:
                # If we hit non-printable, we might be done
                if message:
                    break
        
        return message
    
    def extract_metadata(self) -> dict:
        """
        Extract image metadata and EXIF data
        
        Returns:
            Dictionary of metadata
        """
        metadata = {
            'format': self.image.format,
            'mode': self.image.mode,
            'size': self.image.size,
            'width': self.width,
            'height': self.height,
        }
        
        # Try to extract EXIF data
        try:
            exif_data = self.image._getexif()
            if exif_data:
                metadata['exif'] = str(exif_data)
        except:
            pass
        
        return metadata
    
    def extract_all(self) -> dict:
        """
        Extract all possible hidden data from the image
        
        Returns:
            Dictionary containing all extracted data
        """
        results = {
            'image_path': self.image_path,
            'metadata': self.extract_metadata(),
            'lsb_message': self.extract_lsb_message(),
        }
        
        return results
    
    @staticmethod
    def analyze_image(image_path: str) -> None:
        """
        Analyze an image for steganographic content and print results
        
        Args:
            image_path: Path to image file to analyze
        """
        print(f"\n{'='*60}")
        print(f"Steganography Extractor - Image Analysis")
        print(f"{'='*60}\n")
        
        try:
            extractor = SteganographyExtractor(image_path)
            results = extractor.extract_all()
            
            print(f"Image: {results['image_path']}")
            print(f"\nMetadata:")
            for key, value in results['metadata'].items():
                print(f"  {key}: {value}")
            
            print(f"\nExtracted Message (LSB):")
            if results['lsb_message']:
                print(f"  {results['lsb_message']}")
            else:
                print(f"  No message found")
            
            print(f"\n{'='*60}\n")
            
        except Exception as e:
            print(f"Error analyzing image: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python steganography_extractor.py <image_path>")
        print("\nExample: python steganography_extractor.py hidden_message.png")
        sys.exit(1)
    
    image_file = sys.argv[1]
    SteganographyExtractor.analyze_image(image_file)
