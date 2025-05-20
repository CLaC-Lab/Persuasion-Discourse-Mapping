import config
from utils.llm_prompt_handlers.claude_prompt_handler import claude_prompt_handler
from utils.llm_prompt_handlers.gemini_prompt_handler import gemini_prompt_handler
from utils.llm_prompt_handlers.gpt_prompt_handler import gpt_prompt_handler

def get_parser_and_model_name(parser_id):
    """
    Retrieves the parser handler function and model name based on the provided parser ID.

    Args:
        parser_id (int): Identifier for the parser (1: GPT, 2: Gemini, 3: Claude).

    Returns:
        tuple: A tuple containing the parser handler function and the model name.

    Raises:
        ValueError: If an invalid parser_id is provided.
    """
    
    parser_config = {
        1: (gpt_prompt_handler, config.OPENAI_MODEL_NAME),
        2: (gemini_prompt_handler, config.GEMINI_MODEL_NAME),
        3: (claude_prompt_handler, config.CLAUDE_MODEL_NAME),
    }

    if parser_id in parser_config:
        parser, model_name = parser_config[parser_id]
        return parser, model_name
    else:
        raise ValueError("Invalid parser id provided.")