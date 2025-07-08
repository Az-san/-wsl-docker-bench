import statistics

# Docker Ubuntuコンテナ ↔ Windows PowerShell 結果
docker_mean = [0.305, 0.396, 0.299, 0.315, 0.306, 0.305, 0.304, 0.311, 0.303, 0.310]
docker_p99 = [1.069, 1.865, 1.146, 1.177, 1.175, 1.153, 1.163, 1.200, 1.143, 1.148]

# WSL Ubuntu ↔ Windows PowerShell 結果
wsl_mean = [0.078, 0.085, 0.076, 0.086, 0.082, 0.087, 0.088, 0.087, 0.076, 0.086]
wsl_p99 = [0.144, 0.200, 0.174, 0.189, 0.169, 0.195, 0.161, 0.226, 0.175, 0.200]

print("=== Docker Ubuntuコンテナ ↔ Windows PowerShell ===", flush=True)
print("| Test | Mean (ms) | P99 (ms) |", flush=True)
print("|------|-----------|----------|", flush=True)
for i, (m, p) in enumerate(zip(docker_mean, docker_p99), 1):
    print(f"| {i:>4} | {m:>9.3f} | {p:>8.3f} |", flush=True)
print(flush=True)

print("=== WSL Ubuntu ↔ Windows PowerShell ===", flush=True)
print("| Test | Mean (ms) | P99 (ms) |", flush=True)
print("|------|-----------|----------|", flush=True)
for i, (m, p) in enumerate(zip(wsl_mean, wsl_p99), 1):
    print(f"| {i:>4} | {m:>9.3f} | {p:>8.3f} |", flush=True)
print(flush=True)

def eval_latency(val):
    if val < 0.1:
        return "⭐⭐⭐⭐⭐ 極めて優秀"
    elif val < 0.3:
        return "⭐⭐⭐⭐ 優秀"
    elif val < 1.0:
        return "⭐⭐⭐ 良好"
    else:
        return "⭐⭐ 普通"

def eval_stability(std):
    if std < 0.05:
        return "⭐⭐⭐⭐⭐ 非常に安定"
    elif std < 0.15:
        return "⭐⭐⭐⭐ 安定"
    else:
        return "⭐⭐⭐ 普通"

print("=== 通信性能まとめ ===", flush=True)
print("| 指標 | Docker値 | WSL値 | 評価 |", flush=True)
print("|------|----------|--------|----------------------|", flush=True)
print(f"| 平均レイテンシ | {statistics.mean(docker_mean):.3f} ms | {statistics.mean(wsl_mean):.3f} ms | Docker: {eval_latency(statistics.mean(docker_mean))} / WSL: {eval_latency(statistics.mean(wsl_mean))} |", flush=True)
print(f"| 99パーセンタイル | {statistics.mean(docker_p99):.3f} ms | {statistics.mean(wsl_p99):.3f} ms | Docker: {eval_latency(statistics.mean(docker_p99))} / WSL: {eval_latency(statistics.mean(wsl_p99))} |", flush=True)
print(f"| 標準偏差(平均) | {statistics.stdev(docker_mean):.3f} ms | {statistics.stdev(wsl_mean):.3f} ms | Docker: {eval_stability(statistics.stdev(docker_mean))} / WSL: {eval_stability(statistics.stdev(wsl_mean))} |", flush=True)
print(f"| 標準偏差(P99) | {statistics.stdev(docker_p99):.3f} ms | {statistics.stdev(wsl_p99):.3f} ms | Docker: {eval_stability(statistics.stdev(docker_p99))} / WSL: {eval_stability(statistics.stdev(wsl_p99))} |", flush=True) 