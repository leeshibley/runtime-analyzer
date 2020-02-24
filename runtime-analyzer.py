#!/usr/bin/env python
# coding: utf-8

import random
import time
import sys

import SortingMethods as sm

if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 8)

filename = "runtime_data.csv"

print("\n", "=" * 68)
length = int(input("How many values would you like to sort? "))

a = 0
b = int(input("What is the highest value you would like in the array? "))

n_runs = int(input("How many runs would you like to do? "))

print("\n", "=" * 68)

for n in range(n_runs):
    ## create new random list
    nums = []
    for i in range(length):
        nums.append(random.randint(a, b))
    alg = sm.SortingMethod(nums)

    print(f"Run {n + 1} of {n_runs}")
    
    runtime_string = f""

    if length <= 10000:  ## Inefficient (O(n^2)) algorithms omitted for large n
        t_bubblesort_0 = time.time()
        alg.bubblesort()
        t_bubblesort_1 = time.time()

        bubblesort_time = t_bubblesort_1 - t_bubblesort_0
        print(f"Bubble Sort ------ {round(bubblesort_time, 4)} seconds")

        t_selectionsort_0 = time.time()
        alg.selectionsort()
        t_selectionsort_1 = time.time()

        selectionsort_time = t_selectionsort_1 - t_selectionsort_0
        print(f"Selection Sort --- {round(selectionsort_time, 4)} seconds")

        t_insertionsort_0 = time.time()
        alg.insertionsort()
        t_insertionsort_1 = time.time()

        insertionsort_time = t_insertionsort_1 - t_insertionsort_0
        print(f"Insertion Sort --- {round(insertionsort_time, 4)} seconds")
        
        runtime_string = runtime_string + f",{bubblesort_time},{selectionsort_time},{insertionsort_time}"
    else:
        runtime_string = runtime_string + f",NA,NA,NA"

    t_mergesort_0 = time.time()
    alg.mergesort()
    t_mergesort_1 = time.time()

    mergesort_time = t_mergesort_1 - t_mergesort_0
    print(f"Merge Sort ------- {round(mergesort_time, 4)} seconds")
    
    runtime_string = runtime_string + f",{mergesort_time}"

    if length <= 1000000:
        t_quicksort_0 = time.time()
        alg.quicksort()
        t_quicksort_1 = time.time()

        quicksort_time = t_quicksort_1 - t_quicksort_0
        print(f"Quick Sort ------- {round(quicksort_time, 4)} seconds")
        
        runtime_string = runtime_string + f",{quicksort_time}"
    else:
        runtime_string = runtime_string + f",NA"

    with open(f"{filename}", "a+") as f:
        data = f"{length},{b},{n + 1}" + runtime_string + "\n"
        f.write(data)
    f.close()
    print(f"Results written to file {filename}")

    print("=" * 68, "\n")
