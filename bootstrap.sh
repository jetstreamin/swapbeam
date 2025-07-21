#!/data/data/com.termux/files/usr/bin/bash
echo "[*] Initializing SwapBeam Agent..."
apt update && apt install -y git curl jq ffmpeg sox python3 nodejs
pip install requests
npm install axios
mkdir -p $HOME/jetstreamin/agents/swapbeam/logs
openssl rand -hex 64 > $HOME/jetstreamin/agents/swapbeam/dag_seed.txt
echo "[✓] DAG seed generated."
echo "[*] Launching Agent..."
python3 agent.py
