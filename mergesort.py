def sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    # Compare each index of the two halves and merge them
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # Add any remaining elements of left (if any)
    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx += 1

    # Add any remaining elements of right (if any)
    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx += 1

    return merged


def main():
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original Array:", arr)
    sorted_arr = sort(arr)
    print("Sorted Array:", sorted_arr)


if __name__ == '__main__':
    main()