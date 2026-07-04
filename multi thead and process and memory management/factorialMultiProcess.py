'''
                        MultiProcessing
Factorial cal for large number, 
distribute the workload to multiple CPU cores, imporving performance henceforth;

'''
import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(100000)

# def computeFactorial(num):
#     print(f"Computing factorial for {num}")
#     result = math.factorial(num)
#     print(f'Factorial of {num} is {result}')
#     return result

# if __name__ == "__main__":
#     numbers = [5000, 6000, 7000, 8000]
#     start_time = time.time()
    
#     ## creating the pool of workers
#     with multiprocessing.Pool() as pool:
#         results = pool.map(computeFactorial, numbers)
        
#     end_time = time.time()
    
#     print(f"Results: {results}")
#     print(f"Time Taken : {end_time - start_time} second")

for _ in range(3):
    print(".", end="")
    time.sleep(1)