import sys
import os

def get_prompt_template(prompt_key):
    """
    Loads and returns the content of a prompt template file based on the given key.

    Args:
        prompt_key (str): The filename key (without .txt) of the prompt template to load.

    Returns:
        str: The content of the prompt template.

    Exits:
        If the file is not found, exits the program with an error message.
    """
    try:
        path = os.path.join('prompts', f'{prompt_key}.txt')
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        sys.exit(f'Prompt File was not found... {prompt_key}')
