## Processes that run in parallel
### CPU-Bound Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
## Parallel execution- Multiple cores of the CPU

import multiprocessing
import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"Square : {i*i}")

def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube : {i*i*i}")

square_number()
cube_number()

if __name__=="__main__":
    #create 2 processes
    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cube_number)

    t = time.time()
    #start the process
    p1.start()
    p2.start()

    #wait for the process to complete
    p1.join()
    p2.join()
    finished_time = time.time()-t
    print(finished_time)

