from llama_cpp import Llama
import os
import tweepy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
twitter_consumer_key = os.getenv("twitter_consumer_key")
twitter_consumer_key_secret = os.getenv("twitter_consumer_key_secret")
twitter_authentication_key = os.getenv("twitter_authentication_key")
twitter_authentication_key_secret = os.getenv("twitter_authentication_key_secret")

# Create tweepy client
# client = tweepy.Client(
#     consumer_key=twitter_consumer_key,
#     consumer_secret=twitter_consumer_key_secret,
#     access_token=twitter_authentication_key,
#     access_token_secret=twitter_authentication_key_secret
# )

auth = tweepy.OAuth1UserHandler(twitter_consumer_key, twitter_consumer_key_secret, twitter_authentication_key, twitter_authentication_key_secret)
api = tweepy.API(auth)

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


def format_prompt_to_llama_2(raw_prompt: str):
    formatted_prompt = f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

    ### Instruction:
    {raw_prompt}

    ### Response:
    """

    return formatted_prompt


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
    formatted_prompt = format_prompt_to_llama_2(prompt)
    response = llm(formatted_prompt, max_tokens=max_tokens, temperature=temperature)
    simple_response = response['choices'][0]['text']
    # print('Simple Response: ')
    # print(simple_response)

    return simple_response


# def post_tweet(tweet_text):
#     """Posts a tweet to X (Twitter)."""
#     try:
#         response = client.create_tweet(text=tweet_text)
#         print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
#     except tweepy.TweepyException as e:
#         print(f"Error posting tweet: {e}")

def post_tweet(tweet_text):
    """Posts a tweet using OAuth 1.0a authentication."""
    try:
        response = api.update_status(status=tweet_text)
        print(f"✅ Tweet posted successfully! Tweet ID: {response.id}")
    except tweepy.TweepyException as e:
        print(f"❌ Error posting tweet: {e}")


content_string="""
Synthetic Diamond Fabrication: Methods and Applications

Synthetic diamonds, also known as lab-grown or man-made diamonds, are engineered to replicate the physical, chemical, and optical properties of natural diamonds. Their production has evolved significantly over the decades, with advanced fabrication techniques allowing for a wide range of industrial and commercial applications. The two primary methods for fabricating synthetic diamonds are High-Pressure High-Temperature (HPHT) and Chemical Vapor Deposition (CVD).

High-Pressure High-Temperature (HPHT) Method

The HPHT method, first developed in the 1950s, mimics the natural geological processes that create diamonds deep within the Earth's mantle. This process requires extreme conditions:

Pressure and Temperature – Carbon sources, typically graphite, are subjected to pressures exceeding 5 GPa (gigapascals) and temperatures above 1,500°C (2,732°F).

Metal Catalyst – A metal catalyst, such as iron (Fe), nickel (Ni), or cobalt (Co), facilitates the conversion of carbon into diamond.

Crystallization – Under these conditions, carbon atoms arrange into a diamond lattice, forming synthetic diamonds over hours or days.

HPHT diamonds can be color-enhanced by introducing specific elements, such as boron for blue or nitrogen for yellow diamonds. This method is widely used in industrial applications, including cutting tools, drilling equipment, and high-performance electronic components.

Chemical Vapor Deposition (CVD) Method

CVD technology, developed later, offers a more controlled way to grow high-purity synthetic diamonds, especially for scientific and jewelry applications. The process involves:

Gas Mixture – A hydrocarbon gas, usually methane (CH₄), is introduced into a low-pressure chamber along with hydrogen (H₂).

Plasma Activation – The gases are activated using microwave plasma, hot filaments, or lasers to break down the methane molecules.

Carbon Deposition – Carbon atoms settle onto a diamond seed substrate, growing layer by layer into a pure diamond structure.

CVD diamonds are prized for their high purity and ability to be engineered with specific properties. They are commonly used in electronics, quantum computing, and high-performance optics.

Comparing HPHT and CVD Diamonds

Purity: CVD diamonds tend to have fewer metal inclusions, making them preferable for optical and electronic applications.

Cost: HPHT is often more cost-effective for industrial diamonds, whereas CVD allows for more controlled production of high-quality gems.

Size & Shape: CVD can grow diamonds into large, flat plates, while HPHT produces bulkier, more naturally shaped crystals.

Applications of Synthetic Diamonds

Jewelry – Lab-grown diamonds are now widely used as an ethical and sustainable alternative to mined diamonds, offering identical brilliance and durability at lower costs.

Industrial Cutting and Drilling – HPHT diamonds are crucial for cutting, grinding, and drilling in industries such as mining, construction, and manufacturing.

Electronics & Semiconductors – Due to their exceptional thermal conductivity and resistance to wear, synthetic diamonds are used in high-power electronics and heat sinks.

Medical and Scientific Uses – CVD diamonds are used in laser optics, surgical tools, and high-precision spectroscopy.

Future of Synthetic Diamond Fabrication

As fabrication techniques improve, synthetic diamonds will continue to revolutionize industries, from quantum computing to next-generation semiconductors. With the growing demand for sustainable and ethically sourced materials, lab-grown diamonds are poised to play a vital role in the future of technology and commerce.

"""

prompt = """
Generate a very eye-catching and interesting fact based on the above content. The fact should include something about the main subject. Make sure your fact is only 50 characters.
"""

# Generate
llm = initialize_llm()
response = generate_response(llm, content_string + prompt)

print('response')
print(response)

# 'Lab-grown diamonds are now widely used as an ethical and sustainable alternative to mined diamonds, offering identical brilliance and durability at lower costs.'

# post_tweet(response)