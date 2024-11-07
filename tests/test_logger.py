import pytest
import logging
from pathlib import Path
from src.utils.logger import LogConfig, get_logger

def test_logger_setup(tmp_path):
    # Test basic logger setup
    logger = LogConfig.setup_logger()
    assert logger.level == logging.INFO
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.StreamHandler)
    
    # Test logger with file
    log_file = tmp_path / "test.log"
    logger = LogConfig.setup_logger(log_file=str(log_file))
    assert len(logger.handlers) == 2
    assert isinstance(logger.handlers[1], logging.FileHandler)
    assert Path(logger.handlers[1].baseFilename).exists()
    
def test_get_logger():
    logger = get_logger("test_module")
    assert logger.name == "ai_binary_detector.test_module"
    
def test_logger_message(capsys, tmp_path):
    log_file = tmp_path / "test.log"
    logger = LogConfig.setup_logger(log_file=str(log_file))
    
    test_message = "Test log message"
    logger.info(test_message)
    
    # Check console output
    captured = capsys.readouterr()
    assert test_message in captured.out
    
    # Check file output
    with open(log_file) as f:
        log_content = f.read()
        assert test_message in log_content