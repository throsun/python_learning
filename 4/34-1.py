# 需要先安装pynput包
# pip3 install pynput

from pynput.keyboard import  Key, Listener, KeyCode

def on_press(key):

    if key == KeyCode.from_char('w'):
        print("你按下了 上 键")
    elif key == KeyCode.from_char('s'):
        print("你按下了 下 键")
    elif key == KeyCode.from_char('a'):
        print("你按下了 左 键")
    elif key == KeyCode.from_char('d'):
        print("你按下了 右 键") 

    print()

with Listener(on_press=on_press) as listener:
    listener.join()