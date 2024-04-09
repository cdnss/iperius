import pyautogui as pag
import time
import pyperclip
import subprocess

"C:\Program Files\IperiusRemote\IperiusRemote.exe"

>>> pag.position()
Point(x=)
# Define the coordinates and use the `actions` list
actions = [
    (266, y=287, 4),  # unattended access
    (681, y=564, 4),  # next
    (260, y=507, 4),  # i accept agreement
    (673, y=567, 4),  # next
    (672, y=565, 4),  # next
    (265, y=299, 4),  # untic create desktop icon
    (675, y=566, 10),  # next
    (677, y=570, 4),  # install (wait 15sec)
    (261, y=306, 4),  # type pass
    (671, y=567, 4),  # next (wait 15sec)
    (437, y=303, 10),  # tic launch iperius
    (667, y=567, 4),  # finish
    (447, y=286, 4),  # copy id
]

# Wait for a few seconds to give time to focus on the target application
time.sleep(10)
password = "TheDisa1a"
timeout = "10"
    
for x, y, duration in actions:
    if (x, y, duration) == (387, 253, 10):
        pag.click(x, y, duration=duration)
        pag.typewrite(password)
    elif (x, y, duration) == (387, 298, 4):
        pag.click(x, y, duration=duration)
        pag.typewrite(password)
    elif (x, y, duration) == (460, 321, 4):
        pag.rightClick(x, y, duration=duration)
    elif (x, y, duration) == (610, 531, 4):
        pag.click(x, y, duration=duration)
        cmd = r'"C:\Program Files (x86)\LiteManager Pro - Server\ROMServer.exe" /start'
        subprocess.run(cmd, shell=True)
    elif (x, y, duration) == (510, 312, 4):
        pag.click(x, y, duration=duration)
        pag.press('backspace')  # Press backspace once
        pag.press('backspace')  # Press backspace again
        pag.typewrite(timeout)
    else:
        pag.click(x, y, duration=duration)

def save_echo_to_batch(file_path, echo_text):
    with open(file_path, 'a') as file:
        file.write(f'\necho {echo_text}')

def save_command():
    clipboard_text = pyperclip.paste()
    password_echo = 'LiteManager Password : TheDisa1a'  
    save_echo_to_batch('show.bat', f'LiteManager ID: {clipboard_text}')
    save_echo_to_batch('show.bat', password_echo)

if __name__ == "__main__":
    save_command()

print("Done , Log in Credintials is below")
