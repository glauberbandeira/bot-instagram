import webbrowser
import pyautogui
from time import sleep

def logout():
    pyautogui.click(1216,549,duration=3)
    pyautogui.click(78,624,duration=3)
    pyautogui.click(1185,148,duration=3)
    pyautogui.click(674,604,duration=3)


while True:
    webbrowser.open_new_tab('https://www.instagram.com')
    sleep(1)

    pyautogui.moveTo(823, 545, duration=2)
    sleep(1)
    pyautogui.click(823, 545, duration=2)
    sleep(1)


    pyautogui.click(759, 304, duration=1)
    pyautogui.typewrite('glauberbandeiradev')
    sleep(1)

    pyautogui.click(773, 346, duration=1)
    pyautogui.typewrite('*********')
    sleep(1)

    pyautogui.click(821, 399, duration=1)
    sleep(3)

    pyautogui.click(795, 464, duration=1)
    sleep(1)

    # Pesquisar Página / Search page
    pyautogui.click(75, 288, duration=1)
    sleep(1)

    pyautogui.click(101, 216, duration=1)
    sleep(1)
    pyautogui.typewrite('premier group recruitment')
    sleep(1)

    pyautogui.move(60, 70, duration=1)
    pyautogui.click()
    sleep(10)

    pyautogui.click(447, 649, duration=1)
    sleep(2)

    liked = pyautogui.locateCenterOnScreen('liked.png')
    sleep(1)

    if liked is not None:
        logout()
        sleep(86400)
    elif liked == None:
        pyautogui.click(682,578, duration=1)
        sleep(5)
        pyautogui.click(721,577, duration=1)
        sleep(3)
        pyautogui.click(713,678, duration=1)
        sleep(1)
        pyautogui.typewrite(
            'Hello, how are you? I made this comment using automation in Python because I saw you offering vacancies for Python developers and I want to apply for this vacancy.')
        sleep(5)
        pyautogui.click(1110, 679, duration=1)
        logout()
        sleep(86400)
