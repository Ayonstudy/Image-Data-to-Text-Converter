import sys
from PIL import Image
# Image-Data-to-Text-Convertor (IDTC)
# Made in 20 August 2024 by Ayonstudy :)
# This program converts Image pixel data into text form. More specifically, it just makes a seperate text file with data about the image.
# The program has two parameters
# The first arguement is compulsory, it is the name of the image file (e.g. image.png)
# The second arguement is optional, it is the name of the final file to be given where the data will be saved to (e.g. file.txt) [the default is "image-data.txt"]
# Example of running command         --> "IDTC image.png file.txt" or "./IDTC.py image.png"
# After running the program, the data will be saved onto the image-data.txt file or the file name you will give as the second arguement.
# The first line in the text file will be width and hieght respectively
# From the next line and onwards will be the pixel data in hexadecimal. Each two digit of the hexadecimal values goes in order red,green,blue then finally transperancy level
# Each pixel data will be seperated by a comma (,) and each new line represents the next row of pixels from the image.
parameter_number = len(sys.argv)                                                                 # Number of arguements
if parameter_number == 1:                                                                        # Lack of arguements
    print("Syntax error: Must include image file name")
    exit()
elif parameter_number == 2:                                                                      # arguement for image file name
    final_file_name = "image-data.txt"
elif parameter_number == 3:                                                                      # arguement for text file name (optional)
    final_file_name = sys.argv[2]
elif parameter_number >= 4:                                                                      # Excess arguements
    print("Syntax error: Too many arguements!")
    exit()
im = Image.open(sys.argv[1])                                                                      # sys.argv[1] is parameter for image file to be load onto program and be converted
px = im.load()
width, hieght = im.size                                                                           # get height and width values
print()

f = open(final_file_name, "w")                                                                    # Empty previous file
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
        f = open(final_file_name, "a")
        if x > 0:
            f.write(",")
        f.write("0x" + format(r, '02x') + format(g, '02x') + format(b, '02x') + format(t, '02x')) # save pixel data from second line
        f.close()
    f = open(final_file_name, "a")
    f.write("\n")                                                                                 # start new line
    f.close()
    progress=format(((y/hieght)*100), ".2f")      
    sys.stdout.write("\rFile Formating Progress: " + str(progress) + "%")                         # update and show current progress
    sys.stdout.flush()
sys.stdout.write("\r\rFile Formating Progress: 100.00%\n")
print("Process completed!!")                                                                      # final result with data will be in the text file after completion
print("Data saved in " + final_file_name)                                                         # recommended to use another text file name to prevent overwrite
