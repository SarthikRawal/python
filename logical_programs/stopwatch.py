# 6. Stopwatch simulation 
import time

def start_stopwatch():
    return time.time()

def end_stopwatch(start_time):
    return time.time() - start_time

if __name__ == "__main__":
    input("Please Enter to start the stopwatch ⏱️")
    start_time = start_stopwatch()

    input("stop the stopwatch ->⏱️")
    elapsed_time = end_stopwatch(start_time)

    print(f"Elapsed time: {elapsed_time:.2f} seconds")