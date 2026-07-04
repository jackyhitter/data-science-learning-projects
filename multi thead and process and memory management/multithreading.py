## multithreading 
### when to use multi threading
## I/O - bound tasks : tasts that spend more time waiting for i/o operations (e.g. file operation )
## concurrent execution : when you want to improve the throughput of your application 

import threading
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(2)
        print(f"Number: {i}")
        
def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        time.sleep(2)
        print(f"Letter: {letter}")

## create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()
### start the threads
t1.start()
t2.start()

#### wait for the threads to finish
t1.join()
t2.join()

finished_time = time.time() - t
print(f"Finished in {finished_time} seconds")
