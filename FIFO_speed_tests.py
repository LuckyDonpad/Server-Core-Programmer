from task2 import FIFOLinkedListWay, FIFOListWay
import timeit

time_sum = 0

for _ in range(1000):
    begin = timeit.default_timer()
    fifo = FIFOListWay(1000)
    end = timeit.default_timer()
    time_sum += end - begin

print(F'initialization speed for FIFOListWay: {time_sum / 1000}')

time_sum = 0

for _ in range(1000):
    begin = timeit.default_timer()
    fifo = FIFOLinkedListWay(1000)
    end = timeit.default_timer()
    time_sum += end - begin
print(F'initialization speed for FIFOLinkedListWay: {time_sum / 1000}')

time_sum = 0

for _ in range(1000):
    fifo = FIFOListWay(1000)
    begin = timeit.default_timer()

    end = timeit.default_timer()
    for j in range(10000):
        fifo.push(j)
    time_sum += end - begin

print(F'push speed for FIFOListWay: {time_sum / 1000}')

time_sum = 0

for _ in range(1000):
    fifo = FIFOLinkedListWay(1000)
    begin = timeit.default_timer()

    end = timeit.default_timer()
    for j in range(10000):
        fifo.push(j)
    time_sum += end - begin

print(F'push speed for FIFOLinkedListWay: {time_sum / 1000}')

time_sum = 0

for _ in range(1000):
    fifo = FIFOListWay(1000)
    begin = timeit.default_timer()

    end = timeit.default_timer()
    for j in range(10000):
        fifo.pop()
    time_sum += end - begin

print(F'push speed for FIFOListWay: {time_sum / 1000}')

time_sum = 0

for _ in range(1000):
    fifo = FIFOLinkedListWay(1000)
    begin = timeit.default_timer()

    end = timeit.default_timer()
    for j in range(10000):
        fifo.pop()
    time_sum += end - begin

print(F'push speed for FIFOLinkedListWay: {time_sum / 1000}')
