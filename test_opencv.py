import cv2
import numpy as np

def main():
    img = cv2.imread('./IMG_0208.JPG')
    px = img[100, 100]
    print(px)
    print(img.shape)
    print(img.size)
    print(img.dtype)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
