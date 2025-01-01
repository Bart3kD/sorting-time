import time
import random

from bubbleSort import bubble_sort
from insertionSort import insertion_sort
from quickSort import quick_sort
from mergeSort import merge_sort
from timSort import tim_sort
from introsort import intro_sort


def generate_random_list(size: int) -> list[int]:
    return [random.randint(1, 10000) for _ in range(size)]

def measure_sort_time(sort_function, data: list[int]) -> float:
    data_copy = data[:]
    start_time = time.time()
    sort_function(data_copy)
    end_time = time.time()
    return round(end_time - start_time, 3)

data_sizes = [100, 1000, 10000]
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Tim Sort": tim_sort,
    "Intro Sort": intro_sort,
    "Python Sort": lambda x: x.sort(),
}

print(f"{'Rozmiar danych':<15} | {' | '.join(algorithms.keys()):<70}")
print("-" * 110)

for size in data_sizes:
    data = generate_random_list(size)
    results = [f"{measure_sort_time(alg, data):<10}" for alg in algorithms.values()]
    print(f"{size:<15} | {' | '.join(results):<70}")