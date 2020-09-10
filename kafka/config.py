"""Service-wide config"""
import os

AUTO_OFFSET_RESET = os.environ.get("AUTO_OFFSET_RESET", "earliest")
BROKERS = os.environ.get("BROKERS", "127.0.0.1:9092")
SESSION_TIMEOUT_MS = int(os.environ.get("SESSION_TIMEOUT_MS", 6000))
GROUP_ID = os.environ.get("GROUP_ID", "streaming")
