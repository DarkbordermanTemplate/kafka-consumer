"""Utility Class, function setup"""
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class TopicHandler:
    """
        Mininum unit for processing topic messages
        Assign a handler function, a topic and enable it to make it works

    Arguments:
        handle: {Callable[[Any], Any]}
        topic {str} -- targeted topic
        streaming {bool} -- enable streaming (default False, pass "true" to enable)
    """

    handle: Callable[[Any], Any] = print
    topic: str = ""
    enabled: bool = False
