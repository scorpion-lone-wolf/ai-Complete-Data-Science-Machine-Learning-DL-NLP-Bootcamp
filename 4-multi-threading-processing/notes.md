# Threading and Multiprocessing Notes

These notes explain the four files in this folder in simple language.

## Big Picture

Python can run multiple tasks in different ways:

1. **Threading**
   - Uses multiple threads inside the same Python program.
   - Best for **I/O-bound tasks**.
   - Example: downloading files, reading files, API calls, waiting for database response.

2. **Multiprocessing**
   - Uses multiple separate Python processes.
   - Best for **CPU-bound tasks**.
   - Example: heavy calculations, image processing, machine learning computations.

## I/O-Bound vs CPU-Bound

| Type | Meaning | Best Tool |
| --- | --- | --- |
| I/O-bound | Program spends time waiting | Threading |
| CPU-bound | Program spends time calculating | Multiprocessing |

### I/O-bound example

Downloading a file:

```python
time.sleep(5)
```

Here the program is mostly waiting. Threads are useful because while one thread waits, another thread can work.

### CPU-bound example

Running a big loop:

```python
for _ in range(5000000):
    pass
```

Here the CPU is busy. Multiprocessing is useful because separate processes can use separate CPU cores.

## Main Difference

| Feature | Threading | Multiprocessing |
| --- | --- | --- |
| Runs in | Same process | Separate processes |
| Memory | Shared memory | Separate memory |
| Best for | Waiting tasks | Calculation tasks |
| Startup cost | Lower | Higher |
| Python GIL issue | Affected for CPU work | Avoids GIL |

## What Is GIL?

GIL means **Global Interpreter Lock**.

In CPython, only one thread can execute Python bytecode at one time. This means threads are not great for heavy CPU calculations.

But threads are still useful for I/O tasks because while one thread is waiting, another thread can run.

Multiprocessing avoids this issue because each process has its own Python interpreter.

## File 1: `1-multithreading.py`

This file shows basic manual threading.

### What happens

There are two functions:

```python
print_number()
print_variable()
```

Each function waits using:

```python
time.sleep(1)
```

Then two threads are created:

```python
thread1 = threading.Thread(target=print_number, name="thread1")
thread2 = threading.Thread(target=print_variable, name="thread2")
```

Then both are started:

```python
thread1.start()
thread2.start()
```

### Important methods

| Code | Meaning |
| --- | --- |
| `threading.Thread(...)` | Creates a new thread |
| `target=print_number` | Function that the thread will run |
| `start()` | Starts the thread |
| `join()` | Waits until the thread finishes |
| `threading.current_thread().name` | Shows which thread is running |

### Simple understanding

Without threading:

```text
print numbers first
then print letters
```

With threading:

```text
print numbers and letters together
```

This is useful because both functions spend time waiting.

## File 2: `2-thread-pool-executor.py`

This file shows thread pooling.

Instead of manually creating every thread, Python manages a group of reusable threads.

### What is a thread pool?

A thread pool is a fixed group of worker threads.

In your code:

```python
with ThreadPoolExecutor(max_workers=3) as executor:
```

This means:

```text
Create a pool with 3 threads.
Only 3 downloads can run at the same time.
Other downloads wait in a queue.
```

### What happens

You have 10 files:

```python
files = range(1, 11)
```

You submit each file download to the thread pool:

```python
future = executor.submit(download_file, file_id)
```

### What is `Future`?

A `Future` is a placeholder for a result that will be available later.

When you submit a task, it may be:

| Future state | Meaning |
| --- | --- |
| pending | Waiting to start |
| running | Currently executing |
| finished | Completed |
| failed | Error happened |

### What does `as_completed()` do?

```python
for future in as_completed(futures):
    print(future.result())
```

This gives results as soon as each task finishes.

It does not follow the original order. It follows completion order.

### Simple understanding

You have 10 downloads and 3 workers:

```text
First 3 downloads start
Remaining 7 wait
When one finishes, the next one starts
```

This is better than creating 10 manual threads yourself.

## File 3: `3-multiprocess.py`

This file shows basic manual multiprocessing.

### What happens

There are two CPU-heavy functions:

```python
print_number()
print_variable()
```

They run loops:

```python
for i in range(50000):
    pass
```

and:

```python
for i in range(500000):
    pass
```

Then two processes are created:

```python
process1 = multiprocessing.Process(target=print_number, name="process1")
process2 = multiprocessing.Process(target=print_variable, name="process2")
```

Then both are started:

```python
process1.start()
process2.start()
```

### Important methods

| Code | Meaning |
| --- | --- |
| `multiprocessing.Process(...)` | Creates a new process |
| `target=print_number` | Function that process will run |
| `start()` | Starts the process |
| `join()` | Waits until the process finishes |

### Why use `if __name__ == "__main__"`?

This is very important in multiprocessing:

```python
if __name__ == "__main__":
```

It prevents child processes from accidentally starting the whole script again.

Always use this guard when writing multiprocessing code.

## File 4: `4-proccess-pool-executor.py`

This file shows process pooling.

Instead of manually creating every process, Python manages a group of reusable processes.

### What is a process pool?

A process pool is a fixed group of worker processes.

In your code:

```python
with ProcessPoolExecutor(max_workers=3) as executor:
```

This means:

```text
Create a pool with 3 processes.
Only 3 CPU-heavy tasks run at the same time.
Other tasks wait in a queue.
```

### What happens

You have this list:

```python
numbers = [1, 2, 3, 4, 5]
```

But inside the loop, each task receives the same value:

```python
future = executor.submit(cpu_heavy_task, (5000000))
```

So the loop submits 5 tasks, and each task runs:

```python
cpu_heavy_task(5000000)
```

### Important point

This code:

```python
for i in numbers:
    future = executor.submit(cpu_heavy_task, (5000000))
```

does not use `i`.

If you wanted each task to use a different number, you could write:

```python
future = executor.submit(cpu_heavy_task, i)
```

But for learning process pools, your current code is still okay because it submits multiple CPU-heavy tasks.

### Simple understanding

You submit 5 heavy tasks and allow 3 processes:

```text
First 3 tasks start
Remaining 2 wait
When one finishes, the next one starts
```

## Pooling vs Manual Creation

| Style | Example | Meaning |
| --- | --- | --- |
| Manual threading | `threading.Thread` | You create each thread yourself |
| Thread pool | `ThreadPoolExecutor` | Python manages reusable threads |
| Manual multiprocessing | `multiprocessing.Process` | You create each process yourself |
| Process pool | `ProcessPoolExecutor` | Python manages reusable processes |

## When To Use What?

| Situation | Use |
| --- | --- |
| One or two simple waiting tasks | `threading.Thread` |
| Many waiting tasks | `ThreadPoolExecutor` |
| One or two CPU-heavy tasks | `multiprocessing.Process` |
| Many CPU-heavy tasks | `ProcessPoolExecutor` |

## Easy Memory Trick

Use this rule:

```text
Waiting work  -> Threading
CPU work      -> Multiprocessing
Many tasks    -> Executor pool
Few tasks     -> Manual Thread/Process
```

## Final Summary

Threading helps when tasks spend time waiting.

Multiprocessing helps when tasks spend time calculating.

Thread pools and process pools are cleaner when you have many tasks because you do not need to manually create and manage every thread or process.

