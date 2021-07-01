import time as t
print(t.ctime()) 		# Sun Jan 25 10:42:17 2015
                        # Fri Oct 30 21:59:45 2020

t1=t.time()
pass
t2=t.time()

print(f"Time took to load: {t2-t1} seconds.")

print(dir(t)) 
'''
['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 
'altzone', 'asctime', 'ctime', 'daylight', 'get_clock_info', 
'gmtime', 'localtime', 'mktime', 
'monotonic', 'monotonic_ns', 
'perf_counter', 'perf_counter_ns', 'process_time', 
'process_time_ns', 
'sleep', 'strftime', 'strptime', 'struct_time', 
'thread_time', 'thread_time_ns', 
'time', 'time_ns', 
'timezone', 'tzname']
'''