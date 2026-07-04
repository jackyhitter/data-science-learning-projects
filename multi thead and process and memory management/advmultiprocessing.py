### Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(number):
    time.sleep(1)
    return f"Square: {number * number}"

numbers = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9]

t = time.time()

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers = 3) as executor:
        results = executor.map(square_numbers, numbers)

    for result in results:
        print(result)
        
    finished = time.time() - t
    print(f"Finished in {finished} seconds")
