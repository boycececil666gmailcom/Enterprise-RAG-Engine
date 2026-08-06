---
title: Meshes best practices
source: https://docs.kanzi.com/4.1.0/en/best-practices/meshes/meshes-best-practices.html
---

# Meshes best practices


Meshes, along with textures, have a major role in affecting the performance of any 3D application. To improve efficiency of meshes in your Kanzi applications:

- Reduce the amount of vertex data in the meshes. See Optimizing meshes.
- Reduce the number of vertices. See Reducing the number of rendered vertices.
- Access mesh vertices from the cache. See Setting the correct size of vertex cache.
- Optimize the performance of meshes by setting the culling properties. See Setting culling.
- When the pivot point of a mesh is centered to the mesh, you can use the half-float accuracy for the vertex attributes. When you use half-float accuracy for vertex attributes, instead of float, you decrease the mesh data size by half.

See Editing the origin of nodes and setting the data type for vertex attributes.
- When users run your Kanzi application in an environment with a multi-core processor, Kanzi automatically uses multiple CPU cores to load the GPU resources in the kzb files to RAM.

Kanzi enables you to configure how many cores you want your application to use. See Loading resources in parallel.
- Use instancing to render a large number of copies of the same mesh. See Creating meshes with instancing.
