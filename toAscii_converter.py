import argparse
from PIL import Image
import cv2
import numpy as np

DENSITY = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

parser = argparse.ArgumentParser(description="")

parser.add_argument("-f", "--file", help="./image.jpg", default=1)


def scale(val):
        # val/255 = new_val/len(DENSITY) => new_val = val*len(DENSITY)/255
        new_val = val*len(DENSITY)/255
        return int(new_val)

def convert_frame(frame):
        #if len(frame.shape) == 3:
        #    frame = frame[:,:,0]
        
        frame = cv2.resize(frame, (int(frame.shape[1]*1), int(frame.shape[0]*0.6)), interpolation = cv2.INTER_AREA)
        
        text = ""
        for i in frame:
            for j in i:
                text += DENSITY[scale(j) ] if scale(j) < len(DENSITY) else DENSITY[-1]
            text += '\n'
        return text

if __name__ == "__main__":
    args = parser.parse_args()
    file_dir = args.file
    image = Image.open(file_dir)
    image = np.array(image)
    print(convert_frame(image[:,:,0]))
    try:
       
        pass
        
    except Exception as e:
        print(e)