# Green-Cloud-Profiler 🌿⚡

`Green-Cloud-Profiler` is a lightweight Python dynamic profiling engine designed to benchmark CPU runtime performance, track process memory footprints, and measure floating-point throughput for deep learning workloads (PyTorch). Built for system resource monitoring and sustainable green cloud compute optimization.

---

## 🚀 Key Features

* **Deterministic CPU Benchmarking**: High-resolution execution timing via high-precision performance counters.
* **ML Workload Analytics**: Automated PyTorch tensor matrix multiplication profiling ($4000 \times 4000$).
* **Memory Tracking**: Real-time Resident Set Size (RSS) peak RAM consumption logging using `psutil`.
* **Automated Data Pipelines**: Multi-module pipeline outputting structured JSON telemetry (`benchmark_results.json`, `ml_benchmark_results.json`).
* **Visual Telemetry**: Matplotlib visual engine generating resource comparison charts (`benchmark_plot.png`).

---

## 🛠 Tech Stack

* **Language**: Python 3.14+
* **ML/Compute Engine**: PyTorch
* **System Metrics**: `psutil`
* **Data Visualization**: `matplotlib`
* **Format & Storage**: JSON Data Streams

---

## 📥 Installation & Setup

1. **Clone Repository**:
   ```bash
   git clone [https://github.com/mohdmujtaba5200/Green-Cloud-Profiler.git](https://github.com/mohdmujtaba5200/Green-Cloud-Profiler.git)
   cd Green-Cloud-Profiler