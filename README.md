[![Python Continuous Integration](https://github.com/architkaila/Visual-Question-Answering-CLI/actions/workflows/main.yml/badge.svg)](https://github.com/architkaila/Visual-Question-Answering-CLI/actions/workflows/main.yml)

# Visual-Question-Answering-CLI  
> #### _Archit | Summer '23 | Duke AIPI 561 MLOPS Project 1_  

&nbsp;  
## Project Description ⭐ 
This `CLI Tool` with Continuous Integration using GitHub Actions allows you to generate answers to questions with a image input. The tool uses the `Vision-and-Language Transformer (ViLT)` model from [Hugging Face](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa). You provide the tool with and image and a question, and it will generate an answer to the question based on the image.  

For example, if the following image and question are input into the model, it will produce the following answer:
>![img](assets/test_img_2.jpg)  

```Question: what is the animal doing?```   
```Predicted Answer: laying```  

&nbsp;  
## Setting up the Tool 🛠️  
**1. The tool has been packaged into a package, and can be installed using the following command:**  
```
make setup
```  
This upgrades pip, installs the requirements and sets up the cli tool with `qanswer` as the command input

**2. To run linting on the code:**  
```
make lint
```  

**3. To run unit tests on the code:**  
```
make test
```  

**4. To run all the steps including setup, code formating using black, linting and testing:**  
```
make all
```  
  

&nbsp;  
## Running the Tool 🏃‍♂️
The CLI tool has an entry point called `qanswer` which can be used to run the tool. The tool takes in two arguments: `--image_path` and `--question`. The `image_path` is the path to the image you want to use as input, and the `question` is the question you want to ask about the image.  

**1. To run the tool, you can use the following command:**  
```
qanswer --image_path <path_to_image> --question <question>
```
**2. To run the tool with the default image and question:**  
```
qanswer --image_path assets/test_img_2.jpg --question "what is the animal doing?"
```

&nbsp;  
## Continuous Integration using Github Actions 🤖 
The tool has been integrated with Github Actions to run the following steps on every push to the main branch:
1. Installing dependencies and environment setup using make setup
2. Linting the code using pylint
3. Formatting the code using black
4. Running unit tests on the code usoing pytest

The github workflow yaml file can be found [here](.github/workflows/main.yml)  


&nbsp;   
## Project Structure 🧬  
The project codes are arranged in the following manner:

```
├── .github                           <- directory for github templates
    ├── workflows                     <- directory for github actions workflow
        ├── main.yml                  <- github actions workflow file
├── assets                            <- directory for repository image assets
├── model                             <- directory for model code
    ├── run_model.py                  <- script to run the hugging face model
├── tests                             <- directory for unit tests   
    ├── test_run_model.py             <- script to run unit tests on the model 
├── .gitignore                        <- git ignore file
├── LICENSE                           <- license file
├── README.md                         <- description of project and how to set up and run it
├── requirements.txt                  <- requirements file to document dependencies
├── setup.py                          <- setup file for the package
```  
