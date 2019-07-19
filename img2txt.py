from PIL import Image

#max value for luminance is ~277 (rounded down), min is 0 #print(255*0.299+255*0.7152+255*0.0722) #max value for luminance is 277.032

chars = ["@","$","#","H","E","W","g","h","f","e","c","n","<","+","=","~","-","^","*","'"] #chars in order of perceived brightness: left to right - dark to bright
mult = 1.5 #has to be greater than 1 #inversely proportional to the size of the image output

img = "cat.jpg"

textImg = open((img + ".txt"), "w")
image = Image.open(img)
imageWidth, imageHeight = image.size
imgDat = image.load()
for y in range(0, round(imageHeight/mult)):
    for x in range(0, round(imageWidth/mult)):
        luminance = (100/277.032) * (imgDat[x*mult,y*mult][0]*0.2126 + imgDat[x*mult,y*mult][1]*0.7152 + imgDat[x*mult,y*mult][2]*0.0722) #imgDat[x,y][0, 1, or 2 for R, G, or B vals]
        textImg.write(chars[int(round(luminance)/5)])
    textImg.write("\n")
textImg.close()
