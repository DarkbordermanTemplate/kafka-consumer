"""Streaming entry file"""
from multiprocessing import Pool

from confluent_kafka import Consumer
from loguru import logger

from config import AUTO_OFFSET_RESET, BROKERS, GROUP_ID, SESSION_TIMEOUT_MS
from topics import TOPIC_HANDLERS
from topics.utils import TopicHandler


def start_streaming(handler: TopicHandler) -> None:
    """
        Initialize Kafka consumer according to `TopicHandler` and global config setup
    Args:
        handler (TopicHandler): Topic handler to process
    """
    logger.info(f"Topic {handler.topic} is set to {handler.enabled}")
    if handler.enabled:
        options = {
            "bootstrap.servers": BROKERS,
            "group.id": GROUP_ID,
            "session.timeout.ms": SESSION_TIMEOUT_MS,
            "auto.offset.reset": AUTO_OFFSET_RESET,
        }
        logger.info(
            f"Consumer is subscribing {handler.topic}@{BROKERS} and using {handler.handle}"
        )
        consumer = Consumer(options)
        consumer.subscribe([handler.topic])
        while True:
            try:
                msg = consumer.poll(timeout=1.0)
                if msg is None:
                    pass
                elif msg.error():
                    logger.warning(msg.error())
                else:
                    handler.handle(msg.value())
            except Exception as error:
                logger.warning(error)
        consumer.close()


if __name__ == "__main__":

    POOL = Pool(len(TOPIC_HANDLERS))
    POOL.map(start_streaming, TOPIC_HANDLERS)
