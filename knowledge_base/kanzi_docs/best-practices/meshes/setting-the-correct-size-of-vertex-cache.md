---
title: Setting the correct size of vertex cache
source: https://docs.kanzi.com/4.1.0/en/best-practices/meshes/setting-the-correct-size-of-vertex-cache.html
---

# Setting the correct size of vertex cache


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
