import os

def disable_communication_systems():
    os.system("sudo systemctl stop network-manager")

disable_communication_systems()