import subprocess
import os
import json


# Config dosyasını yükleyen fonksiyon
def get_config():
    with open('cfg.json', 'r') as f:
        return json.load(f)


# Yürütülebilir dosyanın yolunu alan fonksiyon
def get_executable_path(executable_name):
    return os.path.join(os.getcwd(), executable_name)


# Programı çalıştıran ana fonksiyon
def run_program(app, os_choice):
    config = get_config()

    if os_choice == "Windows":
        file_path = get_executable_path(config["windows_executable"])
    elif os_choice == "Ubuntu":
        file_path = get_executable_path(config["ubuntu_executable"])
    else:
        raise ValueError("Geçersiz işletim sistemi seçimi")

    if file_path and os.path.exists(file_path):
        try:
            process = subprocess.Popen([file_path])
            app.withdraw()
            process.wait()
        except subprocess.CalledProcessError as e:
            print(f"Program başlatılamadı: {e}")
        finally:
            app.quit()
    else:
        print("Dosya bulunamadı.")
        app.quit()
