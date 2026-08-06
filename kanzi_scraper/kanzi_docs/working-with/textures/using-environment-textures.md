---
title: Using environment textures
source: https://docs.kanzi.com/4.1.0/en/working-with/textures/using-environment-textures.html
---

# Using environment textures


Use an environment texture to represent the environment, such as an outdoor scene or an indoor space. You can create an environment texture from an HDR or EXR image:

- An environment cubemap texture combines six square-shaped images into a texture that represents the environment. See Using an environment cubemap texture.
- An environment lat-long (equirectangular) texture is a single image that represents the environment. See Using a lat-long environment texture.

## Using an environment cubemap texture


To use an environment cubemap texture:

1.

Create an environment cubemap texture:

  1.

In the Assets click Import Assets and select an HDR or EXR image from which you want to create an environment cubemap texture.

> **Tip:** To create an environment cubemap texture for an HDR or EXR image that you have already imported to your Kanzi Studio project, in the Library > Resource Files > Images press Alt and right-click that image and select Environment Cubemap Texture.
> 2.
>
> In the Create Textures for HDR Images dialog:
>
> 1.
>
> Select Environment Cubemap Texture.
>
> Tip
>
> To create for the image also irradiance and specular cubemap textures that represent the lighting coming from the environment, select Image-Based Lighting Cubemap Textures. See Using image-based lighting cubemap textures.
> 2.
>
> (Optional) To manually set the size of the cubemap faces, disable the Automatic setting and set the Cubemap Face Resolution.
>
> For example, to create an environment cubemap texture where the size of each cubemap face is 512 by 512 pixels, set Cubemap Face Resolution to 512.
>
> Kanzi Studio by default creates a cubemap texture where the width and height of each cubemap face is one quarter of the width of the image that you import.
> 3.
>
> Click Create.


Kanzi Studio imports the image and creates in the Library > Materials and Textures > Textures an environment Cubemap Texture for that image.

Kanzi Studio creates and sets the cubemap face images:

    - NegZ Image to the front face image
    - PosZ Image to the back face image
    - NegX Image to the left face image
    - PosX Image to the right face image
    - NegY Image to the bottom face image
    - PosY Image to the top face image


> **Tip:** You can restrict the brightness of strongly lit areas in the textures that you create from an HDR image.
>
> To set the maximum brightness level in the cubemap textures that you create from an HDR image:
>
> 1.
>
> In the Library > Resource Files > Images, select the image. In the Properties, add the Clamp Pixels property and set it to the value to which you want to restrict the color values in the cubemap face images that you create from that image.
> 2.
>
> In the Library > Resource Files > Images, press Alt and right-click the image and select the cubemap texture that you want to create.


2.

In the Library > Materials and Textures, press Alt and right-click Material Types, and select CubemapSkybox.

Kanzi Studio creates in the Library > Materials and Textures the CubemapSkybox material type and CubemapSkyboxMaterial, which supports showing a cubemap texture as a skybox.
3.

In the Library, select the CubemapSkyboxMaterial material. In the Properties, set the TextureCube property to the cubemap texture that you want to use to render a skybox.
4.

Create a Box or Sphere node that you use to render the skybox. In the Properties, set:

  - Mesh Material to CubemapSkyboxMaterial
  - The size of the node so that it is large enough to fit the content that you want to show inside it:

    - For a Box, set the Width, Height, and Depth properties.
    - For a Sphere, set the Radius property.

  - Generate Mesh Inside Out to enabled

When this property is enabled, Kanzi renders the cubemap texture inside the mesh.

5.

Position a Camera node inside the node that you created.


When you rotate the camera, in the Preview you can see the environment texture rendered as a skybox.
## Using a lat-long environment texture


To use a lat-long (equirectangular) environment texture:

1.

Create a lat-long environment texture:

  1.

In the Assets click Import Assets and select an HDR or EXR image that you want to use for the lat-long environment texture.

> **Note:** If you use an LDR image, import the image, select the texture in the Library > Materials and Textures > Textures, and in the Properties set the Wrap Mode property to Repeat.
> 2.
>
> In the Create Textures for HDR Images dialog, select Single Texture, and click Create.
>
> Kanzi Studio imports the image and creates a Single Texture in the Library > Materials and Textures > Textures.
>
> 2.
>
> In the Library > Materials and Textures, press Alt and right-click Material Types, and select LatLongSkybox.
>
> Kanzi Studio creates in the Library > Materials and Textures the LatLongSkybox material type and LatLongSkyboxMaterial, which supports showing a lat-long environment texture as a skybox.
> 3.
>
> In the Library, select the LatLongSkyboxMaterial material. In the Properties, set the Texture property to the lat-long (equirectangular) texture that you want to use to render a skybox.
> 4.
>
> Create a Box or Sphere node that you use to render the skybox. In the Properties, set:
>
> - Mesh Material to LatLongSkyboxMaterial
> - The size of the node so that it is large enough to fit the content that you want to show inside it:
> - For a Box, set the Width, Height, and Depth properties.
> - For a Sphere, set the Radius property.
> - Generate Mesh Inside Out to enabled


When this property is enabled, Kanzi renders the environment texture inside the mesh.
5.

Position a Camera node inside the node that you created.


When you rotate the camera, in the Preview you can see the environment texture rendered as a skybox.
