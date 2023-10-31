def two_pivot_quicksort(arr, low, high):
    if low < high:
        # Make sure p1 <= p2
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        
        # The two pivots
        p1, p2 = arr[low], arr[high]
        
        i = low + 1
        lt, gt = low + 1, high - 1
        while i <= gt:
            if arr[i] < p1:
                arr[i], arr[lt] = arr[lt], arr[i]
                lt += 1
                i += 1
            elif arr[i] > p2:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        
        # Swap the pivots into their correct positions
        arr[low], arr[lt-1] = arr[lt-1], arr[low]
        arr[high], arr[gt+1] = arr[gt+1], arr[high]
        
        # Recursive calls for the three sub-arrays
        two_pivot_quicksort(arr, low, lt - 2)  # Before p1
        two_pivot_quicksort(arr, lt, gt)       # Between p1 and p2
        two_pivot_quicksort(arr, gt + 2, high) # After p2

def sort(arr):
    two_pivot_quicksort(arr, 0, len(arr) - 1)
    return arr

def main():
    arr = [24, 8, 42, 75, 29, 77, 38, 57]
    print(sort(arr))


if __name__ == "__main__":
    main()
