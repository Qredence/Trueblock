from custom_nodes.pipeline_executor import PipelineExecutor
from custom_nodes.image_loader import ImageLoader
from custom_nodes.image_processor import ImageProcessor
from custom_nodes.bounding_box_visualizer import BoundingBoxVisualizer
from custom_nodes.image_comparator import ImageComparator
from custom_nodes.trulens_node import TrulensNode

# Parameters from the object_detection.json configuration
image_urls = [
    "https://storage.googleapis.com/tfweb/visualblocks-input-images/pic4.jpeg",
    "https://storage.googleapis.com/tfweb/visualblocks-input-images/pic5.jpg",
    "https://storage.googleapis.com/tfweb/visualblocks-input-images/pic6.jpg"
]
resize_width = 448  # Set according to the actual configuration
resize_height = 240  # Set according to the actual configuration
model_path = 'models/object_detection_model'  # Assuming a default model path
score_threshold = 0.5  # Set according to the actual configuration
max_boxes = 20  # Set according to the actual configuration
column_labels = 'input image, post processed image, result'

# Instantiate the custom nodes
image_loader = ImageLoader(image_urls)
image_processor = ImageProcessor(resize_width, resize_height)
trulens_node = TrulensNode(model_path, score_threshold, max_boxes)
bounding_box_visualizer = BoundingBoxVisualizer()
image_comparator = ImageComparator(column_labels)

# Set up the pipeline
nodes = [image_loader, image_processor, trulens_node, bounding_box_visualizer, image_comparator]
pipeline_executor = PipelineExecutor(nodes)

# Execute the pipeline
pipeline_executor.execute_pipeline()
