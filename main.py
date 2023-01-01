import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WatermarkApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Watermark App")
        self.minsize(width=1000, height=700)
        self.config(padx=20, pady=30)

        self.canvas = tk.Canvas(width=500, height=680)
        self.welcome_img = tk.PhotoImage(file=r"welcome.png")
        self.canvas_img = self.canvas.create_image((0, 0), image=self.welcome_img, anchor="nw")
        self.canvas.grid(row=0, column=0, rowspan=5)

        self.select_button = tk.Button(text="Choose an Image", command=self.select_image)
        self.select_button.grid(row=0, column=1, columnspan=2)

        self.watermark_label = tk.Label(text="Enter Your Watermark")
        self.watermark_label.grid(row=1, column=1)

        self.watermark_entry = tk.Entry(width=50)
        self.watermark_entry.grid(row=1, column=2, padx=40)

        self.add_button = tk.Button(text="Add Watermark", command=self.add_watermark)
        self.add_button.grid(row=2, column=1, columnspan=2)

        self.save_button = tk.Button(text="Save Watermarked Image", command=self.save_watermarked_image)
        self.save_button.grid(row=3, column=1, columnspan=2)

        self.img_name = None
        self.selected_img = None
        self.watermark = None
        self.filename = None
        self.result_img = None

    def select_image(self):
        f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
        self.filename = filedialog.askopenfilename(initialdir="C:/Users/MUC/Downloads/",
                                                   title="Select an Image",
                                                   filetypes=f_types)
        self.img_name = self.filename.split("/")[4]
        img = Image.open(self.filename)
        resized_img = img.resize((400, 600))
        self.selected_img = ImageTk.PhotoImage(resized_img)
        self.canvas.itemconfig(self.canvas_img, image=self.selected_img)

    def add_watermark(self):
        opened_image = Image.open(self.filename)

        self.watermark = self.watermark_entry.get()

        img_width, img_height = opened_image.size
        draw = ImageDraw.Draw(opened_image)

        font_size = int(img_width / 10)
        font = ImageFont.truetype("arial.ttf", font_size)

        draw.text((0, 0), self.watermark, font=font, fill="#FFF8E1", stroke_width=5, stroke_fill="#FFE5F1")

        resized_opened_image = opened_image.resize((400, 600))
        self.result_img = ImageTk.PhotoImage(resized_opened_image)

        self.canvas.itemconfig(self.canvas_img, image=self.result_img)

    def save_watermarked_image(self):
        path = filedialog.asksaveasfile(title="Save as",
                                        confirmoverwrite=True,
                                        defaultextension="png",
                                        filetypes=[
                                            ("jpeg", ".jpg"),
                                            ("png", ".png"),
                                            ("bitmap", "bmp"),
                                            ("gif", ".gif")
                                        ])
        if path is not None:
            watermarked_img = ImageTk.getimage(self.result_img)
            watermarked_img.convert("RGB").save(path)

        self.watermark_entry.delete(0, tk.END)
        self.canvas.itemconfig(self.canvas_img, image=self.welcome_img)
        print("Saved Successfully")


app = WatermarkApp()
app.mainloop()



