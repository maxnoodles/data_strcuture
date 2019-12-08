import time
from functools import wraps, reduce


def time_count(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        print('time count: ', end_time - start_time)
        return ret
    return wrapper


@time_count
def test(n):
    return reduce(lambda x, y: x + y, list(range(n)))


# time_count(test)(n)
a = test(10000)
print(a)
print(test.__name__)
