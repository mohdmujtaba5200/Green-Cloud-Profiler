import time
import torch

def profile_matrix_multiplication(size=4000):
    print(f"--- Benchmarking Matrix Multiplication (Size: {size}x{size}) ---")
    
    # 1. CPU Benchmark
    start_cpu = time.perf_counter()
    x_cpu = torch.randn(size, size, device="cpu")
    y_cpu = torch.randn(size, size, device="cpu")
    z_cpu = torch.matmul(x_cpu, y_cpu)
    end_cpu = time.perf_counter()
    cpu_duration = end_cpu - start_cpu
    print(f"CPU Execution Time: {cpu_duration:.4f} seconds")

    # 2. GPU Benchmark (CUDA check)
    if torch.cuda.is_available():
        start_gpu = time.perf_counter()
        x_gpu = torch.randn(size, size, device="cuda")
        y_gpu = torch.randn(size, size, device="cuda")
        z_gpu = torch.matmul(x_gpu, y_gpu)
        torch.cuda.synchronize()  # Force GPU sync before stopping timer
        end_gpu = time.perf_counter()
        gpu_duration = end_gpu - start_gpu
        print(f"GPU Execution Time: {gpu_duration:.4f} seconds")
    else:
        print("CUDA Device Not Available. (Running CPU-only mode)")

if __name__ == "__main__":
    profile_matrix_multiplication()