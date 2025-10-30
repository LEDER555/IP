# Made by LEDER555
# GitHub: github.com/LEDER555

import flet as ft
import socket
import urllib.request
import json


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        return f"Ошибка: {e}"


def get_external_ip():
    urls = ["https://ifconfig.co/ip", "https://ifconfig.io/ip", "https://api.ipify.org"]
    for url in urls:
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                ip = response.read().decode().strip()
                if ip:
                    return ip
        except Exception:
            continue
    return "❌ Не удалось получить внешний IP"


def get_all_info():
    try:
        with urllib.request.urlopen("https://ifconfig.co/json", timeout=5) as response:
            data = json.loads(response.read().decode())
            return json.dumps(data, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Ошибка: {e}"


def check_port(host, port, timeout=3):
    try:
        port = int(port)
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False


def main(page: ft.Page):
    page.title = "IP Tools"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- Переводы ---
    texts = {
        "ru": {
            "title": "IP Address Tool",
            "local_ip": "Локальный IP",
            "external_ip": "Внешний IP",
            "all_info": "Вся информация",
            "port_check": "Проверка порта",
            "check": "Проверить",
            "host_label": "Хост (например, 8.8.8.8)",
            "port_label": "Порт (например, 443)",
            "enter_both": "⚠️ Введите хост и порт.",
            "port_open": "✅ Порт {port} на {host} открыт.",
            "port_closed": "❌ Порт {port} на {host} закрыт.",
            "local_result": "Ваш локальный IP: {ip}",
            "external_result": "Ваш внешний IP: {ip}",
            "info_result": "Вся информация:\n{info}",
            "footer": "Сделано LEDER555",
        },
        "en": {
            "title": "IP Address Tool",
            "local_ip": "Local IP",
            "external_ip": "External IP",
            "all_info": "All info",
            "port_check": "Port check",
            "check": "Check",
            "host_label": "Host (e.g., 8.8.8.8)",
            "port_label": "Port (e.g., 443)",
            "enter_both": "⚠️ Enter host and port.",
            "port_open": "✅ Port {port} on {host} is open.",
            "port_closed": "❌ Port {port} on {host} is closed.",
            "local_result": "Your local IP: {ip}",
            "external_result": "Your external IP: {ip}",
            "info_result": "All info:\n{info}",
            "footer": "Made by LEDER555",
        },
    }

    lang = "ru"

    # --- Элементы интерфейса ---
    result_text = ft.Text(value="", selectable=True, size=14)
    result = ft.Column(
        controls=[result_text],
        scroll="always",
        expand=True,
    )

    host_field = ft.TextField(label=texts[lang]["host_label"], width=250)
    port_field = ft.TextField(label=texts[lang]["port_label"], width=250)

    # Функции обработки
    def show_local_ip(e):
        ip = get_local_ip()
        result_text.value = texts[lang]["local_result"].format(ip=ip)
        page.update()

    def show_external_ip(e):
        ip = get_external_ip()
        result_text.value = texts[lang]["external_result"].format(ip=ip)
        page.update()

    def show_all_info(e):
        info = get_all_info()
        result_text.value = texts[lang]["info_result"].format(info=info)
        page.update()

    def check_port_action(e):
        host = host_field.value
        port = port_field.value
        if not host or not port:
            result_text.value = texts[lang]["enter_both"]
        else:
            opened = check_port(host, port)
            result_text.value = (
                texts[lang]["port_open"].format(host=host, port=port)
                if opened
                else texts[lang]["port_closed"].format(host=host, port=port)
            )
        page.update()

    # Функция переключения языка
    def switch_language(new_lang):
        nonlocal lang
        lang = new_lang
        # обновляем все надписи
        title.value = texts[lang]["title"]
        host_field.label = texts[lang]["host_label"]
        port_field.label = texts[lang]["port_label"]
        port_check_text.value = texts[lang]["port_check"]
        check_button.text = texts[lang]["check"]
        local_button.text = texts[lang]["local_ip"]
        external_button.text = texts[lang]["external_ip"]
        info_button.text = texts[lang]["all_info"]
        footer.value = texts[lang]["footer"]
        page.update()

    # Основные элементы
    title = ft.Text(texts[lang]["title"], size=24, weight=ft.FontWeight.BOLD)
    local_button = ft.ElevatedButton(texts[lang]["local_ip"], on_click=show_local_ip, icon=ft.Icons.COMPUTER)
    external_button = ft.ElevatedButton(texts[lang]["external_ip"], on_click=show_external_ip, icon=ft.Icons.PUBLIC)
    info_button = ft.ElevatedButton(texts[lang]["all_info"], on_click=show_all_info, icon=ft.Icons.INFO)
    check_button = ft.ElevatedButton(texts[lang]["check"], on_click=check_port_action)
    port_check_text = ft.Text(texts[lang]["port_check"], size=18, weight=ft.FontWeight.BOLD)
    footer = ft.Text(texts[lang]["footer"], italic=True, size=12, color=ft.Colors.GREY)

    # Dropdown выбора языка
    language_dropdown = ft.Dropdown(
        options=[ft.dropdown.Option("ru"), ft.dropdown.Option("en")],
        value="ru",
        width=120,
        on_change=lambda e: switch_language(e.control.value),
    )

    # Добавляем всё на страницу
    page.add(
        ft.Row(
            [title, ft.Container(content=language_dropdown, alignment=ft.alignment.center_right, expand=True)],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        ft.Divider(),
        ft.Row([local_button, external_button, info_button], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        port_check_text,
        ft.Row([host_field, port_field, check_button], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        result,
        footer,
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)
