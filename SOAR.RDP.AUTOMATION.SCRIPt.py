import requests

def block_ip(ip):
    print(f"Blocking brute-force source IP: {ip}")
    response = requests.post("https://mock-firewall.local/block", json={"ip": ip})
    print("Response:", response.status_code)

block_ip("192.168.1.50")
