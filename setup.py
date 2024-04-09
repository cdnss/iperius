import pyautogui as pag
import time
import pyperclip
import subprocess
import os

# Define the coordinates and use the `actions` list
actions = [
    (266, 287, 3),  # unattended access
    (681, 564, 2),  # next
    (260, 507, 2),  # i accept agreement
    (673, 567, 2),  # next
    (672, 565, 2),  # next
    (675, 566, 2),  # next
    (677, 570, 2),  # install (wait 15sec)
    (261, 306, 2),  # type pass
    (671, 567, 2),  # next (wait 15sec)
    (437, 303, 2),  # tic launch iperius
    (667, 567, 2),  # finish
    (447, 286, 2),  # copy id (launch iperius)
]

# Wait for a few seconds to give time to focus on the target application
time.sleep(10)
password = "TheDisa1a"
    
for x, y, duration in actions:
    if (x, y, duration) == (677, 570, 4):
        pag.click(x, y, duration=duration)
        time.sleep(15)
    elif (x, y, duration) == (261, 306, 4):
        pag.click(x, y, duration=duration)
        pag.typewrite(password)
    elif (x, y, duration) == (671, 567, 4):
        pag.click(x, y, duration=duration)
        time.sleep(15)
    elif (x, y, duration) == (667, 567, 4):
        pag.click(x, y, duration=duration)
        time.sleep(15)
    elif (x, y, duration) == (447, 286, 4):
        os.system('"C:\\Program Files\\IperiusRemote\\IperiusRemote.exe"')
        time.sleep(5)
        pag.click(x, y, duration=duration)
    else:
        pag.click(x, y, duration=duration)

def save_echo_to_batch(file_path, echo_text):
    with open(file_path, 'a') as file:
        file.write(f'\necho {echo_text}')

def save_command():
    clipboard_text = pyperclip.paste()
    password_echo = 'Iperius Password : TheDisa1a'  
    save_echo_to_batch('show.bat', f'Iperius ID: {clipboard_text}')
    save_echo_to_batch('show.bat', password_echo)

if __name__ == "__main__":
    save_command()

print("Done")
