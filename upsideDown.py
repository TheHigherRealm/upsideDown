#Made by Joseph Tams
from pynput.keyboard import Key, Controller, Listener

control = Controller()

upsideDown  = ['ɐ','q','ɔ','p','ǝ','ɟ','ƃ','ɥ','ᴉ','ɾ','ʞ','l','ɯ','u','o','d','b','ɹ','s','ʇ','n','ʌ','ʍ','x','ʎ','z']
rightSideUp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def on_release(key):
    if hasattr(key, "char") and key.char not in upsideDown:
        pos = rightSideUp.index(key.char)
        control.press(Key.backspace)
        control.release(Key.backspace)
        control.press(upsideDown[pos])
        control.release(upsideDown[pos])
    if key == Key.esc:
        return False

with Listener(on_release=on_release) as listener:
    listener.join()
