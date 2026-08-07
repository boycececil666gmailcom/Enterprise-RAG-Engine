---
title: Optimizing meshes
source: https://docs.kanzi.com/4.1.0/en/working-with/meshes/editing-meshes.html
---

# Optimizing meshes

You can improve the performance of your Kanzi application by reducing the amount of vertex data in the meshes the application shows. When you reduce the amount of mesh vertex data, the size of the kzb file and the amount of GPU memory required at runtime decrease.
## Editing mesh attributes

You can change vertex data of a mesh using the Mesh Attributes Editor.

For example, you can use the Mesh Attributes Editor to remove the attributes you do not use and select the optimal data type for your needs.

To edit mesh attributes:

1.

In the Library > Meshes right-click the mesh you want to edit and select Open Mesh Attributes Editor.

In the Mesh Attributes Editor the Import table shows the semantic, number of dimensions, and data range of the attributes of the mesh as you imported it to Kanzi Studio
2.

In the Mesh Attributes Editor in the Export table set these attributes to control how Kanzi Studio exports the mesh to the kzb file:

  - Semantic sets the meaning of the attribute. The semantics of the mesh attributes match the semantics of the shader attributes of the material type the mesh uses.

For example, the position, normal, tangent, texture coordinate, or color vector.
**Tip:** To view and edit the semantics of the shader attributes of a material type, in the Library > Materials and Textures > Material Types right-click a material type and select Open Shader Attributes Editor.
- Semantic Index sets the index of the attribute in the material type.
For example, the correct texture coordinate.
The semantic index of each mesh attribute matches the semantic index of the shader attribute with the same semantic.
- Data Type sets the data type Kanzi uses when storing the attribute to the GPU memory and exporting it to the kzb file. See Setting the correct size of vertex cache.
- Dimensions sets the number of dimensions Kanzi uses for the attribute.
Kanzi Studio automatically sets this value when you import a mesh.
- Output Components sets the components to which Kanzi maps the attribute.
Kanzi Studio automatically sets this value when you import a mesh.
- Export sets the attributes Kanzi exports to the kzb file.
Select the checkbox for the attributes you use and clear the checkbox for the attributes you do not use.
Make sure you export all attributes that match the shader attributes of the material types the mesh is using.
In this example the tangent and texture coordinate attributes are not exported because they are not among the shader attributes of the material type the mesh uses.

The status bar at the bottom of the Mesh Attributes Editor shows the size of the mesh vertex data if you export the kzb file with the values you have currently set in the Export table.

## Setting the correct size of vertex cache

GPUs have a vertex cache of a certain size. Accessing mesh vertices from the cache is an order of magnitude faster than accessing vertices from elsewhere in the memory. You can optimize the mesh data for a certain cache size by reordering vertices and indices in the vertex buffer so that the amount of cache hits is optimal.

For example, a 16-byte vertex cache can store Position + Normal + Texcoord (XYZ * 2 + XYZ * 2 + UV * 2), but is too small to store Position + Normal + Texcoord + Color.

To set the correct size of vertex cache for your target hardware:

1.

Find out the vertex cache size of your target hardware.
2.

In Kanzi Studio select Project > Properties and in the Properties in the Binary Export property category set:

  - Optimize Meshes to enabled

When you enable the Optimize Meshes property, Kanzi Studio sets the vertex cache of the exported meshes to use the size you set in the Target Vertex Cache Size property.
  - Target Vertex Cache Size to the cache size in bytes on the target device
  - Default Vertex Attribute Data Type to the data type you want to use for the vertex buffer attributes

The vertex buffer of a mesh contains a set of attributes which Kanzi uses to send data to vertex shaders.

For example, if you set the Default Vertex Attribute Data Type property to Half-float, compared to Float you decrease the mesh data size by half, but also decrease the mesh accuracy.

## Setting the optimal data type for mesh attributes

To optimize your meshes, set for each mesh attribute the data type that occupies the least amount of space while providing enough visual accuracy for your needs. Kanzi uses the data type when storing the attribute to the GPU memory and exporting it to the kzb file. When you use data types that occupy less space, the size of the kzb file and the amount of GPU memory required at runtime decrease. See Data types for mesh attributes.

To set the optimal data type for a mesh attribute:

1.

In the Library > Meshes right-click the mesh you want to edit and select Open Mesh Attributes Editor.
2.

In the Mesh Attributes Editor in the Import table check the values in the Data Range column for the attribute the data type of which you want to set.

Kanzi Studio marks the data ranges of the different dimensions of a mesh attribute with different colors.
3.

In the Mesh Attributes Editor in the Export table use the dropdown in the Data Type column to set the export data type.

When setting the data type, keep in mind:

  - Select the data type that occupies the least amount of space while providing enough visual accuracy for your needs.

You can see in the status bar at the bottom of the Mesh Attributes Editor the size of the mesh vertex data with the data types you set, and visually inspect the accuracy of the rendering in the Preview.
  - Select a data type the range of which covers all the values in the Data Range column. See Data types for mesh attributes.

For example, in most cases when the data range for all components of the attribute is 0 â¦ 1 you can set the Data Type to 16_UNORM, and when the data range is -1 â¦ 1 you can use 16_SNORM.
  - The list of available data types depends on what your target graphics API supports. See Data types for mesh attributes.
  - The normalized 32-bit data types (32_UNORM and 32_SNORM) provide the highest accuracy. Normalized data types provide uniform accuracy across the data range, while the Float and Half-float data types provide higher accuracy for values close to zero, and lower accuracy for large values.
  - This table lists recommendations for choosing the export data type for different mesh attributes.
|

Semantic |

Recommended data type |

Kanzi Engine normalizes before export |
|

Position |

Based on data range |   |
|

Normal, Tangent, Bitangent |

2_10_10_10_SNORM_PACK32 |

x |
|

Texture coordinate |

Based on data range, 16_UNORM / 16_SNORM / Float |   |
|

Color |

Based on data range, 8_UNORM / Half-float / Float |   |
|

Weight |

Based on data range |   |
|

Matrix palette  |

Based on data range |   |

## Data types for mesh attributes

This table lists the mesh attribute data types that Kanzi supports.
|

Data type |

Description |

Range |
|

Float |

Single-precision floating-point (32 bits) |   |
|

Half-float |

Half-precision floating-point (16 bits) |   |
|

8_SNORM |

8-bit signed normalized |

-1.0f â¦ 1.0f |
|

8_UNORM |

8-bit unsigned normalized |

0.0f â¦ 1.0f |
|

16_SNORM |

16-bit signed normalized |

-1.0f â¦ 1.0f |
|

16_UNORM |

16-bit unsigned normalized |

0.0f â¦ 1.0f |
|

8_SINT |

8-bit signed integer |

-128 â¦ 127 |
|

8_UINT |

8-bit unsigned integer |

0 â¦ 255 |
|

16_SINT |

16-bit signed integer |

-32 768 â¦ 32 767 |
|

16_UINT |

16-bit unsigned integer |

0 â¦ 65,535 |
|

32_SINT |

32-bit signed integer |

-2 147 483 648 â¦ 2 147 483 647 |
|

32_UINT |

32-bit unsigned integer |

0 â¦ 4 294 967 295 |
|

32_SNORM |

32-bit signed normalized |

-1.0f â¦ 1.0f |
|

32_UNORM |

32-bit unsigned normalized |

0.0f â¦ 1.0f |
|

2_10_10_10_SNORM_PACK32 |

Four-component 32-bit packed signed normalized with:

- 10-bit X component in bits 0..9
- 10-bit Y component in bits 10..19
- 10-bit Z component in bits 20..29
- 2-bit W component in bits 30..31
  |

(-1, -1, -1, -1) â¦ (1, 1, 1, 1) |
|

2_10_10_10_UNORM_PACK32 |

Four-component 32-bit packed unsigned normalized with:

- 10-bit X component in bits 0..9
- 10-bit Y component in bits 10..19
- 10-bit Z component in bits 20..29
- 2-bit W component in bits 30..31
  |

(0, 0, 0, 0) â¦ (1, 1, 1, 1) |
