# Brought from AUTOMATIC1111's stable-diffusion-webui-tokenizer and modified
# https://github.com/AUTOMATIC1111/stable-diffusion-webui-tokenizer/blob/master/scripts/tokenizer.py

from typing import List
from modules import sd_hijack
from modules import shared
from scripts import logger

import open_clip.tokenizer

class VanillaClip:
    def __init__(self, clip):
        self.clip = clip

    def vocab(self):
        return self.clip.tokenizer.get_vocab()

    def byte_decoder(self):
        return self.clip.tokenizer.byte_decoder

class OpenClip:
    def __init__(self, clip):
        self.clip = clip
        self.tokenizer = open_clip.tokenizer._tokenizer

    def vocab(self):
        return self.tokenizer.encoder

    def byte_decoder(self):
        return self.tokenizer.byte_decoder

def tokenize(text: str, use_raw_token=True):
    if not hasattr(shared, 'sd_model') or shared.sd_model is None:
        logger.error("shared.sd_model not available for tokenization.")
        return ([], 0)

    if not hasattr(shared.sd_model, 'get_prompt_lengths_on_ui'):
        logger.error("Method 'get_prompt_lengths_on_ui' not found on shared.sd_model.")
        return ([], 0)

    try:
        result = shared.sd_model.get_prompt_lengths_on_ui(text)

        token_count = -1
        if isinstance(result, int):
            token_count = result
        elif isinstance(result, (tuple, list)) and len(result) > 0 and isinstance(result[0], int):
             token_count = result[0]
        elif hasattr(result, 'item') and isinstance(result.item(), int):
             token_count = result.item()

        if token_count == -1:
             logger.error(f"get_prompt_lengths_on_ui returned unexpected type: {type(result)}. Could not get count.")
             return ([], 0)

        tokens = []
        return tokens, token_count
    except Exception as e:
        logger.error(f"Error calling shared.sd_model.get_prompt_lengths_on_ui for text '{text}': {e}")
        return ([], 0)

def get_target_token_count(token_count: int):
     print("INFO: Using default calculation for target token count (75 per chunk).")
     return (token_count // 75 + 1) * 75 if token_count > 0 else 75
