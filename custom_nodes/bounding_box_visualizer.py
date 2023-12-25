import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


class BoundingBoxVisualizer:
    def __init__(self, color='#00FF00'):
        self.color = color

    def draw_boxes(self, image, boxes):
        # Create a figure and axis for the image
        fig, ax = plt.subplots(1)
        ax.imshow(image)

        # Draw each bounding box on the image
        for box in boxes:
            rect = Rectangle((box['x'], box['y']), box['width'], box['height'], linewidth=1, edgecolor=self.color, facecolor='none')
            ax.add_patch(rect)

        # Remove axis ticks
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()

        return fig
