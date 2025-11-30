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

def unset_proxy():
    print("\n=== Unsetting Proxy ===")

    # Git
    run_command('git config --global --unset http.proxy')
    run_command('git config --global --unset https.proxy')

    # NPM
    run_command('npm config delete proxy')
    run_command('npm config delete https-proxy')
    run_command('npm config delete strict-ssl')

    print("\n✅ Proxy has been REMOVED successfully.")


