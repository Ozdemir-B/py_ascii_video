import cv2
import time
import numpy as np
import argparse

DENSITY = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

parser = argparse.ArgumentParser(description="")

parser.add_argument("-s", "--size_scale", help="like 0.5, 0.2, 2, etc", default=1)


def scale(val):
        # val/255 = new_val/len(DENSITY) => new_val = val*len(DENSITY)/255
        new_val = val*len(DENSITY)/255
        return int(new_val)

def convert_frame(frame):
        text = ""
        for i in frame:
            for j in i:
                text += DENSITY[scale(j) ] if scale(j) < len(DENSITY) else DENSITY[-1]
            text += '\n'
        return text


def video_capture(size_scale):
    # define a video capture object
    vid = cv2.VideoCapture(0)
    
    while(vid.isOpened()):
        time.sleep(0.1)
        ret, frame = vid.read()
        frame = frame[:,:,0] ## frame is 3D, we only need the first 2 dimensions -> this is the grayscale image
        gray = cv2.resize(frame, (int(1400*size_scale), int(480*size_scale)), interpolation = cv2.INTER_AREA)
        matrix = convert_frame(gray)
        print(convert_frame(gray),end='\r')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    args = parser.parse_args()
    size_scale = float(args.size_scale)
    video_capture(size_scale)