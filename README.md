# Code Breaker & Deciphering Application 🔐

A comprehensive Python application for extracting hidden messages from images and breaking various cipher types.

## Features

### 🖼️ Steganography
- **LSB (Least Significant Bit) Extraction**: Extract hidden messages embedded in images
- **Image Metadata**: Extract and display image metadata
- Supports common image formats (PNG, JPG, BMP, etc.)

### 🔓 Cipher Breaking

#### Caesar Cipher
- Brute-force attack trying all 26 shifts
- Frequency analysis scoring to identify correct decryption
- Displays top 5 possible decryptions

#### Substitution Cipher
- Uses simulated annealing algorithm
- Chi-squared frequency analysis for scoring
- Attempts 2000 iterations for optimal results

#### ROT13
- Simple rotation cipher decoder
- Instant decoding

#### Atbash Cipher
- Reverse alphabet mapping decoder
- Used in classical cryptography

#### Frequency Analysis
- Calculate letter frequency distribution
- Compare against English language statistics
- Visual frequency chart with percentage display

## Installation

### Requirements
- Python 3.7+
- Pillow (for image processing)

### Setup

```bash
# Clone the repository
git clone https://github.com/farmerm2023-dev/Code-breaker.git
cd Code-breaker

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Interactive Mode

Run the application without arguments:

```bash
python main_app.py
```

### Command Line Mode

```bash
# Break Caesar cipher
python main_app.py --caesar "ufrjvhp"

# Extract hidden message from image
python main_app.py --image hidden.png

# Analyze letter frequency
python main_app.py --frequency "hello world"

# Break substitution cipher
python main_app.py --substitution "khoor zruog"

# Decode ROT13
python main_app.py --rot13 "Uryyb Jbeyq"

# Decode Atbash
python main_app.py --atbash "svool dliow"
```

## Module Overview

### `steganography_extractor.py`
Extracts hidden messages from images using LSB technique.

### `cipher_breaker.py`
Breaks various cipher types using cryptanalysis.

### `main_app.py`
Main application combining all features.

## Examples

### Break Caesar Cipher
```bash
python main_app.py --caesar "khoor zruog"
```

Output:
```
CAESAR CIPHER BREAKER

Ciphertext: khoor zruog

Possible Decryptions (ranked by score):

   1. Shift:  3 | Text: hello world
   2. Shift:  4 | Text: gdkkn vnqkc
   3. Shift:  5 | Text: fcjjm umpjb
   4. Shift:  2 | Text: ifmmp xpsme
   5. Shift:  6 | Text: ebiil tnoia
```

## Performance

- **Caesar Cipher**: < 1ms for typical texts
- **Frequency Analysis**: < 100ms for 1000+ character texts
- **Substitution Breaking**: 1-5 seconds depending on text length
- **Image Extraction**: 100ms-1s depending on image size

## Security Note

This tool is designed for educational purposes and authorized penetration testing only.

## Author

farmerm2023-dev
