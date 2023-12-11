from annotator.dwpose import DWposeDetector

if __name__ == "__main__":
    pose = DWposeDetector()
    import cv2
    test_image = 'test_imgs/pose1.png'
    oriImg = cv2.imread(test_image)  # B,G,R order
    import matplotlib.pyplot as plt
    out = pose(oriImg)
    plt.imsave('result.jpg', out)
