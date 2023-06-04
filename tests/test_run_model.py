import pytest
from click.testing import CliRunner
from model.run_model import main


def test_cli():
    """
    Function to test the run model scripts main function using the click.testing.CliRunner
    """
    runner = CliRunner()
    result = runner.invoke(main, ["--image", "assets/test_img_1.jpg", "--text", "How many cats are there?"])
    assert result.exit_code == 0
    assert "2" in result.output