---
title: Step 3 - Set the materials for tires, rims, and chrome parts
source: https://docs.kanzi.com/4.1.0/en/tutorials/materials-and-textures/step-3.html
---

# Step 3 - Set the materials for tires, rims, and chrome parts

Now that you created the textures for the car body, you start filling in the details of the car, creating textures and assigning them to materials for specific car parts.

In this step you create textures and define the materials for the tires and rims, and you define the properties to create the chrome effect for the chrome parts.
## Set the materials for tires and rims

1.

In the Library > Materials and Textures > Materials select the Tire material and in the Properties set:

  - Material Type to VertexPhongTextured
  - Texture to CarTire

2.

In the Library > Materials and Textures > Materials select the Rim material and in the Properties set:

  - Material Type to VertexPhongTexturedCube
  - Texture to CarRim
  - TextureCube to CarBodyCubemapTexture
  - CubemapColor Lightness (L) property field to 186

For the rims you use the same cubemap texture as you do for the car because you want the environment reflection to be the same for the rims as it is for the car.

## Define the properties for the chrome parts

1.

In the Library > Materials and Textures > Materials select Chrome, and in the Properties set:

  - Material Type to VertexPhongTexturedCube
  - Texture to CarBody
  - TextureCube to CarBodyCubemapTexture
  - CubemapColor Lightness (L) property field to 161

2.

In the Properties adjust the color properties to get the chrome reflection.

For example, set:

  - Ambient Color property:

    - Lightness (L) property field to 140
    - Intensity (I) property field to +2

  - Diffuse Color property Lightness (L) property field to 60
  - Emissive Color property Lightness (L) property field to 20

Previous step Next step
