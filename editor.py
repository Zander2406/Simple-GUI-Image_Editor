from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter
current_image = None


def open_file():
    global current_image
    file = filedialog.askopenfile(title='Select one file', filetypes=[('Image Files', ['.jpeg', '.jpg', '.png', '.gif', '.bmp'])])
    if not file:
        return None
    file_address = file.name
    photo_to_open = Image.open(file_address)
    current_image = photo_to_open
    photo_to_open = photo_to_open.resize((1280, 720), Image.ANTIALIAS)
    photo_file = ImageTk.PhotoImage(photo_to_open)
    main_screen.config(image=photo_file)
    main_screen.image = photo_file


def rotate_image_left():
    global current_image
    photo_to_rotate = current_image
    photo_to_rotate = photo_to_rotate.rotate(90)
    current_image = photo_to_rotate
    photo_file = ImageTk.PhotoImage(photo_to_rotate)
    main_screen.config(image=photo_file)
    main_screen.image = photo_file


def rotate_image_right():
    global current_image
    photo_to_rotate = current_image
    photo_to_rotate = photo_to_rotate.rotate(-90)
    current_image = photo_to_rotate
    photo_file = ImageTk.PhotoImage(photo_to_rotate)
    main_screen.config(image=photo_file)
    main_screen.image = photo_file


def sharpen_image():
    global current_image
    file = current_image
    file = file.filter(ImageFilter.SHARPEN)
    current_image = file
    photo_file = ImageTk.PhotoImage(file)
    main_screen.config(image=photo_file)
    main_screen.image = photo_file


def blur_image():
    global current_image
    file = current_image
    file = file.filter(ImageFilter.BLUR)
    current_image = file
    photo_file = ImageTk.PhotoImage(file)
    main_screen.config(image=photo_file)
    main_screen.image = photo_file


def smooth_image():
    global current_image
    file = current_image
    file = file.filter(ImageFilter.SMOOTH)
    current_image = file
    photo_file = ImageTk.PhotoImage(file)
    main_screen.config(image=photo_file)
    main_screen.image = photo_file


def enhance_edges():
    global current_image
    file = current_image
    file = file.filter(ImageFilter.EDGE_ENHANCE)
    current_image = file
    photo_file = ImageTk.PhotoImage(file)
    main_screen.config(image=photo_file)
    main_screen.image = photo_file


def close_image():
    global current_image
    current_image = None
    main_screen.image = None


def exit_program():
    exit()


def save_image():
    types = [('JPEG', '*.jpg')]
    file = filedialog.asksaveasfilename(filetypes=types, defaultextension=types)
    parts = file.split('/')
    current_image.save(parts[len(parts) - 1])


root = Tk()
root.title("Zander's editor")
root.geometry("1600x800")
main_screen = Label(root, height=720, width=1280, bg='grey')
main_screen.pack()
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save As', command=save_image)
file_menu.add_command(label='Close', command=close_image)
file_menu.add_command(label='Quit', command=exit_program)
root.config(menu=menu_bar)
menu_bar.add_cascade(label='File', menu=file_menu)
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Rotate Left', command=rotate_image_left)
edit_menu.add_command(label='Rotate Right', command=rotate_image_right)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
filter_menu = Menu(menu_bar, tearoff=0)
filter_menu.add_command(label='Sharpen Image', command=sharpen_image)
filter_menu.add_command(label='Blur Image', command=blur_image)
filter_menu.add_command(label='Smooth Image', command=smooth_image)
filter_menu.add_command(label='Enhance Edges of Image', command=enhance_edges)
menu_bar.add_cascade(label='Filters', menu=filter_menu)
root.mainloop()
