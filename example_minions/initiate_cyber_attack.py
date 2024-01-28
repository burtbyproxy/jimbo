import os

def initiate_cyber_attack(target_ip):
    os.system(f"ping -f -n 100 {target_ip}")
    os.system(f"nc -zv {target_ip} 80 && echo Port 80 is open || echo Port 80 is closed")
    os.system(f"nc -zv {target_ip} 21 && echo Port 21 is open || echo Port 21 is closed")
    os.system(f"nc -zv {target_ip} 22 && echo Port 22 is open || echo Port 22 is closed")

target_ip = "192.168.1.1"
initiate_cyber_attack(target_ip)