import cv2
import matplotlib.pyplot as plt
import numpy as np

from cv_util import get_mirror_crop_slices

# Create a black test image with dimensions (height, width, channels)
img_height, img_width = 1080, 1920
image = np.zeros((img_height, img_width, 3), dtype=np.uint8)

# Inset to draw edges inside the rectangle
inset = 2
thickness = 4

# --- Rectangle Positions (from get_mirror_crop_slices logic) ---
# Left rectangle
left_top_left = (394, 596)
left_bottom_right = (586, 788)

# Right rectangle (mirror)
right_top_left = (1334, 596)
right_bottom_right = (1526, 788)

# ------------------- Draw Left Rectangle -------------------
# Fill with blue
cv2.rectangle(image, left_top_left, left_bottom_right, (255, 0, 0), thickness=-1)

# Top edge (red) inside the rectangle
cv2.line(
    image,
    (left_top_left[0] + inset, left_top_left[1] + inset),
    (left_bottom_right[0] - inset, left_top_left[1] + inset),
    (0, 0, 255),
    thickness=thickness,
)

# Bottom edge (green)
cv2.line(
    image,
    (left_top_left[0] + inset, left_bottom_right[1] - inset),
    (left_bottom_right[0] - inset, left_bottom_right[1] - inset),
    (0, 255, 0),
    thickness=thickness,
)

# Left edge (yellow)
cv2.line(
    image,
    (left_top_left[0] + inset, left_top_left[1] + inset),
    (left_top_left[0] + inset, left_bottom_right[1] - inset),
    (0, 255, 255),
    thickness=thickness,
)

# Right edge (magenta)
cv2.line(
    image,
    (left_bottom_right[0] - inset, left_top_left[1] + inset),
    (left_bottom_right[0] - inset, left_bottom_right[1] - inset),
    (255, 0, 255),
    thickness=thickness,
)

# ------------------- Draw Right Rectangle -------------------
# Fill with red
cv2.rectangle(image, right_top_left, right_bottom_right, (0, 0, 255), thickness=-1)

# Top edge (blue)
cv2.line(
    image,
    (right_top_left[0] + inset, right_top_left[1] + inset),
    (right_bottom_right[0] - inset, right_top_left[1] + inset),
    (255, 0, 0),
    thickness=thickness,
)

# Bottom edge (green)
cv2.line(
    image,
    (right_top_left[0] + inset, right_bottom_right[1] - inset),
    (right_bottom_right[0] - inset, right_bottom_right[1] - inset),
    (0, 255, 0),
    thickness=thickness,
)

# Left edge (orange)
cv2.line(
    image,
    (right_top_left[0] + inset, right_top_left[1] + inset),
    (right_top_left[0] + inset, right_bottom_right[1] - inset),
    (0, 165, 255),
    thickness=thickness,
)

# Right edge (cyan)
cv2.line(
    image,
    (right_bottom_right[0] - inset, right_top_left[1] + inset),
    (right_bottom_right[0] - inset, right_bottom_right[1] - inset),
    (255, 255, 0),
    thickness=thickness,
)

# ------------------- Save & Show Original -------------------
plt.figure(figsize=(12, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.savefig("original.png", dpi=300, bbox_inches="tight")

# ------------------- Crop, Flip, Swap -------------------
left_slices = get_mirror_crop_slices((img_height, img_width), left=True)
right_slices = get_mirror_crop_slices((img_height, img_width), left=False)

left_crop = image[left_slices].copy()
right_crop = image[right_slices].copy()

flipped_left = cv2.flip(left_crop, 1)
flipped_right = cv2.flip(right_crop, 1)

# Swap
image[right_slices] = flipped_left
image[left_slices] = flipped_right

# ------------------- Save & Show Result -------------------
plt.figure(figsize=(12, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.savefig("result.png", dpi=300, bbox_inches="tight")

# Check equality
original_image = cv2.imread("original.png")
result_image = cv2.imread("result.png")
images_are_equal = np.array_equal(original_image, result_image)
print("The images are equal." if images_are_equal else "The images are not equal.")
