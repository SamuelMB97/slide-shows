import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import os

class SlideShow():
    def __init__(self, directory, images_data, album=None):
        self.directory = directory
        self.root = tk.Tk()
        if album:
            self.album = album
            #print(f"{album=}")
            album_name = [c for c in os.path.basename(album)]
            c = "c"
            while c != ".":
                c = album_name.pop()
            self.album_name = "".join(album_name)
            #print(f"{self.album_name=}")
            self.root.title(self.album_name)
        else:
            self.root.title(directory)
        self.root.minsize(700, 700)
        self.root.maxsize(900, 900)
        self.root.geometry("700x700+25+50")
        self.root.configure(bg='gray20')
        self.data = images_data
        self.load_images()
            
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
            self.root)

        self.img_data_label = tk.Label(
            self.img_data_frame,
            background="gray11",
            foreground="white",
            text="Image File Name\ncaption\ncredit\nalt\nkeywords")
        self.img_data_label.pack(expand=True, fill="both")
        
        self.img_data_frame.pack(anchor="s", fill="x")
        self.set_img(self.data[self.img_idx])


        self.buttons_frame = tk.Frame(
            self.root,
            background="gray20")
        
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

    def load_images(self):
        print("LOADING IMAGES")
        for img_data in self.data:
            try:
                if not img_data.get("image_path"):
                    #Build the image path
                    album_path = os.path.dirname(self.album)
                    img_data["image_path"] = os.path.join(
                        album_path, img_data["file_name"]
                        )

                print(f"\t{img_data["file_name"]=}\n\t{img_data["image_path"]=}\n")

                #Create tkinter Image
                img_data["image"] = ImageTk.PhotoImage(
                        self.scale_img(img_data["image_path"])
                        )

                #Format image data for label
                label_info = []
                label_info.append(img_data.get("file_name"))
                for key in ["caption", "credit", "alt", "keywords"]:
                    value = img_data.get(key)
                    if value:
                        label_info.append(f"{key}: {value}")
        
                label_text = "\n".join(label_info)
                img_data["label_text"] = label_text
            except:
                print("IMAGE FAILED TO LOAD")
                print(f"\tData:\n\t{img_data=}")
                self.data.remove(img_data)
        
        print("DONE LOADING IMAGES")


    def set_img(self, img_data:dict):
        self.img_data_label.config(text=img_data["label_text"])

        img_data["image"] = ImageTk.PhotoImage(
            self.autoscale_img(img_data["image_path"])
            )
        
        self.image_label.config(image=img_data["image"])



    def scale_img(self, file):# TODO Fix the auto-sizing
        img = Image.open(file)
        return ImageOps.contain(img, (700, 700))

    def autoscale_img(self, file):
        img = Image.open(file)
        master_width = max(700, self.image_frame.winfo_width())
        #print(f"{master_width = }")
        master_height = max(700, self.image_frame.winfo_height())
        #print(f"{master_height = }")
        return ImageOps.contain(img, (master_width, master_height))


    def run_app(self):
        self.root.mainloop()

    def toggle_run(self):
        print("clicked run/stop!")

    def stop(self):
        print("clicked stop!")

    def previous(self):
        print("clicked previous!")
        try:
            self.img_idx = (self.img_idx - 1) % len(self.data)
            self.set_img(self.data[self.img_idx])
        except:
            print("Image failed to load")

    def next(self):
        print("clicked next!")
        try:
            self.img_idx = (self.img_idx + 1) % len(self.data)
            self.set_img(self.data[self.img_idx])
        except:
            print("Image failed to load")

