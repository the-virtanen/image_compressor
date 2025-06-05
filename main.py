from PIL import Image, ImageOps
import os

size = (100, 150)
mode = input("Select mode: 1 - contain, 2 - cover, 3 - fit, 4 - pad: ")
#contain, cover, fit, pad

directory = "img_input"
output = "img_output"


files = sorted(os.listdir(directory))

files = [f for f in files if os.path.isfile(os.path.join(directory, f))]

if files:
    first_file_path = os.path.join(directory, files[0])

else:
    print("No files found in the directory.")

file_name = first_file_path.split("/", -1)
file_name = file_name[-1].rstrip(".png")



with Image.open(first_file_path) as im:
    match mode:
        case "1":
            ImageOps.contain(im, size).save(f"img_output/{file_name}_contain_{size[0]}x{size[1]}.png")
        case "2":
            ImageOps.cover(im, size).save(f"img_output/{file_name}_cover_{size[0]}x{size[1]}.png")
        case "3":
            ImageOps.fit(im, size).save(f"img_output/{file_name}_fit_{size[0]}x{size[1]}.png")
        case "4":
            ImageOps.pad(im, size, color="#f00").save(f"img_output/{file_name}_pad_{size[0]}x{size[1]}.png")
        case _:
            raise Exception("invalid mode")

