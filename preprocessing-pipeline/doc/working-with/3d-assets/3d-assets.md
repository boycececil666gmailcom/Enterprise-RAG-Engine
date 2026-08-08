---
title: 3D assets
source: https://docs.kanzi.com/4.1.0/en/working-with/3d-assets/3d-assets.html
---

# 3D assets

Kanzi Studio is a tool for composing 3D content and 3D user interfaces to be presented with Kanzi. While you can create in Kanzi Studio placeholder 3D meshes such as spheres, cubes, and planes, you have to import 3D assets for your Kanzi applications from third-party tools.

Kanzi Studio is tested, but not limited to use imported data from:

- Autodesk 3ds max 2010-2011, 3ds max 2012 using OpenCollada exporter
- Autodesk Maya 2010-2011
- Autodesk Softimage 2009-2012, Crosswalk exporter preferred
- Blender
- Modo

When you want to bring the 3D assets created with a third-party tool to Kanzi Studio you have to import or merge the assets. You can import or merge 3D assets in these formats:

- glTF 2.0 (gltf, glb) for meshes, animations, skins, and morphs
- COLLADA (dae) for meshes, animations, skins, and morphs
- Filmbox (fbx) for meshes, animations, skins, morphs, and splines
- Geometry definitions (obj) for meshes

Different exporters in third-party tools handle content differently. For example, if you cannot get the expected result using the fbx format, try using the dae format.

To create 3D assets in third-party tools and export them so that they require the minimum amount of effort after importing to Kanzi Studio, see Preparing 3D assets in third-party tools.

These file formats can contain 3D scene information with mesh, animation, and spline data. To bring your 3D assets to your Kanzi Studio project you can:

- Import 3D Assets.

When you import 3D assets, Kanzi Studio creates for each 3D asset:

  - In the Prefabs, a Scene prefab for each scene in the imported file.

Kanzi Studio names each Scene prefab after the imported file. When you import a glTF file that contains multiple scenes, Kanzi Studio appends to the name of each Scene prefab the name of the scene.

In each Scene prefab, Kanzi Studio creates the scene hierarchy from the imported file and places the assets from the imported file into that prefab.
  - In the Library, Kanzi Studio places all resources from the imported file, such as Meshes, Splines, Animations, and Materials.

See Importing 3D assets.
- Merge 3D Asset File.

Merging 3D assets allows you to bring to your project all or only selected items from an asset file. It is very useful when you change the 3D assets outside of Kanzi Studio and want to take the changes into use in your project. Additionally, merging allows you to update only specific properties. For example, if you plan to edit object transformations in Kanzi Studio, you can discard the transformation properties when merging assets with your project.

See Merging 3D assets.
