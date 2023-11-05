import sys
import time
import mergesort
import two_pivot_block_quicksort
from memory_profiler import memory_usage


def profile_runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime_milliseconds = (end_time - start_time) * 1000
        print(f"Runtime of {func.__name__} is {runtime_milliseconds:.2f} ms")
        return result
    return wrapper


def profile_memory(func):
    def wrapper(*args, **kwargs):
        def target():
            return func(*args, **kwargs)
        
        mem_usage, retval = memory_usage(target, interval=.1, timeout=1, retval=True, max_usage=True)
        print(f"Memory usage of {func.__name__} is {mem_usage} MiB.")
        return retval
    return wrapper


@profile_memory
# @profile_runtime
def sort_mergesort(arr):
    return mergesort.sort(arr)


@profile_memory
# @profile_runtime
def sort_two_pivot_block_quicksort(arr):
    return two_pivot_block_quicksort.sort(arr)


def read_from_file_to_list(filename):
    with open(filename, 'r') as f:
        content = [int(line.strip()) for line in f.readlines()]
    return content


def save_to_file(filename, dataset):
    with open(filename, 'w') as f:
        for number in dataset:
            f.write(f"{number}\n")


def main():
    filename = "2^16_sorted.txt"
    arr = read_from_file_to_list(filename)
    arr = sort_two_pivot_block_quicksort(arr)
    # save_to_file("2^9_sorted.txt", arr)


if __name__ == '__main__':
    main()