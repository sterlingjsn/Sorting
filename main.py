import random
import time
import csv
import Graph


def bubble_sort(arr):
    a = arr
    n = len(a)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def insertion_sort(arr):
    a = arr
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key


def partition(a, low, high):
    i = low - 1
    pivot = a[high]

    for j in range(low, high):
        if a[j] <= pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def quick_sort_1(a, low, high):
    st = [0] * (high - low + 1)
    top = -1

    top = top + 1
    st[top] = low
    top = top + 1
    st[top] = high

    while top >= 0:
        high = st[top]
        top = top - 1
        low = st[top]
        top = top - 1
        pi = partition(a, low, high)

        if pi - 1 > low:
            top = top + 1
            st[top] = low
            top = top + 1
            st[top] = pi - 1

        if pi + 1 < high:
            top = top + 1
            st[top] = pi + 1
            top = top + 1
            st[top] = h


def quick_sort(arr):
    a = arr
    quick_sort_1(a, 0, len(a) - 1)


def tim_sort(arr):
    a = arr
    a.sort()


if __name__ == '__main__':

    list_sizes = [10, 50, 100, 500, 1000, 5000]
    functions = [bubble_sort, insertion_sort, quick_sort, tim_sort]

    with open("results.csv", mode="w", newline="") as csvfile:
        fieldnames = ['n', 'bubble sort', 'insertion sort', 'quick sort', 'tim sort']
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(fieldnames)

        for n in list_sizes:

            sorting_time = {'bubble_sort': 0, 'insertion_sort': 0, 'quick_sort': 0, 'tim_sort': 0}

            for i in range(0, 10):
                a = [random.randint(1, n) for i in range(n)]

                for sorting in functions:
                    t_start = time.perf_counter()
                    sorting(a)
                    t_stop = time.perf_counter()

                    sorting_time[sorting.__name__] += t_stop - t_start

            results_row = [n]
            for value in sorting_time.values():
                value = value / 10
                results_row.append(value)

            csvwriter.writerow(results_row)
