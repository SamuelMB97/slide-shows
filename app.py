import tkinter as tk

class SlideShow():
    def __init__(self, window_title):
        self.root = tk.Tk()
        self.root.title(window_title)
        self.root.minsize(700, 700)
        self.root.maxsize(900, 900)
        self.root.geometry("700x700+25+50")

        self.image_frame = tk.Frame(self.root, background="light blue").grid(row=1, column=1)#.pack(fill="both")
        """
        self.image = tk.PhotoImage(
            self.image_frame
            )
        """
        tk.Label(self.image_frame, text="This is a label for the image frame...").grid(row=1, column=1)#.pack(fill="y")

        self.buttons_frame = tk.Frame(self.root).grid(row=2, column=0)#.pack(fill="x")
        self.run_button = tk.Button(
            self.buttons_frame, text="run", command=self.run
            ).grid(row=0, column=0)#.pack(anchor="w")
        self.stop_button = tk.Button(
            self.buttons_frame, text="stop", command=self.stop
            ).grid(row=0, column=1)#.pack(anchor="w")
        self.previous_button = tk.Button(
            self.buttons_frame, text="previous", command=self.previous
            ).grid(row=0, column=2)#.pack(anchor="w")
        self.next_button = tk.Button(
            self.buttons_frame, text="next", command=self.next
            ).grid(row=0, column=3)#.pack(anchor="w")

    def run_app(self):
        self.root.mainloop()

    def run(self):
        print("clicked run!")

    def stop(self):
        print("clicked stop!")

    def previous(self):
        print("clicked previous!")

    def next(self):
        print("clicked next!")

