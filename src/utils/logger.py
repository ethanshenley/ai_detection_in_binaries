import logging
import sys
from pathlib import Path
from typing import Optional

class LogConfig:
    """Configuration for application logging."""
    
    DEFAULT_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    DEFAULT_LEVEL = logging.INFO
    
    @staticmethod
    def setup_logger(
        name: str = "ai_binary_detector",
        level: int = DEFAULT_LEVEL,
        log_file: Optional[str] = None,
        format_str: str = DEFAULT_FORMAT
    ) -> logging.Logger:
        """
        Configure and return a logger instance.
        
        Args:
            name: Logger name
            level: Logging level
            log_file: Optional file path for logging
            format_str: Log message format
            
        Returns:
            Configured logger instance
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)
        
        # Create formatters and handlers
        formatter = logging.Formatter(format_str)
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # File handler if specified
        if log_file:
            log_path = Path(log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)
            
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        return logger

def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance with the specified name.
    
    Args:
        name: Logger name (typically __name__ of the calling module)
        
    Returns:
        Logger instance
    """
    return logging.getLogger(f"ai_binary_detector.{name}")