def quicksort(arr, low, high):
    if low < high:
        # Temukan pivot element sehingga elemen lebih kecil daripada pivot
        # berada di sebelah kiri dan elemen yang lebih besar berada di sebelah kanan
        pi = lomuto_partition(arr, low, high)

        # Rekursif sort elemen sebelum dan sesudah partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def lomuto_partition(arr, low, high):
    # Menggunakan skema partisi Lomuto: pilih elemen paling kanan sebagai pivot
    pivot = arr[high]

    # Indeks untuk elemen yang lebih kecil
    i = low

    for j in range(low, high):
        # Jika elemen saat ini lebih kecil atau sama dengan pivot
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]  # tukar
            i = i + 1

    arr[i], arr[high] = arr[high], arr[i]  # tukar pivot ke posisi yang benar
    return i

def sort(arr):
    quicksort(arr, 0, len(arr) - 1)
    return arr

def main():
    arr = [24, 8, 42, 75, 29, 77, 38, 57]
    print(sort(arr))


if __name__ == '__main__':
    main()
