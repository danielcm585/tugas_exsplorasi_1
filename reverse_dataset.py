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
arr.reverse()
save_to_file("2^16_reversed.txt", arr)
