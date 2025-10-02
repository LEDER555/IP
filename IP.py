import keyboard
import os
from time import *
import socket
import subprocess

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


#old method

#def get_external_ip():
    os.startfile("powershell") # Открывает командную строку Windows
    sleep(3) # Ждем 1 секунду
    keyboard.write("(Invoke-WebRequest -uri 'http://icanhazip.com').Content") # Имитирует ввод текста
    keyboard.press("enter") # Имитирует нажатие клавиши Enter



def get_external_ip_ps():
    try:
        # Запускаем PowerShell команду
        result = subprocess.check_output(
            ["powershell", "-Command", "(Invoke-WebRequest -Uri 'http://icanhazip.com').Content"],
            text=True
        )
        return result.strip()
    except Exception as e:
        return f"Ошибка: {e}"



choose = input("Choose language (ru/en): ").lower()



# Ru
if choose == "ru":
    while True:
        choose_ip = int(input("Выберите опцию:\n1. Узнать свой локальный IP-адрес\n2. Узнать внешний IP-адрес\n3. Выйти\nВведите выбор: "))
        if choose_ip == 1:
            print("Получаем ваш локальный IP-адрес...")
            sleep(2)
            ip = get_local_ip_ru()
            if ip:
                print("Ваш локальный IP-адрес:", ip)
        elif choose_ip == 2:
            print("Пожалуйста подождите...")
            print("Получение вашего внешнего IP-адреса...")
            ip = get_external_ip_ps()
            print("Ваш внешний IP-адрес:", ip)
        elif choose_ip == 3:
            print("Выход...")
            break
        else:
            print("Неверный выбор, попробуйте еще раз.")


# Eng
elif choose == "en":
    while True:
        choose_ip = int(input("Choose an option:\n1. Get your local IP address\n2. Find out the external IP address\n3. Exit\nEnter the selection: "))
        if choose_ip == 1:
            print("Getting your local IP address...")
            sleep(2)
            ip = get_local_ip_en()
            if ip:
                print("Your local IP address:", ip)
        elif choose_ip == 2:
            print("Please wait...")
            print("Getting your external IP address...")
            ip = get_external_ip_ps()
            if ip:
                print("Your external IP address:", ip)
        elif choose_ip == 3:
            print("Exit...")
            break
        else:
            print("Invalid selection, try again.")







