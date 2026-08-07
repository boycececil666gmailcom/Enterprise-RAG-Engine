---
title: Adjusting the data size
source: https://docs.kanzi.com/4.1.0/en/best-practices/images-and-textures/adjusting-the-data-size.html
---

# Adjusting the data size

When you use the correct data sizes for images, textures and shaders you reduce the memory requirements. Adjust the data size to reflect the requirements of your application:

- If the screen resolution of the target devices is low, make sure the texels of the texture match the pixels of the target screen. For example, when you have a 50 by 40 pixels textured button on a screen 320 by 200 pixels, the optimal size of the texture that returns the best quality is a 50 by 40 pixels texture. You can combine image downscaling with image compression. Try to find a compromise between required visual quality and application performance. See Compressing textures.
- You have to have a really good reason to use textures larger than 1024 pixels. If texture is 1024 pixels wide or high and contains a repeating pattern, extract the smallest repeating pattern and in the texture set the Wrap Mode to Repeat.
- The memory required by a texture corresponds directly to the texture format you use. For example, an 8-bit grayscale texture requires 8 bits for each pixel, whereas RGBA8 requires four 8-bit channels (32 bits for each pixel).
- Make sure that all faces of a cubemap texture use images of the same size and format. When the size and format of the images in a cubemap texture do not match, Kanzi uses the default cubemap texture.

For example, for all faces of a cubemap texture use images that are 256 by 256 pixels large and are 8-bit grayscale.

When the size and format of the images in a cubemap texture do not match, Kanzi Studio uses red type to mark such textures.
- Use mipmaps to create a set of downscaled sublevels from a large texture. Mipmaps increase the GPU memory use by one third, but improve the performance when the full texture does not have to be sampled. Use mipmaps to improve the performance whenever you scale a textured node.

See Using mipmaps.

Avoid creating textures from very large images. For example, do not create textures directly from digital camera pictures. Instead create textures from preprocessed and properly detailed graphics. - Make sure that the tools you use for creating and converting images create images of the smallest possible size. For example, if you are using PNG images, use tools like [pngcheck](http://www.libpng.org/pub/png/apps/pngcheck.html) and [Pngcrush](http://pmt.sourceforge.net/pngcrush/) to ensure that the images are of the correct type and do not contain any unnecessary data.
