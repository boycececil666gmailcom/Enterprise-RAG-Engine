---
title: Empty Node 3D
source: https://docs.kanzi.com/4.1.0/en/reference/node-and-resource-reference/empty-node-3d-reference.html
---

# Empty Node 3D

## Empty Node 3D properties

Name |

Description |

Inherited |

Exported to Kanzi Engine |

Tags |

List of tags attached to the item |

No |

No |

Effective Data Context |

The data context in the current node that is resolved from data context properties and bindings |

No |

No |
## Empty Node 3D available properties

Name |

Description |

Inherited |

Exported to Kanzi Engine |

2D to 3D Projection Scale |

Sets the scale factor to project pixels to 3D size. When scale is 1, then the size of one pixel is one 3D space unit. |

No |

Yes |

A |

Tonemapping parameter A. |

No |

Yes |

Active Activity Index |

The index of the active Activity in the Data-Driven Exclusive Activity Host. After instantiating all Activity from a Data Source, this property refers to the only currently active Activity in this Data-Driven Exclusive Activity Host. To deactivate all the Activities in this Data-Driven Exclusive Activity Host, set this property to -1. |

No |

Yes |

Activity Source |

The data object that provides the data for this Activity node. |

No |

Yes |

Activity Status |

Sets the possible states of the Activity when its Activity Host activates or deactivates that Activity. |

No |

Yes |

Activity Template |

If set, the Data-Driven Exclusive Activity Host uses this prefab for Activity nodes that it creates. |

No |

Yes |

Actual Layout Depth |

The calculated size of the node in depth direction when used in a layout. |

No |

Yes |

Actual Layout Height |

The calculated height of the node when used in a layout. |

No |

Yes |

Actual Layout Width |

The calculated width of the node when used in a layout. |

No |

Yes |

Alpha Cutoff |

Sets the cutoff threshold for alpha cutting. If the alpha value is less than the value of this property, Kanzi discards the fragment. The default value is 0.5. |

No |

Yes |

Ambient Color |

Sets the color of the material when lights are not present. Use the Intensity (I) property field to adjust the exposure of the color. |

No |

Yes |

Ambient Occlusion Blur Direction |

Blur direction of the ambient occlusion bilateral blur. |

No |

Yes |

Ambient Occlusion Focal Length |

HBAO input property for focal length. |

No |

Yes |

Ambient Occlusion LinMAD |

HBAO input property for LinMAD uniform. |

No |

Yes |

Ambient Occlusion Radius |

Screen-space ambient occlusion (SSAO) effect radius. Used to calculate the SSAO texture. |

No |

Yes |

Ambient Occlusion Strength |

Screen-space ambient occlusion (SSAO) strength. Used to calculate the SSAO texture. |

No |

Yes |

Ambient Occlusion UV to View A |

HBAO input property for UVToViewA uniform. |

No |

Yes |

Ambient Occlusion UV to View B |

HBAO input property for UVToViewB uniform. |

No |

Yes |

Amount |

Sets the chromatic aberration amount. |

No |

Yes |

Auto Press Interval |

Sets the time in milliseconds after which a button that the user keeps pressed down sends the Button: Click message. While the user holds the button down, the button keeps sending the Button: Click message at the time interval set by this property. To disable the behavior, set to 0. |

No |

Yes |

B |

Tonemapping parameter B. |

No |

Yes |

Base Color Factor |

Sets the base color for the material. |

No |

Yes |

Base Color Texture |

Sets the texture that contains the base color for the material. Use the Base Color Factor property to filter the value from this texture. |

No |

Yes |

Baseline |

Font baseline in 3D space units. |

No |

Yes |

Blend Intensity |

Controls the intensity of materials that are blended on top of an existing color. Attached property enables overriding of the blend intensity of the used materials at render pass or object node level. |

No |

Yes |

Blend Mode |

Sets how to combine the color and alpha values of pixels in one layer or image with those in the underlying layer or image. |

No |

Yes |

Bloom Intensity |

Bloom intensity for the material. |

No |

Yes |

Bloom Intensity Texture |

Sets the bloom intensity texture. |

No |

Yes |

Bloom Radius |

Bloom radius for the material. |

No |

Yes |

Blur Direction |

Sets the direction for the blur. |

No |

Yes |

Blur Radius |

Blur radius for the material. |

No |

Yes |

Bottom Image |

The image to use in middle of the bottom row. |

No |

Yes |

Bottom-Left Image |

Image to use in the bottom-left corner. |

No |

Yes |

Bottom-Right Image |

The image to use in the bottom-right corner. |

No |

Yes |

BRDF Lookup Table |

Gets the Bidirectional Reflectance Distribution Function (BRDF) lookup table for the material. The BRDF table is a texture that contains precomputed information about how light reflects off a material. You can use it to improve rendering quality. |

No |

Yes |

Bring Activated Activity To Front |

Sets whether to show the activated Activity in front within its Parallel Activity Host. This property affects the z-order of the activated Activity within the same Activity priority layer: * When enabled, the Activity is shown in front. * When disabled, the z-order of the activated child Activity is determined by the order in which you added that Activity to the parent Parallel Activity Host. This is the default behavior. |

No |

Yes |

Brush Color |

Color for brush. Set alpha to 0 to disable brush. |

No |

Yes |

Brush Horizontal Tiling |

Horizontal Tiling for the brush. Affects the scale of texture coordinates. |

No |

Yes |

Brush Modulate Color |

Modulation color for brush. Effects brush rendering that needs color modulation. |

No |

Yes |

Brush Texture |

Texture for brush. |

No |

Yes |

Brush Vertical Tiling |

Vertical Tiling for the brush. Affects the scale of texture coordinates. |

No |

Yes |

C |

Tonemapping parameter C. |

No |

Yes |

Calculated Offset |

Reports the current relative offset of an item in the Grid List Box in proportional range [0, 1]. |

No |

Yes |

Calculated Offset |

Reports the current offset of an item in a Trajectory Layout in the proportional range [0, 1]. |

No |

Yes |

Center Image |

The image to use in the center. |

No |

Yes |

Character Spacing |

Sets the character spacing in pixels. |

No |

Yes |

Clear Coat Normal Scale |

Sets the clear coat normal scale for the material. Use the scale to set the intensity of the Clear Coat Normal Texture. |

No |

Yes |

Clear Coat Normal Texture |

Sets the texture that contains a clear coat normal map for the material. Use the Clear Coat Normal Scale property to scale the texture value. |

No |

Yes |

Clear Coat Roughness Factor |

Sets the roughness of the outer clear coat layer for the material: 0 represents a smooth, glossy surface, and 1 represents a rough, diffuse surface. |

No |

Yes |

Clear Coat Roughness Texture |

Sets the texture that contains a clear coat roughness map for the material. Kanzi reads the roughness from the Green channel of the texture. Use the Clear Coat Roughness Factor property to scale the roughness from this texture. |

No |

Yes |

Clear Coat Strength Factor |

Sets the clear coat strength for the material: 0 represents a material with no clear coat, and 1 represents a full strength clear coat. |

No |

Yes |

Clear Coat Strength Texture |

Sets the texture that contains a clear coat strength map for the material. Kanzi reads the strength from the Red channel of the texture. Use the Clear Coat Strength Factor property to scale the strength from this texture. |

No |

Yes |

Clip Children |

Sets whether to clip the child nodes of this node. Kanzi clips the child nodes whose bounding box is completely outside of the bounding box of their parent node. Use this property with layout nodes. The child nodes can use only translation transformation. |

No |

Yes |

Code Behind Source |

Sets the metaclass name of the code behind class for this node. |

No |

Yes |

Color Font Material |

Sets the material whose shader is used to render the text containing colored glyphs. The shader must use the ContentTexture uniform which is automatically filled with glyph data. |

No |

Yes |

Column |

The column into which grid layout places the item. |

No |

Yes |

Column Span |

Defines the number of columns an item in a grid layout occupies. |

No |

Yes |

Command |

The command executed by a UI control |

No |

Yes |

Constraint In World Coordinates |

Specifies if the object constraining is done in world coordinates (when false, done in local coordinates). |

No |

Yes |

Constraint Orientation |

Makes an object node where the property is attached to obtain orientation from target object |

No |

Yes |

Constraint Position |

Makes an object node where the property is attached to obtain position from target object |

No |

Yes |

Controller Property |

Sets the property type that the Exclusive Activity Host node uses to switch between its child Activity nodes. |

No |

Yes |

Cubemap Texture |

Sets the cubemap texture you want the Blit render pass to blit. |

No |

Yes |

Custom Asset Thumbnail |

When enabled, the asset will have selected image as thumbnail instead of the generated one. |

No |

No |

Cyclic Focus Navigation |

Sets whether the focus chain navigation within the focus scope is cyclic. When you enable this property: * When the user navigates in the forward direction and the focus reaches the last focusable UI element of the focus scope, the focus navigation moves to the first focusable UI element. * When the user navigates in the backward direction and the focus reaches the first focusable UI element of the focus scope, the focus navigation moves to the last focusable UI element. |

No |

Yes |

D |

Tonemapping parameter D. |

No |

Yes |

Data Context |

Source of data for this node and its descendants |

No |

Yes |

Data Source Controller Property Path |

Sets the path in the Data Source object of an Exclusive Activity Host node to a Data Object item that the Exclusive Activity Host node uses as the Controller Property. |

No |

Yes |

Depth Alignment |

The alignment in depth direction the node should use when it resides under a layout. |

No |

Yes |

Depth Margin |

Sets the depth distance between this node and other nodes that are adjacent to this node in a layout.

To access the Depth Margin property fields in a binding, use: * X for the **Back** property field * Y for the **Front** property field  |

No |

Yes |

Description |

Add a description of the purpose of this item. To export descriptions to a plain text file, select File > Export > Export Descriptions. When you export the kzb file, this description is not included in the exported file. |

No |

No |

Detail Base Color Factor |

Sets the detail base color for the material. The detail base color is alpha blended with the standard base color. |

No |

Yes |

Detail Base Color Texture |

Sets the detail texture that contains the base color for the material. Use the Detail Base Color Factor property to filter the value from this texture. The detail base color is alpha blended with the standard base color. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |

Detail Clear Coat Normal Scale |

Sets the detail clear coat normal scale for the material. Use the scale to set the intensity of the Detail Clear Coat Normal Texture. |

No |

Yes |

Detail Clear Coat Normal Texture |

Sets the detail texture that contains a clear coat normal map for the material. Use the Detail Clear Coat Normal Scale property to scale the texture value. |

No |

Yes |

Detail Clear Coat Roughness Texture |

Sets the detail texture that contains a clear coat roughness map for the material. Use the Clear Coat Roughness Factor and Clear Coat Roughness Texture properties to scale the roughness from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |

Detail Clear Coat Strength Texture |

Sets the detail texture that contains a clear coat strength map for the material. Kanzi reads the strength from the Red channel of the texture. Use the Clear Coat Strength Factor and Clear Coat Strength Texture properties to scale the strength from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |

Detail Diffuse Color Factor |

Sets the detail diffuse color for the material. Kanzi alpha blends the detail diffuse color with the standard diffuse color. |

No |

Yes |

Detail Diffuse Color Texture |

Sets the detail texture that contains the diffuse color for the material. Use the Detail Diffuse Color Factor property to filter the value from this texture. Kanzi alpha blends the detail diffuse color with the standard diffuse color. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |

Detail Emissive Factor |

Sets the color of the light that is emitted from a detail texture for the material. Use the Intensity (I) property field to adjust the brightness of the light. This color affects the local material rendering, but the light is not cast to other objects. The detail emissive light is alpha blended with the standard emissive light. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |

Detail Emissive Texture |

Sets the detail texture that contains the light emitted from the material. Use the Detail Emissive Factor property to scale the value from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |

Detail Glossiness Texture |

Sets the detail texture that contains a glossiness map for the material. Kanzi reads the glossiness from the Alpha channel of this texture. Use the Glossiness Factor and Glossiness Texture properties to scale the glossiness from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |

Detail Metallic Texture |

Sets the detail texture that contains a metallic map for the material. Kanzi reads the metalness from the Blue channel of this texture. Use the Metallic Factor and Metallic Texture properties to scale the metalness from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |

Detail Normal Scale |

Sets the detail normal scale for the material. Use the scale to set the intensity of the Detail Normal Texture. |

No |

Yes |

Detail Normal Texture |

Sets the detail texture that contains a normal map for the material. Use the Detail Normal Scale property to scale the texture value. |

No |

Yes |

Detail Occlusion Strength |

Sets the detail occlusion strength for the material. Use the strength to set the intensity of the Detail Occlusion Texture. |

No |

Yes |

Detail Occlusion Texture |

Sets the detail texture that contains an occlusion map for the material. Kanzi reads the occlusion from the Red channel of this texture. Use the Detail Occlusion Strength property to scale the occlusion from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |

Detail Roughness Texture |

Sets the detail texture that contains a roughness map for the material. Kanzi reads the roughness from the Green channel of the texture. Use the Roughness Factor and Roughness Texture properties to scale the roughness from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |

Detail Specular Color Factor |

Sets the detail specular color for the material. Kanzi alpha blends the detail specular color with the standard specular color. |

No |

Yes |

Detail Specular Color Texture |

Sets the detail texture that contains the specular color for the material. Use the Detail Specular Color Factor property to filter the value from this texture. Kanzi alpha blends the detail specular color with the standard specular color. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |

Detail Texture Offset |

Sets the detail texture offset for the material. Kanzi adds this value to the UVs to produce a second set of detail UVs to use for all detail texture properties. |

No |

Yes |

Detail Texture Tiling |

Sets the detail texture tiling factor for the material. Kanzi multiplies this value by the UVs to produce a second set of detail UVs to use for all detail texture properties. |

No |

Yes |

Diffuse Color |

Sets the color of the material when it is lit by a light. |

No |

Yes |

Diffuse Color Factor |

Sets the diffuse color for the material. |

No |

Yes |

Diffuse Color Texture |

Sets the texture that contains the diffuse color for the material. Use the Diffuse Color Factor property to filter the value from this texture. |

No |

Yes |

Directional Light View Projection |

The premultiplied projection view matrix of a directional light. |

No |

Yes |

Directional Shadow Map |

Depth map used to calculate directional shadows. |

No |

Yes |

Disable KZB Export |

Disables the exporting of the item into KZB. Can be used for, e.g. letting items out from certain profiles. The disabled items are always included in preview. |

No |

No |

Dithering Amount |

Sets the chromatic aberration dithering amount. |

No |

Yes |

Down On Hover |

Whether holding a finger on the device screen and moving it over the button transitions the button to the down state. |

No |

Yes |

Drawn as Bounding Box |

When enabled the object is drawn its solid bounding box. |

No |

Yes |

E |

Tonemapping parameter E. |

No |

Yes |

Effectively Enabled |

Indicates whether this node and its ancestor nodes are enabled. Use this property in state managers and bindings to observe whether a node is effectively enabled. To enable or disable a node, use the Enabled property. When a node is effectively disabled: * When that node is focused, it receives key input until the focus moves to another node. * When that node is not focused, it is not part of the focus chain and does not receive key input. |

No |

Yes |

Emissive Color |

Sets the color of the light that is emitted from the material surface. |

No |

Yes |

Emissive Factor |

Sets the color of the light that is emitted from the material. Use the Intensity (I) property field to adjust the brightness of the light. This color affects the local material rendering, but the light is not cast to other objects. |

No |

Yes |

Emissive Texture |

Sets the texture that contains the light emitted from the material. Use the Emissive Factor property to scale the value from this texture. |

No |

Yes |

Enabled |

Whether this node is enabled. When you disable this property in a node, that node and its descendant nodes in the same overlay focus scope are effectively disabled. Effectively disabling a node removes that node from the focus chain and cancels all the active input manipulators.Use the Effectively Enabled property to observe whether a node is effectively enabled. |

No |

Yes |

Environment Ambient Factor |

Sets the strength of the cubemap texture to use for ambient environment light. Use the Environment Ambient Texture property to set the cubemap texture. The ambient environment light affects diffuse lighting in image based lighting. |

No |

Yes |

Environment Ambient Texture |

Sets the cubemap to use for the ambient environment light for the material. This cubemap affects the diffuse lighting during image based lighting. Use the Environment Ambient Factor property to set the strength of the cubemap texture. |

No |

Yes |

Environment Reflection Factor |

Sets the strength of the cubemap texture to use for specular environment light. Use the Environment Reflection Texture property to set the cubemap texture. The specular environment light affects reflective lighting in image based lighting. |

No |

Yes |

Environment Reflection Texture |

Sets the cubemap to use for the specular environment light for the material. This cubemap affects reflective lighting during image based lighting. Use the Environment Reflection Factor property to set the strength of the cubemap texture. |

No |

Yes |

Export in Asset Package |

When enabled, this item is exported into asset package if this project is saved as one. |

No |

No |

Exposure |

Sets the exposure compensation for the material. The exposure compensation emulates camera exposure by controlling the total amount of light rendered. Use a negative value to darken the rendered image, and a positive value to lighten the image. Exposure is exponential: 1.0 is twice as bright as 0.0, and -1.0 is half as bright as 0.0. |

No |

Yes |

F |

Tonemapping parameter F. |

No |

Yes |

Face to Camera Mode |

Sets how to rotate the 3D node towards a camera: * **Disabled** does not make the node turn to the camera. * **Look at** rotates the node along all axes to turn to the camera. * **Billboarding** keeps the node perpendicular to the camera FOV. * **Cylindrical** rotates the node along the y axis to turn to the camera.

By default, the node turns to the Scene default camera. To use a different camera, set the **Face to Camera Target Camera** property.  |

No |

Yes |

Face to Camera Target Camera |

Sets the camera towards which the 3D node turns when you set the **Face to Camera Mode** property. The default is the Scene default camera. |

No |

Yes |

Final Transformation |

The combined location, orientation and scale of the node and its ancestor nodes. Automatically calculated by the system. |

No |

Yes |

Fixed Character Width |

When set, overrides the font advance widths to make each character take a fixed amount of space specified in pixels. |

No |

Yes |

Focus On Press |

Sets where to set the focus when the user presses the node that has this property: * **None** (0) keeps the focus where it was. This is the default. * **Node** (1) sets the focus to the node. * **Node or ancestor** (2) sets the focus to the node or, if that fails, to the closest focusable ancestor node. * **Node or overlay** (3) sets the focus to the node or, if that fails, to the closest ancestor overlay scope, which then forwards the focus according to its settings.

The descendants of the node where you set this property inherit value of the property.  |

No |

Yes |

Focus Order |

Sets the focus chain order of the node within the focus scope. |

No |

Yes |

Focus Scope Type |

Sets the type of the focus scope node: * **Group** groups focusable nodes. * **Fence** keeps the focus chain navigation inside the scope and does not allow the focus chain navigation to enter or leave that scope. * **Modal** overlay blocks the key and touch input that originates outside of its boundaries and keeps the focus navigation within the scope boundaries. * **Auto-Closing Modal** overlay loses focus when key or touch input originates from a node that is outside of its node tree, and suppresses that input. * **Modeless** overlay propagates the key and touch input that originates outside of its boundaries to the nodes outside of its boundaries. * **Auto-Closing Modeless** overlay loses focus when key or touch input originates from a node that is outside of its boundaries, and propagates that input. |

No |

Yes |

Focus State |

Reports the focus state of a node: * **No focus** (0) indicates that the node is not focused. For a focus scope node indicates that none of the nodes in the scope have focus. * **Logical focus** (1) indicates that the node is the logical focus node of an overlay-type focus scope. For a focus scope node indicates that one of the nodes in that scope is the logical focus node. * **Key focus** (2) indicates that the node is the key focus node of the application and receives key input. For a focus scope node indicates that one of the nodes in that scope is the key focus node.

Use this property in state managers and bindings to implement focus states in the UI nodes.

To observe whether a node is the key focus node, you can use the boolean **Focus** > **Focused** property.  |

No |

Yes |

Focusable |

Indicates whether the node can receive focus. |

No |

Yes |

Focused |

Indicates whether the node has the key focus. |

No |

Yes |

Font Color |

Sets the color of the text in a 3D text node. |

No |

Yes |

Font Family |

The font family used to render the text. |

No |

Yes |

Font Hinting Preference |

Sets the hinting preference of the font. * **No hinting**: Render text without hinting the outlines of glyphs. * **Native hinting**: Prefer native hinter of the font over the auto-hinter of the rasterizer. * **Auto hinting**: Prefer auto-hinter of the rasterizer over the native hinter of the font. |

No |

Yes |

Font Material |

Sets the material whose shader is used to render the text. The shader must use the ContentTexture uniform which is automatically filled with glyph data. |

No |

Yes |

Font Size |

Sets the size of the font in pixels. |

No |

Yes |

Font Style |

Sets the style of the font. |

No |

Yes |

Font Weight |

Sets the weight of the font. |

No |

Yes |

Fractional Character Width |

Sets whether Kanzi uses fractional or rounded character widths to lay out text. In most cases fractional widths provide the best result. However, with small font sizes, fractional widths can cause the characters to run together or have too much space, making it difficult to read. * When enabled, Kanzi uses fractional character widths, which means that the spacing between characters varies and can be a fraction of a pixel. * When disabled, Kanzi uses character widths rounded to the nearest pixel. Disable fractional widths when you want to fix character spacing in whole-pixel increments and prevent characters in small font sizes from running together. |

No |

Yes |

Frustum Cull Margin |

The margin of the frustum cull radius of the node. For example, set the margin when a vertex shader modifies the geometry of the node. To use this property, enable the Frustum Culling property in the Draw Objects Render Pass you use to render the node. |

No |

Yes |

Global Ambient Color |

Sets the color that is multiplied automatically with the Ambient property of the materials in the scene. Use the Intensity (I) property field to adjust the exposure of the color. |

No |

Yes |

Glossiness Factor |

Sets the glossiness of the material: 0 represents a rough, diffuse surface, and 1 represents a smooth, glossy surface. |

No |

Yes |

Glossiness Texture |

Sets the texture that contains a glossiness map for the material. Kanzi reads the glossiness from the Alpha channel of this texture. Use the Glossiness Factor property to scale the glossiness from this texture. |

No |

Yes |

Grading Color Highlight |

Sets the color grading highlight color. |

No |

Yes |

Grading Color Midtone |

Sets the color grading midtone color. |

No |

Yes |

Grading Color Shadow |

Sets the color grading shadow color. |

No |

Yes |

Grading Highlight Range |

Sets the luminance range where the highlight color is applied. |

No |

Yes |

Grading Hue Saturation Value |

Sets the HSV adjustment for the input color. |

No |

Yes |

Grading Shadow Range |

Sets the luminance range where the shadow color is applied. |

No |

Yes |

Hit Testable |

When enabled, the node can be hit tested. Enabling Hit Testable for a 2D node enables hit testing only for that node. Enabling Hit Testable for a 3D node enables hit testing also for the child nodes. Kanzi hit tests 3D nodes using the default Camera node or the Hit Test Camera node of the active Scene node. |

No |

Yes |

Hit Testable Container |

When enabled, Kanzi uses the layout bounds as geometry for hit testing. |

No |

Yes |

Hold Interval |

Sets the amount of time in milliseconds that the user must hold the button pressed down for Kanzi to recognize it as a long-press gesture. To disable the long-press gesture, set to 0. |

No |

Yes |

Horizontal Alignment |

The alignment in horizontal direction the node should use when it resides under a layout. |

No |

Yes |

Horizontal Fit |

Whether to horizontally scale the glyphs to make them fit into the **Layout Width** of the Text Block. To adjust the scale, use the **Horizontal Fit Scale Limits** property. |

No |

Yes |

Horizontal Fit Scale Limits |

When the **Horizontal Fit** property is enabled, sets the minimum and maximum scale for glyphs when the width of text in a Text Block does not match the **Layout Width** of that Text Block. For example: * **Min** property field set to 1.0 does not squeeze the glyphs, while 0.5 squeezes the glyphs to half their size. * **Max** property field set to 1.0 does not stretch the glyphs, while 2.0 stretches the glyphs to double their size. |

No |

Yes |

Horizontal Margin |

Sets the horizontal space between this node and other nodes that are adjacent to this node in a layout.

To access the Horizontal Margin property fields in a binding, use: * X for the **Left** property field * Y for the **Right** property field  |

No |

Yes |

Horizontal Padding |

Sets the padding spaces between the content and the left and right boundaries of the Text node. |

No |

Yes |

Hover |

Indicates whether a node is the foremost hit testable node under the cursor. |

No |

Yes |

Index In Group |

Sets the index of the Toggle Button in the Toggle Button Group to which that Toggle Button is registered. If a Toggle Button does not have a local value for this property, it is not registered to the ancestor Toggle Button Group. When set to -1, the Toggle Button Group assigns an index for the Toggle Button. |

No |

Yes |

Inner Distance |

Sets the distnace range where the vignette color transition starts. |

No |

Yes |

Is Down |

Indicates whether the button is pressed and in the down state. |

No |

Yes |

Is Value Changing |

Whether the value is currently changing. |

No |

Yes |

Item Index |

Reports the index of the item in the List Box Item Container. |

No |

Yes |

Layout Depth |

The size of the node in depth direction when used in a layout. Overrides the default bounds of the item. |

No |

Yes |

Layout Height |

The height of the node when used in a layout. Overrides the default bounds of the item. |

No |

Yes |

Layout Transformation |

The location, orientation and scale of the node relative to its parent node. Layout Transformation affects the layout. If you do not want to affect the layout, use Render Transformation. |

No |

Yes |

Layout Width |

The width of the node when used in a layout. Overrides the default bounds of the item. |

No |

Yes |

Left Image |

The image to use in the center-left. |

No |

Yes |

Line Spacing |

Sets the line spacing in multiples of the normal line height of the selected font. |

No |

Yes |

Look At |

Makes a node to always face the node set in this property. |

No |

Yes |

Mask Texture |

Sets the texture that masks another texture or color. |

No |

Yes |

Mask Texture Offset |

Sets an offset for mask in materials. |

No |

Yes |

Mask Texture Tiling |

Determines the number of times a mask is presented in a material |

No |

Yes |

Maximum Distance From Curve |

The distance from the curve where hit testing succeeds. |

No |

Yes |

Maximum Value |

The maximum value that the range allows. |

No |

Yes |

Metallic Factor |

Sets the metalness of the material: 0 represents a non-metallic or dielectric object, and 1 represents a metallic object. |

No |

Yes |

Metallic Texture |

Sets the texture that contains a metallic map for the material. Kanzi reads the metalness from the Blue channel of this texture. Use the Metallic Factor property to scale the value from this texture. |

No |

Yes |

Minimum Value |

The minimum value that the range allows. |

No |

Yes |

Morph Data Texture |

Data texture to use for storing morph data when the are are too many targets to use regular attribute channels. |

No |

Yes |

Morphing |

Add morph weights to Model3D to enable Morphing. |

No |

Yes |

Node.Path |

Full path to the node. |

No |

Yes |

Normal Scale |

Sets the normal scale for the material. Use the scale to set the intensity of the Normal Texture. |

No |

Yes |

Normal Texture |

Sets the texture that contains a normal map for the material. Use the Normal Scale property to scale the texture value. |

No |

Yes |

Normalized Value |

The current value normalized to range [0, 1]. |

No |

Yes |

Occlusion Render Strength |

Sets the SSAO strength for the material. Use the strength to set the intensity of the SSAO Texture. |

No |

Yes |

Occlusion Render Texture |

Sets the texture that contains a SSAO computed for the scene. Use the Occlusion Render Strength property to scale the strength of the SSAO. |

No |

Yes |

Occlusion Strength |

Sets the occlusion strength for the material. Use the strength to set the intensity of the Occlusion Texture. |

No |

Yes |

Occlusion Texture |

Sets the texture that contains an occlusion map for the material. Use the Occlusion Strength property to scale the occlusion from the texture. |

No |

Yes |

Opacity |

Opacity of the node. |

No |

Yes |

Outer Color |

Sets the vignette color. |

No |

Yes |

Outer Distance |

Sets the distnace range where the vignette color transition ends. |

No |

Yes |

Overflow |

Sets the characters that represent the truncated text when the text does not fit in this node. The default value is ââ¦â. By default, Kanzi truncates the text at the end. Use the **Truncation Direction** property to set the part of the text that you want to truncate.

Kanzi truncates text to fit within the vertical and horizontal limits of the control. If there is not enough vertical space to fit a single line of text, Kanzi truncates all text and does not show the **Overflow** characters.  |

No |

Yes |

Override Material |

Sets the override material to use to render the content of the 2D prefab in the Viewport 3D node. In the Viewport 3D node, bind a texture property of the override material to the Viewport3D.PrefabTexture property. |

No |

Yes |

Planar Reflection Map |

Rendered texture for planar reflections. |

No |

Yes |

Planar Reflection View Projection |

The premultiplied projection view matrix for planar reflections. |

No |

Yes |

Point Shadow Map |

Depth cubemap used to calculate point light shadows. |

No |

Yes |

Point Shadow Near Far |

Sets the near & far values used for point shadow calculations. |

No |

Yes |

Prefab Template |

Sets the 2D prefab whose content the Viewport 3D node renders in 3D space. |

No |

Yes |

Previous Final Transformation |

Final transformation (world matrix) from the previous frame, used for velocity buffer calculation. |

No |

Yes |

Remove Side Bearings |

Whether to position the leftmost characters of left-aligned text and rightmost characters of right-aligned text exactly within the boundary of the text node. |

No |

Yes |

Render Transformation |

The location, orientation, and scale of the node relative to its parent node. Render transformation does not affect the layout of the node. |

No |

Yes |

Right Image |

The image to use in the center-right. |

No |

Yes |

Roughness Factor |

Sets the roughness of the material: 0 represents a smooth, glossy surface, and 1 represents a rough, diffuse surface. |

No |

Yes |

Roughness Texture |

Sets the texture that contains a roughness map for the material. Kanzi reads the roughness from the Green channel of the texture. Use the Roughness Factor property to scale the roughness from this texture. |

No |

Yes |

Row |

The row into which grid layout places the item. |

No |

Yes |

Row Span |

Defines the number of rows an item in a grid layout occupies. |

No |

Yes |

Selected |

Indicates whether the List Box item held by this List Box Item Container is selected. The List Box sets the value of this property. |

No |

Yes |

Selected Item Index |

Sets the index of the item that is currently selected in the List Box node. A List Box node updates this property when the user scrolls that List Box node. To select an item in the List Box node, set this property to the index of the item that you want to select. The indexing starts from 0. To update this property with a binding, use a to-source or two-way binding. |

No |

Yes |

Show Material Debug Objects |

When enabled, Kanzi Studio does not hide material debug objects. |

No |

No |

Side |

The docking side of an item in the dock layout. |

No |

Yes |

Snap Character To Pixel |

Sets whether Kanzi positions characters in 2D rendering to the nearest pixel: * When enabled, text sharpness improves, but some characters can shift a fraction of a pixel. * When disabled, certain combinations of screen resolution, use of anti-aliasing, and font size can cause the text to appear blurry. In that case, you can improve the appearance of the text with the **Fractional Character Width** and **Character Spacing** properties. |

No |

Yes |

Specular Anti-Aliasing Strength |

Sets the strength of the specular anti-aliasing effect. Higher value results in blurrier specular highlights. For no specular anti-aliasing, set the value to 0. For full specular anti-aliasing, set the value to 1. The default value is 0.25. |

No |

Yes |

Specular Anti-Aliasing Threshold |

Sets the upper limit for the amount of specular anti-aliasing effect to apply. The default value is 0.18. |

No |

Yes |

Specular Color |

Sets the color of the specular reflection. |

No |

Yes |

Specular Color Factor |

Sets the specular color for the material. |

No |

Yes |

Specular Color Texture |

Sets the texture that contains the specular color for the material. Use the Specular Color Factor property to filter the value from this texture. |

No |

Yes |

Specular Exponent |

Sets the size of the specular highlight. |

No |

Yes |

Spot Light View Projection |

The premultiplied projection view matrix of a spot light. |

No |

Yes |

Spot Shadow Map |

Depth map used to calculate spot shadows. |

No |

Yes |

State Manager |

Sets the State Manager to the node. |

No |

Yes |

Step Value |

The minimum amount that the value of the range can change at a time. |

No |

Yes |

Stretch |

Whether to scale this Trajectory Layout to match the layout size. |

No |

Yes |

Style |

Sets a style to the node. |

No |

Yes |

Tags |

List of tags attached to the item |

No |

No |

Text |

Sets the text content that the text node renders. To create a line break press Shift+Enter. |

No |

Yes |

Text Horizontal Alignment |

Sets the horizontal alignment of the text. |

No |

Yes |

Text Vertical Alignment |

Sets the vertical alignment of the text. |

No |

Yes |

Texture |

Sets the texture of the material. |

No |

Yes |

Texture 0 |

Sets the first texture you want the Blit render pass to blit. |

No |

Yes |

Texture 1 |

Sets the second texture you want the Blit render pass to blit. |

No |

Yes |

Texture 2 |

Sets the third texture you want the Blit render pass to blit. |

No |

Yes |

Texture 3 |

Sets the fourth texture you want the Blit render pass to blit. |

No |

Yes |

Texture 4 |

Sets the fifth texture you want the Blit render pass to blit. |

No |

Yes |

Texture 5 |

Sets the sixth texture you want the Blit render pass to blit. |

No |

Yes |

Texture 6 |

Sets the seventh texture you want the Blit render pass to blit. |

No |

Yes |

Texture 7 |

Sets the eighth texture you want the Blit render pass to blit. |

No |

Yes |

Texture 8 |

Sets the ninth texture you want the Blit render pass to blit. |

No |

Yes |

Texture 9 |

Sets the tenth texture you want the Blit render pass to blit. |

No |

Yes |

Texture Offset |

Sets an offset for texture in materials. |

No |

Yes |

Texture Tiling |

Determines the number of times a texture is presented in a material. |

No |

Yes |

Toggle State |

Sets the toggle state of a Toggle Button. To update this property with a binding, use a to-source or two-way binding. |

No |

Yes |

Toggle State Count |

Sets the number of toggle states of a Toggle Button. |

No |

Yes |

Tone Map Linear Scale |

Sets the scale for the linear tonemap option for the material. When linear tonemapping is used, Kanzi divides all output color by the value of this property. |

No |

Yes |

Top Image |

The image to use in the middle of the top row. |

No |

Yes |

Top-Left Image |

The image to use in the top-left corner. |

No |

Yes |

Top-Right Image |

The image to use in the top-right corner. |

No |

Yes |

Trajectory Override Offset |

Sets the offset of an item in a Trajectory Layout. When you do not set this property, the Trajectory Layout sets the offset. |

No |

Yes |

Transition Phase |

The phase of the transition. For example, use for pixel-based effects. |

No |

Yes |

Truncation |

Sets how Kanzi truncates text when either **Truncation** or **Overflow** property is set and the text does not fit in this node: * **None** disables text truncation. * **At character** truncates text character by character. Default value. * **At word** truncates text by entire words.

Kanzi truncates text to fit within the vertical and horizontal limits of the control. If there is not enough vertical space to fit a single line of text, Kanzi truncates all text and does not show overflow characters.  |

No |

Yes |

Truncation Direction |

Sets which part Kanzi truncates when either the **Truncation** or **Overflow** property is set and the text does not fit in this node: * **Trailing** truncates single- and multiline text at the end. Default value. * **Center** truncates single-line text in the middle. For multiline text, truncates entire lines from the middle, if the text does not fit in the height of this node, and clips text that does not fit in the width of this node. * **Leading** truncates single-line text in the beginning. For multiline text, truncates entire lines from the beginning, if the text does not fit in the height of this node, and clips text that does not fit in the width of this node. |

No |

Yes |

Two Pass Rendering |

Defines whether the Text Block 3D is rendered in two passes. Disabling the two pass rendering improves performance, but can cause invalid rendering results when glyph bounds overlap. |

No |

Yes |

Use Intensity Texture |

Enable or disable the use of the Bloom Intensity texture property. |

No |

Yes |

Value |

The current value. To update this property with a binding, use a to-source or two-way binding. |

No |

Yes |

Vertical Alignment |

The alignment in vertical direction the node should use when it resides under a layout. |

No |

Yes |

Vertical Margin |

Sets the vertical space between this node and other nodes that are adjacent to this node in a layout.

To access the Vertical Margin property fields in a binding, use: * X for the **Bottom** property field * Y for the **Top** property field  |

No |

Yes |

Vertical Padding |

Sets the padding spaces between the content and the top and bottom boundaries of the Text node. |

No |

Yes |

Visible |

When disabled, Kanzi does not render the node. |

No |

Yes |

Visible Amount in Parent |

Sets the amount the node is inside its parent. Use the value of this property in shaders to implement fades. Calculated by the parent node. |

No |

Yes |

White Scale |

Sets the value that will be tonemapped to pure white. |

No |

Yes |

Word Wrap |

Sets whether to break long lines into multiple lines to make the text fit within the boundaries of the Text Block node. |

No |

Yes |
## Empty Node 3D messages

Name |

Description |

Inherited |

Exported to Kanzi Engine |

Activity Host: Activity Prefab Attached |

An Activity Host sends this message when it attaches the prefab of the Activity that is activated. |

No |

Yes |

Activity Host: Activity Prefab Detached |

An Activity Host sends this message when it detaches the prefab of the Activity that is deactivated. |

No |

Yes |

Activity: Activated |

An Activity sends this message when it is activated. |

No |

Yes |

Activity: Activating |

An Activity sends this message when it is in the activating state. |

No |

Yes |

Activity: Deactivated |

An Activity sends this message when it is deactivated. |

No |

Yes |

Activity: Deactivating |

An Activity sends this message when it is in the deactivating state. |

No |

Yes |

Activity: Status Changed |

An Activity sends this message when the value of its Activity Status property changes. |

No |

Yes |

Animation Player: Completed |

Occurs when an Animation Player completes animation playback. |

No |

Yes |

Animation Player: Started |

Occurs when an Animation Player starts animation playback. |

No |

Yes |

Animation Player: Stopped |

Occurs when an Animation Player stops animation playback. |

No |

Yes |

Button: Cancel |

Occurs when a user lifts their finger outside of a Button that they previously pressed. |

No |

Yes |

Button: Click |

Occurs when a user lifts their finger on top of a Button that they previously pressed and when the time set by the Auto Press Interval property in the pressed Button expires. |

No |

Yes |

Button: Down |

Occurs when the user presses down the Button. |

No |

Yes |

Button: Enter |

Button: Enter trigger is set off: * When the user presses down the button. * When the user presses down the button, moves the pointer outside of the button area, and then moves the pointer back to the button area while still holding down the pointer. |

No |

Yes |

Button: Leave |

Button: Leave trigger is set off: * When the user presses down the button and then lifts the pointer. * When the user presses down the button and then moves the pointer outside of the button area. * When the user sets off a **Button: Long Press** trigger. |

No |

Yes |

Button: Long Press |

Occurs when the user presses down a Button and holds the Button pressed for the amount of milliseconds defined in the Hold Interval property of that Button. |

No |

Yes |

Click: Begin |

Occurs when the user presses a hit-testable node with a Click Manipulator.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |

Click: Cancel |

Occurs when the user first presses a hit-testable node with a Click Manipulator, then moves the pointer outside of the node area, and lifts the pointer.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |

Click: Click |

Occurs when the user presses and releases a hit-testable node with a Click Manipulator, while the pointer is still within the node area and Kanzi does not recognize another gesture.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |

Click: Enter |

Occurs when the user presses a hit-testable node with a Click Manipulator and then every time the user moves the pointer on top of that node while still holding down the pointer.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |

Click: Leave |

Occurs when the user presses a hit-testable node with a Click Manipulator and then every time the user moves the pointer outside of that node.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |

Command: Command |

Command message arguments |

No |

Yes |

Data Trigger |

Monitors changes in properties and data source values. Use a Data Trigger to apply an action to either set a property value of a target node or activate an Activity node. |

No |

Yes |

Drag and Drop: Drag and Drop Canceled |

Occurs when focus moves away from the node during the drag-and-drop gesture. |

No |

Yes |

Drag and Drop: Drag and Drop Finished |

Occurs when the user lifts their finger after starting the drag-and-drop gesture. |

No |

Yes |

Drag and Drop: Drag and Drop Moved |

Occurs when the user moves their finger after starting the drag-and-drop gesture. |

No |

Yes |

Drag and Drop: Drag and Drop Started |

Occurs when the user holds their finger for 500ms on the node. |

No |

Yes |

Focus: About To Gain Focus |

Kanzi sends this message before a focusable node receives focus. |

No |

Yes |

Focus: About To Lose Focus |

Kanzi sends this message before the focused node loses focus. |

No |

Yes |

Focus: Focus Entered Focus Scope |

When focus enters a focus scope, Kanzi sends this message to the focus scope node that contains the node that gains focus. |

No |

Yes |

Focus: Focus Gained |

Kanzi sends this message to the node that received focus. |

No |

Yes |

Focus: Focus Left Focus Scope |

When focus leaves a focus scope, Kanzi sends this message to the focus scope node that contains the node that loses focus. |

No |

Yes |

Focus: Focus Lost |

Kanzi sends this message to the node that lost focus. |

No |

Yes |

Focus: Input Outside Overlay |

Kanzi sends this message to an overlay focus scope when the application area outside the boundaries of that overlay receives input. |

No |

Yes |

Focus: Overlay Brought To Front |

Occurs when an overlay focus scope becomes the foremost overlay scope in the overlay focus scope stack. |

No |

Yes |

Focus: Overlay Gained Focus |

When an overlay scope gains focus, Kanzi sends this message to the overlay scope node that contains the node that gains focus. |

No |

Yes |

Focus: Overlay Lost Focus |

When an overlay scope loses focus, Kanzi sends this message to the overlay scope node that contains the node that loses focus. |

No |

Yes |

Focus: Overlay Sent To Back |

Occurs when an overlay focus scope is no longer the foremost overlay scope in the overlay focus scope stack. |

No |

Yes |

Key Input: Key Canceled |

Occurs when Kanzi recognizes a key-canceled gesture. A key-canceled gesture occurs when Kanzi recognizes that the user canceled a gesture. |

No |

Yes |

Key Input: Key Pressed |

Occurs when Kanzi recognizes a key-pressed gesture. A key-pressed gesture occurs when Kanzi recognizes a key event that contains all the elements that compose that gesture. |

No |

Yes |

Key Input: Key Released |

Occurs when Kanzi recognizes a key-released gesture. A key-released gesture occurs when Kanzi recognizes the release of one of the elements that compose that gesture. |

No |

Yes |

Key Navigation: Key Navigation Canceled |

Occurs when the key-pressed gesture is canceled for the navigation direction. |

No |

Yes |

Key Navigation: Key Navigation Finished |

Occurs when Kanzi recognizes the key-released gesture for the navigation direction. To capture key navigation gestures for a node, create a Navigation Manipulator component in that node. |

No |

Yes |

Key Navigation: Key Navigation Started |

Occurs when Kanzi recognizes the key-pressed and key repeat gestures for the navigation direction. To capture key navigation gestures for a node, create a Navigation Manipulator component in that node. |

No |

Yes |

List Box: Item Loaded |

Occurs when an item is loaded to the working memory. To set how many items you want to keep loaded in the working memory at a time, use the Keep Alive Item Count property. |

No |

Yes |

List Box: Item Selected |

Occurs when an item is selected. |

No |

Yes |

List Box: Item Unloaded |

Occurs when an item is unloaded from the working memory. To set how many items you want to keep loaded in the working memory at a time, use the Keep Alive Item Count property. |

No |

Yes |

List Box: Scroll Finished |

Occurs when the List Box stops scrolling. |

No |

Yes |

List Box: Scroll Started |

Occurs when the List Box starts to scroll. |

No |

Yes |

List Box: Scrolled |

Occurs when the List Box scrolls. |

No |

Yes |

List Box: Target Changed |

Occurs when List Box gets a new target item. |

No |

Yes |

List Box: User Scroll Finished |

Occurs when the application user stops scrolling the List Box. |

No |

Yes |

List Box: User Scroll Started |

Occurs when the application user starts to scroll the List Box. |

No |

Yes |

Long Press: Long Press |

Occurs when the user presses a hit-testable node with a Long-Press Manipulator and holds the press for the time that you set in the Long-Press Manipulator.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |

Long Press: Long Press Cancel |

Occurs during the long-press gesture when the user moves the focus away from a hit-testable node with a Long-Press Manipulator.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |

Message Trigger |   |

No |

Yes |

Multi-Click: Intermediate Click |

Occurs when the user presses and releases a hit-testable node with a Multi-Click Manipulator that is set to send messages for intermediate clicks.

To set a Multi-Click Manipulator to send messages for intermediate clicks, in the Multi-Click Manipulator enable the Send Intermediate Click Messages property.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |

Multi-Click: Multi-Click |

Occurs when the user presses and releases a hit-testable node with a Multi-Click Manipulator a specified number of times (default 2) within a set amount of time (default 250 ms) between presses.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |

Multi-Click: Multi-Click Canceled |

Occurs during the multi-click gesture when the user moves the focus away from a hit-testable node with a Multi-Click Manipulator.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |

On Attached |

This trigger is set off when the item is initialized. For example, when you add a node to the node tree, or enter a state that contains this trigger. |

No |

Yes |

On Property Change |

Occurs when a property is changed |

No |

Yes |

On Timer |

Occurs when timer interval is elapsed |

No |

Yes |

Page (deprecated): Activated (deprecated) |

Page has been activated. |

No |

Yes |

Page (deprecated): Deactivated (deprecated) |

Page has been deactivated. |

No |

Yes |

Page Host (deprecated): Page Navigation Finished (deprecated) |

Page host has finished navigation process. |

No |

Yes |

Page Host (deprecated): Page Navigation Started (deprecated) |

Page host has started navigation process. |

No |

Yes |

Pan: Pan Canceled |

Occurs when focus moves away from the node during the pan gesture. |

No |

Yes |

Pan: Pan Entered |

Occurs when the pan gesture enters the node to which the Pan Manipulator is attached. |

No |

Yes |

Pan: Pan Finished |

Occurs when the user lifts their finger after Kanzi recognizes a pan gesture. |

No |

Yes |

Pan: Pan Left |

Occurs when the pan gesture leaves the node to which the Pan Manipulator is attached. |

No |

Yes |

Pan: Pan Moved |

Occurs when the user changes the position of their finger and that change exceeds the recognition thresholds. |

No |

Yes |

Pan: Pan Started |

Occurs when the user presses down their finger on the node. If the user lifts their finger before exceeding the position change threshold, Kanzi cancels the pan gesture. |

No |

Yes |

Pinch: Pinch Canceled |

Occurs when focus moves away from the node during the pinch gesture. |

No |

Yes |

Pinch: Pinch Finished |

Occurs when the user lifts their finger after Kanzi recognizes a pinch gesture. |

No |

Yes |

Pinch: Pinch Moved |

Occurs when the user changes the position of their finger and that change exceed the scale or rotation threshold. |

No |

Yes |

Pinch: Pinch Started |

Occurs when the user presses down their finger. If the user lifts their finger before it exceeds the scale or rotate threshold, Kanzi cancels the pinch. |

No |

Yes |

Prefab View: Asynchronous Load Completed |

Occurs when asynchronous loading of resources from a prefab has been finished. |

No |

Yes |

Property Target Easing Interpolator: Easing Interpolation Completed |

Occurs when Property Target Easing Interpolator completes its interpolation. |

No |

Yes |

Property Target Interpolator: Interpolation Completed |

Occurs when property target interpolator completes interpolation. |

No |

Yes |

Range: Value Change Finished |

Occurs when the range value stops changing. |

No |

Yes |

Range: Value Change Started |

Occurs when the range value starts changing. |

No |

Yes |

Range: Value Changed |

Occurs when the range value has changed. |

No |

Yes |

Scroll View: Scroll Ended |

Occurs when the scroll position of a Scroll View node stops changing. |

No |

Yes |

Scroll View: Scroll Started |

Occurs when the scroll position of a Scroll View node starts changing. |

No |

Yes |

Scroll View: Scroll Zoomed |

Occurs when the zoom level of a Scroll View node changes. |

No |

Yes |

Scroll View: Scrolled |

Occurs when the scroll position of a Scroll View node changes. |

No |

Yes |

Scroll View: Snap Request |

Occurs when a Scroll View node requests snapping target from the hosting component. |

No |

Yes |

Scroll View: User Scroll Ended |

Occurs when the user stops scrolling a Scroll View node. |

No |

Yes |

Scroll View: User Scroll Started |

Occurs when the user starts scrolling a Scroll View node. |

No |

Yes |

State Manager: Entered State |

Occurs when a state manager has entered a state. |

No |

Yes |

State Manager: Left State |

Occurs when a state manager has left a state. |

No |

Yes |

State Manager: Transition Finished |

Occurs when a state manager finishes a transition to a state. |

No |

Yes |

State Manager: Transition Started |

Occurs when a state manager begins a transition to a state. |

No |

Yes |

Text Box: Composition Text Changed |

Occurs when the text produced in an Input Method Editor is updated in a Text Box node. |

No |

Yes |

Text Box: Composition Text Committed |

Occurs: * When the text produced in an Input Method Editor is committed to the cached text in a Text Box node. * When a trigger executes the **Text Box: Commit Composition Text** action. |

No |

Yes |

Text Box: Cursor Moved |

Occurs when the user moves the cursor in a Text Box node. |

No |

Yes |

Text Box: Editing Finished |

Occurs when a Text Box node leaves the editing state after the user modified the text content. |

No |

Yes |

Text Box: Editing Started |

Occurs when the user makes the first modification to the text in a Text Box node that is in the editing state. |

No |

Yes |

Text Box: Entered Editing State |

Occurs when a Text Box node enters the editing state. |

No |

Yes |

Text Box: Input Method Action |

Occurs when the user taps the action button on their on-screen keyboard while editing the text in a Text Box node. |

No |

Yes |

Text Box: Input Method Available |

Occurs when an input method becomes available to a Text Box node. For example, an on-screen keyboard becomes available when it appears on the screen. |

No |

Yes |

Text Box: Input Method Unavailable |

Occurs when the input method that is composing text in a Text Box node becomes unavailable. For example, an on-screen keyboard becomes unavailable when the user hides it. |

No |

Yes |

Text Box: Left Editing State |

Occurs when a Text Box node leaves the editing state |

No |

Yes |

Text Box: Selection Changed |

Occurs when the user changes the text selection in a Text Box node. |

No |

Yes |

Text Box: Selection Cleared |

Occurs when the user clears or resets the text selection in a Text Box node. |

No |

Yes |

Text Box: Selection Started |

Occurs when the user starts selecting text in a Text Box node. |

No |

Yes |

Text Box: Text Changed |

Occurs when the user changes the text in a Text Box node. |

No |

Yes |

Text Box: Text Composition Canceled |

Occurs: * When the text composition in a Text Box node is canceled by Input Method that is in text composition state. * When a trigger executes the **Text Box: Cancel Text Composition** action. |

No |

Yes |

Toggle Button Group: Toggled |

Occurs when the toggle state of a **Toggle Button** node in a **Toggle Button Group** node changes. |

No |

Yes |

Toggle Button: State Toggled |

Occurs when the toggle state of a Toggle Button changes. |

No |

Yes |

Toggle Button: Toggled Off |

Occurs when a Toggle Button is toggled off. |

No |

Yes |

Toggle Button: Toggled On |

Occurs when a Toggle Button is toggled on. |

No |

Yes |
