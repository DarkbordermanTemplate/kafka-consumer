"""
    Handler list definition
    Main function imports TOPIC_HANDLERS and maps to each thread
"""
from typing import List

from .example import EXAMPLE_HANDLER
from .utils import TopicHandler

TOPIC_HANDLERS: List[TopicHandler] = [EXAMPLE_HANDLER]
