import datetime
import time
import sys

def warn_slow(func):
    
    def inner(a, b):
        
        start = datetime.datetime.now()
        func(a,b)
        end = datetime.datetime.now() - start
        if end.seconds <= 2:
            print(end.seconds, f'seconds {func.__name__} with arg ({a},{b})')
        else:
            print(f'execution of {func.__name__} with ({a},{b}) arguments took more than 2 seconds')
        
    return inner
@warn_slow
def func_slow(x, y):
    time.sleep(3)

@warn_slow
def func_fast(x, y):
    print(x, y)

func_slow(1, 5)
func_fast(2, 4)
