import threading
import time
import logging


class MyLocal:
    def __init__(self):
        self.storage = {}
        self.get_ident = threading.get_ident

    def set(self, k, v):
        ident = self.get_ident()
        origin = self.storage.get(ident)
        if not origin:
            origin = {k: v}
        else:
            origin[k] = v
        self.storage[ident] = origin

    def get(self, k):
        ident = self.get_ident()
        origin = self.storage.get(ident)
        if not origin:
            return None
        return origin.get(k, None)


class MyLocal2:

    def __init__(self):
        object.__setattr__(self, '__storage__', {})
        object.__setattr__(self, '__ident_func__', threading.get_ident)

    def __setattr__(self, name, value):
        ident = self.__ident_func__()
        storage = self.__storage__
        try:
            storage[ident][name] = value
        except KeyError:
            storage[ident] = {name: value}

    def __getattr__(self, name):
        try:
            return self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)

    def __delattr__(self, name):
        try:
            del self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)


local_value = MyLocal2()


def task(num):
    local_value.name = num
    time.sleep(1)
    logging.warning(f"{local_value.name}, {threading.current_thread().name}")


th = [threading.Thread(target=task, args=(i,), name='线程%s' % i) for i in range(20)]
[i.start() for i in th]
[i.join() for i in th]

print(123)