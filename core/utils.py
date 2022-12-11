
import time
from functools import wraps


def retry_with_params(max_retries: int):
    def retry_decorator(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            for i in range(max_retries):
                try:
                    func(*args, **kwargs)
                    break
                except Exception as ex:
                    time.sleep(1)
                    if i == (max_retries - 1):
                        raise ex
        return _wrapper
    return retry_decorator
