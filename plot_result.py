import json
import os
import matplotlib.pyplot as plt

def generate_benchmark_plot():
    files = {
        "CPU Standard": "benchmark_results.json",
        "PyTorch ML": "ml_benchmark_results.json"
    }
    
    workloads = []
    times = []
    memories = []

    for name, filepath in files.items():
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                data = json.load(f)
                workloads.append(name)
                times.append(data.get("execution_time_seconds", 0))
                memories.append(data.get("memory_peak_mb", 0))

    if not workloads:
        print("No benchmark JSON files found.")
        return

    fig, ax1 = plt.subplots(figsize=(8, 5))

    color = 'tab:blue'
    ax1.set_xlabel('Workload Type')
    ax1.set_ylabel('Execution Time (s)', color=color)
    bars = ax1.bar(workloads, times, color=color, width=0.3, label='Time (s)')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Peak Memory (MB)', color=color)
    ax2.plot(workloads, memories, color=color, marker='o', linewidth=2, label='Memory (MB)')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title("Green Cloud Profiler - Execution & Memory Metrics")
    fig.tight_layout()
    plt.savefig("benchmark_plot.png", dpi=300)
    print("Chart saved to benchmark_plot.png")

if __name__ == "__main__":
    generate_benchmark_plot()