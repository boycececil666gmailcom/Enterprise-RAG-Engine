---
title: Kanzi Studio command reference
source: https://docs.kanzi.com/4.1.0/en/reference/command-reference.html
---

# Kanzi Studio command reference


Here you can find the reference for the Kanzi Studio commands that you can execute by running a script from the command line interface. See Automating Kanzi Studio tasks.
## Basic Editing

### AddToResourceDictionary


Add to resources dictionary
#### Syntax


`AddToResourceDictionary resourceId resource resourceDictionaryHost`
#### Parameters

|

`resourceId` |

The resource ID. |
|

`resource` |

The resource that you add to a resource dictionary. |
|

`resourceDictionaryHost` |

The node to whose resource dictionary you add the resource. |
#### Examples


```
# Add the My Mesh mesh to the resource dictionary of the Screen node
# and set the resource ID of My Mesh to My Mesh ID.
AddToResourceDictionary "My Mesh ID" "/Mesh Data/My Mesh" "/Screens/Screen/RootNode/Viewport 2D/Scene"

```

### CreateBindingItem


Create a binding.
#### Syntax


`CreateBindingItem parent bindingMode pushTarget targetPropertyTypeName attribute code`
#### Parameters

|

`parent` |

The node or render pass to which you add the binding. |
|

`bindingMode` |

The binding mode. For a one-way binding use ONE_WAY. For a to-source binding use TO_SOURCE. |
|

`pushTarget` |

The target in a to-source binding. For a one-way binding use NULL. |
|

`targetPropertyTypeName` |

The property that you bind. |
|

`attribute` |

The property field that you bind. To bind the entire property, use WHOLE_PROPERTY. |
|

`code` |

The binding expression. |
#### Examples


```
# Add to the My Button node a binding that sets the Layout Width of that node
# to 300 pixels less than the width of its parent node, but always between
# 400 and 1200 pixels.
# To improve readability, this example splits the binding expression into two lines.
# Enclose between triple backticks a binding expression that spans multiple lines.
CreateBindingItem "/Screens/Screen/RootNode/My Button" ONE_WAY NULL Node.Width WHOLE_PROPERTY ```parentWidth = {@../Node.ActualWidth}
clamp(400, 1200, parentWidth - 300)```

```

### ExposePrefabProperty


Expose a property to the root of a prefab. This enables you to customize the property in each instance of the prefab.

When you expose a property, Kanzi Studio:

1.

Creates from the property a custom property.
2.

Adds the custom property to the prefab and shows the custom property as a frequently used property in each instance of the prefab.
3.

Creates in this item the ##Template binding to the custom property in the prefab root.

#### Syntax


`ExposePrefabProperty source propertyType`
#### Parameters

|

`source` |

The prefab item whose property you expose. |
|

`propertyType` |

The property that you expose. |
#### Examples


```
# In the Prefabs create a Button 2D prefab named My Button.
CreateButton2D "/Prefabs" "My Button" true
# In the My Button prefab create an Image node named Image.
CreateImage2D "/Prefabs/My Button/My Button" Image true
# In the Image node expose the Image2D.Image property to the root of the My Button prefab.
# Let Kanzi Studio automatically generate a name for the exposed custom property.
ExposePrefabProperty "/Prefabs/My Button/My Button/Image" Image2D.Image

```

#### Syntax


`ExposePrefabProperty source propertyType propertyName`
#### Parameters

|

`source` |

The prefab item whose property you expose. |
|

`propertyType` |

The property that you expose. |
|

`propertyName` |

The name for the exposed custom property. |
#### Examples


```
# In the Prefabs create a Button 2D prefab named My Button.
CreateButton2D "/Prefabs" "My Button" true
# In the My Button prefab create an Image node named Image.
CreateImage2D "/Prefabs/My Button/My Button" Image true
# In the Image node expose the Image2D.Image property to the root of the My Button prefab
# and name the exposed custom property MyButton.Icon.
ExposePrefabProperty "/Prefabs/My Button/My Button/Image" Image2D.Image MyButton.Icon

```

## Advanced Editing

### AddProperty


Add a property to an item.
#### Syntax


`AddProperty propertyCollection propertyName valueAsString`
#### Parameters

|

`propertyCollection` |

The node or resource to which you add the property. |
|

`propertyName` |

The property that you add. |
|

`valueAsString` |

(Optional) The value of the property. |
#### Examples


```
# In the RootNode node add the Description property.
AddProperty "/Screens/Screen/RootNode" Description

```


```
# In the RootNode > Button 2D node add the Background Brush property and set it to the DefaultBackground brush.
AddProperty "/Screens/Screen/RootNode/Button 2D" Node2D.BackgroundBrush "/Brushes/DefaultBackground"

```

### AddPropertyNamespaceToPropertyTypes


Move all property types to the current project property namespace.
#### Syntax


`AddPropertyNamespaceToPropertyTypes`
#### Examples


```
# Add the project property namespace to all property types in the project.
AddPropertyNamespaceToPropertyTypes

```

### BakeTransformation


Transform vertices in the vertex buffer of the model according to the current transformation of the node and set the transformation to an identity transformation.
#### Syntax


`BakeTransformation node`
#### Parameters

|

`node` |

The node whose transformation you want to bake to vertex data. |
#### Examples


```
# Bake the Layout Transformation of the RootNode > Viewport 2D > Scene > Model node
# into the vertex data of the mesh that the node uses.
BakeTransformation "/Screens/Screen/RootNode/Viewport 2D/Scene/Model"

```

### CenterMesh


Centers the vertices of the mesh so that the center of the bounding box moves to origo.
#### Syntax


`CenterMesh meshes`
#### Parameters

|

`meshes` |

The mesh data resource whose vertices you want to center. |
#### Examples


```
# Center the vertices of the CarBody mesh so that the center of the bounding box moves to origo.
CenterMesh "/Mesh Data/My Mesh"

```

### FlipMesh


Invert the direction of polygons and normals in the mesh data.
#### Syntax


`FlipMesh meshes flipPolygons flipNormals flipTextureCoordinateU flipTextureCoordinateV`
#### Parameters

|

`meshes` |

The meshes in the mesh data of which you invert the direction of polygons, normals, and texture coordinates. Separate a list of meshes with semicolons. |
|

`flipPolygons` |

Whether to invert the direction of polygons in the mesh data without modifying normals. |
|

`flipNormals` |

Whether to invert the direction of normals in the mesh data. |
|

`flipTextureCoordinateU` |

Whether to invert the direction of the U coordinates of textures. |
|

`flipTextureCoordinateV` |

Whether to invert the direction of the V coordinates of textures. |
#### Examples


```
# In the MyMesh mesh invert the direction of polygons and normals.
FlipMesh "/Mesh Data/My Mesh" true true false false

```


```
# In the MyMesh mesh invert the direction of the U coordinates of textures.
FlipMesh "/Mesh Data/My Mesh" false false true false

```

### GenerateNormals


Generate normals to the vertex buffer of the mesh.
#### Syntax


`GenerateNormals meshes smoothingAngle`
#### Parameters

|

`meshes` |

The meshes to the vertex buffers of which you generate normals. Separate a list of meshes with semicolons. |
|

`smoothingAngle` |

The smoothing angle in degrees. |
#### Examples


```
# Generate normals to the vertex buffer of the My Mesh mesh with a smoothing angle of 60 degrees.
GenerateNormals "/Mesh Data/My Mesh" 60

```

### GenerateTangents


Generate tangents to the vertex buffer of the mesh.
#### Syntax


`GenerateTangents meshes mode`
#### Parameters

|

`meshes` |

The meshes to the vertex buffers of which you generate tangents. Separate a list of meshes with semicolons. |
|

`mode` |

Tangent generation mode: AUTOMATIC, MIKKTSPACE, or LEGACY. |
#### Examples


```
# Generate tangents to the vertex buffer of the My Mesh mesh using the MikkTSpace tangent space algorithm.
GenerateTangents "/Mesh Data/My Mesh" MIKKTSPACE

```

#### Syntax


`GenerateTangents meshes`
#### Parameters

|

`meshes` |

The meshes to the vertex buffers of which you generate tangents. Separate a list of meshes with semicolons. |
#### Examples


```
# Generate tangents to the vertex buffer of the My Mesh mesh. Let Kanzi choose the tangent generation method based on the material.
GenerateTangents "/Mesh Data/My Mesh"

```

### OptimizeAnimations


Remove all Animations Data resource without data and optimizes existing Animation Data items.
#### Syntax


`OptimizeAnimations animations threshold`
#### Parameters

|

`animations` |

The Animation Data resources from which you remove redundant keyframes. Separate a list of animations with semicolons. |
|

`threshold` |

The threshold value for keyframe removal. When deleting a keyframe changes the animated value by less than the value that you set with this parameter, Kanzi Studio removes the keyframe. |
#### Examples


```
# Remove from the Animation Data resources Animation1 and Animation2
# all keyframes with a delta value smaller than 0.1.
OptimizeAnimations "/Animation Data/Animation1; /Animation Data/Animation2" 0.1

```

### PrintDiagnosticReport


Print to the log the invalid project items and their error messages.
#### Syntax


`PrintDiagnosticReport`
#### Examples


```
# Print a list of invalid project items in the main project and loaded referenced projects
# to the Log window and %USERPROFILE%\AppData\Local\Temp\KanziStudioLogs\KanziStudio.log file.
PrintDiagnosticReport

```

### RemovePropertyAndBindingFromItem


Remove a property and the associated local bindings from an item.
#### Syntax


`RemovePropertyAndBindingFromItem host propertyName`
#### Parameters

|

`host` |

The item from which you remove the property and the local bindings that use that property. |
|

`propertyName` |

The property that you remove. |
#### Examples


```
# In the RootNode node add a To Source binding that targets the Viewport 2D node.
CreateBindingItem "/Screens/Screen/RootNode" TO_SOURCE "/Screens/Screen/RootNode/Viewport 2D" Node2D.BackgroundBrush WHOLE_PROPERTY ```{@./Node2D.BackgroundBrush}```
# Remove both the property and the To Source binding.
RemovePropertyAndBindingFromItem "/Screens/Screen/RootNode" Node2D.BackgroundBrush

```

### RemovePropertyFromItem


Remove a property from an item.
#### Syntax


`RemovePropertyFromItem host propertyName`
#### Parameters

|

`host` |

The item from which you remove the property. |
|

`propertyName` |

The property that you remove. |
#### Examples


```
# In the RootNode node remove the Background Brush property.
RemovePropertyFromItem "/Screens/Screen/RootNode" Node2D.BackgroundBrush

```


```
# In the Library > Rendering > Render Pass Prefabs > Render to Texture Pass prefab root remove the Composition Target property.
RemovePropertyFromItem "/Render Pass Prefabs/Render to Texture Pass/Render to Texture Pass" CompositionTargetRenderPass.CompositionTarget

```

### RenameShaderFiles


Renames all the shader files to corresponding material type name.
#### Syntax


`RenameShaderFiles materialTypes`
#### Parameters

|

`materialTypes` |

The material types whose shader files you rename. Separate a list of material types with semicolons. |
#### Examples


```
# Rename the shader files of My Material Type to My Material Type.frag.glsl and My Material Type.vert.glsl.
RenameShaderFiles "/Material Types/My Material Type"

```

### SetProperty


Set a property value.
#### Syntax


`SetProperty parent propertyName propertyValueAsString`
#### Parameters

|

`parent` |

The node or resource whose property you want to set. |
|

`propertyName` |

The name of the property. |
|

`propertyValueAsString` |

The value to which you want to set the property. |
#### Examples


```
# In the Screen node set the Metrics Type property to Absolute.
SetProperty "/Screens/Screen" Window.MetricsType Absolute
# In the Screen node set the Width property to 1200.
SetProperty "/Screens/Screen" WindowAbsoluteWidth 1200
# In the Screen node set the Height property to 720.
SetProperty "/Screens/Screen" WindowAbsoluteHeight 720

```


```
# In the RootNode node set the Background Brush property to the Color Brush brush.
SetProperty "/Screens/Screen/RootNode" Node2D.BackgroundBrush "/Brushes/Color Brush"

```


```
# In the Prefabs > My Stack Layout prefab set the Direction property to Y.
SetProperty "/Prefabs/My Stack Layout/My Stack Layout" StackLayoutConcept.Direction 1

```


```
# In the RootNode > My Button node add the Double-Click Enabled property and set it to enabled.
AddProperty "/Screens/Screen/RootNode/My Button" ClickConcept.DoubleClickEnabled true

```


```
# In the RootNode node add the Description property and set it to "This is the main page of the application.".
AddProperty "/Screens/Screen/RootNode" Description "This is the main page of the application."

```


```
# In the My Text Block node, set the Text property to
# SERVICE
# VEHICLE
# SOON
#
# Enclose between triple backticks a property value that spans multiple lines.
SetProperty "/Screens/Screen/RootNode/My Text Block" TextConcept.Text ```SERVICE
VEHICLE
SOON```
# In the My Text Block node, add the Text Horizontal Alignment property and set it to Center.
AddProperty "/Screens/Screen/RootNode/My Text Block" TextConcept.TextHorizontalAlignment 2

```

## Destroyer

### DeleteAnimationsWithLessThanTwoEffectiveKeyframes


Delete all Animation Data items with one or no effective keyframes. Repeated keyframes with the same value are regarded as ineffective.
#### Syntax


`DeleteAnimationsWithLessThanTwoEffectiveKeyframes animations`
#### Parameters

|

`animations` |

The animations you want to delete if they have one or no effective keyframes. Separate a list of animations with semicolons. |
#### Examples


```
# Delete the Animation1, Animation2, and Animation3 Animation Data items if they have less than two effective keyframes.
DeleteAnimationsWithLessThanTwoEffectiveKeyframes "/Animation Data/Animation1; /Animation Data/Animation2; /Animation Data/Animation3"

```

### DeleteProjectItem


Delete the selected project item(s)
#### Syntax


`DeleteProjectItem items`
#### Parameters

|

`items` |

The nodes and resources you want to delete. Separate a list of items with semicolons. |
#### Examples


```
# Delete the RootNode > Viewport 2D node.
DeleteProjectItem "/Screens/Screen/RootNode/Viewport 2D"

```


```
# Delete the RootNode > Button 2D node and Button 2D prefab.
DeleteProjectItem "/Screens/Screen/RootNode/Button 2D; /Prefabs/Button 2D"

```


```
# Delete the Library > Materials and Textures > Textures > Default Texture texture.
DeleteProjectItem "/Textures/Default Texture"

```


```
# Delete the ColorTextureMaterial material and ColorTexture material type.
DeleteProjectItem "/Materials/ColorTextureMaterial; /Material Types/ColorTexture"

```

## Conversions

### ConvertBindingsToTemplateBindings


Convert to template bindings those bindings whose source is the template root.
#### Syntax


`ConvertBindingsToTemplateBindings targets`
#### Parameters

|

`targets` |

The node the bindings of which you convert to template bindings. |
#### Examples


```
# In the Prefabs > Toggle Button 2D > Stack Layout 2D and its child nodes convert
# to template bindings those bindings whose source is the template root.
ConvertBindingsToTemplateBindings "/Prefabs/Toggle Button 2D/Toggle Button 2D/Stack Layout 2D"

```

### ConvertNode2DPrefabPlaceholderToPrefabView2D


Convert this Prefab Placeholder 2D node to a Prefab View 2D node.

When you instantiate a prefab with a Prefab View node, Kanzi monitors the value of the Prefab Template property and adds the prefab to which that property points as a child node of the Prefab View node. This allows you to change the prefab that the Prefab View instantiates and to keep your application responsive when it is loading resources.
#### Syntax


`ConvertNode2DPrefabPlaceholderToPrefabView2D prefabPlaceholder`
#### Parameters

|

`prefabPlaceholder` |

The Prefab Placeholder 2D node that you convert to a Prefab View 2D node. |
#### Examples


```
# Convert the RootNode > Toggle Button 2D Prefab Placeholder 2D node to a Prefab View 2D node.
ConvertNode2DPrefabPlaceholderToPrefabView2D "/Screens/Screen/RootNode/Toggle Button 2D"

```

### ConvertNode3DPrefabPlaceholderToPrefabView3D


Convert this Prefab Placeholder 3D node to a Prefab View 3D node.

When you instantiate a prefab with a Prefab View node, Kanzi monitors the value of the Prefab Template property and adds the prefab to which that property points as a child node of the Prefab View node. This allows you to change the prefab that the Prefab View instantiates and to keep your application responsive when it is loading resources.
#### Syntax


`ConvertNode3DPrefabPlaceholderToPrefabView3D prefabPlaceholder`
#### Parameters

|

`prefabPlaceholder` |

The Prefab Placeholder 3D node that you convert to a Prefab View 3D node. |
#### Examples


```
# Convert the RootNode > Viewport 2D > Scene > Toggle Button 3D Prefab Placeholder 3D node to a Prefab View 3D node.
ConvertNode3DPrefabPlaceholderToPrefabView3D "/Screens/Screen/RootNode/Viewport 2D/Scene/Toggle Button 3D"

```

### ConvertNodesToPrefabs


Create prefab templates for the selected nodes and replace the nodes with placeholders pointing to the created templates.
#### Syntax


`ConvertNodesToPrefabs nodes`
#### Parameters

|

`nodes` |

The nodes that you convert to prefabs. Separate a list of nodes with semicolons. |
#### Examples


```
# Convert to prefabs the RootNode > Button 2D and RootNode > Toggle Button 2D nodes.
ConvertNodesToPrefabs "/Screens/Screen/RootNode/Button 2D; /Screens/Screen/RootNode/Toggle Button 2D"

```

### ConvertPageHostToPage


Page Host and Page nodes are deprecated. Use Activity Host and Activity nodes instead.

Convert this Page Host node to a Page node.

Use the Page nodes to create the structure of the user interface in your application, and the Page Host nodes to manage navigation requests and transitions between Page nodes under a Page Host node.
#### Syntax


`ConvertPageHostToPage pageHost`
#### Parameters

|

`pageHost` |

The Page Host node that you convert to a Page node. |
#### Examples


```
# Convert the Page Host node RootNode > Settings to a Page node.
ConvertPageHostToPage "/Screens/Screen/RootNode/Settings"

```

### ConvertPageToPageHost


Page Host and Page nodes are deprecated. Use Activity Host and Activity nodes instead.

Convert this Page node to a Page Host node.

Use the Page Host nodes to manage navigation requests and transitions between Page nodes under a Page Host node.
#### Syntax


`ConvertPageToPageHost page`
#### Parameters

|

`page` |

The Page node that you convert to a Page Host node. |
#### Examples


```
# Convert the Page node RootNode > Car to a Page Host node.
ConvertPageToPageHost "/Screens/Screen/RootNode/Car"

```

### ConvertProjectReferenceItemToKzbReferenceItem


Convert this Project Reference to a Kzb Reference.
#### Syntax


`ConvertProjectReferenceItemToKzbReferenceItem projectReferenceItem`
#### Parameters

|

`projectReferenceItem` |

The project reference you convert to a kzb file reference. |
#### Examples


```
# Convert the Resources project reference to a kzb file reference.
ConvertProjectReferenceItemToKzbReferenceItem "/Project References/Resources/"

```

## Brush Creation

### CreateBrush


Create a brush
#### Syntax


`CreateBrush itemName brushTypeName`
#### Parameters

|

`itemName` |

The name of the brush. |
|

`brushTypeName` |

The type of the brush. |
#### Examples


```
# Create a Color Brush named My Color Brush in the Library > Materials and Textures > Brushes.
CreateBrush "My Color Brush" Kanzi.ColorBrush

```


```
# Create a Content Brush named My Content Brush in the Library > Materials and Textures > Brushes.
CreateBrush "My Content Brush" Kanzi.ContentBrush

```


```
# Create a Material Brush named My Material Brush in the Library > Materials and Textures > Brushes.
CreateBrush "My Material Brush" Kanzi.MaterialBrush

```


```
# Create a Texture Brush named My Texture Brush in the Library > Materials and Textures > Brushes.
CreateBrush "My Texture Brush" Kanzi.TextureBrush

```

## Component Creation

### CreateComponentNode2D


Create a 2D node.
#### Syntax


`CreateComponentNode2D parent itemName componentTypeName`
#### Parameters

|

`parent` |

The node in which you create the 2D node. |
|

`itemName` |

The name of the 2D node. |
|

`componentTypeName` |

The type of the 2D node. |
#### Examples


```
# Create a Content Layout 2D node named My Content Layout in the RootNode node.
CreateComponentNode2D "/Screens/Screen/RootNode" "My Content Layout" Kanzi.ContentLayout2D

```


```
# Create a List Box Item Container 2D prefab named My List Box Item Container in the Prefabs.
CreateComponentNode2D "/Prefabs" "My List Box Item Container" Kanzi.ListBoxItemContainer2D

```


```
# Create a Prefab View 2D node named My Prefab View in the RootNode node.
CreateComponentNode2D "/Screens/Screen/RootNode" "My Prefab View" Kanzi.PrefabView2D

```

### CreateComponentNode


Create a 3D node.
#### Syntax


`CreateComponentNode parent itemName componentTypeName`
#### Parameters

|

`parent` |

The node in which you create the 3D node. |
|

`itemName` |

The name of the 3D node. |
|

`componentTypeName` |

The type of the 3D node. |
#### Examples


```
# Create a Content Layout 3D node named My Content Layout in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Content Layout" Kanzi.ContentLayout3D

```


```
# Create a Dock Layout 3D node named My Dock Layout in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Dock Layout" Kanzi.DockLayout3D

```


```
# Create a Flow Layout 3D node named My Flow Layout in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Flow Layout" Kanzi.FlowLayout3D

```


```
# Create a Grid Layout 3D node named My Grid Layout in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Grid Layout" Kanzi.GridLayout3D

```


```
# Create a Stack Layout 3D node named My Stack Layout in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Stack Layout" Kanzi.StackLayout3D

```


```
# Create a Trajectory Layout 3D node named My Trajectory Layout in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Trajectory Layout" Kanzi.TrajectoryLayout3D

```


```
# Create a Grid List Box 3D node named My Grid List Box in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Grid List Box" Kanzi.GridListBox3D

```


```
# Create a List Box Item Container 3D prefab named My List Box Item Container in the Prefabs.
CreateComponentNode "/Prefabs" "My List Box Item Container" Kanzi.ListBoxItemContainer3D

```


```
# Create a Trajectory List Box 3D node named My Trajectory List Box in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Trajectory List Box" Kanzi.TrajectoryListBox3D

```


```
# Create a Text Block 3D node named My Text Block in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Text Block" Kanzi.TextBlock3D

```


```
# Create a Button 3D node named My Button in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Button" Kanzi.Button3D

```


```
# Create a Button 3D prefab named My Button in the Prefabs.
CreateComponentNode "/Prefabs" "My Button" Kanzi.Button3D

```


```
# Create a Scroll View 3D node named My Scroll View in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Scroll View" Kanzi.ScrollView3D

```


```
# Create a Slider 3D node named My Slider in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Slider 3D" Kanzi.Slider3D

```


```
# Create a Toggle Button 3D node named My Toggle Button in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Toggle Button" Kanzi.ToggleButton3D

```


```
# Create a Toggle Button Group 3D node named My Toggle Button Group in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Toggle Button Group" Kanzi.ToggleButtonGroup3D

```


```
# Create a Prefab View 3D node named My Prefab View in the Screen > RootNode > Viewport 2D > Scene node.
CreateComponentNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Prefab View" Kanzi.PrefabView3D

```

## Empty Node

### CreateEmptyNode2D


Use an Empty Node 2D to group 2D objects and to apply property changes to these objects as a group.
#### Syntax


`CreateEmptyNode2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Empty Node 2D node or prefab. |
|

`name` |

The name of the Empty Node 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Empty Node 2D node or prefab that you created. |
#### Examples


```
# Create an Empty Node 2D node named My Empty Node in the Screen > RootNode node
# and select the My Empty Node node.
CreateEmptyNode2D "/Screens/Screen/RootNode" "My Empty Node" true

```


```
# Create an Empty Node 2D prefab named My Empty Node in the Prefabs
# and select the My Empty Node prefab.
CreateEmptyNode2D "/Prefabs" "My Empty Node" true

```

### CreateEmptyNode3D


Use an Empty Node 3D to group 3D objects and to apply property changes to these objects as a group.
#### Syntax


`CreateEmptyNode3D parent itemName`
#### Parameters

|

`parent` |

The node or prefab in which you create the Empty Node 3D node or prefab. |
|

`itemName` |

The name of the Empty Node 3D node or prefab. |
#### Examples


```
# Create an Empty Node 3D node named My Empty Node 3D in the Screen > RootNode > Viewport 2D > Scene node.
CreateEmptyNode3D "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Empty Node 3D"

```


```
# Create an Empty Node 3D prefab named My Empty Node 3D in the Prefabs.
CreateEmptyNode3D "/Prefabs" "My Empty Node 3D"

```

## Layout Node

### CreateDockLayout2D


Use a Dock Layout 2D to divide objects relative to each other in 2D space.
#### Syntax


`CreateDockLayout2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Dock Layout 2D node or prefab. |
|

`name` |

The name of the Dock Layout 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Dock Layout 2D node or prefab that you created. |
#### Examples


```
# Create a Dock Layout 2D node named My Dock Layout in the Screen > RootNode node
# and select the My Dock Layout node.
CreateDockLayout2D "/Screens/Screen/RootNode" "My Dock Layout" true

```


```
# Create a Dock Layout 2D prefab named My Dock Layout in the Prefabs
# and select the My Dock Layout prefab.
CreateDockLayout2D "/Prefabs" "My Dock Layout" true

```

### CreateFlowLayout2D


Use a Flow Layout 2D to place 2D objects in rows in 2D space. When a row is full, it places objects in a new row.
#### Syntax


`CreateFlowLayout2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Flow Layout 2D node or prefab. |
|

`name` |

The name of the Flow Layout 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Flow Layout 2D node or prefab that you created. |
#### Examples


```
# Create a Flow Layout 2D node named My Flow Layout in the Screen > RootNode node
# and select the My Flow Layout node.
CreateFlowLayout2D "/Screens/Screen/RootNode" "My Flow Layout" true

```


```
# Create a Flow Layout 2D prefab named My Flow Layout in the Prefabs
# and select the My Flow Layout prefab.
CreateFlowLayout2D "/Prefabs" "My Flow Layout" true

```

### CreateGridLayout2D


Use a Grid Layout 2D to arrange 2D content in a grid in 2D space.
#### Syntax


`CreateGridLayout2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Grid Layout 2D node or prefab. |
|

`name` |

The name of the Grid Layout 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Grid Layout 2D node or prefab that you created. |
#### Examples


```
# Create a Grid Layout 2D node named My Grid Layout in the Screen > RootNode node
# and select the My Grid Layout node.
CreateGridLayout2D "/Screens/Screen/RootNode" "My Grid Layout" true

```


```
# Create a Grid Layout 2D prefab named My Grid Layout in the Prefabs
# and select the My Grid Layout prefab.
CreateGridLayout2D "/Prefabs" "My Grid Layout" true

```

### CreateStackLayout2D


Use a Stack Layout 2D to arrange content in a stack on the selected axis in 2D space.
#### Syntax


`CreateStackLayout2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Stack Layout 2D node or prefab. |
|

`name` |

The name of the Stack Layout 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Stack Layout 2D node or prefab that you created. |
#### Examples


```
# Create a Stack Layout 2D node named My Stack Layout in the Screen > RootNode node
# and select the My Stack Layout node.
CreateStackLayout2D "/Screens/Screen/RootNode" "My Stack Layout" true

```


```
# Create a Stack Layout 2D prefab named My Stack Layout in the Prefabs
# and select the My Stack Layout prefab.
CreateStackLayout2D "/Prefabs" "My Stack Layout" true

```

### CreateTrajectoryLayout2D


Use a Trajectory Layout 2D to arrange content along a trajectory path in 2D space.
#### Syntax


`CreateTrajectoryLayout2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Trajectory Layout 2D node or prefab. |
|

`name` |

The name of the Trajectory Layout 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Trajectory Layout 2D node or prefab that you created. |
#### Examples


```
# Create a Trajectory Layout 2D node named My Trajectory Layout in the Screen > RootNode node
# and select the My Trajectory Layout node.
CreateTrajectoryLayout2D "/Screens/Screen/RootNode" "My Trajectory Layout" true

```


```
# Create a Trajectory Layout 2D prefab named My Trajectory Layout in the Prefabs
# and select the My Trajectory Layout prefab.
CreateTrajectoryLayout2D "/Prefabs" "My Trajectory Layout" true

```

## Container Node

### CreateGridListBox2D


Use a Grid List Box 2D to arrange 2D content in a grid in 2D space.
#### Syntax


`CreateGridListBox2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Grid List Box 2D node or prefab. |
|

`name` |

The name of the Grid List Box 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Grid List Box 2D node or prefab that you created. |
#### Examples


```
# Create a Grid List Box 2D node named My Grid List Box in the Screen > RootNode node
# and select the My Grid List Box node.
CreateGridListBox2D "/Screens/Screen/RootNode" "My Grid List Box" true

```


```
# Create a Grid List Box 2D prefab named My Grid List Box in the Prefabs
# and select the My Grid List Box prefab.
CreateGridListBox2D "/Prefabs" "My Grid List Box" true

```

## Content Node

### CreateImage2D


Use an Image to display a single or a render target texture.
#### Syntax


`CreateImage2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Image node or prefab. |
|

`name` |

The name of the Image node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Image node or prefab that you created. |
#### Examples


```
# Create an Image node named My Image in the Screen > RootNode node
# and select the My Image node.
CreateImage2D "/Screens/Screen/RootNode" "My Image" true

```


```
# Create an Image prefab named My Image in the Prefabs
# and select the My Image prefab.
CreateImage2D "/Prefabs" "My Image" true

```

### CreatePage


Page Host and Page nodes are deprecated. Use Activity Host and Activity nodes instead.

Use a Page to add structure to your Kanzi application.
#### Syntax


`CreatePage parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Page node or prefab. |
|

`name` |

The name of the Page node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Page node or prefab that you created. |
#### Examples


```
# Create a Page node named Media Page in the Screen > RootNode node
# and select the Media Page node.
CreatePage "/Screens/Screen/RootNode" "Media Page" true

```


```
# Create a Page prefab named My Page in the Prefabs and select the My Page prefab.
CreatePage "/Prefabs" "My Page" true

```

### CreatePageHost


Page Host and Page nodes are deprecated. Use Activity Host and Activity nodes instead.

Use Page Host to manage the navigation between Page nodes within its subtree.
#### Syntax


`CreatePageHost parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Page Host node or prefab. |
|

`name` |

The name of the Page Host node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Page Host node or prefab that you created. |
#### Examples


```
# Create a Page Host node named Main Page Host in the Screen > RootNode node
# and select the Main Page Host node.
CreatePageHost "/Screens/Screen/RootNode" "Main Page Host" true

```


```
# Create a Page Host prefab named My Page Host in the Prefabs and select the My Page Host prefab.
CreatePageHost "/Prefabs" "My Page Host" true

```

### CreateProgressiveRenderingNode2D


Use a Progressive Rendering Viewport 2D to display a view into a 3D scene through a camera.
#### Syntax


`CreateProgressiveRenderingNode2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Progressive Rendering Viewport 2D node or prefab. |
|

`name` |

The name of the Progressive Rendering Viewport 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Progressive Rendering Viewport 2D node or prefab that you created. |
#### Examples


```
# Create a Progressive Rendering Viewport 2D node named My Progressive Rendering Viewport
# in the Screen > RootNode node and select the Progressive Rendering Viewport node.
CreateProgressiveRenderingNode2D "/Screens/Screen/RootNode" "My Progressive Rendering Viewport" true

```


```
# Create a Progressive Rendering Viewport 2D prefab named My Progressive Rendering Viewport
# in the Prefabs and select the My Progressive Rendering Viewport prefab.
CreateProgressiveRenderingNode2D "/Prefabs" "My Progressive Rendering Viewport" true

```

### CreateTextBlock2D


Use a Text Block 2D to display text in 2D space. It uses fonts to render text and has location and orientation in 2D space.
#### Syntax


`CreateTextBlock2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Text Block 2D node or prefab. |
|

`name` |

The name of the Text Block 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Text Block 2D node or prefab that you created. |
#### Examples


```
# Create a Text Block 2D node named My Text Block in the Screen > RootNode node
# and select the My Text Block node.
CreateTextBlock2D "/Screens/Screen/RootNode" "My Text Block" true

```


```
# Create a Text Block 2D prefab named My Text Block in the Prefabs
# and select the My Text Block prefab.
CreateTextBlock2D "/Prefabs" "My Text Block" true

```

### CreateViewport2D


Use a Viewport 2D to display a view into a 3D scene through a camera.
#### Syntax


`CreateViewport2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Viewport 2D node or prefab. |
|

`name` |

The name of the Viewport 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Viewport 2D node or prefab that you created. |
#### Examples


```
# Create a Viewport 2D node named My Viewport in the Screen > RootNode node
# and select the My Viewport node.
CreateViewport2D "/Screens/Screen/RootNode" "My Viewport" true

```


```
# Create a Viewport 2D prefab named My Viewport in the Prefabs
# and select the My Viewport prefab.
CreateViewport2D "/Prefabs" "My Viewport" true

```

## Interactivity Node

### CreateButton2D


Use a Button 2D to create buttons in 2D space.
#### Syntax


`CreateButton2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Button 2D node or prefab. |
|

`name` |

The name of the Button 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Button 2D node or prefab that you created. |
#### Examples


```
# Create a Button 2D node named My Button in the Screen > RootNode node
# and select the My Button node.
CreateButton2D "/Screens/Screen/RootNode" "My Button" true

```


```
# Create a Button 2D prefab named My Button in the Prefabs
# and select the My Button prefab.
CreateButton2D "/Prefabs" "My Button" true
# In the My Button prefab create an Image node named Image
# but do not select the Image node.
CreateImage2D "/Prefabs/My Button/My Button" Image false

```

### CreateScrollView2D


Use a Scroll View 2D to get user input from scroll gestures in 2D space.
#### Syntax


`CreateScrollView2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Scroll View 2D node or prefab. |
|

`name` |

The name of the Scroll View 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Scroll View 2D node or prefab that you created. |
#### Examples


```
# Create a Scroll View 2D node named My Scroll View in the Screen > RootNode node
# and select the My Scroll View node.
CreateScrollView2D "/Screens/Screen/RootNode" "My Scroll View" true

```


```
# Create a Scroll View 2D prefab named My Scroll View in the Prefabs
# and select the My Scroll View prefab.
CreateScrollView2D "/Prefabs" "My Scroll View" true

```

### CreateSlider2D


Use a Slider 2D to allow users to set a value between a set of minimum and maximum values in 2D space.
#### Syntax


`CreateSlider2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Slider 2D node or prefab. |
|

`name` |

The name of the Slider 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Slider 2D node or prefab that you created. |
#### Examples


```
# Create a Slider 2D node named My Slider in the Screen > RootNode node
# and select the My Slider node.
CreateSlider2D "/Screens/Screen/RootNode" "My Slider" true

```


```
# Create a Slider 2D prefab named My Slider in the Prefabs
# and select the My Slider prefab.
CreateSlider2D "/Prefabs" "My Slider" true

```

### CreateToggleButton2D


Use a Toggle Button 2D to create buttons with multiple toggle states in 2D space.
#### Syntax


`CreateToggleButton2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Toggle Button 2D node or prefab. |
|

`name` |

The name of the Toggle Button 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Toggle Button 2D node or prefab that you created. |
#### Examples


```
# Create a Toggle Button 2D node named My Toggle Button in the Screen > RootNode node
# and select the My Toggle Button node.
CreateToggleButton2D "/Screens/Screen/RootNode" "My Toggle Button" true

```


```
# Create a Toggle Button 2D prefab named My Toggle Button in the Prefabs
# and select the My Toggle Button prefab.
CreateToggleButton2D "/Prefabs" "My Toggle Button" true
# In the My Toggle Button prefab create an Image node named Image
# but do not select the Image node.
CreateImage2D "/Prefabs/My Toggle Button/My Toggle Button" Image false

```

### CreateToggleButtonGroup2D


Use a Toggle Button Group 2D to group toggle buttons in 2D space where only one can be active at a time. Toggle buttons in a group behave like radio buttons.
#### Syntax


`CreateToggleButtonGroup2D parent name selectNewItems`
#### Parameters

|

`parent` |

The node or prefab in which you create the Toggle Button Group 2D node or prefab. |
|

`name` |

The name of the Toggle Button Group 2D node or prefab. |
|

`selectNewItems` |

Whether Kanzi Studio selects the Toggle Button Group 2D node or prefab that you created. |
#### Examples


```
# Create a Toggle Button Group 2D node named My Toggle Button Group in the Screen > RootNode node
# and select the My Toggle Button Group node.
CreateToggleButtonGroup2D "/Screens/Screen/RootNode" "My Toggle Button Group" true

```


```
# Create a Toggle Button Group 2D prefab named My Toggle Button Group in the Prefabs
# and select the My Toggle Button Group prefab.
CreateToggleButtonGroup2D "/Prefabs" "My Toggle Button Group" true

```

## Material Creation

### CreateComputeMaterialType


Compute material types contain a single compute shader stage and are used by Compute Render Passes. By adjusting compute material property values, you control the compute dispatch.
#### Syntax


`CreateComputeMaterialType materialTypeName createMaterial`
#### Parameters

|

`materialTypeName` |

The name of the compute material type. |
|

`createMaterial` |

(Optional) Whether Kanzi Studio also creates a material which uses the compute material type. The default value is false. |
#### Examples


```
# Create a compute material type named My Compute Material Type in the Library > Materials and Textures > Material Types,
# and create a material named My Compute Material Type Material which uses My Compute Material Type.
CreateComputeMaterialType "My Compute Material Type" true

```

### CreateMaterial


Use materials to set the appearance of 3D nodes and Material Brush brushes.
#### Syntax


`CreateMaterial materialName selectNewItem materialType`
#### Parameters

|

`materialName` |

The name of the material. |
|

`selectNewItem` |

Whether Kanzi Studio selects the material. |
|

`materialType` |

The material type that the material uses. |
#### Examples


```
# Create a material named My Material in the Library > Materials and Textures > Materials,
# select the material, and set the material to use the My Material Type material type.
CreateMaterial "My Material" true "/Material Types/My Material Type"

```

### CreateMaterialType


Material types define the property types of materials. By adjusting material property values defined by a material type, you set the appearance of a material.
#### Syntax


`CreateMaterialType materialTypeName createMaterial`
#### Parameters

|

`materialTypeName` |

The name of the material type. |
|

`createMaterial` |

(Optional) Whether Kanzi Studio also creates a material which uses the material Type. The default value is false. |
#### Examples


```
# Create a material type named My Material Type in the Library > Materials and Textures > Material Types,
# and create a material named My Material Type Material which uses My Material Type.
CreateMaterialType "My Material Type" true

```

### MaterialTypeSyncWithUniforms


Synchronize material type shader variable and binding information with the current shader uniforms.
#### Syntax


`MaterialTypeSyncWithUniforms materialType`
#### Parameters

|

`materialType` |

Project-item path to the material type, for example â/Material Types/MyMaterialTypeâ. |
#### Examples


```
runTest: false

```

## Primitive Creation

### CreateBoxNode


Create a cube mesh centered in its origin.
#### Syntax


`CreateBoxNode parent itemName`
#### Parameters

|

`parent` |

The node or prefab in which you create the Box node or prefab. |
|

`itemName` |

The name of the Box node or prefab. |
#### Examples


```
# Create a Box node named My Box in the Screen > RootNode > Viewport 2D > Scene node.
CreateBoxNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Box"

```


```
# Create a Box prefab named My Box in the Prefabs.
CreateBoxNode "/Prefabs" "My Box"

```

### CreateMeshNode


Use a Model to add imported 3D models created in third-party tools to your Kanzi application.
#### Syntax


`CreateMeshNode parent itemName mesh`
#### Parameters

|

`parent` |

The node or prefab in which you create the Model node or prefab. |
|

`itemName` |

The name of the Model node or prefab. |
|

`mesh` |

(Optional) The Mesh that the Model shows. |
#### Examples


```
# Create a Model node named My Model in the Screen > RootNode > Viewport 2D > Scene node
# and set the Mesh property of My Model to the My Mesh mesh.
CreateMeshNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Model" "/Mesh Data/My Mesh"

```


```
# Create a Model prefab named My Model in the Prefabs.
CreateMeshNode "/Prefabs" "My Model"

```

### CreatePlaneNode


Create a filled planar mesh with four vertices.
#### Syntax


`CreatePlaneNode parent itemName`
#### Parameters

|

`parent` |

The node or prefab in which you create the Plane node or prefab. |
|

`itemName` |

The name of the Plane node or prefab. |
#### Examples


```
# Create a Plane node named My Plane in the Screen > RootNode > Viewport 2D > Scene node.
CreatePlaneNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Plane"

```


```
# Create a Plane prefab named My Plane in the Prefabs.
CreatePlaneNode "/Prefabs" "My Plane"

```

### CreateSphereNode


Create a sphere mesh centered in its origin.
#### Syntax


`CreateSphereNode parent itemName`
#### Parameters

|

`parent` |

The node or prefab in which you create the Sphere node or prefab. |
|

`itemName` |

The name of the Sphere node or prefab. |
#### Examples


```
# Create a Sphere node named My Sphere in the Screen > RootNode > Viewport 2D > Scene node.
CreateSphereNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Sphere"

```


```
# Create a Sphere prefab named My Sphere in the Prefabs.
CreateSphereNode "/Prefabs" "My Sphere"

```

## Node 3D Creation

### CreateScene


Use a Scene node to show 3D content in your Kanzi application. A Scene node can contain light nodes, Camera node, and any other 3D node.
#### Syntax


`CreateScene parent itemName createCameraAndLight`
#### Parameters

|

`parent` |

The node or prefab in which you create the Scene node or prefab. |
|

`itemName` |

The name of the Viewport 2D node or prefab. |
|

`createCameraAndLight` |

(Optional) Whether to create in the Scene node a Camera node and a Directional Light. The default value is true. |
#### Examples


```
# Create a Scene node named My Scene in the RootNode > My Viewport node,
# and in the My Scene node create a Camera node and a Directional Light node.
CreateScene "/Screens/Screen/RootNode/My Viewport" "My Scene"

```


```
# Create a Scene prefab named My Scene in the Prefabs.
# Do not create a Camera and a Directional Light node in My Scene prefab.
CreateScene "/Prefabs" "My Scene" false

```

## Helper Node 3D Creation

### CreateCameraNode


Use a Camera node to show the content of a Scene in your Kanzi Studio project and in your Kanzi application.
#### Syntax


`CreateCameraNode parent itemName`
#### Parameters

|

`parent` |

The node in which you create the Camera node. |
|

`itemName` |

The name of the Camera node. |
#### Examples


```
# Create a Camera node named Camera in the Screen > RootNode > Viewport 2D > Scene node.
CreateCameraNode "/Screens/Screen/RootNode/Viewport 2D/Scene" Camera

```

#### Syntax


`CreateCameraNode parent itemName activateAsPreviewCamera setAsDefaultCamera3D setDefaultOrientation`
#### Parameters

|

`parent` |

The node in which you create the Camera node. |
|

`itemName` |

The name of the Camera node. |
|

`activateAsPreviewCamera` |

Whether to activate the camera as the Preview camera. |
|

`setAsDefaultCamera3D` |

Whether to set the camera as the default camera. |
|

`setDefaultOrientation` |

Whether to set the Layout Transformation to the default orientation. |
#### Examples


```
# Create a Camera node named Camera in the Screen > RootNode > Viewport 2D > Scene node,
# activate the camera as the Preview camera, set the camera as the default camera,
# and set the Layout Transformation to the default orientation.
CreateCameraNode Camera "/Screens/Screen/RootNode/Viewport 2D/Scene" true true true

```

### CreateDirectionalLightNode


Directional Light emits light only in one direction. You can use Directional Light to model sunlight. By default each Scene node contains a Directional Light.
#### Syntax


`CreateDirectionalLightNode itemName parent`
#### Parameters

|

`itemName` |

The name of the light node. |
|

`parent` |

The node in which you create the light node. |
#### Examples


```
# Create a Directional Light node named My Directional Light in the Screen > RootNode > Viewport 2D > Scene node.
CreateDirectionalLightNode "My Directional Light" "/Screens/Screen/RootNode/Viewport 2D/Scene"

```

### CreateInstantiatorNode


Use an Instantiator node to create a copy of the object it targets. Instantiated nodes are not interactive.
#### Syntax


`CreateInstantiatorNode parent itemName target`
#### Parameters

|

`parent` |

The node in which you create the Instantiator node. |
|

`itemName` |

The name of the Instantiator node. |
|

`target` |

(Optional) The node that the Instantiator node instantiates. |
#### Examples


```
# Create an Instantiator node named My Instantiator in the Screen > RootNode > Viewport 2D > Scene node.
CreateInstantiatorNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Instantiator"

```


```
# Instantiate the Screen > RootNode > Viewport 2D > Scene > Directional Light node into
# an Instantiator node named Directional Light Instance in the Screen > RootNode > Viewport 2D > Scene node.
CreateInstantiatorNode "/Screens/Screen/RootNode/Viewport 2D/Scene" "Directional Light Instance" "/Screens/Screen/RootNode/Viewport 2D/Scene/Directional Light"

```

### CreatePointLightNode


Point Light emits light from a specific location uniformly to all directions (360 degrees).
#### Syntax


`CreatePointLightNode itemName parent`
#### Parameters

|

`itemName` |

The name of the light node. |
|

`parent` |

The node in which you create the light node. |
#### Examples


```
# Create a Point Light node named My Point Light in the Screen > RootNode > Viewport 2D > Scene node.
CreatePointLightNode "My Point Light" "/Screens/Screen/RootNode/Viewport 2D/Scene"

```

### CreateSpotLightNode


Spot Light emits light from a specific location towards a specified direction in the shape of a cone.
#### Syntax


`CreateSpotLightNode itemName parent`
#### Parameters

|

`itemName` |

The name of the light node. |
|

`parent` |

The node in which you create the light node. |
#### Examples


```
# Create a Spot Light node named My Spot Light in the Screen > RootNode > Viewport 2D > Scene node.
CreateSpotLightNode "My Spot Light" "/Screens/Screen/RootNode/Viewport 2D/Scene"

```

## Render Pass Creation

### CreateRenderPass


Create a render pass.
#### Syntax


`CreateRenderPass parent itemName renderPassTypeName`
#### Parameters

|

`parent` |

(Optional) The render pass or render pass prefab root in which you create the render pass. To create a render pass prefab, omit this parameter. |
|

`itemName` |

The name of the render pass. |
|

`renderPassTypeName` |

The name of the render pass type. |
#### Examples


```
# Create a Group Render Pass render pass prefab named Group in the Library > Rendering > Render Pass Prefabs.
CreateRenderPass "Group" Kanzi.RenderPass
# Create a Clear Render Pass named Clear in the Library > Rendering > Render Pass Prefabs > Group.
CreateRenderPass "/Render Pass Prefabs/Group/Group" "Clear" Kanzi.ClearRenderPass
# Create a Gather Lights Render Pass named Gather Lights in the Library > Rendering > Render Pass Prefabs > Group.
CreateRenderPass "/Render Pass Prefabs/Group/Group" "Gather Lights" Kanzi.GatherLightsRenderPass
# Create a Draw Objects Render Pass named Draw in the Library > Rendering > Render Pass Prefabs > Group > Gather Lights.
CreateRenderPass "/Render Pass Prefabs/Group/Group/Gather Lights" "Draw" Kanzi.DrawObjectsRenderPass

```


```
# This example creates the render passes that you need to render content to a composition target.
# Create a Group Render Pass prefab named Render Composition Target in the Library > Rendering > Render Pass Prefabs.
CreateRenderPass "Render Composition Target" Kanzi.RenderPass
# In the Render Composition Target create a Composition Target Render Pass named Composition Target Render Pass.
CreateRenderPass "/Render Pass Prefabs/Render Composition Target/Render Composition Target" "Composition Target Render Pass" Kanzi.CompositionTargetRenderPass
# In the Composition Target Render Pass create a Default Render Pass which contains a basic set of render passes that first render opaque nodes and then transparent nodes.
CreateDefaultRenderPassTree "/Render Pass Prefabs/Render Composition Target/Render Composition Target/Composition Target Render Pass" "Default Render Pass"
# In the Render Composition Target create a Blit Render Pass named Blit Render Pass.
CreateRenderPass "/Render Pass Prefabs/Render Composition Target/Render Composition Target" "Blit Render Pass" Kanzi.BlitRenderPass
# In the Blit Render Pass bind the Texture 0 property to the Result Texture 0 property of the Composition Target Render Pass.
CreateBindingItem "/Render Pass Prefabs/Render Composition Target/Render Composition Target/Blit Render Pass" ONE_WAY null BlitRenderPass.Texture0 WHOLE_PROPERTY "{../Composition Target Render Pass/CompositionTargetRenderPass.ResultTexture0}"

```


```
# Create a Pipeline State Render Pass named Pipeline State in the Library > Rendering > Render Pass Prefabs > Group Render Pass render pass prefab.
CreateRenderPass "/Render Pass Prefabs/Group Render Pass/Group Render Pass" "Pipeline State" Kanzi.PipelineStateRenderPass

```


```
# Create a Draw Objects With Material Render Pass named Draw Objects with Material in the Library > Rendering > Render Pass Prefabs > Group Render Pass render pass prefab.
CreateRenderPass "/Render Pass Prefabs/Group Render Pass/Group Render Pass" "Draw Objects with Material" Kanzi.DrawObjectsWithMaterialRenderPass

```


```
# Create a Material Setup Render Pass named Material Setup in the Library > Rendering > Render Pass Prefabs > Group Render Pass render pass prefab.
CreateRenderPass "/Render Pass Prefabs/Group Render Pass/Group Render Pass" "Material Setup" Kanzi.MaterialSetupRenderPass

```

## Render Pass Preset Creation

### CreateComposeAndBlitRenderPassTree


Use the Compose and Blit Pass render pass preset to create the render passes that you need to blit a Composition Target Render Pass using a specific material.
#### Syntax


`CreateComposeAndBlitRenderPassTree parent itemName`
#### Parameters

|

`parent` |

(Optional) The render pass prefab or render pass in which you create the Compose to Blit Pass. To create a Compose to Blit Pass prefab, omit this parameter. |
|

`itemName` |

The name of the Compose to Blit Pass. |
#### Examples


```
# Create a Compose and Blit Pass render pass prefab named Compose and Blit
# in the Library > Rendering > Render Pass Prefabs.
CreateComposeAndBlitRenderPassTree "Compose and Blit"

```


```
# Create a Group Render Pass render pass prefab named Group in the Library > Rendering > Render Pass Prefabs.
CreateRenderPass "Group" Kanzi.RenderPass
# Create a Compose and Blit Pass named Compose and Blit in the Group render pass prefab.
CreateComposeAndBlitRenderPassTree "/Render Pass Prefabs/Group/Group" "Compose and Blit"

```

### CreateDefaultRenderPassTree


Use the Default Render Pass render pass preset to create a basic set of render passes that you need to get started. The Default Render Pass first renders opaque nodes and then transparent nodes.
#### Syntax


`CreateDefaultRenderPassTree parent itemName`
#### Parameters

|

`parent` |

(Optional) The render pass prefab or render pass in which you create the Default Render Pass. To create a Default Render Pass prefab, omit this parameter. |
|

`itemName` |

The name of the Default Render Pass. |
#### Examples


```
# Create a Default Render Pass prefab named Default Rendering in the Library > Rendering > Render Pass Prefabs.
CreateDefaultRenderPassTree "Default Rendering"

```


```
# Create a Group Render Pass render pass prefab named Group in the Library > Rendering > Render Pass Prefabs.
CreateRenderPass "Group" Kanzi.RenderPass
# Create a Default Render Pass named Default Render Pass in the Group render pass prefab.
CreateDefaultRenderPassTree "/Render Pass Prefabs/Group/Group" "Default Render Pass"

```

### CreateImageBasedLightingFilterPassTree


Use the Image-Based Lighting Filter Pass preset to create render passes that pre-filter an environment map texture to an Environment Ambient Texture and Environment Reflection Texture. You can use these textures for image-based lighting with Physically-Based Rendering materials.
#### Syntax


`CreateImageBasedLightingFilterPassTree parent itemName`
#### Parameters

|

`parent` |

(Optional) The render pass in which you create the Image-Based Lighting Filter Pass. To create a Image-Based Lighting Filter Pass prefab, omit this parameter. |
|

`itemName` |

The name of the Image-Based Lighting Filter Pass. |
#### Examples


```
# Create an Image-Based Lighting Filter Pass render pass prefab named Image-Based Lighting Filter
# in the Library > Rendering > Render Pass Prefabs.
CreateImageBasedLightingFilterPassTree "Image-Based Lighting Filter"

```


```
# Create a Group Render Pass render pass prefab named Group in the Library > Rendering > Render Pass Prefabs.
CreateRenderPass "Group" Kanzi.RenderPass
# Create a Image-Based Lighting Filter Pass named Image-Based Lighting Filter in the Group render pass prefab.
CreateImageBasedLightingFilterPassTree "/Render Pass Prefabs/Group/Group" "Image-Based Lighting Filter"

```

### CreateRenderToTexturePassTree


Use the Render to Texture Pass render pass preset to create the render passes that you need to render to a texture.
#### Syntax


`CreateRenderToTexturePassTree parent itemName`
#### Parameters

|

`parent` |

(Optional) The render pass in which you create the Render to Texture Pass. To create a Render to Texture Pass prefab, omit this parameter. |
|

`itemName` |

The name of the Render to Texture Pass. |
#### Examples


```
# Create a Render to Texture Pass render pass prefab named Render to Texture
# in the Library > Rendering > Render Pass Prefabs.
CreateRenderToTexturePassTree "Render to Texture"

```


```
# Create a Group Render Pass render pass prefab named Group in the Library > Rendering > Render Pass Prefabs.
CreateRenderPass "Group" Kanzi.RenderPass
# Create a Render to Texture Pass named Render to Texture in the Group render pass prefab.
CreateRenderToTexturePassTree "/Render Pass Prefabs/Group/Group" "Render to Texture"

```

## Effect Creation

### CreateNodeEffect2D


Use effects to apply post-processing effects to 2D nodes.
#### Syntax


`CreateNodeEffect2D itemName effectTypeName`
#### Parameters

|

`itemName` |

The name of the effect. |
|

`effectTypeName` |

The type of the effect. |
#### Examples


```
# Create a Shadow Effect 2D in the Library > Effects > 2D Effects.
CreateNodeEffect2D "Shadow" Kanzi.ShadowEffect2D

```

## Effect Preset Creation

### CreateDefaultEffectStack


Use the Default Effect Stack 2D preset to quickly create and apply common effect types.
#### Syntax


`CreateDefaultEffectStack itemName`
#### Parameters

|

`itemName` |

The name of the Default Effect Stack 2D. |
#### Examples


```
# Create a Default Effect Stack 2D prefab named Default Effect in the Library > Effects > 2D Effects.
CreateDefaultEffectStack "Default Effect"

```

## Misc Creation

### CreateApplicationConfiguration


Create a set of build parameters for your project.
#### Syntax


`CreateApplicationConfiguration itemName configurationType`
#### Parameters

|

`itemName` |

The name of the build configuration. |
|

`configurationType` |

(Optional) The type of the build configuration: Android, QNX, or Windows. The default is Common Build Configuration. |
#### Examples


```
# Create a common build configuration named My Build Configuration in the Library > Build Configurations.
CreateApplicationConfiguration "My Build Configuration"
# In My Build Configuration, set the Application Root Directory to ..\..\..\Application.
SetProperty "/Resource Files/Build Configurations/My Build Configuration" BuildConfigurationApplicationRootDirectory "..\..\..\Application"
# In My Build Configuration, set the Build Profile to Debug.
SetProperty "/Resource Files/Build Configurations/My Build Configuration" BuildConfiguration.BuildProfile Debug

```


```
# Create an Android build configuration named My Android Build Configuration in the Library > Build Configurations.
CreateApplicationConfiguration "My Android Build Configuration" Android
# In My Android Build Configuration, set the CPU Architecture to ARM.
SetProperty "/Resource Files/Build Configurations/My Android Build Configuration" BuildConfigurationTargetArchitecture ARM
# In My Android Build Configuration, set the Launch Application property to disabled.
SetProperty "/Resource Files/Build Configurations/My Android Build Configuration" BuildConfigurationRunApplication False
# In My Android Build Configuration, set the APK Path to output\my-directory.
SetProperty "/Resource Files/Build Configurations/My Android Build Configuration" BuildConfigurationAPKPath "output\my-directory"

```

### CreateDataSource


Create a data source.
#### Syntax


`CreateDataSource itemName dataSourceTypeName`
#### Parameters

|

`itemName` |

The name of the data source. |
|

`dataSourceTypeName` |

The name of the data source type as declared in the Kanzi Engine data source plugin code. |
#### Examples


```
# Create a data source named Cluster of the type CustomDataSourceType.
CreateDataSource Cluster CustomDataSourceType
# To create data objects from the Cluster data source, update the data source.
UpdateDataSourceContents "/Data Sources/Cluster/"

```

### CreateFontFamily


Create an empty font family.
#### Syntax


`CreateFontFamily fontFamilyName fontFile`
#### Parameters

|

`fontFamilyName` |

The name of the font family. |
|

`fontFile` |

(Optional) The font file resource that you set the Font Family to use. |
#### Examples


```
# Create a single font family named My Font Family in the Library > Font Families.
CreateFontFamily "My Font Family"

```

### CreateLocale


Create a locale.
#### Syntax


`CreateLocale parent name`
#### Parameters

|

`parent` |

The Localization Table in which you create the locale. |
|

`name` |

The name of the locale. |
#### Examples


```
# Create a Locale named fi-FI in the Library > Localization > My Localization Table.
CreateLocale "/Localization/My Localization Table" fi-FI

```

### CreateLocalizationTable


Create a localization table.
#### Syntax


`CreateLocalizationTable name selectNewItems`
#### Parameters

|

`name` |

The name of the Localization Table. |
|

`selectNewItems` |

(Optional) Whether Kanzi Studio selects the Localization Table. The default value is false. |
#### Examples


```
# Create a Localization Table named My Localization Table in the Library > Localization.
CreateLocalizationTable "My Localization Table"

```

### CreateNode3DPrefabPlaceholder


Use a Prefab Placeholder 3D node to instantiate a 3D prefab.

Kanzi replaces the Prefab Placeholder node with the root node of the prefab it instantiates.
#### Syntax


`CreateNode3DPrefabPlaceholder parent itemName prefabTemplate`
#### Parameters

|

`parent` |

The node in which you create the Prefab Placeholder 3D node. |
|

`itemName` |

The name of the Prefab Placeholder 3D node. |
|

`prefabTemplate` |

(Optional) The prefab template which you set the Prefab Placeholder 3D node to use. |
#### Examples


```
# Create a Prefab Placeholder 3D node named My Prefab Placeholder 3D in the Screen > RootNode > Viewport 2D > Scene node.
CreateNode3DPrefabPlaceholder "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Prefab Placeholder 3D"

```


```
# Create a Prefab Placeholder 3D node named My Prefab Placeholder 3D in the Screen > RootNode > Viewport 2D > Scene node
# and set the Prefab Template property of the My Prefab Placeholder 3D node to the Prefabs > Toggle Button 3D prefab.
CreateNode3DPrefabPlaceholder "/Screens/Screen/RootNode/Viewport 2D/Scene" "My Prefab Placeholder 3D" "/Prefabs/Toggle Button 3D"

```

### CreateResourceDictionary


Create a resource dictionary in the selected node. A resource dictionary is a collection of resource IDs pointing to resources.
#### Syntax


`CreateResourceDictionary parent`
#### Parameters

|

`parent` |

The node to which you add the resource dictionary. |
#### Examples


```
# Add a resource dictionary to the RootNode node.
CreateResourceDictionary "/Screens/Screen/RootNode"

```

### CreateState


Use a state to collect properties that define the appearance and behavior of the node to which you assign the state manager. In a state group, only one state can be active at a time.
#### Syntax


`CreateState parent name selectNewItems`
#### Parameters

|

`parent` |

The state group in which you create the state. |
|

`name` |

The name of the state. |
|

`selectNewItems` |

Whether Kanzi Studio selects the state. |
#### Examples


```
# Create states named State1 and State 2 in the Library > State Managers > My State Manager > State Group.
# Do not select the states.
CreateState "/State Managers/My State Manager/State Group" "State 1" false
CreateState "/State Managers/My State Manager/State Group" "State 2" false

```

### CreateStateGroup


A state group contains states and defines a controller property and transitions between states.
#### Syntax


`CreateStateGroup parent name selectNewItems`
#### Parameters

|

`parent` |

The state manager in which you create the state group. |
|

`name` |

The name of the state group. |
|

`selectNewItems` |

(Optional) Whether Kanzi Studio selects the state group. The default value is true. |
#### Examples


```
# Create a state group named State Group in the Library > State Managers > My State Manager.
# Do not select the state group.
CreateStateGroup "/State Managers/My State Manager" "State Group" false

```

### CreateStateManager


Use a State Manager to define the look and behavior of your Kanzi application in different states.
#### Syntax


`CreateStateManager itemName selectNewItems`
#### Parameters

|

`itemName` |

The name of the state manager. |
|

`selectNewItems` |

(Optional) Whether Kanzi Studio selects the state manager. The default value is true. |
#### Examples


```
# Create a state manager named My State Manager in the Library > State Managers and select My State Manager.
CreateStateManager "My State Manager"

```


```
# Create a state manager named My State Manager in the Library > State Managers but do not select the state manager.
CreateStateManager "My State Manager" false

```

#### Syntax


`CreateStateManager itemName selectNewItems createContent`
#### Parameters

|

`itemName` |

The name of the state manager. |
|

`selectNewItems` |

Whether Kanzi Studio selects the state manager. |
|

`createContent` |

Whether to create in the state manager a state group with two states. |
#### Examples


```
# Create a state manager named My State Manager in the Library > State Managers,
# select the state manager, and in the state manager create a state group with two states.
CreateStateManager "My State Manager" true true

```

### CreateStateWithTarget


Use a state object to define the properties of a node for a state.
#### Syntax


`CreateStateWithTarget parent name stateObjectPath selectNewItems`
#### Parameters

|

`parent` |

The state in which you create the state object. |
|

`name` |

The name of the state object. |
|

`stateObjectPath` |

The value of the Target Object Path property of the state object. |
|

`selectNewItems` |

Whether Kanzi Studio selects the state object. |
#### Examples


```
# Create a state object named Car Object in the Library > State Managers > My State Manager > State Group > State 1 state,
# and set the Target Object Path property to Car. Do not select the Car Object state object.
CreateStateWithTarget "/State Managers/My State Manager/State Group/State 1" "Car Object" "Car" false

```

#### Syntax


`CreateStateWithTarget name parent selectNewItems`
#### Parameters

|

`name` |

The name of the state object. |
|

`parent` |

The state in which you create the state object. |
|

`selectNewItems` |

Whether Kanzi Studio selects the state object. |
#### Examples


```
# Create a state object named State Object in the Library > State Managers > My State Manager > State Group > State 1 state.
# Do not select the state object.
CreateStateWithTarget "State Object" "/State Managers/My State Manager/State Group/State 1" false

```

### CreateTag


Use tags to group, find, and filter nodes in your project. You can assign multiple tags to a single node.
#### Syntax


`CreateTag itemName selectNewItems`
#### Parameters

|

`itemName` |

The name of the tag. |
|

`selectNewItems` |

Whether Kanzi Studio selects the tag. |
#### Examples


```
# Create a tag named My Tag in the Library > Tags and select the tag.
CreateTag "My Tag" true

```

### CreateTheme


Use Themes to define the look and feel of your application.
#### Syntax


`CreateTheme parent name`
#### Parameters

|

`parent` |

The Theme Group in which you create the Theme. |
|

`name` |

The name of the Theme. |
#### Examples


```
# Create a Theme named Classic in the Cluster Themes theme group.
CreateTheme "/Themes/Cluster Themes" Classic

```

### CreateThemeGroup


Use a Theme Group to define a collection of Themes that define the look and feel of your application. Themes enable you to use a single Kanzi Studio project for multiple variants of your product.
#### Syntax


`CreateThemeGroup name selectNewItems`
#### Parameters

|

`name` |

The name of the Theme Group. |
|

`selectNewItems` |

(Optional) Whether Kanzi Studio selects the Theme Group. The default value is false. |
#### Examples


```
# Create a Theme Group named Cluster Theme in the Library > Themes.
CreateThemeGroup "Cluster Theme"

```

### ExportLocalizationTable


Export the localization table template to a .pot file, and as many .po files as there are locales in that localization table to <ProjectName>/Localization/<LocalizationTableName>.
#### Syntax


`ExportLocalizationTable localizationTable localizationDirectoryPath`
#### Parameters

|

`localizationTable` |

The localization table that you export. |
|

`localizationDirectoryPath` |

The directory to which you export the localization table. |
#### Examples


```
# Export the Library > Localization > Localization Table to the C:\Temp directory.
# Kanzi Studio creates the C:\Temp\Localization Table directory, and exports to the directory
# the localization table template to a .pot file, and as many .po files as you have locales
# in that localization table.
ExportLocalizationTable "/Localization/Localization Table" "C:\Temp"

```

### ImportAllLocalizationTables


Import all PO files from all localization table folders in the Localization directory of your project.
#### Syntax


`ImportAllLocalizationTables localizationDirectoryPath`
#### Parameters

|

`localizationDirectoryPath` |

Path to the directory that contains the localization table folders. Kanzi Studio looks in this directory for folders that contain PO files, and creates for each such folder a localization table named after the folder. If a localization table already exists, Kanzi Studio updates it. |
#### Examples


```
# Imports all PO files from all directories found in the
# C:\KanziWorkspace\Projects\MyProject\Tool_Project\Localization directory.
# Kanzi Studio imports the files for all localization tables in the Library > Localization.
ImportAllLocalizationTables "C:\KanziWorkspace\Projects\MyProject\Tool_Project\Localization"

```

### ImportEnginePlugin


Import Kanzi Engine plugin. During import the components, property types, messages and triggers contained in the plugin become available to the project.
#### Syntax


`ImportEnginePlugin loadPath existingPlugin`
#### Parameters

|

`loadPath` |

To update an existing Kanzi Engine plugin leave this parameter empty. |
|

`existingPlugin` |

The Kanzi Engine plugin that you update. |
#### Examples


```
# Update the XML_data_source Kanzi Engine plugin in the project.
# You leave the first parameter empty because you do not import a new plugin to the project.
ImportEnginePlugin "" "/Kanzi Engine Plugins/XML_data_source"

```

#### Syntax


`ImportEnginePlugin existingPluginFile`
#### Parameters

|

`existingPluginFile` |

The Kanzi Engine plugin DLL. |
#### Examples


```
# Import the Kanzi Engine plugin DLL MyPluginProject\Application\lib\Win64\vs2022_Debug_DLL\MyPluginProject.dll.
# Kanzi Studio adds to the Library > Kanzi Engine Plugins a reference to the Kanzi Engine plugin DLL that you import.
ImportEnginePlugin "C:\KanziWorkspace\Projects\MyPluginProject\Application\lib\Win64\vs2022_Debug_DLL\MyPluginProject.dll"

```

### TagItems


Adds a tag to a set of items.
#### Syntax


`TagItems tags itemsToTag`
#### Parameters

|

`tags` |

The tags that you assign. Separate a list of tags with semicolons. |
|

`itemsToTag` |

The nodes to which you assign the tags. Separate a list of nodes with semicolons. |
#### Examples


```
# Create a tag named Lights in the Library > Tags and select the tag.
CreateTag "Lights" true
# Create a Spot Light node named Spot Light in the Screen > RootNode > Viewport 2D > Scene node.
CreateSpotLightNode "Spot Light" "/Screens/Screen/RootNode/Viewport 2D/Scene"
# Tag the Directional Light and Spot Light nodes with the Lights tag.
TagItems "/Tags/Lights" "/Screens/Screen/RootNode/Viewport 2D/Scene/Directional Light; /Screens/Screen/RootNode/Viewport 2D/Scene/Spot Light"

```

### UpdateDataSourceContents


Read and cache data from data source for creating data bindings in UI.
#### Syntax


`UpdateDataSourceContents dataSource`
#### Parameters

|

`dataSource` |

The data source that you update. |
#### Examples


```
# Update the Cluster data source.
UpdateDataSourceContents "/Data Sources/Cluster/"

```

### UpdateProjectDataSources


Read and cache data from data sources defined in this project for creating data bindings in UI.
#### Syntax


`UpdateProjectDataSources`
#### Examples


```
# Update all data sources in the project.
UpdateProjectDataSources

```

### UpdateProjectEnginePlugins


To see changes in the custom nodes, property types, triggers, and actions that the Kanzi Engine plugins in this project define, load the latest versions of the plugins.
#### Syntax


`UpdateProjectEnginePlugins`
#### Examples


```
# Update all Kanzi Engine plugins in the project.
UpdateProjectEnginePlugins

```

### UpdateSolutionDataSources


Read and cache data from data sources defined in this solution for creating data bindings in UI.
#### Syntax


`UpdateSolutionDataSources`
#### Examples


```
# Update all data sources in the project and all referenced projects.
UpdateSolutionDataSources

```

### UpdateSolutionEnginePlugins


To see changes in the custom nodes, property types, triggers, and actions that the Kanzi Engine plugins in this solution define, load the latest versions of the plugins.
#### Syntax


`UpdateSolutionEnginePlugins`
#### Examples


```
# Update all Kanzi Engine plugins in the project and all referenced projects.
UpdateProjectEnginePlugins

```

## Object Source Creation

### CreateCombineObjectSource


Use a Combine Object Source to collect and combine nodes from one or more input sources, such as filters.
#### Syntax


`CreateCombineObjectSource itemName`
#### Parameters

|

`itemName` |

The name of the Combine Object Source. |
#### Examples


```
# Create a Combine Object Source named My Combine Object Source in the Library > Rendering > Object Sources.
CreateCombineObjectSource "My Combine Object Source"
# In My Combine Object Source set the Inputs list to contain the Transparent and My Tag Filter filters.
SetProperty "/Object Sources/My Combine Object Source" CombineObjectSourceInputs "/Object Sources/Transparent#/Object Sources/My Tag Filter"

```

### CreateContainsPropertyFilterObjectSource


Use a Contains Property Filter to collect nodes that contain, or do not contain a specific property.
#### Syntax


`CreateContainsPropertyFilterObjectSource itemName`
#### Parameters

|

`itemName` |

The name of the filter. |
#### Examples


```
# Create a Contains Property Filter named My Contains Property Filter
# in the Library > Rendering > Object Sources.
CreateContainsPropertyFilterObjectSource "My Contains Property Filter"
# In My Contains Property Filter set the Property Type property to Ambient Color (Ambient).
SetProperty "/Object Sources/My Contains Property Filter" ContainsPropertyFilterPropertyTypeName Ambient
# In My Contains Property Filter set the Operation property to EXCLUDE.
SetProperty "/Object Sources/My Contains Property Filter" ContainsPropertyFilterOperation EXCLUDE

```

### CreateFixedSortFilterObjectSource


Use a Sorting Filter to either order nodes by their position on the z axis or to group them by their material type.
#### Syntax


`CreateFixedSortFilterObjectSource itemName`
#### Parameters

|

`itemName` |

The name of the filter. |
#### Examples


```
# Create a Sorting Filter named My Sorting Filter in the Library > Rendering > Object Sources.
CreateFixedSortFilterObjectSource "My Sorting Filter"
# Set the Sorting Type property of My Sorting Filter to Material type.
SetProperty "/Object Sources/My Sorting Filter" FixedSortType MATERIAL_TYPE
# In My Sorting Filter set the Reverse Order property to enabled.
SetProperty "/Object Sources/My Sorting Filter" FixedSortReverse true

```

### CreateObjectTypeFilterObjectSource


Use an Object Type Filter to collect nodes based on their type.
#### Syntax


`CreateObjectTypeFilterObjectSource itemName`
#### Parameters

|

`itemName` |

The name of the filter. |
#### Examples


```
# Create an Object Type Filter named My Object Type Filter in the Library > Rendering > Object Sources.
CreateObjectTypeFilterObjectSource "My Object Type Filter"
# In My Object Type Filter set the Type property to Light.
SetProperty "/Object Sources/My Object Type Filter" ObjectTypeFilterObjectType LIGHT
# In My Object Type Filter set the Operation property to Exclude.
SetProperty "/Object Sources/My Object Type Filter" ObjectTypeFilterOperation EXCLUDE

```

### CreatePropertyIsEqualObjectSource


Use a Property is Equal Filter to collect nodes that contain, or do not contain a specific property the value of which matches a specific value.
#### Syntax


`CreatePropertyIsEqualObjectSource itemName`
#### Parameters

|

`itemName` |

The name of the filter. |
#### Examples


```
# Create a Property Is Equal Filter named My Property Is Equal Filter in the Library > Rendering > Object Sources.
CreatePropertyIsEqualObjectSource "My Property Is Equal Filter"

```

### CreateTagFilter


Use a Tag Filter to collect the nodes that have a specific tag assigned.
#### Syntax


`CreateTagFilter itemName`
#### Parameters

|

`itemName` |

The name of the filter. |
#### Examples


```
# Create a Tag Filter named My Tag Filter in the Library > Rendering > Object Sources.
CreateTagFilter "My Tag Filter"
# Create a tag named My Tag in the Library > Tags.
CreateTag "My Tag" false
# Create a tag named Lights in the Library > Tags.
CreateTag "Lights" false
# In My Tag Filter set the Included Tags list to contain the My Tag and Lights tags.
SetProperty "/Object Sources/My Tag Filter" TagFilterIncludeList "/Tags/My Tag#/Tags/Lights"
# In My Tag Filter set the Excluded Tags list to contain the Transparent tag.
SetProperty "/Object Sources/My Tag Filter" TagFilterExcludeList "/Tags/Transparent"

```

## Texture Creation

### CreateEnvironmentCubeMapTexture


Use an environment cubemap texture to represent the environment, such as an outdoor scene. An environment cubemap texture combines six square-shaped images into one texture.
#### Syntax


`CreateEnvironmentCubeMapTexture imageFile size name`
#### Parameters

|

`imageFile` |

The HDR image from which you want to generate the environment cubemap texture. |
|

`size` |

The width and height of the square-shaped cubemap side images. |
|

`name` |

(Optional) The name of the environment cubemap texture. |
#### Examples


```
# Create an environment cubemap texture named My Environment Cubemap Texture
# from the Library > Resource Files > Images > my_skybox_image.exr image and
# set the size of the cubemap side images to 1024x1024 pixels.
CreateEnvironmentCubeMapTexture "/Resource Files/Images/my_skybox_image.exr" 1024 "My Environment Cubemap Texture"

```


```
# Create an environment cubemap texture from the Library > Resource Files >
# Images > my_skybox_image.exr image. Let Kanzi Studio name the texture
# my_skybox_image_environment and set the size of the cubemap side images to
# 1024x1024 pixels.
CreateEnvironmentCubeMapTexture "/Resource Files/Images/my_skybox_image.exr" 1024

```

#### Syntax


`CreateEnvironmentCubeMapTexture imageFile`
#### Parameters

|

`imageFile` |

The HDR image from which you want to generate the environment cubemap texture. |
#### Examples


```
# Create an environment cubemap texture from the Library > Resource Files >
# Images > my_skybox_image.exr image and let Kanzi Studio name the texture
# my_skybox_image_environment. Kanzi Studio creates cubemap side images whose
# dimensions are one quarter of the width of the input image.
CreateEnvironmentCubeMapTexture "/Resource Files/Images/my_skybox_image.exr"

```

### CreateIrradianceCubeMapTexture


Use an irradiance cubemap texture for image-based lighting. An irradiance cubemap texture combines six square-shaped images into one texture to represent diffuse environment lighting.
#### Syntax


`CreateIrradianceCubeMapTexture sourceImage samples size name`
#### Parameters

|

`sourceImage` |

The HDR image from which you want to generate the irradiance cubemap texture. |
|

`samples` |

The number of samples to use to generate the cubemap. A larger number of samples results in a cubemap that approximates the environment lighting more accurately. |
|

`size` |

The width and height of the square-shaped cubemap side images. |
|

`name` |

(Optional) The name of the irradiance cubemap texture. |
#### Examples


```
# Create an irradiance cubemap texture named My Irradiance Cubemap Texture
# from the Library > Resource Files > Images > my_skybox_image.exr image.
# Use 256 samples and set the size of the cubemap side images to 1024x1024
# pixels.
CreateIrradianceCubeMapTexture "/Resource Files/Images/my_skybox_image.exr" 256 1024 "My Irradiance Cubemap Texture"

```


```
# Create an irradiance cubemap texture from the Library > Resource Files >
# Images > my_skybox_image.exr image and let Kanzi Studio name the texture
# my_skybox_image_irradiance. Use 1024 samples and set the size of the cubemap
# side images to 256x256 pixels.
CreateIrradianceCubeMapTexture "/Resource Files/Images/my_skybox_image.exr" 1024 256

```

#### Syntax


`CreateIrradianceCubeMapTexture sourceImage`
#### Parameters

|

`sourceImage` |

The HDR image from which you want to generate the irradiance cubemap texture. |
#### Examples


```
# Create an irradiance cubemap texture from the Library > Resource Files >
# Images > my_skybox_image.exr image and let Kanzi Studio name the texture
# my_skybox_image_irradiance. Kanzi Studio uses 1024 samples to generate the
# cubemap and creates cubemap side images whose dimensions are one quarter
# of the width of the input image but at most 256 pixels.
CreateIrradianceCubeMapTexture "/Resource Files/Images/my_skybox_image.exr"

```

### CreateRenderTargetTexture


Use a Render Target Texture to dynamically render content from 2D layouts into a texture.
#### Syntax


`CreateRenderTargetTexture textureName`
#### Parameters

|

`textureName` |

The name of the texture. |
#### Examples


```
# Create a render target texture named My Render Target Texture in the Library > Materials and Textures > Textures.
CreateRenderTargetTexture "My Render Target Texture"
# In My Render Target Texture set the Width and Height properties to 256.
SetProperty "/Textures/My Render Target Texture" RenderTargetTextureWidth 256
SetProperty "/Textures/My Render Target Texture" RenderTargetTextureHeight 256

```

### CreateSingleTexture


Use a Single Texture when you want to use a single image as a texture.
#### Syntax


`CreateSingleTexture textureName image`
#### Parameters

|

`textureName` |

The name of the texture. |
|

`image` |

(Optional) The image resource that you set the texture to use. |
#### Examples


```
# Create a single texture named My Single Texture in the Library > Materials and Textures > Textures.
CreateSingleTexture "My Single Texture"

```


```
# Create a single texture named Image01 Texture in the Library > Materials and Textures > Textures and
# set the texture to use the Library > Resource Files > Images > Image01.png image.
CreateSingleTexture "Image01 Texture" "/Resource Files/Images/Image01.png"

```

### CreateSpecularCubeMapTexture


Use a specular cubemap texture for image-based lighting. A specular cubemap texture combines six square-shaped images into one texture to represent reflective environment lighting.
#### Syntax


`CreateSpecularCubeMapTexture sourceImage samples size name`
#### Parameters

|

`sourceImage` |

The HDR image from which you want to generate the specular cubemap texture. |
|

`samples` |

The number of samples to use to generate the cubemap. A larger number of samples results in a cubemap that approximates the environment lighting more accurately. |
|

`size` |

The width and height of the square-shaped cubemap side images. |
|

`name` |

(Optional) The name of the specular cubemap texture. |
#### Examples


```
# Create a specular cubemap texture named My Specular Cubemap Texture
# from the Library > Resource Files > Images > my_skybox_image.exr image.
# Use 256 samples and set the size of the cubemap side images to 1024x1024 pixels.
CreateSpecularCubeMapTexture "/Resource Files/Images/my_skybox_image.exr" 256 1024 "My Specular Cubemap Texture"

```


```
# Create a specular cubemap texture from the Library > Resource Files >
# Images > my_skybox_image.exr image and let Kanzi Studio name the texture
# my_skybox_image_specular. Use 1024 samples and set the size of the cubemap
# side images to 256x256 pixels.
CreateSpecularCubeMapTexture "/Resource Files/Images/my_skybox_image.exr" 1024 256

```

#### Syntax


`CreateSpecularCubeMapTexture sourceImage`
#### Parameters

|

`sourceImage` |

The HDR image from which you want to generate the specular cubemap texture. |
#### Examples


```
# Create a specular cubemap texture from the Library > Resource Files >
# Images > my_skybox_image.exr image and let Kanzi Studio name the texture
# my_skybox_image_specular. Kanzi Studio uses 1024 samples to generate the
# cubemap and creates cubemap side images whose dimensions are one quarter
# of the width of the input image but at most 256 pixels.
CreateSpecularCubeMapTexture "/Resource Files/Images/my_skybox_image.exr"

```

### CreateVolumeTexture


Use a Volume Texture when you want to use a single image as a volume texture.
#### Syntax


`CreateVolumeTexture textureName image`
#### Parameters

|

`textureName` |

The name of the texture. |
|

`image` |

(Optional) The image resource that you set the texture to use. |
## Trajectory Creation

### CreateAngleTrajectory


Use an Angle Trajectory to create a path where two straight lines form an angle in 3D space.
#### Syntax


`CreateAngleTrajectory itemName`
#### Parameters

|

`itemName` |

The name of the trajectory. |
#### Examples


```
# Create an Angle Trajectory named My Angle Trajectory in the Library > Trajectories.
CreateAngleTrajectory "My Angle Trajectory"

```

#### Syntax


`CreateAngleTrajectory itemName selectNewItems resourceDictionary`
#### Parameters

|

`itemName` |

The name of the trajectory. |
|

`selectNewItems` |

Whether Kanzi Studio selects the trajectory that you created. |
|

`resourceDictionary` |

The resource dictionary to which you add the trajectory. |
#### Examples


```
# Create an Angle Trajectory named My Angle Trajectory and add it to the resource dictionary of the Screen node.
CreateAngleTrajectory "My Angle Trajectory" false "/Screens/Screen/<ResourceDictionaryInNode>"

```

### CreateArcTrajectory


Use an Arc Trajectory to create a path in the shape of an arc in 3D space.
#### Syntax


`CreateArcTrajectory itemName`
#### Parameters

|

`itemName` |

The name of the trajectory. |
#### Examples


```
# Create an Arc Trajectory named My Arc Trajectory in the Library > Trajectories.
CreateArcTrajectory "My Arc Trajectory"

```

#### Syntax


`CreateArcTrajectory library itemName selectNewItems resourceDictionary`
#### Parameters

|

`library` |

(Optional) The Trajectory Library in which you create the trajectory. |
|

`itemName` |

The name of the trajectory. |
|

`selectNewItems` |

Whether Kanzi Studio selects the trajectory that you created. |
|

`resourceDictionary` |

The resource dictionary to which you add the trajectory. |
#### Examples


```
# Create an Arc Trajectory named My Arc Trajectory and add it to the resource dictionary of the Screen node.
CreateArcTrajectory "My Arc Trajectory" false "/Screens/Screen/<ResourceDictionaryInNode>"

```

### CreateCircleTrajectory


Use a Circle Trajectory to create a path in the shape of a circle in 3D space.
#### Syntax


`CreateCircleTrajectory itemName`
#### Parameters

|

`itemName` |

The name of the trajectory. |
#### Examples


```
# Create a Circle Trajectory named My Circle Trajectory in the Library > Trajectories.
CreateCircleTrajectory "My Circle Trajectory"

```

#### Syntax


`CreateCircleTrajectory library itemName resourceDictionary`
#### Parameters

|

`library` |

(Optional) The Trajectory Library in which you create the trajectory. |
|

`itemName` |

The name of the trajectory. |
|

`resourceDictionary` |

The resource dictionary to which you add the trajectory. |
#### Examples


```
# Create a Circle Trajectory named My Circle Trajectory and add it to the resource dictionary of the Screen node.
CreateCircleTrajectory "My Circle Trajectory" "/Screens/Screen/<ResourceDictionaryInNode>"

```

### CreateEllipseTrajectory


Use an Ellipse Trajectory to create a path in the shape of an ellipse in 3D space.
#### Syntax


`CreateEllipseTrajectory itemName`
#### Parameters

|

`itemName` |

The name of the trajectory. |
#### Examples


```
# Create an Ellipse Trajectory named My Ellipse Trajectory in the Library > Trajectories.
CreateEllipseTrajectory "My Ellipse Trajectory"

```

#### Syntax


`CreateEllipseTrajectory library itemName selectNewItems resourceDictionary`
#### Parameters

|

`library` |

(Optional) The Trajectory Library in which you create the trajectory. |
|

`itemName` |

The name of the trajectory. |
|

`selectNewItems` |

Whether Kanzi Studio selects the trajectory that you created. |
|

`resourceDictionary` |

The resource dictionary to which you add the trajectory. |
#### Examples


```
# Create an Ellipse Trajectory named My Ellipse Trajectory and add it to the resource dictionary of the Screen node.
CreateEllipseTrajectory "My Ellipse Trajectory" false "/Screens/Screen/<ResourceDictionaryInNode>"

```

### CreateLineTrajectory


Use a Line Trajectory to create a path with a single straight line in 3D space.
#### Syntax


`CreateLineTrajectory itemName`
#### Parameters

|

`itemName` |

The name of the trajectory. |
#### Examples


```
# Create a Line Trajectory named My Line Trajectory in the Library > Trajectories.
CreateLineTrajectory "My Line Trajectory"

```

#### Syntax


`CreateLineTrajectory library itemName selectNewItems resourceDictionary`
#### Parameters

|

`library` |

(Optional) The Trajectory Library in which you create the trajectory. |
|

`itemName` |

The name of the trajectory. |
|

`selectNewItems` |

Whether Kanzi Studio selects the trajectory that you created. |
|

`resourceDictionary` |

The resource dictionary to which you add the trajectory. |
#### Examples


```
# Create a Line Trajectory named My Line Trajectory and add it to the resource dictionary of the Screen node.
CreateLineTrajectory "My Line Trajectory" false "/Screens/Screen/<ResourceDictionaryInNode>"

```

### CreateRectangleTrajectory


Use a Rectangle Trajectory to create a path in the shape of a rectangle in 3D space.
#### Syntax


`CreateRectangleTrajectory itemName`
#### Parameters

|

`itemName` |

The name of the trajectory. |
#### Examples


```
# Create a Rectangle Trajectory named My Rectangle Trajectory in the Library > Trajectories.
CreateRectangleTrajectory "My Rectangle Trajectory"

```

#### Syntax


`CreateRectangleTrajectory library itemName selectNewItems resourceDictionary`
#### Parameters

|

`library` |

(Optional) The Trajectory Library in which you create the trajectory. |
|

`itemName` |

The name of the trajectory. |
|

`selectNewItems` |

Whether Kanzi Studio selects the trajectory that you created. |
|

`resourceDictionary` |

The resource dictionary to which you add the trajectory. |
#### Examples


```
# Create a Rectangle Trajectory named My Rectangle Trajectory and add it to the resource dictionary of the Screen node.
CreateRectangleTrajectory "My Rectangle Trajectory" false "/Screens/Screen/<ResourceDictionaryInNode>"

```

### CreateSpiralTrajectory


Use a Spiral Trajectory to create a path in the shape of a spiral in 3D space.
#### Syntax


`CreateSpiralTrajectory itemName`
#### Parameters

|

`itemName` |

The name of the trajectory. |
#### Examples


```
# Create a Spiral Trajectory named My Spiral Trajectory in the Library > Trajectories.
CreateSpiralTrajectory "My Spiral Trajectory"

```

#### Syntax


`CreateSpiralTrajectory library itemName selectNewItems resourceDictionary`
#### Parameters

|

`library` |

(Optional) The Trajectory Library in which you create the trajectory. |
|

`itemName` |

The name of the trajectory. |
|

`selectNewItems` |

Whether Kanzi Studio selects the trajectory that you created. |
|

`resourceDictionary` |

The resource dictionary to which you add the trajectory. |
#### Examples


```
# Create a Spiral Trajectory named My Spiral Trajectory and add it to the resource dictionary of the Screen node.
CreateSpiralTrajectory "My Spiral Trajectory" false "/Screens/Screen/<ResourceDictionaryInNode>"

```

### CreateTrapezoidTrajectory


Use a Trapezoid Trajectory to create a path in the shape of a trapezoid in 3D space.
#### Syntax


`CreateTrapezoidTrajectory itemName`
#### Parameters

|

`itemName` |

The name of the trajectory. |
#### Examples


```
# Create a Trapezoid Trajectory named My Trapezoid Trajectory in the Library > Trajectories.
CreateTrapezoidTrajectory "My Trapezoid Trajectory"

```

#### Syntax


`CreateTrapezoidTrajectory library itemName selectNewItems resourceDictionary`
#### Parameters

|

`library` |

(Optional) The Trajectory Library in which you create the trajectory. |
|

`itemName` |

The name of the trajectory. |
|

`selectNewItems` |

Whether Kanzi Studio selects the trajectory that you created. |
|

`resourceDictionary` |

The resource dictionary to which you add the trajectory. |
#### Examples


```
# Create a Trapezoid Trajectory named My Trapezoid Trajectory and add it to the resource dictionary of the Screen node.
CreateTrapezoidTrajectory "My Trapezoid Trajectory" false "/Screens/Screen/<ResourceDictionaryInNode>"

```

## Import

### ImportAsset3DSourceFile


Import 3D asset file into project
#### Syntax


`ImportAsset3DSourceFile filePath`
#### Parameters

|

`filePath` |

The path to the 3D asset file that you import. |
#### Examples


```
# Import the 3D asset file.
ImportAsset3DSourceFile "C:\KanziWorkspace\Assets\3DAsset.fbx"

```

### ImportImages


Import images into project
#### Syntax


`ImportImages filePath createTextures`
#### Parameters

|

`filePath` |

The path to the image you import. |
|

`createTextures` |

Whether to create a texture of the image. |
#### Examples


```
# Import the C:\Temp\Image.png image to the project and create a single texture of the image.
ImportImages "C:\Temp\Image.png" true

```

## Disk

### CleanCachedFiles


Delete the cache files that Kanzi Studio created in the project directory when you opened the project or exported the kzb file.
#### Syntax


`CleanCachedFiles`
#### Examples


```
# Delete the cache files that Kanzi Studio created in the project directory when you opened the project or exported the kzb file.
CleanCachedFiles

```

### CloseSolution


Close the currently open primary project and its referenced projects.
#### Syntax


`CloseSolution`
#### Examples


```
# Close all projects.
CloseSolution

```

### CompressImage


Preprocess the selected images. Preprocessing can include image compression and the generation of mipmaps.
#### Syntax


`CompressImage imageFiles`
#### Parameters

|

`imageFiles` |

The image files that you want to preprocess. |
#### Examples


```
# Preprocess the images Car.png and Background.png.
CompressImage "/Resource Files/Images/Image01.png; /Resource Files/Images/Image02.png"

```

### CreateKanziApplication


Create a Kanzi Engine application for the selected build configuration.
#### Syntax


`CreateKanziApplication buildConfiguration`
#### Parameters

|

`buildConfiguration` |

The path to the build configuration for which you want to create the application. |
#### Examples


```
# Create an Android build configuration named MyAndroidProject in the
# Library > Build Configurations.
CreateApplicationConfiguration MyAndroidProject Android
# Create a Kanzi application directory hierarchy for the MyAndroidProject
# build configuration.
CreateKanziApplication "/Resource Files/Build Configurations/MyAndroidProject"

```


```
# Create a common build configuration named MyProject in the
# Library > Build Configurations.
CreateApplicationConfiguration MyProject
# Create a Kanzi application directory hierarchy for the MyProject
# build configuration.
CreateKanziApplication "/Resource Files/Build Configurations/MyProject"

```

### DeleteExportedBinaries


Delete all exported files from the directory set in the Project > Properties in the Binary Export Directory property. This command deletes all exported files, including those from other projects.
#### Syntax


`DeleteExportedBinaries`
#### Examples


```
# Delete the kzb files from the location set in the main project properties in the Binary Export Directory property.
DeleteExportedBinaries

```

#### Syntax


`DeleteExportedBinaries exportDirectory`
#### Parameters

|

`exportDirectory` |

The directory from which you want to delete kzb files. |
#### Examples


```
# Delete all kzb files from the C:\Temp directory.
DeleteExportedBinaries "C:\Temp"

```

### ExitApplication


Close Kanzi Studio.
#### Syntax


`ExitApplication allowCancel silentExit`
#### Parameters

|

`allowCancel` |

Whether the user can cancel the action. |
|

`silentExit` |

Whether Kanzi Studio closes without showing any dialogs. |
#### Examples


```
# Close Kanzi Studio but let the user cancel the closing. Show dialogs when closing Kanzi Studio.
ExitApplication true false

```

#### Syntax


`ExitApplication`
#### Examples


```
# Close Kanzi Studio.
ExitApplication

```

### ExportAllProjectBinaries


Export the kzb files of the main project and loaded referenced projects. Copy exported kzb files to the directory set in the Binary Export Directory property of the main project properties.
#### Syntax


`ExportAllProjectBinaries`
#### Examples


```
# Export the kzb files of the main project and loaded referenced projects to the location set
# in the main project properties in the Binary Export Directory property.
ExportAllProjectBinaries

```

#### Syntax


`ExportAllProjectBinaries targetDirectory compressImages exportKzbPlayer`
#### Parameters

|

`targetDirectory` |

The directory to which you want to export the kzb files. |
|

`compressImages` |

Whether to preprocess the images in the project. |
|

`exportKzbPlayer` |

Whether to export the project as a standalone Windows application using the kzb Player. |
#### Examples


```
# Export the kzb files of the main project and loaded referenced projects to the C:\Temp\MyProject\ directory,
# preprocess the images, and export the project as kzb Player for Windows.
ExportAllProjectBinaries "C:\Temp\MyProject\" true true

```

### ExportBakedThemeBinaries


Export a kzb file for each combination of theme groups and main localization table that have the Export Baked Usages property enabled.
#### Syntax


`ExportBakedThemeBinaries`
#### Examples


```
# Export baked themes.
ExportBakedThemeBinaries

```

### ExportBinary


Export kzb files for use with the Kanzi Engine API and kzb resource packs for locales and themes according to their settings.
#### Syntax


`ExportBinary exportThemesAndLocaleResourcesSeparately exportXml`
#### Parameters

|

`exportThemesAndLocaleResourcesSeparately` |

Whether Kanzi Studio exports the theme and locale resources to separate kzb files. |
|

`exportXml` |

Whether Kanzi Studio exports kza file, which is the XML version of the kzb file. |
#### Examples


```
# Export the kzb file, theme and locale resources, and the kza file to the location set in the Project > Properties in the Binary Export Directory property.
ExportBinary true true

```

#### Syntax


`ExportBinary fileName`
#### Parameters

|

`fileName` |

The name of the kzb file. |
#### Examples


```
# Export the kzb file to the C:\Temp\project.kzb file.
ExportBinary C:\Temp\project.kzb

```

### ExportBinaryWithApplication


Export the project as a standalone Windows application using the kzb Player and kzb file.
#### Syntax


`ExportBinaryWithApplication`
### ExportDescriptions


Export the content of all Description properties in the project to a plain text file.
#### Syntax


`ExportDescriptions root outputFile`
#### Parameters

|

`root` |

(Optional) The root node of the node tree the descriptions of which you export. If you do not set this parameter, Kanzi Studio exports the descriptions of all items in the project. |
|

`outputFile` |

The file to which you export the descriptions. |
#### Examples


```
# Export the project documentation to the plain text file C:\Temp\Descriptions.txt.
# The file includes the name, path, and description of items that have the Description property.
ExportDescriptions "C:\Temp\Descriptions.txt"

```


```
# Export the descriptions of the RootNode > Viewport 2D > Scene node and its descendants
# to the plain text file C:\Temp\Descriptions.txt.
ExportDescriptions "/Screens/Screen/RootNode/Viewport 2D/Scene" "C:\Temp\Descriptions.txt"

```

### ExportProjectItems


Export selected project item(s) and their dependencies as a project archive (.kzexport).
#### Syntax


`ExportProjectItems itemToExport`
#### Parameters

|

`itemToExport` |

The project item to export. |
#### Examples


```
runTest: false

```

### ImportProject


Import another Kanzi Studio project to the active project.
#### Syntax


`ImportProject importProjectPath`
#### Parameters

|

`importProjectPath` |

Full path name of the Kanzi Studio project file that you import. |
#### Examples


```
# Import the Kanzi Studio project C:\KanziWorkspace\Projects\My Project\My Project.proj.kzm.
ImportProject "C:\KanziWorkspace\Projects\My Project\My Project.proj.kzm"

```

### ImportProjectItems


Import project item(s) and their dependencies from an exported project archive(.kzexport).
#### Syntax


`ImportProjectItems archiveToImport`
#### Parameters

|

`archiveToImport` |

The path to the archive to import. |
#### Examples


```
runTest: false

```

### LoadMaterialType


(Deprecated) Load material type from disk. Use export and import project items instead.
#### Syntax


`LoadMaterialType loadPath`
#### Parameters

|

`loadPath` |

The path to the kzmat file you load. |
#### Examples


```
# Load the C:\Program Files\Rightware\Kanzi\Studio\Asset Library\MaterialTypes\VertexPhong\Postprocessing\PostprocessingBoxBlur.kzmat file.
# Kanzi Studio adds to the Library > Materials and Textures > Material Types the PostprocessingBoxBlur material type and
# creates the PostprocessingBoxBlurMaterial material which uses the PostprocessingBoxBlur material type.
LoadMaterialType "C:\Program Files\Rightware\Kanzi\Studio\Asset Library\MaterialTypes\VertexPhong\Postprocessing\PostprocessingBoxBlur.kzmat"

```

### LoadProject


Open a project from disk.
#### Syntax


`LoadProject path`
#### Parameters

|

`path` |

The project that you open. |
#### Examples


```
# Open the C:\KanziWorkspace\Projects\MyProject\Tool_project\MyProject.proj.kzm project.
LoadProject "C:\KanziWorkspace\Projects\MyProject\Tool_project\MyProject.proj.kzm"

```

### NewProject


Create a Kanzi Studio project.
#### Syntax


`NewProject projectDirectory projectName`
#### Parameters

|

`projectDirectory` |

The directory where to create the project. |
|

`projectName` |

The name of the project. |
#### Examples


```
# Create a new Kanzi Studio project named MyProject in C:\KanziWorkspace\Projects\MyProject\Tool_project\.
NewProject "C:\KanziWorkspace\Projects\MyProject\Tool_project\" "MyProject"

```

### SaveProject


Save the project to disk.
#### Syntax


`SaveProject saveDirectory continueWorkingInOldPath`
#### Parameters

|

`saveDirectory` |

The directory in which to save the project. |
|

`continueWorkingInOldPath` |

Whether Kanzi Studio continues working in the directory where you opened the project. When you want to save a copy of a project but continue working with the original copy, set this to true. |
#### Examples


```
# Save the current project to C:\KanziWorkspace\Projects\MyProject\Tool_project\.
SaveProject "C:\KanziWorkspace\Projects\MyProject\Tool_project\" false

```

#### Syntax


`SaveProject`
#### Examples


```
# Save the current project to its current path.
SaveProject

```

## Building

### ExportApk


Build and deploy an Android Package (APK) using the build configuration set in Project > Properties > Building > Default Build Configuration.
#### Syntax


`ExportApk buildConfiguration compressImages`
#### Parameters

|

`buildConfiguration` |

The build configuration to use when building the Android Package (APK). |
|

`compressImages` |

Whether to preprocess the images in the project. |
#### Examples


```
# Build the APK file using the Library > Build Configurations > MyProject application configuration.
# If the project contains images that use texture compression, compress these images.
ExportApk "/Resource Files/Build Configurations/MyProject" true

```

## Preview

### StartPreview


Start the Preview.
#### Syntax


`StartPreview`
#### Examples


```
# Start the Preview.
StartPreview

```

## General

### Plugin


Execute commands defined in Kanzi Studio plugins.
#### Syntax


`Plugin pluginCommandName projectItem`
#### Parameters

|

`pluginCommandName` |

The internal name of the plugin command. |
|

`projectItem` |

(Optional) The project item from the context menu of which you want to run the plugin command. |
#### Examples


```
# Execute the Kanzi Studio plugin command named MyPluginCommand.
Plugin "MyPluginCommand"

```


```
# Execute the Kanzi Studio plugin command named MyPluginCommand from the context menu of the RootNode node.
Plugin "MyPluginCommand" "/Screens/Screen/RootNode"

```
