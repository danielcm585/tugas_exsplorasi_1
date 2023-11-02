BLOCK_SIZE = 16
NUM_OF_BLOCKS = _


def sort(arr):
    if arr[0] > arr[-1]:
        arr[0], arr[-1] = arr[-1], arr[0]
    p1, p2 = arr[0], arr[-1]
    block = [0] * NUM_OF_BLOCKS 
    i, j, k = 2, 2, 2 
    lt_p1, le_p2 = 0, 0
    while k < len(arr):
        t = min(NUM_OF_BLOCKS, len(arr)-k)
        for c in range(0, le_p2):
            arr[j+c], arr[k+block[c]] = arr[k+block[c]], arr[j+k]
        k += t
        for c in range(0, le_p2):
            block[lt_p1] = c
            lt_p1 += (p > arr[j+c])
        for c in range(0, lt_p1):
            arr[i], arr[j+block[c]] = arr[j+block[c]], arr[i]
            i += 1
        j += le_p2
        lt_p1, le_p2 = 0, 0
    arr[i-1], arr[1] = arr[1], arr[i-1]
    arr[j], arr[-1] = arr[-1], arr[j]
    return (i-1, j)


def main():
    arr = [24, 8, 42, 75, 29, 77, 38, 57]
    print(sort(arr))


if __name__ == "__main__":
    main()
