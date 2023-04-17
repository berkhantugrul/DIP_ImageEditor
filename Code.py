from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageEnhance, ImageFilter, ImageOps
import os


root = Tk()
root.title("Image")
root.geometry("1600x800")

menu_bar = Menu(root)
root.config(menu=menu_bar)


def browse_command():
    global img_raw, img_prew_raw, mainsize, prewsize, gray_image
    file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Browse Image", filetypes=(("PNG file","*.png"),("JPG file", "*.jpg"),("All files", "*.*")))

    img_raw = Image.open(file)
    img_prew_raw = Image.open(file)

    mainsize = (1200, 775)
    prewsize = (400,225)
    img_raw.thumbnail(mainsize, Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img_raw)
    img_label.configure(image=img)
    img_label.image = img

    img_prew_raw.thumbnail(prewsize, Image.Resampling.LANCZOS)
    prew = ImageTk.PhotoImage(img_prew_raw)
    prew_label.configure(image=prew)
    prew_label.image = prew

    studio.pack(fill="both", expand=1)


browse_menu = Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=browse_menu)
browse_menu.add_command(label="Browse", command= browse_command)

studio = Frame(root, width=1600, height=800,)

img_label = Label(studio)
prew_label = Label(studio)
img_label.grid(column=0,row=0, columnspan= 6, rowspan=2, padx= 50, pady= 30)
prew_label.grid(column=6,row=0, padx= 50, pady= 30)

current_frame = Frame(studio)


def brightness(factor, img, label):
    global img_raw, img_prew_raw
    brightness_prev(factor, img_prew_raw, prew_label )
    enhancer = ImageEnhance.Brightness(img)
    new_image = enhancer.enhance(factor/50)
    new_image.thumbnail(mainsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output
    img_raw = new_image
    img_prew_raw = new_image


def brightness_prev(factor, img, label):
    global img_prew_raw
    enhancer = ImageEnhance.Brightness(img)
    new_image = enhancer.enhance(factor/50)
    new_image.thumbnail(prewsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output


def brightness_menu():
    global current_frame
    current_frame.destroy()
    brightness_frame = Frame(studio, height=300, width=400, bg="dark blue")
    brightness_frame.grid(column=6,row=1, rowspan=2)
    current_frame = brightness_frame
    default_val = IntVar(root)
    default_val.set(50)
    title = Label(brightness_frame, text="Brightness")
    title.pack(side="top")
    factor_box = Spinbox(brightness_frame, from_=0, to=100, textvariable=default_val)
    factor_box.pack(side="top")
    apply_button = Button(brightness_frame, text="Apply", command= lambda: brightness(int(factor_box.get()),img_raw, img_label))
    apply_button.pack(side="bottom")
    prev_button = Button(brightness_frame, text="Preview", command=lambda: brightness_prev(int(factor_box.get()), img_prew_raw, prew_label))
    prev_button.pack(side="bottom")


def saturation(factor, img, label):
    global img_raw, img_prew_raw
    saturation_prev(factor, img_prew_raw, prew_label )
    enhancer = ImageEnhance.Color(img)
    new_image = enhancer.enhance(factor/50)
    new_image.thumbnail(mainsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output
    img_raw = new_image
    img_prew_raw = new_image


def saturation_prev(factor, img, label):
    global img_prew_raw
    enhancer = ImageEnhance.Color(img)
    new_image = enhancer.enhance(factor/50)
    new_image.thumbnail(prewsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output


def saturation_menu():
    global current_frame
    current_frame.destroy()
    saturation_frame = Frame(studio, height=300, width=400, bg="dark blue")
    saturation_frame.grid(column=6,row=1, rowspan=2)
    current_frame = saturation_frame
    default_val = IntVar(root)
    default_val.set(50)
    title = Label(saturation_frame, text="Saturation")
    title.pack(side="top")
    factor_box = Spinbox(saturation_frame, from_=0, to=100, textvariable=default_val)
    factor_box.pack(side="top")
    apply_button = Button(saturation_frame, text="Apply", command= lambda: saturation(int(factor_box.get()),img_raw, img_label))
    apply_button.pack(side="bottom")
    prev_button = Button(saturation_frame, text="Preview", command=lambda: saturation_prev(int(factor_box.get()), img_prew_raw, prew_label))
    prev_button.pack(side="bottom")


def blur(factor, img, label):
    global img_raw, img_prew_raw
    blur_prev(factor, img_prew_raw, prew_label )
    new_image = img.filter(ImageFilter.BoxBlur(factor/50))
    new_image.thumbnail(mainsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output
    img_raw = new_image
    img_prew_raw = new_image


def blur_prev(factor, img, label):
    global img_prew_raw
    new_image = img.filter(ImageFilter.BoxBlur(factor/50))
    new_image.thumbnail(prewsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output


def sharpen(factor, img, label):
    global img_raw, img_prew_raw
    sharpen_prev(factor, img_prew_raw, prew_label )
    enhancer = ImageEnhance.Sharpness(img)
    new_image = enhancer.enhance(factor/50)
    new_image.thumbnail(mainsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output
    img_raw = new_image
    img_prew_raw = new_image


def sharpen_prev(factor, img, label):
    global img_prew_raw
    enhancer = ImageEnhance.Sharpness(img)
    new_image = enhancer.enhance(factor/50)
    new_image.thumbnail(prewsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output


def blur_and_sharpening_menu():
    global current_frame
    current_frame.destroy()
    blur_and_sharpening_frame = Frame(studio, height=300, width=400, bg="dark blue")
    blur_and_sharpening_frame.grid(column=6,row=1, rowspan=2)
    current_frame = blur_and_sharpening_frame
    default_val = IntVar(root)
    default_val.set(50)

    blur_label = Label(blur_and_sharpening_frame)
    blur_label.pack(side="left")
    title_blur = Label(blur_label, text="Blur")
    title_blur.pack(side="top")

    sharpening_label = Label(blur_and_sharpening_frame)
    sharpening_label.pack(side="right")
    title_sharpening = Label(sharpening_label, text="Sharpening")
    title_sharpening.pack(side="top")
    
    factor_box_blur = Spinbox(blur_label, from_=0, to=100, textvariable=0)
    factor_box_blur.pack(side="top")
    apply_button = Button(blur_label, text="Apply", command= lambda: blur(int(factor_box_blur.get()),img_raw, img_label))
    apply_button.pack(side="bottom")
    prev_button = Button(blur_label, text="Preview", command=lambda: blur_prev(int(factor_box_blur.get()), img_prew_raw, prew_label))
    prev_button.pack(side="bottom")
    
    factor_box_sharpen = Spinbox(sharpening_label, from_=0, to=100, textvariable=default_val)
    factor_box_sharpen.pack(side="top")
    apply_button = Button(sharpening_label, text="Apply", command= lambda: sharpen(int(factor_box_sharpen.get()),img_raw, img_label))
    apply_button.pack(side="bottom")
    prev_button = Button(sharpening_label, text="Preview", command=lambda: sharpen_prev(int(factor_box_sharpen.get()), img_prew_raw, prew_label))
    prev_button.pack(side="bottom")


def edges(img, label):
    global img_raw, img_prew_raw
    edges_prev(img_prew_raw, prew_label )
    img = img.convert("L")
    new_image = img.filter(ImageFilter.FIND_EDGES)
    new_image.thumbnail(mainsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output
    img_raw = new_image
    img_prew_raw = new_image


def edges_prev(img, label):
    global img_prew_raw
    img = img.convert("L")
    new_image = img.filter(ImageFilter.FIND_EDGES)
    new_image.thumbnail(prewsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output


def edges_menu():
    global current_frame
    current_frame.destroy()
    edges_frame = Frame(studio, height=300, width=400, bg="dark blue")
    edges_frame.grid(column=6,row=1, rowspan=2)
    current_frame = edges_frame
    title = Label(edges_frame, text="Find Edges")
    edges_frame.grid_propagate(0)
    title.pack(side="top")
    apply_button = Button(edges_frame, text="Apply", command= lambda: edges(img_raw, img_label))
    apply_button.pack(side="bottom")
    prev_button = Button(edges_frame, text="Preview", command=lambda: edges_prev(img_prew_raw, prew_label))
    prev_button.pack(side="bottom")


def selected():
    frame = Frame(studio, height=300, width=400, bg="dark blue")
    frame.grid(column=6,row=1, rowspan=2)


def equalize(img, label):
    global img_raw, img_prew_raw
    equalize_prev(img_prew_raw, prew_label )
    new_image = ImageOps.equalize(img.convert('L'), mask=None)
    new_image.thumbnail(mainsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output
    img_raw = new_image
    img_prew_raw = new_image


def equalize_prev(img, label):
    global img_prew_raw
    new_image = ImageOps.equalize(img.convert('L'), mask=None)
    new_image.thumbnail(prewsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output


def histogram_menu():
    global current_frame
    current_frame.destroy()
    histogram_frame = Frame(studio, height=300, width=400, bg="dark blue",)
    histogram_frame.grid(column=6,row=1, rowspan=2)
    current_frame = histogram_frame
    title = Label(histogram_frame, text="Histogram of Grayscale Values")
    title.pack(side="top")
    apply_button = Button(histogram_frame, text="Apply Equalization", command= lambda: equalize(img_raw, img_label))
    apply_button.pack(side="bottom")
    prev_button = Button(histogram_frame, text="Preview Equalization", command=lambda: equalize_prev(img_prew_raw, prew_label))
    prev_button.pack(side="bottom")


def noise_reduction(img, label):
    global img_raw, img_prew_raw
    noise_reduction_prev(img_prew_raw, prew_label )
    new_image = img.filter(ImageFilter.MedianFilter(3))
    new_image.thumbnail(mainsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output
    img_raw = new_image
    img_prew_raw = new_image


def noise_reduction_prev(img, label):
    global img_prew_raw
    new_image = img.filter(ImageFilter.MedianFilter(3))
    new_image.thumbnail(prewsize, Image.Resampling.LANCZOS)
    image_output = ImageTk.PhotoImage(new_image)
    label.configure(image = image_output)
    label.image = image_output


def noise_menu():
    global current_frame
    current_frame.destroy()
    histogram_frame = Frame(studio, height=300, width=400, bg="dark blue")
    histogram_frame.grid(column=6,row=1, rowspan=2)
    current_frame = histogram_frame
    title = Label(histogram_frame, text="Noise Reduction")
    title.pack(side="top")
    apply_button = Button(histogram_frame, text="Apply Reduction", command= lambda: noise_reduction(img_raw, img_label))
    apply_button.pack(side="bottom")
    prev_button = Button(histogram_frame, text="Preview Reduction", command=lambda: noise_reduction_prev(img_prew_raw, prew_label))
    prev_button.pack(side="bottom")


def save(img, file_name, extension):
    name = file_name.get()
    ext = extension.get()
    full_name = name+ext
    img.save(full_name)

clicked = StringVar()

Histogram = Button(studio, text="Histogram", command = lambda: histogram_menu())
Histogram.grid(column=0,row=3)
Brightness = Button(studio, text="Brightness", command = lambda: brightness_menu())
Brightness.grid(column=1,row=3)
Blur_and_Sharpening = Button(studio, text="Blur and Sharpening", command = lambda: blur_and_sharpening_menu())
Blur_and_Sharpening.grid(column=2,row=3)
Saturation = Button(studio, text="Saturation", command = lambda: saturation_menu())
Saturation.grid(column=3,row=3)
Find_Edges = Button(studio, text="Find Edges", command = lambda: edges_menu())
Find_Edges.grid(column=4,row=3)
Noise_Removal = Button(studio, text="Noise Removal", command = lambda: noise_menu())
Noise_Removal.grid(column=5,row=3)
Save = Button(studio, text="Save", command= lambda: save(img_raw, file_name, clicked))
Save.grid(column=6, row=3)
file_name = Entry(studio)
file_name.grid(column=6, row=2)

extension = OptionMenu(studio, clicked, ".png", ".jpg")
extension.grid(column=7, row=2)


root.mainloop()
