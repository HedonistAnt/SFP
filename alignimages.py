import cv2
import numpy  as np

def Align(template, source):
    im1 = cv2.imread(template)
    im2 = cv2.imread(source)

    im1_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2_gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    sz = im1.shape

    warp_mode = cv2.MOTION_HOMOGRAPHY

    if warp_mode == cv2.MOTION_HOMOGRAPHY:
        warp_matrix = np.eye(3, 3, dtype=np.float32)
    else:
        warp_matrix = np.eye(2, 3, dtype=np.float32)

    number_of_iterations = 8000

    termination_eps = 1e-20

    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, number_of_iterations, termination_eps)

    (cc, warp_matrix) = cv2.findTransformECC(im1_gray, im2_gray, warp_matrix, warp_mode, criteria)

    if warp_mode == cv2.MOTION_HOMOGRAPHY:

        im2_aligned = cv2.warpPerspective(im2, warp_matrix, (sz[1], sz[0]),
                                          flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
    else:

        im2_aligned = cv2.warpAffine(im2, warp_matrix, (sz[1], sz[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)

    cv2.imshow("Template", im1)
    cv2.imshow("Source", im2)
    cv2.imshow("Aligned", im2_aligned)
    cv2.waitKey(0)



if __name__ == "__main__":
    source = "./motion/Cam1/test3/IMG_3.png"
    template = "./motion/Cam1/test2/IMG_2.png"

    Align(template, source)
