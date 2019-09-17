import threading
import time

def action(arg):
    time.sleep(1)
    print('the arg is {}'.format(arg))

for i in xrange(4):
    t=threading.Thread(target=action,args=(i,))
    t.start()

print('main thread end!')