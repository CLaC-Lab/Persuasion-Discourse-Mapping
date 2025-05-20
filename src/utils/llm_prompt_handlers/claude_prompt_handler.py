import anthropic
import config

model_name = config.CLAUDE_MODEL_NAME

def claude_prompt_handler(paragraph, prompt_template):
    """
    Sends a prompt to the Claude API using the given paragraph and prompt template.

    Args:
        paragraph (str): The input paragraph to annotate or analyze.
        prompt_template (str): A template string with a `{paragraph}` placeholder.

    Returns:
        str: The generated response text from Claude.
    """
    
    prompt = prompt_template.format(paragraph=paragraph)

    client = anthropic.Anthropic(api_key=config.CLAUDE_API_KEY)
    message = client.messages.create(
        model=model_name,
        max_tokens=8192,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text.strip()