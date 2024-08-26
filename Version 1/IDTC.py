import sys
from PIL import Image
# Image-Data-to-Text-Convertor (IDE)
# Made in 20 August 2024 by Ayonstudy :)
# This program converts Image pixel data into text form, more specifically just makes a seperate text file with data about the image.
# The program requires one parameter --> The name of the image file (e.g. image.png)
# Example of running command         --> "IDTC image.png" or "./IDTC image.png"
# The image file has to be in the same directory as the IDTC.py file.
# After running the program, the data will be saved onto the image-data.txt file which will be created after the process is finished.
# The first line in the image-data.txt file will be width and hieght respectively
# From the next line and onwards will be the pixel data in hexadecimal. Each two digit goes in order red,green,blue then finally transperancy level
# Each pixel data will be seperated by a comma (,) and each new line represents the next row of pixels from the image.
im = Image.open(sys.argv[1])                                                                      # sys.argv[1] is parameter for image file to load onto program
px = im.load()
width, hieght = im.size                                                                           # get height and width values
print()

f = open("image-data.txt", "w")                                                                   # to reset previous file
f.write(str(width) + "," + str(hieght) + "\n")                                                    # save width and hieght data on first line
f.close()
progress=0
for y in range(hieght):
    for x in range(width):
        try:                                                                                      # in case t doesn't exist in image file
            r,g,b,t = px[x,y]                                                                     # r = red, g = green, b = blue, t = transparency
        except ValueError:
            r,g,b = px[x,y]                                                                       # r = red, g = green, b = blue
            t = 255                                                                               # t = transparency (set to 0xff)
        f = open("image-data.txt", "a")
        if x > 0:
            f.write(",")
        f.write("0x" + format(r, '02x') + format(g, '02x') + format(b, '02x') + format(t, '02x')) # save pixel data from second line
        f.close()
    f = open("image-data.txt", "a")
    f.write("\n")                                                                                 # start new line
    f.close()
    progress=format(((y/hieght)*100), ".2f")      
    sys.stdout.write("\rFile Formating Progress: " + str(progress) + "%")                         # update and show current progress
    sys.stdout.flush()
sys.stdout.write("\r\rFile Formating Progress: 100.00%\n")
print("Process completed!!")                                                                      # final result with data will be in file.txt file after completion
print("Data saved in image-data.txt")
