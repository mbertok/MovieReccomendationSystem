# from unittest.mock import MagicMock

from typing import Any

# def make_gemini_response(
#         text: str = "Tell me a joke",
#         prompt_tokens: int = 10,
#         completion_tokens: int = 12,
#         finish_reason: str = "STOP"
# ) -> MagicMock:
#     # usage = MagicMock()
#     # usage.prompt_token_count = prompt_tokens
#     # usage.candidates_token_count = completion_tokens
#     #
#     # candidate = MagicMock()
#     # candidate.finish_reason.name = finish_reason
#
#     response = MagicMock()
#     response.text = text
#     # response.usage_metadata = usage
#     # response.candidates = [candidate]
#     # response.to_dict.return_value = {
#     #     "candidates": [{"content": {"parts": [{"text": text}]}, "finish_reason": finish_reason}],
#     #     "usage_metadata": {"prompt_token_count": prompt_tokens, "candidates_token_count": completion_tokens},
#     # }
#     return response


def generate_payload(
    prompt: str = "Tell me a joke",
    # model: str = "gemini-2.5-flash",
    temperature: float = 0.9,
    max_tokens: int = 256,
) -> dict[str, Any]:
    return {
        "prompt": prompt,
        # "model": model,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
