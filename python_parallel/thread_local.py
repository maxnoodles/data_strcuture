import threading
import time

local = threading.local()
local.num = 1
print(local.num)
log = []


def func():
    local.num = 2
    print(local.num)
    log.append(local.num)
    time.sleep(1)


thread = threading.Thread(target=func)
thread.start()
thread.join()

a = 2
print(log)
print(local.num)





