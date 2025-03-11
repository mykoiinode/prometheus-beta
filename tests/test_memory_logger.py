import pytest
import logging
import io
import memory_profiler
from src.memory_logger import log_memory_usage

# Configure logging to capture log messages
class LogCapture:
    def __init__(self):
        self.log_capture = io.StringIO()
        self.logger = logging.getLogger()
        self.handler = logging.StreamHandler(self.log_capture)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.INFO)
    
    def get_logs(self):
        self.handler.flush()
        return self.log_capture.getvalue()

@log_memory_usage()
def sample_function(n):
    """A sample function that creates a list to test memory usage."""
    return [i for i in range(n)]

def test_log_memory_usage():
    # Capture logs
    log_capture = LogCapture()
    
    # Run the function with a significant list creation
    result = sample_function(100000)
    
    # Get captured logs
    logs = log_capture.get_logs()
    
    # Check that logs contain expected memory usage information
    assert "Memory usage before sample_function" in logs
    assert "Memory usage after sample_function" in logs
    assert "Memory usage change" in logs
    
    # Verify the function still returns its original result
    assert len(result) == 100000

def test_log_memory_usage_with_custom_logger():
    # Create a custom logger
    custom_logger = logging.getLogger("test_logger")
    custom_log_capture = io.StringIO()
    handler = logging.StreamHandler(custom_log_capture)
    custom_logger.addHandler(handler)
    custom_logger.setLevel(logging.INFO)
    
    # Create a decorated function with custom logger
    @log_memory_usage(logger=custom_logger)
    def another_function(x):
        return x * 2
    
    # Call the function
    result = another_function(5)
    
    # Get captured logs from custom logger
    logs = custom_log_capture.getvalue()
    
    # Check logs for custom logger
    assert "Memory usage before another_function" in logs
    assert "Memory usage after another_function" in logs
    
    # Verify function returns correct result
    assert result == 10

def test_log_memory_usage_exception():
    @log_memory_usage()
    def error_function():
        raise ValueError("Test error")
    
    # Capture logs
    log_capture = LogCapture()
    
    # Verify that the exception is re-raised
    with pytest.raises(ValueError, match="Test error"):
        error_function()
    
    # Check error logging
    logs = log_capture.get_logs()
    assert "Error in error_function" in logs