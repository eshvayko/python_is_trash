import time
from pynput.mouse import Button, Controller
from threading import Thread

# Создаем объект мыши
mouse = Controller()

# Переменная для контроля состояния автокликера
running = False

def clicker():
    """Функция для выполнения быстрых кликов."""
    global running
    while running:
        mouse.click(Button.left)
        time.sleep(0.01)  # Пауза между кликами

def start_clicking():
    """Запуск автокликера."""
    global running
    if not running:
        running = True
        Thread(target=clicker).start()

def stop_clicking():
    """Остановка автокликера."""
    global running
    running = False

if __name__ == "__main__":
    print("Инструкции:")
    print("1. Нажмите 's', чтобы запустить автокликер.")
    print("2. Нажмите 'e', чтобы остановить автокликер.")
    print("3. Нажмите 'q', чтобы выйти из программы.")

    from pynput.keyboard import Listener, Key

    def on_press(key):
        try:
            if key.char == 's':  # Запуск
                start_clicking()
                print("Автокликер запущен!")
            elif key.char == 'e':  # Остановка
                stop_clicking()
                print("Автокликер остановлен.")
            elif key.char == 'q':  # Выход
                stop_clicking()
                print("Выход из программы.")
                return False
        except AttributeError:
            pass

    with Listener(on_press=on_press) as listener:
        listener.join()