# Explanation:
# Importing threading: The threading module is used to create and manage threads.
# Defining Functions: Two functions(task1 and task2) simulate separate tasks.
# Creating Threads: threading.Thread creates threads and assigns a function to each.
# Starting Threads: start() begins thread execution.
# Joining Threads: join() ensures the main program waits for threads to complete before proceeding.



import threading
import time

# Function to simulate a time-consuming task


def task1():
    for i in range(5):
        print(f"Task 1 - Count: {i}")
        time.sleep(1)  # Simulate some work by sleeping for 1 second

# Another function to simulate a time-consuming task


def task2():
    for i in range(5):
        print(f"Task 2 - Count: {i}")
        time.sleep(1.5)  # Simulate some work by sleeping for 1.5 seconds


# Create threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both tasks completed!")
