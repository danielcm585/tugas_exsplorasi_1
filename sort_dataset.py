import time
import quicksort
import two_pivot_block_quicksort


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime_milliseconds = (end_time - start_time) * 1000
        print(f"Runtime of {func.__name__} is {runtime_milliseconds:.2f} ms")
        return result
    return wrapper

@timer
def sort_quicksort(arr):
    return quicksort.sort(arr)

@timer
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


filename = "2^16.txt"
arr = read_from_file_to_list(filename)
arr = sort_two_pivot_block_quicksort(arr)
# save_to_file("2^9_sorted.txt", arr)
