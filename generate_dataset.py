import random


def generate_random_integers(n, lower_limit, upper_limit):
    return [random.randint(lower_limit, upper_limit) for _ in range(n)]

def save_to_file(filename, dataset):
    with open(filename, 'w') as f:
        for number in dataset:
            f.write(f"{number}\n")


dataset = generate_random_integers(2**16, 1, 10**9)
save_to_file("2^16.txt", dataset)