---
title: Preparing images in third-party tools
source: https://docs.kanzi.com/4.1.0/en/working-with/images/preparing-images-in-3rd-party-tools.html
---

# Preparing images in third-party tools


When you are preparing in a third-party tool the images that contain transparency, keep in mind that Kanzi by default premultiplies the alpha channel of an image in linear color space. This is the colorimetrically correct way and results in the fewest artifacts.

When preparing images, configure your tool to blend RGB colors in linear color space. This way when you import the images to Kanzi Studio, they by default look the same in Kanzi Studio as they do in the tool where you created them.

For example, to blend colors in linear color space in Photoshop, in the Color Settings - Advanced Controls, set Blend RGB Colors Using Gamma 1.00 to enabled.

If you prepare images in a third-party tool that does not support configuring the blending behavior, and after importing your image to Kanzi Studio the image does not look correct, in the Library > Resource Files > Images select the image and in the Properties disable the Linear Premultiply property.

This way you set Kanzi to premultiply the alpha channel in the color space of the image.

These images show an example of the difference between enabling (left) and disabling (right) the Linear Premultiply property of an image.
