import json
import os
import time
import psutil
import torch

def get_process_memory_mb():
    """Returns current process RAM usage in Megabytes."""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)

def profile_matrix_multiplication(size=4000):
    print(f"--- Benchmarking PyTorch Workload (Size: {size}x{size}) ---")
    
    mem_before = get_process_memory_mb()
    start_time = time.perf_counter()

    # Create tensors & compute matrix multiplication
    x = torch.randn(size, size, device="cpu")
    y = torch.randn(size, size, device="cpu")
    z = torch.matmul(x, y)

    end_time = time.perf_counter()
    mem_after = get_process_memory_mb()

    execution_time = round(end_time - start_time, 4)
    mem_used = round(mem_after - mem_before, 2)

    metrics = {
        "workload": "Matrix Multiplication",
        "matrix_size": f"{size}x{size}",
        "device": "CPU",
        "execution_time_seconds": execution_time,
        "memory_peak_mb": mem_used,
        "status": "Success"
    }

    print(f"Execution Time : {execution_time}s")
    print(f"RAM Peak Usage : {mem_used} MB")

    # Export metrics to JSON
    with open("ml_benchmark_results.json", "w") as f:
        json.dump(metrics, f, indent=4)
        
    print("Saved results to ml_benchmark_results.json")

if __name__ == "__main__":
    profile_matrix_multiplication()