import pyautogui
import pyperclip
import time
import sys

def main():
  voice_path = sys.argv[1]
  start = pyautogui.position()
  pyautogui.click(button="right")
  pyautogui.moveTo(start.x + 14, start.y - 332)
  pyautogui.click(button="left")
  time.sleep(1)
  pyperclip.copy(voice_path)
  pyautogui.hotkey("ctrl", "v")
  pyautogui.press("enter")
  pyautogui.moveTo(start.x, start.y)
  pyperclip.copy('python')

if __name__ == "__main__":
  main()