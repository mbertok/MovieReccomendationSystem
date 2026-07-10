import logging

from django.conf import settings
from google import genai

logger = logging.getLogger(__name__)


class GeminiClient:
    """Wrapper for Google Gemini API"""

    def __init__(self):
        api_key = settings.GEMINI_API_KEY
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set in settings")
        self.client = genai.Client(api_key=api_key)

    def generate_text(
        self,
        prompt: str,
        temperature: float = settings.TEMPERATURE,
        max_tokens: int = settings.MAX_TOKENS,
    ):
        """
        Generate text from a prompt using Gemini Pro.

        Args:
            prompt (str): Input text prompt
            temperature (float): Controls randomness (0.0 - 1.0)
            max_tokens (int): Maximum length of response

        Returns:
            str: Generated text
        """
        try:
            generation_config = {
                "temperature": temperature,
                "max_output_tokens": max_tokens,
            }
            response = self.client.models.generate_content(
                model=settings.GEMINI_MODEL, contents=prompt, config=generation_config
            )
            return response.text
        except Exception as e:
            logger.error(f"Gemini API error: {str(e)}")
            raise Exception(f"Failed to generate response: {str(e)}")

    def chat(self, messages: list, temperature: float = 0.7):
        """
        Chat mode with conversation history.

        Args:
            messages (list): List of dicts with 'role' and 'parts' keys
            temperature (float): Controls randomness

        Returns:
            str: Assistant's reply
        """
        try:
            chat = self.model.start_chat(history=messages)
            response = chat.send_message(
                messages[-1]["parts"][0] if messages else "",
                generation_config={"temperature": temperature},
            )
            return response.text
        except Exception as e:
            logger.error(f"Gemini chat error: {str(e)}")
            raise Exception(f"Chat failed: {str(e)}")


# import google.generativeai as genai
# from django.conf import settings
# import logging
#
# logger = logging.getLogger(__name__)
#
#
# class GeminiClient:
#     """Wrapper for Google Gemini API"""
#
#     def __init__(self):
#         api_key = settings.GEMINI_API_KEY
#         if not api_key:
#             raise ValueError("GEMINI_API_KEY is not set in settings")
#         genai.configure(api_key=api_key)
#         self.model = genai.GenerativeModel('gemini-pro')
#
#     def generate_text(self, prompt: str, temperature: float = 0.7, max_tokens: int = 2048):
#         """
#         Generate text from a prompt using Gemini Pro.
#
#         Args:
#             prompt (str): Input text prompt
#             temperature (float): Controls randomness (0.0 - 1.0)
#             max_tokens (int): Maximum length of response
#
#         Returns:
#             str: Generated text
#         """
#         try:
#             generation_config = {
#                 "temperature": temperature,
#                 "max_output_tokens": max_tokens,
#             }
#             response = self.model.generate_content(
#                 prompt,
#                 generation_config=generation_config
#             )
#             return response.text
#         except Exception as e:
#             logger.error(f"Gemini API error: {str(e)}")
#             raise Exception(f"Failed to generate response: {str(e)}")
#
#     def chat(self, messages: list, temperature: float = 0.7):
#         """
#         Chat mode with conversation history.
#
#         Args:
#             messages (list): List of dicts with 'role' and 'parts' keys
#             temperature (float): Controls randomness
#
#         Returns:
#             str: Assistant's reply
#         """
#         try:
#             chat = self.model.start_chat(history=messages)
#             response = chat.send_message(
#                 messages[-1]["parts"][0] if messages else "",
#                 generation_config={"temperature": temperature}
#             )
#             return response.text
#         except Exception as e:
#             logger.error(f"Gemini chat error: {str(e)}")
#             raise Exception(f"Chat failed: {str(e)}")
