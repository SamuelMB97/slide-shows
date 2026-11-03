import sys


IMG_EXTENSIONS = ("JPG", "JPEG", "PNG", "GIF")


def main():
    dir_name = sys.argv[1]
    print("dir: ", dir_name)
    if len(sys.argv) > 2:
        album_file = sys.argv[2]
        print("album: ", album_file)


if __name__ == "__main__":
    main()

