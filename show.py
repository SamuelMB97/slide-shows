import sys
from app import SlideShow
import json
import os


def main():
    directory = sys.argv[1]
    print("dir: ", directory)

    if len(sys.argv) > 2:#Get data from album
        # album_file = sys.argv[2]
        album_file = r"animalPics\AnimalPics\Animals_album.json"
        print("album: ", album_file)
        with open(album_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        app = SlideShow(album_file, data)#TODO Parse album name!

    else:#Get data from directory
        data = []
        for entry in os.scandir(directory):
            if entry.name.upper().endswith(("JPG", "JPEG", "PNG", "GIF")):
                print(f"{entry.name} is an image!")
                img_info = {
                    "image_path": os.path.relpath(entry.path),
                    "file_name": entry.name}
                data.append(img_info)
            else:
                print(f"{entry.name} is not an image")
        app = SlideShow(directory, data)

                
    print(f"data type={type(data)}")
    print()
    for e in data:
        print(f"e type={type(e)}, {e=}")
    print("Data from album file is ready")

    app.run_app()

if __name__ == "__main__":
    main()

