---
title: Physically-based material properties
source: https://docs.kanzi.com/4.1.0/en/working-with/materials/physically-based-materials.html
---

# Physically-based material properties

The Kanzi default physically-based material types come with preprocessor definitions that you can use to modify the material types and expose properties to the materials that use those material types. See Modifying the default material types, Physically-based shaders and Using smart materials.

This topic lists the preprocessor definitions that you can set in the Kanzi default physically-based material types.
## Lights

To set the number of different types of light nodes to use for the material, use these preprocessor definitions:

- KANZI_SHADER_NUM_DIRECTIONAL_LIGHTS sets the number of Directional Light nodes to use for the material. The default value is 1.
- KANZI_SHADER_NUM_POINT_LIGHTS sets the number of Point Light nodes to use for the material. The default value is 2.
- KANZI_SHADER_NUM_SPOT_LIGHTS sets the number of Spot Light nodes to use for the material. The default value is 1.

See Setting the number of lights for a material type.
## Exposure compensation

Exposure compensation emulates camera exposure by controlling the total amount of rendered light.

To enable setting exposure compensation, set the value of KANZI_SHADER_USE_EXPOSURE to 1.

This way you expose to the material the Exposure property that sets the exposure compensation.
## Gamma correction

Gamma correction is by default disabled for the physically-based material types.

To enable gamma correction, set the value of KANZI_SHADER_USE_GAMMA_CORRECTION to 1.
## Tone mapping

Tone mapping maps one set of colors to another set of colors to approximate the appearance of high-dynamic-range (HDR) images.

To set the tone mapping algorithm that the material type uses, set the value of one of these preprocessor definitions to 1:

- KANZI_SHADER_TONEMAP_ACES enables the approximated ACES (Academy Color Encoding System) filmic tone mapping curve by Krzysztof Narkowicz.
- KANZI_SHADER_TONEMAP_FILMIC enables filmic tone mapping by Jim Hejl and Richard Burgess-Dawson.
- KANZI_SHADER_TONEMAP_LINEAR enables linear tone mapping.
- KANZI_SHADER_TONEMAP_REINHARD enables Reinhard tone mapping.

The Kanzi physically-based material types use this tone-mapping algorithm by default.
- KANZI_SHADER_TONEMAP_UNCHARTED enables Uncharted 2 filmic tone mapping by John Hable.

## Alpha mode

To enable the use of the alpha channel in the base color of the material, set the value of KANZI_SHADER_USE_ALPHA to 1.

To enable alpha masking, set the value of KANZI_SHADER_USE_ALPHA_CUTOFF to 1.

This way you expose to the material the Alpha Cutoff property that sets the threshold for alpha cutting. Kanzi discards fragments whose alpha value is less than the threshold.

This table lists the settings for different alpha modes.
|

Alpha mode |

Settings |
|

Opaque |

- KANZI_SHADER_USE_ALPHA to 0
- KANZI_SHADER_USE_ALPHA_CUTOFF to 0
  |
|

Blend |

- KANZI_SHADER_USE_ALPHA to 1
- KANZI_SHADER_USE_ALPHA_CUTOFF to 0
  |
|

Mask |

- KANZI_SHADER_USE_ALPHA to 0
- KANZI_SHADER_USE_ALPHA_CUTOFF to 1
  |
## Vertex color

Each vertex in a mesh can optionally store a color value.

To enable the use of vertex color, set the value of KANZI_SHADER_USE_VERTEX_COLOR to 1.
## Base color texture

These preprocessor definitions control the use of base color textures:

- To enable the use of a texture that contains the base color for the material, set the value of KANZI_SHADER_USE_BASECOLOR_TEXTURE to 1.

This way you expose to the material the Base Color Texture property that sets the texture that contains the base color map for the material. The base color map is an RGB map that can contain diffuse reflected colors for a dielectric material and reflectance values for a metallic material. Use the Base Color Factor property to filter the value from the texture.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Base Color Texture, set the value of KANZI_SHADER_USE_BASECOLOR_TEXTURE_COORDINATE_INDEX to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.
- To enable the use of a detail texture that contains the base color for the material, set the value of KANZI_SHADER_USE_BASECOLOR_TEXTURE_DETAIL to 1.

This way you expose to the material these properties:

  - Detail Base Color Texture sets the detail texture that contains the base color for the material.
  - Detail Base Color Factor sets the detail base color for the material, which Kanzi alpha-blends with the base color of the material that is set by the Base Color Factor property.
  - Detail Texture Tiling sets the detail texture tiling factor for the material. Kanzi multiplies this value by the UVs to produce a second set of detail UVs to use for all detail texture properties.
  - Detail Texture Offset sets the detail texture offset for the material. Kanzi adds this value to the UVs to produce a second set of detail UVs to use for all detail texture properties.

- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Detail Base Color Texture, set the value of KANZI_SHADER_USE_BASECOLOR_TEXTURE_COORDINATE_INDEX_DETAIL to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.

## Normal map

These preprocessor definitions control the use of normal maps:

- To enable the use of a texture that contains the normal map for the material, set the value of KANZI_SHADER_USE_NORMALMAP_TEXTURE to 1.

This way you expose to the material the Normal Texture property that sets the texture that contains the normal map for the material. Use the Normal Scale property to set the intensity of the Normal Texture.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Normal Texture, set the value of KANZI_SHADER_USE_NORMALMAP_TEXTURE_COORDINATE_INDEX to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.
- To enable the use of a detail texture that contains the normal map for the material, set the value of KANZI_SHADER_USE_NORMALMAP_TEXTURE_DETAIL to 1.

This way you expose to the material these properties:

  - Detail Normal Texture sets the detail texture that contains the normal map for the material.
  - Detail Normal Scale sets the intensity of the Detail Normal Texture
  - Detail Texture Tiling sets the detail texture tiling factor for the material. Kanzi multiplies this value by the UVs to produce a second set of detail UVs to use for all detail texture properties.
  - Detail Texture Offset sets the detail texture offset for the material. Kanzi adds this value to the UVs to produce a second set of detail UVs to use for all detail texture properties.

- To enable the use of explicit binormals when normal mapping, set the value of KANZI_SHADER_USE_EXPLICIT_BINORMALS to 1. When you enable the use of explicit binormals, the shader does not reconstruct the vertex binormal from the vertex normal and vertex tangent.

## Emissive texture

These preprocessor definitions control the use of emissive textures:

- To enable the use of a texture that contains the light emitted from the material, set the value of KANZI_SHADER_USE_EMISSIVE_TEXTURE to 1.

This way you expose to the material the Emissive Texture property that sets the texture that contains the light emitted from the material. Use the Emissive Factor property to scale the value from this texture.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Emissive Texture, set the value of KANZI_SHADER_USE_EMISSIVE_TEXTURE_COORDINATE_INDEX to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.
- To enable the use of a detail texture that contains the light emitted from the material, set the value of KANZI_SHADER_USE_EMISSIVE_TEXTURE_DETAIL to 1.

This way you expose to the material these properties:

  - Detail Emissive Texture sets the detail texture that contains the light emitted from the material.
  - Detail Emissive Factor sets the color of the light that the Detail Emissive Texture emits. You can use the Intensity (I) property field to adjust the exposure of this color. This color affects local material rendering, but the light is not cast to other objects.
  - Detail Texture Tiling sets the detail texture tiling factor for the material. Kanzi multiplies this value by the UVs to produce a second set of detail UVs to use for all detail texture properties.
  - Detail Texture Offset sets the detail texture offset for the material. Kanzi adds this value to the UVs to produce a second set of detail UVs to use for all detail texture properties.

- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Detail Emissive Texture, set the value of KANZI_SHADER_USE_EMISSIVE_TEXTURE_COORDINATE_INDEX_DETAIL to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.

## Metallic-roughness materials

To enable adjusting materials based on their metalness and roughness, set the value of KANZI_SHADER_USE_PBR_METALLIC_ROUGHNESS to 1. This is the default setting for the Kanzi physically-based material types and exposes to the material these properties:

- Roughness Factor sets the roughness of the material on a scale from 0 to 1:

  - For a smooth, glossy surface set the property value to 0.
  - For a rough, diffuse surface set the property value to 1.

- Metallic Factor sets the metalness of the material on a scale from 0 to 1:

  - For a dielectric material set the value to 0.
  - For a material whose reflective behavior fully resembles that of a metal, set the value to 1.

You can use metallic, roughness, and occlusion maps to adjust the appearance of a metallic-roughness material.
### Metallic map

These preprocessor definitions control the use of metallic maps:

- To enable the use of a texture that contains a metallic map for the material, set the value of KANZI_SHADER_USE_METALLIC_TEXTURE to 1.

This way you expose to the material the Metallic Texture property that sets the texture that contains the metallic map.

Kanzi reads the metallic map from the blue channel of the texture. You can use the same texture to set the occlusion, roughness, and metallic maps for a material.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Metallic Texture, set the value of KANZI_SHADER_USE_METALLIC_TEXTURE_COORDINATE_INDEX to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.
- To enable the use of a detail texture that contains a metallic map for the material, set the value of KANZI_SHADER_USE_METALLIC_TEXTURE_DETAIL to 1.

This way you expose to the material the Detail Metallic Texture property that sets the detail texture that contains the metallic map.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Detail Metallic Texture, set the value of KANZI_SHADER_USE_METALLIC_TEXTURE_COORDINATE_INDEX_DETAIL to the semantic index of the texture coordinates.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.

### Roughness map

These preprocessor definitions control the use of roughness maps:

- To enable the use of a texture that contains a roughness map for the material, set the value of KANZI_SHADER_USE_ROUGHNESS_TEXTURE to 1.

This way you expose to the material the Roughness Texture property that sets the texture that contains the roughness map.

Kanzi reads the roughness map from the green channel of the texture. You can use the same texture to set the occlusion, roughness, and metallic maps for a material.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Roughness Texture, set the value of KANZI_SHADER_USE_ROUGHNESS_TEXTURE_COORDINATE_INDEX to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.
- To enable the use of a detail texture that contains a roughness map for the material, set the value of KANZI_SHADER_USE_ROUGHNESS_TEXTURE_DETAIL to 1.

This way you expose to the material the Detail Roughness Texture property that sets the detail texture that contains the roughness map.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Detail Roughness Texture, set the value of KANZI_SHADER_USE_ROUGHNESS_TEXTURE_COORDINATE_INDEX_DETAIL to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.

### Occlusion map

These preprocessor definitions control the use of occlusion maps:

- To enable the use of a texture that contains an occlusion map for the material, set the value of KANZI_SHADER_USE_OCCLUSION_TEXTURE to 1.

This way you expose to the material the Occlusion Texture property that sets the texture that contains the occlusion map.

Kanzi reads the occlusion map from the red channel of the texture. You can use the same texture to set the occlusion, roughness, and metallic maps for a material.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Occlusion Texture, set the value of KANZI_SHADER_USE_OCCLUSION_TEXTURE_COORDINATE_INDEX to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.
- To enable the use of a detail texture that contains an occlusion map for the material, set the value of KANZI_SHADER_USE_OCCLUSION_TEXTURE_DETAIL to 1.

This way you expose to the material these properties:

  - Detail Occlusion Texture sets the detail texture that contains the occlusion map.
  - Detail Occlusion Strength sets the intensity of the Detail Occlusion Texture.

- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Detail Occlusion Texture, set the value of KANZI_SHADER_USE_OCCLUSION_TEXTURE_COORDINATE_INDEX_DETAIL to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.

## Specular-glossiness materials

Kanzi supports the `KHR_materials_pbrSpecularGlossiness` glTF extension which enables adjusting materials based on their specular color and glossiness.

To enable adjusting materials based on their specular color and glossiness, set:

- KANZI_SHADER_USE_PBR_SPECULAR_GLOSSINESS to 1
- KANZI_SHADER_USE_PBR_METALLIC_ROUGHNESS to 0

This way you expose to the material these properties:

- Diffuse Color Factor sets the diffuse color of the material.
- Glossiness Factor sets the glossiness of the material on a scale from 0 to 1:

  - For a rough, diffuse surface set the property value to 0.
  - For a smooth, glossy surface set the property value to 1.

- Specular Color Factor sets the specular color of the material.

You can use diffuse color, glossiness, and specular color maps to adjust the appearance of a specular-glossiness material.
### Diffuse color

These preprocessor definitions control the diffuse color:

- To enable the use of a texture that contains the diffuse color for the material, set the value of KANZI_SHADER_USE_DIFFUSE_TEXTURE to 1.

This way you expose to the material the Diffuse Color Texture property that sets the texture that contains the diffuse color. Use the Diffuse Color Factor property to filter the value from the texture.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Diffuse Color Texture, set the value of KANZI_SHADER_USE_DIFFUSE_TEXTURE_COORDINATE_INDEX to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.
- To enable the use of a detail texture that contains the diffuse color for the material, set the value of KANZI_SHADER_USE_DIFFUSE_TEXTURE_DETAIL to 1.

This way you expose to the material these properties:

  - Detail Diffuse Color Texture sets the detail texture that contains the diffuse color for the material.
  - Detail Diffuse Color Factor sets the detail diffuse color for the material, which Kanzi alpha-blends with the diffuse color of the material that is set by the Diffuse Color Factor property.

- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Detail Diffuse Color Texture, set the value of KANZI_SHADER_USE_DIFFUSE_TEXTURE_COORDINATE_INDEX_DETAIL to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.

### Glossiness map

These preprocessor definitions control the glossiness:

- To enable the use of a texture that contains a glossiness map for the material, set the value of KANZI_SHADER_USE_GLOSSINESS_TEXTURE to 1.

This way you expose to the material the Glossiness Texture property that sets the texture that contains the glossiness map.

Kanzi reads the glossiness map from the alpha channel of the texture. Use the Glossiness Factor property to scale the glossiness from the texture.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Glossiness Texture, set the value of KANZI_SHADER_USE_GLOSSINESS_TEXTURE_COORDINATE_INDEX to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.
- To enable the use of a detail texture that contains a glossiness map for the material, set the value of KANZI_SHADER_USE_GLOSSINESS_TEXTURE_DETAIL to 1.

This way you expose to the material the Detail Glossiness Texture property that sets the detail texture that contains the glossiness map. Use the Glossiness Factor and Glossiness Texture properties to scale the glossiness from the texture.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Detail Glossiness Texture, set the value of KANZI_SHADER_USE_GLOSSINESS_TEXTURE_COORDINATE_INDEX_DETAIL to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.

### Specular color

These preprocessor definitions control the specular color:

- To enable the use of a texture that contains the specular color for the material, set the value of KANZI_SHADER_USE_SPECULAR_TEXTURE to 1.

This way you expose to the material the Specular Color Texture property that sets the texture that contains the specular color. Use the Specular Color Factor property to filter the value from the texture.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Specular Color Texture, set the value of KANZI_SHADER_USE_SPECULAR_TEXTURE_COORDINATE_INDEX to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.
- To enable the use of a detail texture that contains the specular color for the material, set the value of KANZI_SHADER_USE_SPECULAR_TEXTURE_DETAIL to 1.

This way you expose to the material these properties:

  - Detail Specular Color Texture sets the detail texture that contains the specular color for the material.
  - Detail Specular Color Factor sets the detail specular color for the material, which Kanzi alpha-blends with the specular color of the material that is set by the Specular Color Factor property.

- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Detail Specular Color Texture, set the value of KANZI_SHADER_USE_SPECULAR_TEXTURE_COORDINATE_INDEX_DETAIL to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.
- To control specular anti-aliasing, set the value of KANZI_SHADER_USE_SPECULAR_ANTI_ALIASING to 1.

This way you expose to the material these properties:

  - Specular Anti-Aliasing Strength sets the strength of the specular anti-aliasing effect to apply to the material, ranging from 0 for no specular anti-aliasing to 1 for full specular anti-aliasing.
  - Specular Anti-Aliasing Threshold sets an upper limit for the amount of specular anti-aliasing effect to apply to the material.

## Clear coat materials

Kanzi supports the `KHR_materials_clearcoat` glTF extension which enables simulating a layer of clear coat on top of a physically-based metallic-roughness material. This is commonly used for vehicle paint.

The PhysicallyBasedClearCoat material type by default supports setting the roughness of the outer clear coat layer for the material.

To enable clear coat for any physically-based metallic-roughness material type, set the value of KANZI_SHADER_USE_CLEARCOAT to 1.

This way you expose to the material these properties:

- Clear Coat Roughness Factor sets the roughness of the clear coat on a scale from 0 to 1:

  - For a smooth, glossy surface set the property value to 0.
  - For a rough, diffuse surface set the property value to 1.

- Clear Coat Strength Factor sets the strength of the clear coat.

You can use normal, roughness, and strength maps to adjust the appearance of a clear coat material.
### Clear coat normal map

These preprocessor definitions control the use of clear coat normal maps:

- To enable the use of a texture that contains a clear coat normal map for the material, set the value of KANZI_SHADER_USE_CLEARCOAT_NORMALMAP_TEXTURE to 1.

This way you expose to the material these properties:

  - Clear Coat Normal Texture sets the texture that contains the clear coat normal map for the material.
  - Clear Coat Normal Scale sets the intensity of the Clear Coat Normal Texture.

- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Clear Coat Normal Texture, set the value of KANZI_SHADER_USE_CLEARCOAT_NORMALMAP_TEXTURE_COORDINATE_INDEX to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.
- To enable the use of a detail texture that contains a clear coat normal map for the material, set the value of KANZI_SHADER_USE_CLEARCOAT_NORMALMAP_TEXTURE_DETAIL to 1.

This way you expose to the material these properties:

  - Detail Clear Coat Normal Texture sets the detail texture that contains the clear coat normal map for the material.
  - Detail Clear Coat Normal Scale sets the intensity of the Detail Clear Coat Normal Texture.

- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Detail Clear Coat Normal Texture, set the value of KANZI_SHADER_USE_CLEARCOAT_NORMALMAP_TEXTURE_COORDINATE_INDEX_DETAIL to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.

### Clear coat roughness map

These preprocessor definitions control the use of clear coat roughness maps:

- To enable the use of a texture that contains a clear coat roughness map for the material, set the value of KANZI_SHADER_USE_CLEARCOAT_ROUGHNESS_TEXTURE to 1.

This way you expose to the material the Clear Coat Roughness Texture property that sets the texture that contains the clear coat roughness map.

Kanzi reads the roughness map from the green channel of the texture.

Use the Clear Coat Roughness Factor property to scale the roughness from the texture.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Clear Coat Roughness Texture, set the value of KANZI_SHADER_USE_CLEARCOAT_ROUGHNESS_TEXTURE_COORDINATE_INDEX to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.
- To enable the use of a detail texture that contains a clear coat roughness map for the material, set the value of KANZI_SHADER_USE_CLEARCOAT_ROUGHNESS_TEXTURE_DETAIL to 1.

This way you expose to the material the Detail Clear Coat Roughness Texture property that sets the detail texture that contains the clear coat roughness map. Use the Clear Coat Roughness Factor and Clear Coat Roughness Texture properties to scale the roughness from the texture.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Detail Clear Coat Roughness Texture, set the value of KANZI_SHADER_USE_CLEARCOAT_ROUGHNESS_TEXTURE_COORDINATE_INDEX_DETAIL to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.

### Clear coat strength map

These preprocessor definitions control the use of clear coat strength maps:

- To enable the use of a texture that contains a clear coat strength map for the material, set the value of KANZI_SHADER_USE_CLEARCOAT_STRENGTH_TEXTURE to 1.

This way you expose to the material the Clear Coat Strength Texture property that sets the texture that contains the clear coat strength map.

Kanzi reads the strength map from the red channel of the texture.

Use the Clear Coat Strength Factor property to scale the strength from the texture.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Clear Coat Strength Texture, set the value of KANZI_SHADER_USE_CLEARCOAT_STRENGTH_TEXTURE_COORDINATE_INDEX to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.
- To enable the use of a detail texture that contains a clear coat strength map for the material, set the value of KANZI_SHADER_USE_CLEARCOAT_STRENGTH_TEXTURE_DETAIL to 1.

This way you expose to the material the Detail Clear Coat Strength Texture property that sets the detail texture that contains the clear coat strength map. Use the Clear Coat Strength Factor and Clear Coat Strength Texture properties to scale the strength from the texture.
- To enable selecting between texture coordinates `kzTextureCoordinate0` and `kzTextureCoordinate1` for the Detail Clear Coat Strength Texture, set the value of KANZI_SHADER_USE_CLEARCOAT_STRENGTH_TEXTURE_COORDINATE_INDEX_DETAIL to the semantic index of the texture coordinate that you want to use.

For example, to use the texture coordinate whose semantic index is 1, set the value to 1.

## BRDF lookup table

The Bidirectional Reflectance Distribution Function (BRDF) lookup table is a texture that contains precomputed information about how light reflects off a material.

To enable the use of a BRDF lookup table, set the value of KANZI_SHADER_USE_BRDF_LOOKUP_TABLE to 1.

This way you expose to the material the BRDF Lookup Table property that you can use to set the texture that contains the BRDF lookup table.
## Planar reflections

To enable the material to receive planar reflections, set the value of KANZI_SHADER_RECEIVE_PLANAR_REFLECTION to 1.

You can enable either planar reflections or Image-based lighting for a material type, not both.
## Image-based lighting

Image-based lighting uses cubemap textures to simulate lighting coming from the environment. See Using image-based lighting cubemap textures.

To enable image-based lighting, set the value of KANZI_SHADER_USE_LIGHT_IMAGE_BASED to 1.

This way you expose to the material these properties for controlling the environment light:

- Environment Ambient Texture sets the cubemap texture to use for diffuse lighting.
- Environment Ambient Factor sets the strength of the Environment Ambient Texture.
- Environment Reflection Texture sets the cubemap texture to use for specular or reflective lighting.
- Environment Reflection Factor sets the strength of the Environment Reflection Texture.

To configure which mipmap level of the Environment Reflection Texture maps to full roughness, you can set the value of KANZI_SHADER_ROUGHNESS_ONE_LOD_OFFSET preprocessor define. The value of the preprocessor define is the number of mipmap levels from the last mipmap level. The default value is 3.

Note that the Environment Reflection Texture must be generated with compatible roughness mapping. If you use an external tool to generate the cubemap, ensure that the full roughness is mapped to the correct mipmap level.

You can enable either image-based lighting or Planar reflections for a material type, not both.
## Shadows

To enable the material to receive shadows from different types of light nodes, set the value of these preprocessor definitions to 1:

- KANZI_SHADER_RECEIVE_DIRECTIONAL_SHADOW enables the material to receive directional light shadows.
- KANZI_SHADER_RECEIVE_POINT_SHADOW enables the material to receive point light shadows.
- KANZI_SHADER_RECEIVE_SPOT_SHADOW enables the material to receive spot light shadows.

## Skinning

The PhysicallyBasedSkinned material type supports skinning of meshes with up to 64 bones by default.

To set the number of bones in a mesh for skinning, use KANZI_SHADER_SKINNING_BONE_COUNT.
## Morphing

The PhysicallyBasedMorph material type supports morphing with 3 targets by default.

To set the number of morph targets for morphing, use KANZI_SHADER_MORPH_TARGET_COUNT.
## Debug output

To enable debug output, set the value of KANZI_SHADER_DEBUG_OUTPUT to 1.
