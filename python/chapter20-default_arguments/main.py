# default arguements = a default value for certain parameters.
# default is used when argument is omitted and make your function more felxible
# reducing the number of arguments
# 1.positional
# 2.default
# 3.keyword
# 4.arbitrary

import time


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1-discount)*(1+tax)


print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, .2, 0))


def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(30,15)