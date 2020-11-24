# Custom format of time
import time

# get time
now = time.time()

# format time as object
local_time = time.localtime(now)

# display different elements as time object
print(f"It is {local_time.tm_hour}:{local_time.tm_min:02d}")
print(f"on {local_time.tm_mday:02d}/{local_time.tm_mon:02d}/{local_time.tm_year}")