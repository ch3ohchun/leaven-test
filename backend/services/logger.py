import logging
import logging.config
from backend.config.logging import LOGGING_CONFIG

# Apply configuration once
logging.config.dictConfig(LOGGING_CONFIG)

class AppLogger:
    """
    Application Logger class.
    Provides a centralized way to get logger instances.
    """
    
    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        """
        Get a configured logger instance by name.
        """
        return logging.getLogger(name)

# Expose a default logger for convenience
logger = AppLogger.get_logger("app")
