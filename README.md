# Docker vs WSL Network Latency Comparison

Docker UbuntuコンテナとWSL Ubuntu環境でのWindows PowerShellとのTCP通信性能を比較測定するプロジェクトです。

## 📊 測定結果

### 通信性能比較（10回 × 10,000回ping-pong）

| 環境 | 平均レイテンシ | 99パーセンタイル | 評価 |
|------|----------------|------------------|------|
| **Docker Ubuntu** | 0.315 ms | 1.224 ms | ⭐⭐⭐ 良好 |
| **WSL Ubuntu** | 0.083 ms | 0.183 ms | ⭐⭐⭐⭐⭐ 極めて優秀 |

**結論**: WSLの方が平均レイテンシで**3.8倍高速**、99パーセンタイルで**6.7倍安定**

## 🚀 クイックスタート

### 1. 環境準備
```bash
# Docker環境のビルド
docker build -t ros-noetic-dev .

# WSL環境の確認
wsl --list --verbose
```

### 2. サーバー起動（Windows PowerShell）
```bash
python server.py
```

### 3. クライアント実行

#### Docker環境
```bash
docker run --rm -v ${PWD}:/workspace ros-noetic-dev bash -c "cd /workspace && python3 client.py --host host.docker.internal"
```

#### WSL環境
```bash
wsl bash -c "cd /home/natume/docker && python3 client.py --host 172.27.32.1"
```

## 📁 ファイル構成

```
├── Dockerfile              # ROS Noetic + Python 3.9環境
├── server.py               # TCPエコーサーバー
├── client.py               # レイテンシ測定クライアント
├── test_loop.ps1           # Docker 10回テストスクリプト
├── test_wsl_loop.ps1       # WSL 10回テストスクリプト
├── compare_results.py      # 結果比較・分析スクリプト
├── requirements.txt        # Python依存関係
└── entrypoint.sh          # Dockerエントリポイント
```

## 🎯 用途

- **ROS開発環境の選択**: ネットワーク性能が重要な場合の参考
- **Docker vs WSL比較**: 開発環境の性能ベンチマーク
- **ネットワーク性能測定**: シンプルなTCP通信テストツール
- **学習・研究**: ネットワークレイテンシ測定の実装例

## �� ライセンス

MIT License 