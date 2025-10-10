import pyautogui
import time

pyautogui.press("win")
time.sleep(1)
pyautogui.write("Desenhando com Pyautogui")
pyautogui.press("enter")
time.sleep(2)

arvore = [
    "    ^    ",  # 4 intervalos para cada lado
    "   ^^^   ",
    "  ^^^^^  ",
    "   |||   ",
    "   |||   "
]

for linha in arvore:
    pyautogui.write(linha, interval=0.1)
    pyautogui.press("enter")
print("desenho da arvore concluido")