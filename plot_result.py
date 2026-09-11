"""
Green-Cloud-Profiler Visualizer
Module: plot_results.py
Description: Reads benchmark JSON data and generates clean energy & execution 
             time performance comparison plots using matplotlib.
"""

import json
import matplotlib.pyplot as plt

def generate_plots():
    # Load JSON benchmark data
    with open("benchmark_results.json", "r") as f:
        data = json.load(f)

    sizes = [item["input_size"] for item in data["bubble_sort"]]
    bubble_energy = [item["estimated_energy_joules"] for item in data["bubble_sort"]]
    builtin_energy = [item["estimated_energy_joules"] for item in data["builtin_sort"]]
    
    bubble_time = [item["execution_time_sec"] for item in data["bubble_sort"]]
    builtin_time = [item["execution_time_sec"] for item in data["builtin_sort"]]

    # Create figure with 2 subplots (Time vs Energy)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Plot 1: Execution Time
    ax1.plot(sizes, bubble_time, marker='o', label='Bubble Sort O(N^2)', color='#e74c3c')
    ax1.plot(sizes, builtin_time, marker='s', label='Timsort O(N log N)', color='#2ecc71')
    ax1.set_title('Execution Time Comparison (Lower is Better)')
    ax1.set_xlabel('Input Size (N)')
    ax1.set_ylabel('Time (Seconds)')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend()

    # Plot 2: Estimated Energy Footprint
    ax2.plot(sizes, bubble_energy, marker='o', label='Bubble Sort O(N^2)', color='#e74c3c')
    ax2.plot(sizes, builtin_energy, marker='s', label='Timsort O(N log N)', color='#2ecc71')
    ax2.set_title('Estimated Energy Footprint (Lower is Better)')
    ax2.set_xlabel('Input Size (N)')
    ax2.set_ylabel('Energy (Joules)')
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.legend()

    plt.tight_layout()
    plt.savefig("energy_benchmark_plot.png", dpi=300)
    print("Graph generated successfully as energy_benchmark_plot.png!")

if __name__ == "__main__":
    generate_plots()