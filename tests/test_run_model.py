import transformers
import pytest
from click.testing import CliRunner
from model.run_model import main, load_model


def test_load_model():
    """
    Function to test the load model script
    """

    # Load the model and input processor
    processor, model = load_model()

    # Check the loaded model and processor variables are not None
    assert processor is not None
    assert model is not None

    # Check the loaded model and processor variables are of the correct type
    assert isinstance(processor, transformers.models.vilt.processing_vilt.ViltProcessor)
    assert isinstance(
        model, transformers.models.vilt.modeling_vilt.ViltForQuestionAnswering
    )


@pytest.mark.parametrize(
    "image_path, text_input, expected_output",
    [
        ("assets/test_img_1.jpg", "How many cats are there?", "2"),
        ("assets/test_img_2.jpg", "What is the animal doing?", "laying"),
    ],
)
def test_main(image_path, text_input, expected_output):
    """
    Function to test the run model scripts main function using the click.testing.CliRunner
    """

    # Create a click testing runner
    runner = CliRunner()
    # Run the main function with the provided inputs
    result = runner.invoke(main, ["--image", image_path, "--question", text_input])

    # Check the output is as expected
    assert result.exit_code == 0
    assert expected_output in result.output
