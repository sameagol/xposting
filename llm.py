from llama_cpp import Llama
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def initialize_llm(n_ctx=2048):
    """
    Initializes a LLM model using a specified model path and context size.

    Args:
    model_path (str): The file path to the model.
    n_ctx (int): The number of context tokens for the model. Default is 2048.

    Returns:
    LlmModel: An initialized LLM model object.
    """
    
    # Use environment variable if model_path is not provided
    model_path = os.getenv('llm_mistral_path')
    print(model_path)

    # Create an instance of the Llama model
    llm = Llama(model_path=model_path, n_ctx=n_ctx)

    # Optionally, print model metadata
    print(llm.metadata)

    # Return the model instance
    return llm


def generate_response(llm, prompt, max_tokens=4000, temperature=0.5):
    """
    Generates a response from the LLM based on the given prompt.

    Args:
    llm (LlmModel): An instance of the LLM model.
    prompt (str): The prompt to be processed by the model.
    max_tokens (int): The maximum number of tokens to be generated. Default is 4000.
    temperature (float): The creativity of the response. Lower values are less random. Default is 0.5.

    Returns:
    str: The generated text response from the model.
    """
    response = llm(prompt, max_tokens=max_tokens, temperature=temperature)
    simple_response = response['choices'][0]['text']
    # print('Simple Response: ')
    # print(simple_response)

    return simple_response