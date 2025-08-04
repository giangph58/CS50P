import sys
from PIL import Image, ImageOps
import os


def main():
    """Overlay shirt.png on input images"""
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    
    infile = sys.argv[1]
    outfile = sys.argv[2]
    valid_extensions = (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG")

    if not infile.lower().endswith(valid_extensions) or not outfile.lower().endswith(valid_extensions):
        sys.exit("Invalid input")
    
    inext = os.path.splitext(infile.lower())[1]
    outext = os.path.splitext(outfile.lower())[1]
    
    if inext == '.jpeg': inext = '.jpg'
    if outext == '.jpeg': outext = '.jpg'

    if inext != outext:
        sys.exit("Input and output have different extensions")

    try:
        input_image = Image.open(infile)
        shirt_image = Image.open("./shirt.png")
        shirt_size = shirt_image.size

        fitted_input = ImageOps.fit(input_image, shirt_size)
        fitted_input.paste(shirt_image, (0, 0), shirt_image)
        fitted_input.save(outfile)


    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()