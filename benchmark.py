"""
Green-Cloud-Profiler Benchmarking Engine
Module: benchmark.py
Description: Benchmarks computational workloads across varying input sizes
             and logs energy/time performance metrics.
"""

from profiler import profile_workload
import json

def bubble_sort(arr):
    n = len(arr)
    arr_copy = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy

def builtin_sort(arr):
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy

def run_benchmarks():
    input_sizes = [1000, 2500, 5000, 7500, 10000]
    benchmark_data = {
        "bubble_sort": [],
        "builtin_sort": []
    }

    print("Starting Comparative Energy Benchmarks...")

    for size in input_sizes:
        raw_data = list(range(size, 0, -1))
        
        # Profile Bubble Sort - O(N^2)
        _, bubble_metrics = profile_workload(bubble_sort, raw_data)
        bubble_metrics["input_size"] = size
        benchmark_data["bubble_sort"].append(bubble_metrics)
        
        # Profile Built-in Timsort - O(N log N)
        _, builtin_metrics = profile_workload(builtin_sort, raw_data)
        builtin_metrics["input_size"] = size
        benchmark_data["builtin_sort"].append(builtin_metrics)
        
        print(f"Completed size N = {size}")

    # Export benchmark metrics to JSON
    with open("benchmark_results.json", "w") as f:
        json.dump(benchmark_data, f, indent=4)
        
    print("\nBenchmark complete! Results saved to benchmark_results.json")

if __name__ == "__main__":
    run_benchmarks()