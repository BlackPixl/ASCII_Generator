from PIL import Image
from argparse import ArgumentParser

def arguments():
	parser = ArgumentParser(description='asciigen: A very simple ascii asrt generator.')
	parser.add_argument('input_path',
		type=str)
	parser.add_argument('--output',
		'--o',
		dest='output',
		type=str,
		help='Saves the output on the specified file.')
	arguments = parser.parse_args()
	return {
	'input_path': arguments.input_path,
	'output': arguments.output,
	}


def resize_image():
	pass

def color_to_grayscale(image):
	grayscale = image.convert('L')
	return grayscale

def img_to_ascii(image):
	ascii_characters = '@#$S%?*+;:,.'
	image_pixels = image.getdata()
	return image_pixels

def main():
	args = arguments()
	input_path = args.pop('input_path')
	try:
		img = Image.open(input_path)
	except:
		print('Invalid input path: ', input_path)
		return 1

	print('Welcome to asciigen. \ninput image: %s'% (input_path))
	grayscale_image = color_to_grayscale(img)
	ascii_image = img_to_ascii(grayscale_image)
	print(ascii_image)
	return 0
