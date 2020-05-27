import threading


local = threading.local()
local.num = 1
print(local.num)
log = []


def func():
    local.num = 2
    print(local.num)
    log.append(local.num)


thread = threading.Thread(target=func)
thread.start()
thread.join()

print(log)
print(local.num)




