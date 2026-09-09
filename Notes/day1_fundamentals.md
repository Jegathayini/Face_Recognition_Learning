# Day 1 - Computer Vision Fundamentals

## What is Computer Vision?

Computer Vision is a field of Artificial Intelligence that enables computers to understand and interpret images and videos.

## What is an Image?

An image is a collection of pixels arranged in rows and columns.

## What is a Pixel?

Pixel stands for Picture Element.

A pixel is the smallest unit of a digital image.

## What is Resolution?

Resolution represents the width and height of an image.

Example:

1920 x 1080

This image contains:

1920 × 1080 = 2,073,600 pixels

## RGB

RGB stands for:

- Red
- Green
- Blue

Colors are represented using intensity values from 0 to 255.

## OpenCV Color Format

OpenCV uses BGR instead of RGB.

## Pixels

An image is made of pixels.

Pixels are arranged in rows and columns.

A pixel can be accessed using: img[0,0]

## Grayscale Images

A grayscale image stores only brightness information instead of color information.

Pixel values range from:

- 0 = Black
- 255 = White

Grayscale images use a single channel instead of three color channels.

---

### Converting a Color Image to Grayscale

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
``