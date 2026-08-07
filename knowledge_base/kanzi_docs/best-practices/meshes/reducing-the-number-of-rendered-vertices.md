---
title: Reducing the number of rendered vertices
source: https://docs.kanzi.com/4.1.0/en/best-practices/meshes/reducing-the-number-of-rendered-vertices.html
---

# Reducing the number of rendered vertices

Meshes contain vertices inside their vertex buffers and each vertex of a rendered mesh is evaluated by a vertex shader. Polygons are filled between the points marked by vertices. This means that the more meshes, and therefore vertices on the screen, the slower the application is.

To improve the performance of meshes in your application:

- Make sure there are no extra meshes, vertices, or polygons.
- Remove the vertex attributes from meshes that are not used by shaders. The smaller the vertex size, the more efficient is the access to the vertex data, and the lower is memory consumption. You can remove unnecessary vertex attributes in most 3D modeling software during export. The export settings usually include a list of vertex attributes that are exported, such as normals, vertex colors and so on. For example, if a mesh is rendered without a textured material, the texture coordinates vertex attribute is unnecessary, and you can remove it.
- Decrease the number of vertices in the meshes you use in your application.
- Use textures instead of vertices to model the details.
