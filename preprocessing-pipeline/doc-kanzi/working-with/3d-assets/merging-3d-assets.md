---
title: Merging 3D assets
source: https://docs.kanzi.com/4.1.0/en/working-with/3d-assets/merging-3d-assets.html
---

# Merging 3D assets

Merging 3D assets allows you to bring to your project all or only selected items from an asset file. It is very useful when you change the 3D assets outside of Kanzi Studio and want to take the changes into use in your project. Additionally, merging allows you to update only specific properties. For example, if you plan to edit object transformations in Kanzi Studio, you can discard the transformation properties when merging assets with your project.

When you want to bring the 3D assets created with a third-party tool to Kanzi Studio you have to import or merge the assets. You can import or merge 3D assets in these formats:

- glTF 2.0 (gltf, glb) for meshes, animations, skins, and morphs
- COLLADA (dae) for meshes, animations, skins, and morphs
- Filmbox (fbx) for meshes, animations, skins, morphs, and splines
- Geometry definitions (obj) for meshes

Different exporters in third-party tools handle content differently. For example, if you cannot get the expected result using the fbx format, try using the dae format.

In Kanzi Studio you can also merge entire projects. See Merging projects.

If you want to import the assets that you created with third-party tools, use Kanzi Studio importing tools. See Importing.
## Merging 3D assets in a Kanzi Studio project

To merge 3D assets in a Kanzi Studio project:

1.

Select File > Import > Merge 3D Asset File, select the file you want to merge (source) to the currently open project (target), and click Open. Asset Merge window opens.
2.

In the Asset Merge window set:

  - Select referenced items. Select the checkbox when you want Kanzi Studio to automatically select all items to which the selected item refers.

For example, when you check the Select referenced items checkbox and select a mesh that has a material, Kanzi Studio studio automatically selects the material, material type, and shaders used by the mesh you selected.
  - **Transformations**. If Kanzi Studio encounters a conflict in object transformations when an object in the target is replaced with an object from the source, set Keep transformations from to:

    - Target Project: <ProjectName> to keep the object transformations you use in the target. Kanzi Studio remembers all transformation changes you made to the objects in Kanzi Studio.
    - Source Project: <ProjectName> to import the object transformations you use in the source.

  - **Materials**. If Kanzi Studio encounters a conflict in object materials when an object in the target is replaced with an object from the source, set Keep materials from to:

    - Target Project: <ProjectName> to keep the materials you use for the objects in the target. Kanzi Studio remembers all material changes you made to the objects in Kanzi Studio.
    - Source Project: <ProjectName> to import the materials you use for the objects in the source.

3.

Select the checkboxes next to the items you want to merge from the source to target. Depending on the existence of the selected item in the target project, the name of the item is written using:

  - **White** font. Items exist in the source, but not in the target. When you select such items, Kanzi Studio creates them in the target.
  - **Red** font. Items exist in both the source and target, but differ between the two.

Before you can continue with the merging, you have to resolve conflicts by choosing to use either the item in the target or the source.
  - **Purple** font. Items exist in the target, but not in the source. When you select such items, Kanzi Studio removes them from the target.

4.

Resolve conflicts. When your target and source both contain the same item and properties of this item differ, you have to decide which properties you want to keep:

  - Click Resolve to source to use the values in the source to resolve all conflicts.
  - Click Resolve to target to use the values in the target to resolve all conflicts.
  - Click Use base project to select a base project for resolving conflicts between the target and the source. For example, Use base project is useful when you are merging two projects or assets that are modifications of an initial project.

When using three-way merge, this is how conflict resolution works in Kanzi Studio:

    - If the difference is only between the base project and the target, Kanzi Studio uses the change in the target.
    - If the difference is only between the base project and the source, Kanzi Studio uses the change in the source.
    - If the change is between both the base project and the target, and the source and the target, you have to resolve the conflict.

  - To resolve conflicts manually, select the item in the source tree and in the conflicts pane select for each property whether you want to keep the value used in the target or the source.

Once you have resolved all the conflicts, the font color of the item name in the source tree changes to green.
5.

Click Merge.

Kanzi Studio merges the source with the target by placing the content of source into the corresponding places of the target.
