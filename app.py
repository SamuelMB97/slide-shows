import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import os

class SlideShow():
    def __init__(self, album_name, images_data):
        self.root = tk.Tk()
        self.root.title(album_name)
        self.root.minsize(700, 700)
        self.root.maxsize(900, 900)
        self.root.geometry("700x700+25+50")
        self.root.configure(bg='darkgray')
        self.data = images_data

        for img_data in self.data:
            if not img_data.get("image_path"):
                img_data["image_path"] = os.path.relpath(img_data["file_name"])

            img_data["image"] = ImageTk.PhotoImage(
                    self.autosize_img(img_data["image_path"])
                    )
            
        self.img_idx = 0


        self.image_frame = tk.Frame(
            self.root, 
            background="gray11")

        self.image_label = tk.Label(
            self.image_frame,
            background="gray11",
            image=self.data[self.img_idx]["image"])
        self.image_label.place(relx=0.5, rely=0.5, anchor="center")

        self.image_frame.pack(expand=True, fill="both")


        self.img_data_frame = tk.Frame(
            self.root,
            background="blue")

        self.img_data_label = tk.Label(
            self.img_data_frame,
            background="gray11",
            foreground="white",
            text="Image File Name\ncaption\ncredit\nalt\nkeywords")
        self.img_data_label.pack(expand=True, fill="both")
        
        self.img_data_frame.pack(anchor="s", fill="x")
        self.configure_img_data(self.data[self.img_idx])


        self.buttons_frame = tk.Frame(
            self.root,
            background="darkgray")
        
        self.button_width = 10
        
        self.previous_button = tk.Button(
            self.buttons_frame, 
            text="previous", 
            command=self.previous,
            width=self.button_width
            ).grid(row=0, column=0, padx=5, pady=5)
        
        self.runstop_button = tk.Button(
            self.buttons_frame, 
            text="run/stop", 
            command=self.toggle_run,
            width=self.button_width
            ).grid(row=0, column=1, padx=5, pady=5)
        """
        self.stop_button = tk.Button(
            self.buttons_frame, 
            text="stop", 
            command=self.stop,
            width=self.button_width
            ).grid(row=0, column=1, padx=5, pady=5)#.pack(anchor="w")#
        """
        self.next_button = tk.Button(
            self.buttons_frame, 
            text="next", 
            command=self.next,
            width=self.button_width
            ).grid(row=0, column=2, padx=5, pady=5)

        self.buttons_frame.pack(anchor="s")

    def configure_img_data(self, info:dict):
        img_data = []
        img_data.append(info.get("file_name"))
        for key in ["caption", "credit", "alt", "keywords"]:
            value = info.get(key)
            if value:
                img_data.append(f"{key}: {value}")

        print(img_data)
        label_text = "\n".join(img_data)
        print(f"{label_text=}")

        self.img_data_label.config(text=label_text, )

        self.image_label.config(image=info["image"])



    def autosize_img(self, file):# TODO Fix the auto-sizing
        img = Image.open(file)
        return ImageOps.contain(img, (700, 700))


    def run_app(self):
        self.root.mainloop()

    def toggle_run(self):
        print("clicked run/stop!")

    def stop(self):
        print("clicked stop!")

    def previous(self):
        print("clicked previous!")
        self.img_idx = (self.img_idx - 1) % len(self.data)#TODO Make this smarter
        self.configure_img_data(self.data[self.img_idx])

    def next(self):
        print("clicked next!")
        self.img_idx = (self.img_idx + 1) % len(self.data)#TODO Make this smarter
        self.configure_img_data(self.data[self.img_idx])

