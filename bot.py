import pyautogui
import time
import pyperclip
import logging
from openai_custom import get_chat_response  # Custom module for OpenAI calls

# Configure logging
logging.basicConfig(level=logging.INFO)

# Screen coordinates (update if needed based on your screen resolution)
CHROME_ICON_COORDS = (1639, 1412)
SELECTION_START = (972, 202)
SELECTION_END = (2213, 1278)
TEXT_INPUT_COORDS = (1808, 1328)
CHAT_AREA_CLICK = (1994, 281)

# Target contact name to listen to
TARGET_NAME = "Rohan Das"

def is_last_message_from_sender(chat_log: str, sender_name: str = TARGET_NAME) -> bool:
    try:
        last_line = chat_log.strip().split("/2024] ")[-1]
        return sender_name in last_line
    except Exception as e:
        logging.error(f"Error parsing chat: {e}")
        return False

def main():
    logging.info("🤖 Aryan Bot is now active...")

    # Step 1: Click to open browser or chat
    pyautogui.click(*CHROME_ICON_COORDS)
    time.sleep(2)

    while True:
        time.sleep(5)  # Polling interval

        # Step 2: Select chat content
        pyautogui.moveTo(*SELECTION_START)
        pyautogui.dragTo(*SELECTION_END, duration=2.0, button='left')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1.5)

        # Step 3: Refocus to ensure clipboard access
        pyautogui.click(*CHAT_AREA_CLICK)
        time.sleep(1)

        # Step 4: Get chat history
        chat_history = pyperclip.paste()
        logging.info("📄 Chat history captured")

        if is_last_message_from_sender(chat_history):
            logging.info("✅ Message from Rohan Das detected. Generating Aryan's reply...")

            response = get_chat_response(chat_history)
            pyperclip.copy(response)

            # Step 5: Send the message
            pyautogui.click(*TEXT_INPUT_COORDS)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.press('enter')

            logging.info(f"📤 Aryan replied: {response}")
        else:
            logging.info("⏸ No new message from Rohan Das.")

if __name__ == "__main__":
    main()

