from PIL import Image


class ImageProcessor:
    def __init__(self, resize_width=-1, resize_height=-1):
        self.resize_width = resize_width
        self.resize_height = resize_height

    def process_image(self, image):
        # Resize image if required
        if self.resize_width > 0 and self.resize_height > 0:
            image = image.resize((self.resize_width, self.resize_height))
        return image
