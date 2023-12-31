from PIL import Image #pip install Pillow
import os

downloadsFolder = "C:/Users/ezio3/OneDrive/Escritorio/ordenar/"
picturesFolder = "C:/Users/ezio3/OneDrive/Escritorio/photos/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3"]:
            musicFolder = "C:/Users/ezio3/OneDrive/Escritorio/musica/"
            os.rename(downloadsFolder + filename, musicFolder + filename)