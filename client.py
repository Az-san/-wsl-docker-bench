# client.py — レイテンシ測定クライアント
import socket, time, struct, statistics, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--host', default='127.0.0.1')
parser.add_argument('-n', '--loops', type=int, default=10000)
args = parser.parse_args()

latencies = []
with socket.create_connection((args.host, 50007)) as s:
    for _ in range(args.loops):
        t0 = time.perf_counter_ns()
        s.sendall(struct.pack('Q', t0))
        data = s.recv(8)
        t1 = time.perf_counter_ns()
        latencies.append((t1 - struct.unpack('Q', data)[0]) / 1e6)

mean = statistics.mean(latencies)
# Python 3.8+ なら以下が確実に使えます (singular の quantile() が無くても動く)
p99 = statistics.quantiles(latencies, n=100)[98]

print(f"loops={args.loops} mean={mean:.3f} ms")
print(f"p99={p99:.3f} ms")
