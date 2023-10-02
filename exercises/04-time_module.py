"""
importing modules import <module> as t
"""

import time as t

t.localtime()

timeNow = t.localtime()
# print local time by hour and minute
print(
    "Transaction completed on: ", str(timeNow.tm_hour) + "h" + str(timeNow.tm_min), "m"
)

# timestamp = sec passed since unix epoch Jan 1st 1970 -->
# helpful to make calculations with dates use in shipments and deliveries

t.time()
t.time()

timeNow = t.time()
deliveryTime = timeNow + 604800  # 7 days

# share any information to the user in any format you want
print(deliveryTime)

# output any date information to the user
t.localtime(deliveryTime)

# can be used to make a countdown timer
t.sleep(10)
