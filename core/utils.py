
import time
from functools import wraps


def retry_with_params(max_retries: int):
    def retry_decorator(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    func(*args, **kwargs)
                except Exception:
                    time.sleep(1)
        return _wrapper
    return retry_decorator