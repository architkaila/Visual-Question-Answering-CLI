import pytest
from click.testing import CliRunner
from model.run_model import main

@pytest.mark.parametrize("image_path, text_input, expected_output", [
    ("assets/test_img_1.jpg", "How many cats are there?", "2"),
    ("assets/test_img_2.jpg", "What is the animal doing?", "laying"),
    # Add more test cases here
])
def test_cli(image_path, text_input, expected_output):
    """
    Function to test the run model scripts main function using the click.testing.CliRunner
    """
    runner = CliRunner()
    result = runner.invoke(main, ["--image", image_path, "--text", text_input])
    assert result.exit_code == 0
    assert expected_output in result.output