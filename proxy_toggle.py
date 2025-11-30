import os
import subprocess

PROXY = "http://192.168.16.2:3128"

def run_command(cmd):
    print(f"\n> {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print("⚠️  Error running command.")
    return result.returncode

def set_proxy():
    print("\n=== Setting Proxy ===")

    # Git
    run_command(f'git config --global http.proxy {PROXY}')
    run_command(f'git config --global https.proxy {PROXY}')

    # NPM
    run_command(f'npm config set proxy {PROXY}')
    run_command(f'npm config set https-proxy {PROXY}')
    run_command('npm config set strict-ssl false')

    print("\n✅ Proxy has been SET successfully.")


