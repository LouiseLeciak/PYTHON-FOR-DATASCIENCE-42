import sys
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    try:
        img = ft_load("animal.jpeg")
    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)
        return
    if img is None:
        print("image can't be None", file=sys.stderr)
        return
    img_zoom = img[100:500, 200:600]

    if img_zoom.shape[-1] == 1:
        print(f"New shape after slicing: {img_zoom.shape} or {np.squeeze(img_zoom).shape}")
    else:
        print(f"New shape after slicing: {img_zoom.shape}")

    print(img_zoom)
    #img_zoom = np.squeeze(img_zoom)
    plt.imshow(img_zoom)
    plt.savefig("zoomed_image.png")


if __name__ == "__main__":
    main()