"""
    Handler function definition
"""
from typing import Any

from loguru import logger


def handler(raw_data: Any) -> Any:
    """
        An example handler that overrides default `print` function for better understanding

    Args:
        raw_data (Any): Raw data from Kafka topic

    Returns:
        Any: Not limited, default is `None`
    """
    logger.info(raw_data)
    return raw_data
