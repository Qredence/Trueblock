import requests
from PIL import Image
from io import BytesIO


class ImageLoader:
    def __init__(self, urls):
        self.urls = urls

    def load_images(self):
        images = []
        for url in self.urls:
            response = requests.get(url)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                images.append(image)
        return images
