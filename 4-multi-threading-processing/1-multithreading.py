# Multithreading is used for I/O-bound tasks where work can run concurrently.
import threading
import time


# Function 1: prints numbers from 0 to 4
# Each iteration pauses for 1 second to show asynchronous behavior.
def print_number():
    for i in range(5):
        time.sleep(1)
        print(i, "from", threading.current_thread().name)


# Function 2: prints characters from the string "abcdef"
# It also pauses for 1 second before each print.
def print_variable():
    for v in "abcdef":
        time.sleep(1)
        print(v, "from", threading.current_thread().name)


# Record the start time of the program
prev_time = time.time()

# Create two threads and assign each one a task
thread1 = threading.Thread(target=print_number, name="thread1")
thread2 = threading.Thread(target=print_variable, name="thread2")

# Start both threads so they run concurrently
thread1.start()
thread2.start()

# Wait for both threads to finish before moving on
thread1.join()
thread2.join()

# Uncomment these lines to run the functions normally (without threading)
# print_number()
# print_variable()

# Calculate and print total execution time
end_time = time.time() - prev_time
print("Completed At", end_time)


# Notes:
# - This example shows how two tasks can run at the same time using threads.
# - The sleep(1) makes the concurrency visible because each thread waits before printing.
# - `threading.current_thread().name` shows which thread is currently executing the function.
# - `join()` ensures the main program waits until both threads are completed.
# - Without threads, the total time would be longer because the tasks would run one after another.
