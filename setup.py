# Library imports
from setuptools import setup, find_packages

# Extract requirements from the requirements file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Visual-Question-Answering",
    description="A CLI based tool to run Vision-and-Language Transformer (ViLT). It takes an image and a question as input and generates an answer as output.",
    packages=find_packages(),
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        qanswer=model.run_model:main
    """,
    version="0.0.1",
    author="Archit Kaila",
    url="https://github.com/architkaila/Visual-Question-Answering-CLI",
)
