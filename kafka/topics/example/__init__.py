"""
    Topic handler definition
"""
import os

from distutils.util import strtobool

from topics.utils import TopicHandler
from .handler import handler

EXAMPLE_HANDLER = TopicHandler(
    handle=handler,
    topic="example",
    enabled=strtobool(os.environ.get("EXAMPLE_STREAMING", "false")),
)
