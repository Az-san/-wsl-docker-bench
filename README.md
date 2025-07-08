# Docker vs WSL Network Latency Comparison

A project to compare TCP communication performance between Docker Ubuntu containers and WSL Ubuntu environments with Windows PowerShell.

## About This Repository

### Purpose
- **Docker vs WSL Communication Performance Comparison**: Execute the same TCP communication test in both environments and measure performance differences quantitatively
- **ROS Development Environment Evaluation**: Measure network performance in ROS Noetic environment
- **Development Environment Selection Reference**: Provide indicators for environment selection when network performance is critical

### Measurement Content
- Ping-pong communication between TCP echo server/client
- Measurement of average latency and 99th percentile
- 10 rounds × 10,000 communication tests per environment

## File Structure

```
├── Dockerfile              # ROS Noetic + Python 3.9 environment setup
├── server.py               # TCP echo server (run on Windows PowerShell)
├── client.py               # Latency measurement client
├── test_loop.ps1           # Docker 10-round test script
├── test_wsl_loop.ps1       # WSL 10-round test script
├── compare_results.py      # Result comparison and analysis script
├── requirements.txt        # Python dependencies (currently empty)
├── entrypoint.sh          # Docker entrypoint
└── README.md              # This file
```

## About Dockerfile

### Environment Configuration
- **Base Image**: `ros:noetic-ros-core-focal` (Ubuntu 20.04 + ROS Noetic)
- **Python**: 3.9 (default setting)
- **Additional Packages**: 
  - ROS Noetic Desktop Full
  - PyTorch (CUDA 12.4 support)
  - X11, NVIDIA GPU support
  - Scientific computing libraries (numpy, scipy, matplotlib, pandas)

### Features
- **Japanese Locale Support**: `ja_JP.UTF-8`
- **NVIDIA GPU Support**: Container Toolkit compatible
- **Flexible Entrypoint**: Automatically loads ROS environment with `entrypoint.sh`
- **requirements.txt Support**: Python dependency management

## Docker Environment Startup Methods

### 1. Build Image
```bash
docker build -t ros-noetic-dev .
```

### 2. Basic Startup
```bash
# Interactive shell (for development)
docker run -it --rm ros-noetic-dev

# Background execution
docker run -d --name ros-container ros-noetic-dev
```

### 3. Communication Test Startup
```bash
# Server execution (port exposure)
docker run -d --name latency-server -p 50007:50007 ros-noetic-dev python3 server.py

# Client execution (file mount)
docker run --rm -v ${PWD}:/workspace ros-noetic-dev bash -c "cd /workspace && python3 client.py --host host.docker.internal"
```

### 4. Development Startup (Recommended)
```bash
# Development environment with file mount
docker run -it --rm -v ${PWD}:/workspace ros-noetic-dev

# Work inside container
cd /workspace
python3 server.py  # Start server
# In another terminal
python3 client.py --host host.docker.internal  # Execute client
```

## Environment Variables and Settings

### Docker Environment Variables
```bash
# NVIDIA GPU support
NVIDIA_VISIBLE_DEVICES=all
NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics

# Japanese locale
LANG=ja_JP.UTF-8
LC_ALL=ja_JP.UTF-8
```

### Working Directory
- **Inside Container**: `/workspace`
- **Mount**: Mount current host directory to `/workspace`

## Measurement Results (Summary)

| Environment | Average Latency | 99th Percentile |
|-------------|-----------------|-----------------|
| **Docker Ubuntu** | 0.315 ms | 1.224 ms |
| **WSL Ubuntu** | 0.083 ms | 0.183 ms |

**Conclusion**: WSL is **3.8x faster** in average latency and **6.7x more stable** in 99th percentile

## Use Cases

- **ROS Development Environment Selection**: Reference when network performance is critical
- **Docker vs WSL Comparison**: Performance benchmark for development environments
- **Network Performance Measurement**: Simple TCP communication test tool
- **Learning and Research**: Implementation example of network latency measurement

## License

MIT License 