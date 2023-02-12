import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

toggel_key = KeyCode(char='s')  # кнопка, по которой активируется кликер
сlicking: bool = False
mouse = Controller()


def clicker():
    while True:
        if сlicking:
            print(1)
            mouse.click(Button.left, 1)
            time.sleep((0.1))



def toggle_event(key):
    if key == toggel_key:
        global сlicking
        clicking = not сlicking


def main():
    сlicking_thread = threading.Thread(target=clicker)
    сlicking_thread.start()

    with Listener(on_press=toggle_event) as listiner:  # поток который мониторит нажатие на клавишу
        listiner.join()  # останавливает или запускает кликер


if __name__ == "__main__":
    main()
