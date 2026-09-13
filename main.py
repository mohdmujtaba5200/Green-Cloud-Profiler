import os
import sys
import time
from profiler import profile_workload
from profile_ml import profile_matrix_multiplication
from plot_result import generate_benchmark_plot

def sample_cpu_task():
    """Sample CPU-bound workload for standard profiling."""
    total = 0
    for i in range(10_000_000):
        total += i
    return total

def run_pipeline():
    print("==========================================")
    print("   STARTING GREEN CLOUD PROFILER SUITE   ")
    print("==========================================\n")
    
    print("[1/3] Running CPU Standard Profiler...")
    profile_workload(sample_cpu_task)
    
    print("\n[2/3] Running PyTorch ML Profiler...")
    profile_matrix_multiplication()
    
    print("\n[3/3] Generating Analytics & Plots...")
    generate_benchmark_plot()
    
    print("\n==========================================")
    print("   PROFILING COMPLETE - RESULTS GENERATED ")
    print("==========================================")

if __name__ == "__main__":
    run_pipeline()