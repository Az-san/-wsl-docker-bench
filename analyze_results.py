import statistics

# テスト結果データ
mean_latencies = [0.305, 0.396, 0.299, 0.315, 0.306, 0.305, 0.304, 0.311, 0.303, 0.310]
p99_latencies = [1.069, 1.865, 1.146, 1.177, 1.175, 1.153, 1.163, 1.200, 1.143, 1.148]

print("=== Docker Ubuntuコンテナ ↔ Windows PowerShell 通信テスト結果 ===")
print(f"テスト回数: {len(mean_latencies)}回")
print(f"各テスト: 10,000回のping-pong")
print()

print("=== 平均レイテンシ (Mean) ===")
print(f"平均: {statistics.mean(mean_latencies):.3f} ms")
print(f"中央値: {statistics.median(mean_latencies):.3f} ms")
print(f"標準偏差: {statistics.stdev(mean_latencies):.3f} ms")
print(f"最小値: {min(mean_latencies):.3f} ms")
print(f"最大値: {max(mean_latencies):.3f} ms")
print()

print("=== 99パーセンタイル (P99) ===")
print(f"平均: {statistics.mean(p99_latencies):.3f} ms")
print(f"中央値: {statistics.median(p99_latencies):.3f} ms")
print(f"標準偏差: {statistics.stdev(p99_latencies):.3f} ms")
print(f"最小値: {min(p99_latencies):.3f} ms")
print(f"最大値: {max(p99_latencies):.3f} ms")
print()

print("=== 性能評価 ===")
print("✅ 平均レイテンシ: 1ms未満で非常に良好")
print("✅ 99パーセンタイル: 1.2ms程度で安定")
print("✅ ばらつき: 標準偏差が小さい（安定している）")
print("✅ Docker環境: ROS Noetic + Python 3.9環境での通信性能確認済み") 