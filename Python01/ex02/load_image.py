from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """
    A fonction that loads an image, prints its format and its
    pixels content in RGB format
    """
    try:
        img = Image.open(path)
    except:
        AssertionError("An exception occurend while opening image.jpg")
    if img.format not in ('JPEG', 'JPG'):
        raise TypeError("not a valid format")
    img_np = np.array(img)
    print(f"format: {img.format}")
    print(f"The shape of image is: {img_np.shape}")
    print(img_np)
    return img_np
