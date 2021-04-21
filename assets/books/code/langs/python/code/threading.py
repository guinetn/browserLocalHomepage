#%%
# python.exe xxxx.py
# https://pythonprogramming.net/threading-tutorial-python/

# Threading in Python Programming
#   \__ Running multiple processes in parallel

import threading 		# contains a Thread class

def print_message():
	print('The message got printed from a different thread')
	# Still running: is_alive()  
my_thread = threading.Thread(target=print_message)
my_thread.start()


# Use locks to when threads need to access global resources safely
num = 1
my_lock = threading.Lock()
def my_func():
	global num, my_lock
	my_lock.acquire()

	sum = num + 1
	print(sum)
	
	my_lock.release()
my_thread = threading.Thread(target=my_func)
my_thread.start()



# PERFORMANCES
# Run an algorithm 10,000 times and measure the average time taken.
# python3 -m timeit '[print(x) for x in range(100)]'
# 100 loops, best of 3: 11.1 msec per loop 
# python3 -m timeit '[print(x) for x in range(10)]'
# 1000 loops, best of 3: 1.09 msec per loop
# Time per loop changes depending on the input

'''
Why do people say that python is single threaded?

Global interpreter lock:
Python has thread packages, but in some versions of Python the global interpreter lock ensures that at any given point in time only one thread can execute (it holds the lock). It might look like things are running in parallel but they’re really not. It increases the speed of single threaded applications and makes integration of C libraries which aren’t thread-safe easy. So far so good. 

The interviewer then might ask, “Can we run anything in parallel in Python?”. This is when they want you to talk about processes versus threads, and the fact that Python has a good multiprocessing library. We could also farm out requests to a compute pool or a job queue like Celery. The global interpreter lock also doesn’t stop threads processing many input/output requests at the same time – the lock is shared whilst threads are waiting for the requests to finish and this is particularly effective on versions of Python after 3.2.
'''
