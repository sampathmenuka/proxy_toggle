import os
import subprocess

PROXY = "http://192.168.16.2:3128"

def run_command(cmd):
    print(f"\n> {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print("⚠️  Error running command.")
    return result.returncode
