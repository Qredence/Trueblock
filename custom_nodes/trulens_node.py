"""
A module for Trulens node.
"""

import tensorflow as tf
from trulens.nn.models import get_model_wrapper
from trulens.visualizations import Overlay


class TrulensNode:
    """
    A class representing a Trulens node.
    """

    def __init__(self, model_path, score_threshold, max_boxes):
        """
        Initialize the TrulensNode object.
        """
        self.model_path = model_path
        self.score_threshold = score_threshold
        self.max_boxes = max_boxes
        self.model = self.load_model()

    def load_model(self):
        """
        Load the TensorFlow model from the given path.
        """
        model = tf.saved_model.load(self.model_path)
        return get_model_wrapper(model, backend='tf')

    def process_image(self, image):
        """
        Process the image and perform object detection.
        """
        input_tensor = tf.convert_to_tensor(image)
        input_tensor = input_tensor[tf.newaxis, ...]
        detections = self.model.detect_fn(input_tensor)
        return detections

    def explain_predictions(self, image, detections):
        """
        Use Trulens to explain the model's predictions.
        """
        explanations = self.model.explain(image, detections)
        return explanations

    def visualize_explanations(self, image, explanations):
        """
        Visualize the explanations on the image.
        """
        overlay = Overlay()
        visualization = overlay.apply(image, explanations)
        return visualization
