from pprint import pprint

folder = '/Users/David/Desktop/Project1Images/'

pictures = []
counter = 0

for counter in range(0,9):
  imagePath = folder + str(counter + 1) + '.png'
  #print(imagePath)
  pictures.append(makePicture(imagePath))
  counter = counter + 1 

#pprint(pictures)

myList = []
redPixelList = []
greenPixelList = []
bluePixelList = []


def median(myList):
  listLength = len(myList)
  sortedValues = sorted(myList)
  middleIndex = (listLength/2) + 1
  return sortedValues[middleIndex]


  
height = 557
width = 495



canvas = makeEmptyPicture(width, height)
#show(canvas)
for x in range(0,width):
 for y in range(0,height):
   for index in range(0,9):
     
     pixel = getPixel(pictures[index], x, y)
     
     red = getRed(pixel)
     green = getGreen(pixel)
     blue = getBlue(pixel)
     
     redPixelList.append(red)
     greenPixelList.append(green)
     bluePixelList.append(blue)
     
   #find median
   
   newPixel = makeColor(median(redPixelList),median(greenPixelList),median(bluePixelList))
   getPixel(canvas,x,y).setColor(newPixel)
   #repaint(canvas)
   
   
   #clear values
   redPixelList = []
   greenPixelList = []
   bluePixelList = []


show(canvas)