---
title: Images
source: https://docs.kanzi.com/4.1.0/en/working-with/images/images.html
---

# Images


Use image files to bring bitmap assets to Kanzi Studio.

Use image files to bring bitmap assets to Kanzi Studio. You can import images to Kanzi in these file formats:

- .png, including the alpha channel
- .tga, including the alpha channel
- .psd, including layers. See Importing Adobe Photoshop PSD files.
- .dds, can contain cubemaps, mipmaps, or both
- .bmp, .exr, .gif, .hdr, .ico, .iff, .jng, .jpg, .jpeg, .jif, .mng, .pcx, .pmb, .pgm, .ppm, .pfm, .pict, .ras, .sgi, .tiff, .tif, .wbmp, .xmb, and .xpm

## Image Compression


While most image formats contain pixel data in compressed form, the data is usually taken into GPU uncompressed. However, when images are stored in compression formats that are natively supported by GPUs, images are transferred and stored on the GPU in a compressed form. This reduces the time needed for uploading the image data to the GPU and can boost the performance.

The best performing compression level depends on your target device. High compression levels use more CPU but less memory bandwidth, whereas low compression levels use less CPU but more memory bandwidth.

Kanzi supports these compression formats natively supported by GPUs:

- **Adaptive Scalable Texture Compression (ASTC)** ARM and AMDâs block-based compression algorithm. ASTC creates smaller files and better image quality than the ETC algorithm. An ASTC block takes 128 bits, and you can set the size of the block in pixels. Fewer pixels in a block result in better image quality of the compressed image, but create larger file sizes.
- **Ericsson Texture Compression (ETC)** ETC compression saves 5/6 of the memory used by the image on the GPU. However, the space taken by the image in the kzb file is likely to be increased compared to, for example, PNG or JPEG formats.


See Compressing textures.
## Mipmaps


Mipmaps are pre-calculated collections of images that increase the rendering speed and reduce rendering artifacts.

The compression of images and the generation of mipmaps take some time. Kanzi asks you to preprocess the images before exporting the kzb file. Because your Kanzi application can run without the preprocessed data, if the preprocessed data is not available, your application runs without it. See Using mipmaps.
