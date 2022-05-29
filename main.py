import cv2
import random

img = cv2.imread('test.jpg') # black image as background
img = cv2.resize(img, (1000, 800)) 
#print(img.shape[1], img.shape[0])

window_name = 'Color Blindness Test'

# values of the circle
cc1 = (400, 400)
cc2 = (600, 400)
radius = 5
thickness1 = -1

# color palettes
color = [(255,255,0), (35,35,139), (220,245,245)]  # list of colors
name = ['aqua', 'red', 'white']

# values of the text
font = cv2.FONT_HERSHEY_SIMPLEX
p1 = (370,500)
p2 = (570,500)
fontScale = 1
thickness2 = 1

# title
img = cv2.putText(img, window_name, (320,200), cv2.FONT_HERSHEY_TRIPLEX, 
                   fontScale, (255,255,255), 1, cv2.LINE_AA)

img = cv2.putText(img, 'press x to exit', (385, 700), font, 
                   fontScale, (255,255,255), thickness2, cv2.LINE_AA)

key = True
while (key):

    
    # randomly select color
    r1 = random.randrange(0,3)
    r2 = random.randrange(0,3)

    # to avoid getting same color in both circles
    while (r1 == r2):
        r2 = random.randrange(0,3)

    # displaying circles on the screen
    img = cv2.circle(img, cc1, radius, color[r1], thickness1)
    img = cv2.circle(img, cc2, radius, color[r2], thickness1)

    cv2.imshow(window_name, img)
    cv2.waitKey(0)    

    #displaying color name on the screen
    img = cv2.putText(img, name[r1], p1, font, 
                   fontScale, (255,255,255), thickness2, cv2.LINE_AA)
    img = cv2.putText(img, name[r2], p2, font, 
                   fontScale, (255,255,255), thickness2, cv2.LINE_AA)

    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    
    # removing the text for next loop
    img = cv2.circle(img, p1, 100, (0,0,0), thickness1)
    img = cv2.circle(img, p2, 100, (0,0,0), thickness1)

    char = str(input())
    if (char == 'x'):
        key = False
        cv2.destroyWindow(window_name)
        break



#cv2.destroyWindow(window_name)
    
