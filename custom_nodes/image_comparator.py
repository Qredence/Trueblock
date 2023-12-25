import matplotlib.pyplot as plt


class ImageComparator:
    def __init__(self, column_labels):
        self.column_labels = column_labels.split(', ')

    def compare_images(self, images_list):
        # Assuming images_list is a list of lists of images to be compared
        num_rows = len(images_list[0])
        num_cols = len(images_list)

        fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5 * num_rows))
        if num_rows == 1:
            axes = [axes]
        for col, col_images in enumerate(images_list):
            for row, image in enumerate(col_images):
                axes[row].imshow(image)
                if col == 0:
                    axes[row].set_ylabel(f'Image {row + 1}')
                if row == 0:
                    axes[col].set_title(self.column_labels[col])

        plt.tight_layout()
        plt.show()

        return fig
