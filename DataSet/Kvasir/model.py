import os
import cv2
import matplotlib.pyplot as plt

# Paths
image_path = "images"
mask_path = "masks"

# Load image and mask
image_file = os.listdir(image_path)[500]
mask_file = os.listdir(mask_path)[500]

image = cv2.imread(os.path.join(image_path, image_file))
mask = cv2.imread(os.path.join(mask_path, mask_file), 0)

# Display
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Image")
plt.subplot(1, 2, 2)
plt.imshow(mask, cmap='gray')
plt.title("Mask")
plt.show()
