# Made by LEDER555 
# GitHub: github.com/LEDER555

from time import *
import socket
import subprocess
import json

def get_local_ip_ru():
    try:
        # Создаем сокет
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Подключаемся к любому внешнему адресу (не обязательно существующему)
        s.connect(("8.8.8.8", 80))
        # Получаем локальный IP-адрес
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error as e:
        print("Ошибка при получении IP-адреса: {e}")
        return None
    


def get_local_ip_en():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error as e:
        print("Error in getting your local IP address: {e}")
        return None


def all_info():
    try:
        # Запускаем PowerShell команду
        result = subprocess.check_output(
            ["powershell", "-Command", "(Invoke-WebRequest -Uri 'https://ifconfig.co/json').Content"],
            text=True
        )
        return result.strip()
    except Exception as e:
        return e


def check_port_ru(port):
    try:
        ps_command = f'(Invoke-WebRequest -Uri "https://ifconfig.co/port/{port}").Content'
        result = subprocess.check_output(
            ["powershell", "-Command", ps_command],
            text=True
        )
        # Преобразуем JSON в словарь
        data = json.loads(result)
        return "Порт открыт" if data.get("reachable") else "Порт закрыт"
    except Exception as e:
        return e
    

def check_port_en(port):
    try:
        ps_command = f'(Invoke-WebRequest -Uri "https://ifconfig.co/port/{port}").Content'
        result = subprocess.check_output(
            ["powershell", "-Command", ps_command],
            text=True
        )
        data = json.loads(result)
        return "Port is open" if data.get("reachable") else "Port is closed"
    except Exception as e:
        return e

def get_external_ip_ps():
    try:
        # Запускаем PowerShell команду
        result = subprocess.check_output(
            ["powershell", "-Command", "(curl ifconfig.co/ip).Content"],
            text=True
        )
        return result.strip()
    except Exception as e:
        return e




choose = input("Choose language (ru/en): ").lower()



# Ru
if choose == "ru":
    while True:
        try:
            choose_ip = int(input("Выберите опцию:\n1. Узнать свой локальный IP-адрес\n2. Узнать внешний IP-адрес\n3. Проверить порт\n4. Получить всю информация.\n5. Выйти\nВведите выбор: "))
        except ValueError:
            print("❌ Введите число от 1 до 5.")
            continue
        if choose_ip == 1:
            print("Получаем ваш локальный IP-адрес...")
            sleep(1)
            ip = get_local_ip_ru()
            if ip:
                print("Ваш локальный IP-адрес:", ip)
        elif choose_ip == 2:
            print("Пожалуйста подождите...")
            print("Получение вашего внешнего IP-адреса...")
            ip = get_external_ip_ps()
            if isinstance(ip, Exception):
                print(f"Ошибка: {ip}")
            else:
                print("Ваш внешний IP-адрес:", ip)
        elif choose_ip == 3:
            port = input("Введите порт для проверки: ")
            print("Пожалуйста, подождите...")
            print("Проверка порта...")
            result = check_port_ru(port)
            if isinstance(result, Exception):
                print(f"Ошибка: {result}")
            else:
                print("Результат проверки порта:", result)
        elif choose_ip == 4:
            print("Получаем всю информацию...")
            print(all_info())
        elif choose_ip == 5:
            print("Выход...")
            break  # <-- выход из цикла
        else:
            print("❌ Неверный выбор, попробуйте еще раз.")


# Eng
if choose == "en":
    while True:
        try:
            choose_ip = int(input("Choose an option:\n1. Get your local IP address\n2. Get your external IP address\n3. Check a port\n4. Get all information\n5. Exit\nEnter your choice: "))
        except ValueError:
            print("❌ Please enter a number between 1 and 5.")
            continue

        if choose_ip == 1:
            print("Getting your local IP address...")
            sleep(1)
            ip = get_local_ip_en()
            if ip:
                print("Your local IP address:", ip)

        elif choose_ip == 2:
            print("Please wait...")
            print("Fetching your external IP address...")
            ip = get_external_ip_ps()
            if isinstance(ip, Exception):
                print(f"Error: {ip}")
            else:
                print("Your external IP address:", ip)

        elif choose_ip == 3:
            port = input("Enter the port to check: ")
            print("Please wait...")
            print("Checking the port...")
            result = check_port_en(port)
            if isinstance(result, Exception):
                print(f"Error: {result}")
            else:
                print("Port check result:", result)

        elif choose_ip == 4:
            print("Getting all information...")
            print(all_info())

        elif choose_ip == 5:
            print("Exiting...")
            break  # <-- exit loop

        else:
            print("❌ Invalid choice, please try again.")








