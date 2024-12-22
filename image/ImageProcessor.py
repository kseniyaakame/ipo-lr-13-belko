from PIL import Image, ImageFilter, ImageDraw, ImageFont
from image.ImageHandler import ImageHandler

class ImageProcessor:
    def __init__(self, image_handler):
        self.image_handler = image_handler

    def add_filter(self):
        self.image_handler.image = self.image_handler.image.filter(ImageFilter.EMBOSS)

    def add_text(self, text='Вариант 5'):
        width, height = self.image_handler.image.size
        draw = ImageDraw.Draw(self.image_handler.image)
        font = ImageFont.truetype("arial.ttf", 36) 

        text_bbox = draw.textbbox((0, 0), text, font=font) 
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1] 
        position = (width - text_width - 10, height - text_height - 10)

        watermark = Image.new("RGBA", self.image_handler.image.size) 
        watermark_draw = ImageDraw.Draw(watermark) 
        watermark_draw.text(position, text, font=font, fill=(255, 255, 255, 128)) 
        
        self.image_handler.image = Image.alpha_composite(self.image_handler.image.convert("RGBA"), watermark)