# 10回のレイテンシテスト
for ($i=1; $i -le 10; $i++) {
    Write-Host "=== Test $i ===" -ForegroundColor Green
    docker run --rm -v ${PWD}:/workspace ros-noetic-dev bash -c "cd /workspace && python3 client.py --host host.docker.internal"
    Start-Sleep -Seconds 2
} 