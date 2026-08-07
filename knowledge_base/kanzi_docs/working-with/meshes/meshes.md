---
title: Using meshes
source: https://docs.kanzi.com/4.1.0/en/working-with/meshes/meshes.html
---

# Using meshes


A mesh is a collection of vertices, edges, and faces that define the shape of a solid object in 3D with flat faces and straight edges and the triangles that form the surface between the points.

A mesh can have many clusters of triangles that each have their own materials.
## Using primitive meshes


In Kanzi Studio, you can create primitive meshes. Kanzi creates primitive meshes from a set of parameters, while it stores imported meshes in vertex buffers. The main purpose of these primitives is to use them for prototyping. A primitive mesh always has only one cluster and thus only one material.

These primitive meshes are available in Kanzi Studio:

- Box is a cube mesh centered in its origin.
- Plane is a filled planar mesh with four vertices centered in the origin.
- Sphere is a sphere mesh centered in the origin.


Using the Kanzi Engine API, you can create also cone meshes. In the Kanzi Engine C++ API reference, see `generateCone`.
### Setting the tessellation type of a sphere mesh


These sphere tessellation types are available in Kanzi:

- UV Sphere consists of fans of triangles at the poles and quad faces elsewhere. This is the default sphere type in Kanzi.
- Icosphere is a polyhedral sphere that consists of triangles. An icosphere is uniform in every direction.
- Quad Sphere is a subdivided box consisting of quads projected to a sphere.


To set the tessellation type of a sphere mesh, select the Sphere node and in the Properties set the value of the Sphere Type property.

> **Tip:** To see the geometry of a mesh, in the Preview:
>
> 1.
>
> Click  to enter the Analyze mode.
> 2.
>
> Right-click  and select Wireframe.
>
### Setting the tessellation level of a primitive mesh


Tessellation divides the vertex sets, which present objects, into triangles or quads. Tessellation enables you to add or subtract detail in a mesh depending on factors such as the distance between the mesh and the camera. For example, you can use a lower tessellation level for a mesh that is farther away.

Use the Subdivisions property to set the tessellation level of a primitive mesh. When you increase the value of the Subdivisions property, the amount of geometry in the mesh grows quadratically.

These images show the results of rendering a Sphere node of type UV Sphere with different values of the Subdivisions property. The default value is 6.

These images show a Plane node, which uses the VertexPhongMaterial material and is lit by red and blue spot lights, with different values of the Subdivisions property. Each subdivision increases the number of tiles in the plane quadratically: \(tiles = (subdivisions + 1)^2\).
|

0 subdivisions, 1 tile: |

10 subdivisions, 121 tiles: |

100 subdivisions, 10201 tiles: |
|   |    |    |
### Rendering a normal map texture on a primitive mesh


To use a material with a normal map texture on a primitive mesh, select the primitive mesh node and in the Properties enable the Generate Tangents property.
## Using imported meshes


You can import to Kanzi Studio meshes that you created with third-party tools.

Use the Model node to show the imported meshes in your Kanzi application.

See Importing 3D assets.

After you import meshes to your Kanzi Studio project, Kanzi Studio stores those meshes in the Library > Meshes. Kanzi Studio shows in the Library > Resource Files > 3D Assets the file that contains the meshes. See 3D assets.

Kanzi loads the mesh data to memory only when it needs the mesh. When you change the loaded data, Kanzi saves the changes that you made to the mesh.

In Kanzi Studio you can see the mesh data only for the meshes that you imported. The parameters of the primitive meshes are specified in the properties of each mesh.

Kanzi supports 32-bit indices in meshes.
## Attribute mappings


Attribute mappings is a mesh property that specifies how the attributes in the mesh vertex buffer are handled when rendering the geometry. Attribute mappings map the shader attributes to vertex buffer attributes. Attributes are usually automatically deduced using the semantic of vertex attribute. For example, position attributes of a vertex buffer are mapped to position attribute of the used shader. See Shader attributes.

When using more than one texture on a single mesh, you have to manually set which texture coordinate attribute in the vertex buffer maps to which shader attribute.
## Mesh property types


For a list of the available property types for meshes, see Mesh.
## Primitive mesh property types and messages


For lists of the available property types and messages for the primitive mesh nodes, see:

- Box
- Plane
- Sphere
