# record time between two events
import time

start = time.time()

while True:
    response = input("Enter to get lapsed time, q to quit: ")
    if response == "q":
        break
    else:
        now = time.time()
        lapsed = now - start
        start = now
        print(f"Lapsed time: {lapsed}")
        