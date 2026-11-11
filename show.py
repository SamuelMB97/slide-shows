import sys
from app import SlideShow

IMG_EXTENSIONS = ("JPG", "JPEG", "PNG", "GIF")


def main():
    dir_name = sys.argv[1]
    print("dir: ", dir_name)
    app = SlideShow(dir_name)

    if len(sys.argv) > 2:
        album_file = sys.argv[2]
        print("album: ", album_file)

    app.run_app()

if __name__ == "__main__":
    main()

