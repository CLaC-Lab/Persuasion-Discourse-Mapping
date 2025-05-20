import openai
import config

openai.api_key = config.OPENAI_API_KEY
model_name = config.OPENAI_MODEL_NAME


def gpt_prompt_handler(paragraph, prompt_template):
    """
    Sends a prompt to the OpenAI GPT model using a provided paragraph and prompt template.

    Args:
        paragraph (str): The text to include in the prompt.
        prompt_template (str): A string with a `{paragraph}` placeholder to insert the text.

    Returns:
        str: The generated model response.
    """
    
    prompt = prompt_template.format(paragraph=paragraph)
    print(model_name)
    response = openai.ChatCompletion.create(
        model = model_name,
        messages = [{"role": "user", "content": prompt}]
    )

    result = response['choices'][0]['message']['content'].strip()

    return result
