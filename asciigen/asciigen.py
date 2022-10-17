from PIL import Image
from argparse import ArgumentParser


def arguments():
    parser = ArgumentParser(description='asciigen: A very simple ascii asrt generator.')
    parser.add_argument('input_path', type=str)
    parser.add_argument('--output', '--o', dest='output', type=str, help='Saves the output on the specified file.')
    args = parser.parse_args()
    return {
        'input_path': args.input_path,
        'output': args.output,
    }


def resize_image(image):
    new_image = image.resize((int(image.width * 0.5), int(image.height * 0.3)))
    return new_image


def color_to_grayscale(image):
    grayscale = image.convert('L')
    return grayscale


def img_to_ascii(image):
    ascii_characters = '@#$S%?*+;:,.'
    image_pixels = image.getdata()
    image_ascii = "".join([ascii_characters[pixel // 21] for pixel in image_pixels])
    return image_ascii


def main():
    args = arguments()
    input_path = args.pop('input_path')
    try:
        img = Image.open(input_path)
    except:
        print('Invalid input path: ', input_path)

    print('Welcome to asciigen. \ninput image: %s' % input_path)

    img = resize_image(img)
    grayscale_image = color_to_grayscale(img)
    ascii_image = img_to_ascii(grayscale_image)
    count = 0
    for i in range(len(ascii_image)):
        count += 1
        print(ascii_image[i], end='')
        if count == img.width:
            count = 0
            print('\n', end='')
    return 0
