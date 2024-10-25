import subprocess
import threading

def run_adb_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            print(f"Error executing command: {error.decode()}")
        else:
            print(f"Command output: {output.decode()}")
    except Exception as e:
        print(f"Error: {e}")


def connect_tv(ip_address):
    command = f"adb connect {ip_address}"
    threading.Thread(target=run_adb_command, args=(command,)).start()

def disconnect_tv(ip_address):
    command = f"adb disconnect {ip_address}"
    threading.Thread(target=run_adb_command, args=(command,)).start()

def send_key_event(keycode):
    command = f"adb shell input keyevent {keycode}"
    threading.Thread(target=run_adb_command, args=(command,)).start()

