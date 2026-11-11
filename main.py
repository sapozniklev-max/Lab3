import tkinter as tk
import random
import string
from PIL import Image, ImageTk

def get_key():
    entry_imput = hex_entry.get()

    dec_input = str(int(entry_imput,16))
    digits = dec_input[:3]
    last_two = dec_input[-2:]

    alphabet = string.digits + string.ascii_uppercase

    blocks = []
    for digit in digits:
        chars = random.choices(alphabet, k=4)
        block = chars + [digit]
        random.shuffle(block)
        blocks.append(''.join(block))
    result = f"{blocks[0]}-{blocks[1]}-{blocks[2]} {last_two}"

    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)

root = tk.Tk()
root.title("Вариант 3. Сапожник Лев")
width, height = 1200, 562
root.geometry(f"{width}x{height}")

img = Image.open("background.jpg")
resized_img = img.resize((width, height), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(resized_img)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

header = tk.Label(root, text="KEY GENERATION", font=("Arial", 20, "bold"), fg="white", bg="black")
header.pack(side="top", fill="x", pady=20)

inf_label = tk.Label(root, text="Введите число", fg="white", bg="yellow")
header.pack(side="top", pady=20)

hex_entry = tk.Entry(root, font=("Arial", 15), justify="center", width=10)
hex_entry.pack(side="top", pady=20)
hex_entry.insert(0, "54CD1")

gen_button = tk.Button(root, text="ГЕНЕРИРОВАТЬ", command=get_key, 
                       bg="green", fg="#F705E3", font=("Arial", 12, "bold"))
gen_button.pack(side="top", pady=20)

result_entry = tk.Entry(root, font=("Arial", 20, "bold"), justify="center", width=25)
result_entry.pack(side="top", pady=10)

root.mainloop()


