"""
Green-Cloud-Profiler Engine
Module: profiler.py
Description: A lightweight utility to profile execution time, CPU usage, 
             memory consumption, and estimated energy footprint of workloads.
"""

import time
import psutil
import os

def profile_workload(func, *args, **kwargs):
    """
    Executes a target function while monitoring execution time,
    average CPU utilization, peak memory footprint, and estimated energy.
    """
    process = psutil.Process(os.getpid())
    
    # Measure baseline resources
    start_memory = process.memory_info().rss / (1024 * 1024)  # MB
    start_cpu_time = process.cpu_times()
    start_time = time.perf_counter()
    
    # Execute target workload
    result = func(*args, **kwargs)
    
    # Measure post-execution resources
    end_time = time.perf_counter()
    end_cpu_time = process.cpu_times()
    end_memory = process.memory_info().rss / (1024 * 1024)  # MB
    
    # Calculate performance metrics
    execution_time = end_time - start_time  # seconds
    user_cpu_time = end_cpu_time.user - start_cpu_time.user
    system_cpu_time = end_cpu_time.system - start_cpu_time.system
    total_cpu_time = user_cpu_time + system_cpu_time
    
    # Estimated Energy calculation (Standard TDP proxy model ~ 35W per active core)
    estimated_power_watts = 35.0  
    estimated_energy_joules = estimated_power_watts * total_cpu_time
    
    metrics = {
        "execution_time_sec": round(execution_time, 6),
        "total_cpu_time_sec": round(total_cpu_time, 6),
        "peak_memory_mb": round(max(start_memory, end_memory), 2),
        "estimated_energy_joules": round(estimated_energy_joules, 6)
    }
    
    return result, metrics


if __name__ == "__main__":
    # Test Workload: CPU-bound operation (Sorting 1,000,000 elements)
    print("Running initial Green-Cloud-Profiler test...")
    
    def sample_workload():
        data = list(range(1000000, 0, -1))
        data.sort()
        return len(data)

    _, results = profile_workload(sample_workload)
    
    print("\n--- Benchmark Results ---")
    print(f"Execution Time : {results['execution_time_sec']} seconds")
    print(f"CPU Time       : {results['total_cpu_time_sec']} seconds")
    print(f"Peak Memory    : {results['peak_memory_mb']} MB")
    print(f"Est. Energy    : {results['estimated_energy_joules']} Joules")