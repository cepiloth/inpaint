from __future__ import print_function

import numpy as np
import cv2 as cv

from common import Sketcher

def main():
    import sys
    try:
        fn = sys.argv[1]
    except:
        fn = 'example_wood.jpg'

    img = cv.imread(cv.samples.findFile(fn))
    
    if img is None:
        print('Failed to load image file:', fn)
        sys.exit(1)

    img_original = img.copy()
    cv.imshow('original', img_original)

    img_mark = img.copy()
    mark = np.zeros(img.shape[:2], np.uint8)
    sketch = Sketcher('img', [img_mark, mark], lambda : ((255, 255, 255), 255))

    while True:
        ch = cv.waitKey()
        if ch == 27:
            break
        if ch == ord(' '):
            res = cv.inpaint(img_mark, mark, 3, cv.INPAINT_TELEA)
            cv.imshow('inpaint', res)
        if ch == ord('r'):
            img_mark[:] = img
            mark[:] = 0
            sketch.show()

    print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()