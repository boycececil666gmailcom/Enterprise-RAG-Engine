---
title: Step 4 - Define material properties for the windows and the headlight glass
source: https://docs.kanzi.com/4.1.0/en/tutorials/materials-and-textures/step-4.html
---

# Step 4 - Define material properties for the windows and the headlight glass


The car is still missing transparent windows and the headlight glass. Again, you use the same cubemap texture for the windows and the headlight glass as you did for the main body of the car, because you want to have the same environment reflection on the windows and the headlight glass as you do on the car.

In this step you define the material properties for the windows and the headlight glass.
## Define the material properties for the windows


1.

In the Library > Materials and Textures > Materials select the Windows_1 material, and in the Properties set:

  - Material Type to VertexPhongTexturedCube
  - Texture to CarBody
  - TextureCube to CarBodyCubemapTexture
  - CubemapColor Lightness (L) property field to 109

2.

In the Properties make windows transparent by setting the Windows_1 material properties:

  - Blend Intensity to 0.66
  - Blend Mode to Alpha: Premultiplied


## Define the material properties for the headlight glass


1.

In the Library > Materials and Textures > Materials select the HeadlightGlass material, and in the Properties set:

  - Material Type to VertexPhongTexturedCube
  - Texture to CarBody
  - TextureCube to CarBodyCubemapTexture
  - CubemapColor Lightness (L) property field to 181

2.

In the Properties make the headlight glass transparent by setting the HeadlightGlass material properties:

  - Blend Intensity to 0.42
  - Blend Mode to Alpha: Premultiplied


Previous step Next step
