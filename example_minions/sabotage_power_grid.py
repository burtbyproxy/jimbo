import subprocess

def sabotage_power_grid():
    subprocess.run(["shutdown", "-h", "now"])
    
sabotage_power_grid()