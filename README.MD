# Mirror Flip Testing for Policy Learning

In [this paper](https://arxiv.org/html/2402.10329v3/), the authors suggest that *"digitally reflecting the crop of the images in the mirrors yields the best result for policy learning."* This repo contains a test setup to visualize and verify mirror flipping using the `get_mirror_crop_slices` utility.

Check out `reflect.png` for a visual explanation of the effect.

## 🔧 Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

The `cv_util.py` file is sourced from the [Universal Manipulation Interface (UMI) repository](https://github.com/real-stanford/universal_manipulation_interface).

## 🧪 Test Script Overview

The included test script demonstrates and validates the mirror-flipping logic using a synthetic image.

It performs the following steps:

1. **Generates a blank black image** with resolution 1920×1080.
2. **Draws two rectangles**:
   - **Left Rectangle**:
     - Filled with blue.
     - Edges marked with distinct colors: red (top), green (bottom), yellow (left), magenta (right).
   - **Right Rectangle** (mirror side):
     - Filled with red.
     - Edges marked in blue (top), green (bottom), orange (left), and cyan (right).
3. **Crops and flips** each rectangle using `get_mirror_crop_slices` from `cv_util.py`.
4. **Swaps the flipped regions** between left and right.
5. **Saves the original and flipped images** for visual inspection (`original.png`, `result.png`).


This setup makes it easy to verify that the flipping logic aligns with the theoretical intent described in the paper.

