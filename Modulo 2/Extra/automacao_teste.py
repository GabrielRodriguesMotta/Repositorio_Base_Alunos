import pyautogui

pyautogui.press('win')

pyautogui.sleep(1)

# 'write'é um comando que utilizamos para passar o que queremos
#escrever
pyautogui.write('calculadora')
pyautogui.press('Enter')
pyautogui.sleep(1)
pyautogui.write('8 + 2')
pyautogui.sleep(1)

pyautogui.press('Enter')