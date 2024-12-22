from PIL import Image
from datetime import datetime

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        self.image = Image.open(self.image_path)

    def change_size(self, size=0.5):
        new_size = (int(self.image.width * size), int(self.image.height * size))
        self.image = self.image.resize(new_size)

    def save_new(self, filename=None):
        date_str = datetime.now().strftime("%Y%m%d")
        if not filename:
            filename = f"{self.image_path.split('.')[0]}_{date_str}.png"
        self.image.save(filename)
        print(f"Изображение сохранено: {filename}")
        return filename