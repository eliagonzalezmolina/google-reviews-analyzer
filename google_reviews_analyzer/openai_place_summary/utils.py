import logging
from typing import List

import tiktoken

logging.basicConfig(level=logging.INFO)


def build_place_summary_prompt(
    place_name: str, reviews: List[str], model: str, model_max_tokens: int
) -> str:
    prompt = (
        f"Generate a short review of a place named '{place_name}' "
        f"summarizing following reviews:\n"
    )
    for r in reviews:
        prompt += f"- {r} \n"
        if _count_tokens(prompt, model) > model_max_tokens - 200:
            break
    prompt += (
        "The objective is to have a general idea of 5 main pros "
        "and 5 main cons of this place, "
        "so try to capture the details that are repeated from reviews. "
        "Pay special attention to avoid inconsistencies between pros and cons."
    )
    logging.info(f"Prompt generated with {_count_tokens(prompt, model)} tokens")
    return prompt


def _count_tokens(string: str, model: str) -> int:
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(string))
    return num_tokens
