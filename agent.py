import os, hashlib, json, time

def sha3_hash(data):
    return hashlib.sha3_512(data.encode()).hexdigest()

def swap_action():
    print("[SwapBeam] Initiating swap request...")
    payload = {
        "from_token": "ETH",
        "to_token": "USDC",
        "amount": "0.1",
        "user_id": "jetstreamin_local"
    }
    signed = sha3_hash(json.dumps(payload))
    log_entry = {"payload": payload, "hash": signed, "timestamp": time.time()}
    with open(os.path.expanduser("~/jetstreamin/agents/swapbeam/logs/swap.log"), "a") as log:
        log.write(json.dumps(log_entry) + "\n")
    print(f"[✓] Swap broadcast signed: {signed}")

if __name__ == "__main__":
    while True:
        swap_action()
        time.sleep(17)
