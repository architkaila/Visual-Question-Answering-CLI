# Library imports
import click
from transformers import ViltProcessor, ViltForQuestionAnswering
import requests
from PIL import Image
import warnings
warnings.filterwarnings("ignore")

def load_model():
    """
    Loads the pretrained ViLT model and the input processor

    Args:
        None
    
    Returns:
        processor (ViltProcessor): Input processor for the model
        model (ViltForQuestionAnswering): Pretrained ViLT model
    """

    # Load the model and input processor
    processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    
    return processor, model

def run_model(processor, model, image, text):
    """
    Runs the ViLT model on the provided inputs

    Args:
        processor (ViltProcessor): Input processor for the model
        model (ViltForQuestionAnswering): Pretrained ViLT model
        image (str): Path to input image for visual question answer
        text (str): question for the image
    
    Returns:
        answer (str): Answer to the question
    """
    # Prepare inputs
    encoding = processor(image, text, return_tensors="pt")

    # Forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()

    # Get the answer
    answer = "\n[INFO] Predicted Answer: " + model.config.id2label[idx]

    return answer

@click.command
@click.option(
    "--image", type=click.Path(exists=True), help="Path to input image for visual question answer"
)
@click.option(
    "--text", help="question for the image"
)
def main(image, text):
    """
    This is the main driver function. It reads an input image and a text question
    and runs the Vision-and-Language Transformer (ViLT) on the provided inputs.

    Args:
        image (str): Path to input image for visual question answer
        text (str): question for the image
    
    Returns:
        None
    """
    if image is None or text is None:
        print("[INFO] Please provide both image and text inputs")
        return
    
    # Read the image
    input_image = Image.open(image)

    # Load the model and input processor
    processor, model = load_model()

    # Run the model and get the answer
    answer = run_model(processor, model, input_image, text)

    # Print the answer to the console
    click.echo(answer)

if __name__ == "__main__":
    main()