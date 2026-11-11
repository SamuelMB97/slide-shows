import tkinter as tk
from PIL import Image, ImageTk, ImageOps

class SlideShow():
    def __init__(self, window_title):
        self.root = tk.Tk()
        self.root.title(window_title)
        self.root.minsize(700, 700)
        self.root.maxsize(900, 900)
        self.root.geometry("700x700+25+50")
        self.root.configure(bg='darkgray')


        self.image_frame = tk.Frame(self.root, 
                                    background="gray11")

        thumbs = r"pics\Thumbs Up Music.jpg"
        smile = r"pics\Smile to the Music.png"
        music = r"pics\man-enjoying-music-2214037"
        bear = r"pics\grizzlyBear.jpg"
        
        init_img = thumbs
        self.image = ImageTk.PhotoImage(self.prep_img(init_img))

        self.image_label = tk.Label(
            self.image_frame,
            background="gray11",
            image=self.image)
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


    def prep_img(self, file):
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

    def next(self):
        print("clicked next!")

