import time
def print_number(low, high):
    print("Task running")
    sum = 0
    for i in range(low, high):
        print(i)
        sum += i
    print("Task complete")
    return sum

def caculate_sum(a, b):
    time.sleep(3)
    return a + b