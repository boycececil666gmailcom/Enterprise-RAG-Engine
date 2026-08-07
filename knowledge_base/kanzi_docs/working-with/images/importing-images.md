---
title: Importing images
source: https://docs.kanzi.com/4.1.0/en/working-with/images/importing-images.html
---

# Importing images


When you import images Kanzi Studio automatically creates textures from those images.

Use image files to bring bitmap assets to Kanzi Studio. You can import images to Kanzi in these file formats:

- .png, including the alpha channel
- .tga, including the alpha channel
- .psd, including layers. See Importing Adobe Photoshop PSD files.
- .dds, can contain cubemaps, mipmaps, or both
- .bmp, .exr, .gif, .hdr, .ico, .iff, .jng, .jpg, .jpeg, .jif, .mng, .pcx, .pmb, .pgm, .ppm, .pfm, .pict, .ras, .sgi, .tiff, .tif, .wbmp, .xmb, and .xpm

## Importing images to a Kanzi Studio project


To import images:

1.

In the Assets window click Import Assets.
2.

Select the files that you want to import and click Open.


When you import images, Kanzi Studio adds those images to the Library > Resource Files > Images, and creates from them textures in the Library > Materials and Textures > Textures:

- For dds images that contain cubemaps, mipmaps, or both, Kanzi Studio automatically extracts the cubemap faces and mipmap images, creates a Cubemap Texture, and assigns to the Cubemap Texture the cubemap faces from the dds image. See Using cubemap textures.
- For hdr and exr images Kanzi Studio asks you what type of textures you want to create:

  - Single Texture. See Using single textures.
  - Environment cubemap texture. See Using environment textures.
  - Irradiance and specular cubemap textures for image-based lighting. See Using image-based lighting cubemap textures.

- For other images Kanzi Studio creates a Single Texture.
