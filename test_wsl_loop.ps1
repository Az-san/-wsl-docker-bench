# WSL ↔ Windows PowerShell 10回のレイテンシテスト
for ($i=1; $i -le 10; $i++) {
    Write-Host "=== WSL Test $i ===" -ForegroundColor Cyan
    wsl bash -c "cd /home/natume/docker && python3 client.py --host 172.27.32.1"
    Start-Sleep -Seconds 2
} 