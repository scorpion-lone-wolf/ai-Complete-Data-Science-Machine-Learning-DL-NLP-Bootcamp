import multiprocessing
import time


# CPU heavy task
def print_number():
    for i in range(50000):
        pass
    print("Completed print_number")


def print_variable():
    for i in range(500000):
        pass
    print("Completed print_variable")


if __name__ == "__main__":
    # Record the start time of the program
    prev_time = time.time()

    process1 = multiprocessing.Process(target=print_number, name="process1")
    process2 = multiprocessing.Process(target=print_variable, name="process2")

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Completed at", time.time() - prev_time)
