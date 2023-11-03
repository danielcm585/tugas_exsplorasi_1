BLOCK_SIZE = 16


def two_pivot_quicksort(arr, l, r):
    if (l < r):
        i, j = block_lomuto_two_pivot(arr,l,r)
        two_pivot_quicksort(arr,l,i-1)
        two_pivot_quicksort(arr,i+1,j-1)
        two_pivot_quicksort(arr,j+1,r)


def block_lomuto_two_pivot(arr, l, r):
    if arr[l] > arr[r]: 
        arr[l], arr[r] = arr[r], arr[l]
    p1, p2 = arr[l], arr[r]
    block = [0] * BLOCK_SIZE
    i, j, k = l+1, l+1, l+1
    lt_p1, le_p2 = 0, 0
    while k < r:
        t = min(BLOCK_SIZE, r-k)
        for c in range(t):
            block[le_p2] = c
            le_p2 += (arr[k+c] <= p2)
        for c in range(le_p2):
            arr[j+c], arr[k+block[c]] = arr[k+block[c]], arr[j+c]
        k += t
        for c in range(le_p2):
            block[lt_p1] = c
            lt_p1 += (arr[j+c] < p1)
        for c in range(lt_p1):
            arr[i], arr[j+block[c]] = arr[j+block[c]], arr[i]
            i += 1
        j += le_p2
        lt_p1, le_p2 = 0, 0
    arr[i-1], arr[l] = arr[l], arr[i-1]
    arr[j], arr[r] = arr[r], arr[j]
    return (i-1, j)


def sort(arr):
    two_pivot_quicksort(arr, 0, len(arr)-1)
    return arr


def main():
    arr = [24, 8, 42, 75, 29, 77, 38, 57]
    print(sort(arr))


if __name__ == "__main__":
    main()
