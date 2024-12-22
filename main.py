from image.ImageHandler import ImageHandler
from image.ImageProcessor import ImageProcessor

def main():
    image_path = "image_1.jpg"
    size_factor = 0.5  

    image = ImageHandler(image_path)
    image.load_image()
    image.change_size(size=size_factor)

    processor = ImageProcessor(image)
    processor.add_filter()
    processor.add_text("Вариант 5")

    saved_filename = image.save_new()

main()