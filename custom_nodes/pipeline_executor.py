from custom_nodes.trulens_node import TrulensNode
from custom_nodes.image_loader import ImageLoader
from custom_nodes.image_processor import ImageProcessor
from custom_nodes.bounding_box_visualizer import BoundingBoxVisualizer
from custom_nodes.image_comparator import ImageComparator


class PipelineExecutor:
    def __init__(self, nodes):
        self.nodes = nodes

    def execute_pipeline(self):
        # Execute each node in the pipeline in the correct order
        for node in self.nodes:
            if isinstance(node, ImageLoader):
                images = node.load_images()
            elif isinstance(node, ImageProcessor):
                processed_images = [node.process_image(image) for image in images]
            elif isinstance(node, TrulensNode):
                detections = [node.process_image(image) for image in processed_images]
                explanations = [node.explain_predictions(image, detection) for image, detection in zip(processed_images, detections)]
                visualizations = [node.visualize_explanations(image, explanation) for image, explanation in zip(processed_images, explanations)]
            elif isinstance(node, BoundingBoxVisualizer):
                visualized_images = [node.draw_boxes(image, detection) for image, detection in zip(processed_images, detections)]
            elif isinstance(node, ImageComparator):
                comparison_result = node.compare_images([images, processed_images, visualized_images])

        return comparison_result
