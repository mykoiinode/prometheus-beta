import functools
import logging
import memory_profiler

def log_memory_usage(logger=None):
    """
    A decorator that logs memory usage before and after a function call.
    
    :param logger: Optional logger to use. If None, uses the root logger.
    :return: Decorated function that logs memory usage
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Use default logger if not provided
            log = logger or logging.getLogger()
            
            # Get memory usage before function call
            memory_before = memory_profiler.memory_usage()[0]
            log.info(f"Memory usage before {func.__name__}: {memory_before} MiB")
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Get memory usage after function call
                memory_after = memory_profiler.memory_usage()[0]
                log.info(f"Memory usage after {func.__name__}: {memory_after} MiB")
                
                # Calculate and log memory difference
                memory_diff = memory_after - memory_before
                log.info(f"Memory usage change: {memory_diff} MiB")
                
                return result
            
            except Exception as e:
                log.error(f"Error in {func.__name__}: {e}")
                raise
        
        return wrapper
    
    return decorator