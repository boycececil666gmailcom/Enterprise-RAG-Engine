---
title: Prefab View 2D
source: https://docs.kanzi.com/4.1.0/en/reference/node-and-resource-reference/prefab-view-2d-reference.html
---

# Prefab View 2D

## Prefab View 2D properties

|

Name |

Description |

Inherited |

Exported to Kanzi Engine |
|

Tags |

List of tags attached to the item |

No |

No |
|

Effective Data Context |

The data context in the current node that is resolved from data context properties and bindings |

No |

No |
|

Effective Activity Source |

The data source for this Activity node. |

No |

No |
|

Name |

Name of the project item |

No |

No |
|

Component Type |

The component type of this component node |

No |

No |
## Prefab View 2D available properties

|

Name |

Description |

Inherited |

Exported to Kanzi Engine |
|

Disable KZB Export |

Disables the exporting of the item into KZB. Can be used for, e.g. letting items out from certain profiles. The disabled items are always included in preview. |

No |

No |
|

Brush Color |

Color for brush. Set alpha to 0 to disable brush. |

No |

Yes |
|

Brush Texture |

Texture for brush. |

No |

Yes |
|

Align To Tangent |

Whether to align the Trajectory List Box 3D items to match the tangent of the trajectory. |

No |

Yes |
|

Allowed Scroll Axis |

Sets the axis on which you want to allow this Trajectory List Box 3D node to scroll. |

No |

Yes |
|

Cursor Offset |

Sets the offset of the position to use to select the active item, in proportional range [0,1]. |

No |

Yes |
|

Dragging Acceleration |

Sets the acceleration of the Trajectory List Box 3D when the user scrolls the Trajectory List Box 3D by dragging the pointer. The higher the value, the quicker the Trajectory List Box 3D reaches its final position. The default value is 80. |

No |

Yes |
|

Dragging Drag |

Sets the amount that drag affects the movement of the Trajectory List Box 3D when the user scrolls the Trajectory List Box 3D by dragging the pointer. The lower the value, the higher the drag and the quicker the scrolling stops. The default value is 150. |

No |

Yes |
|

Dragging Impulse |

Sets the amount of impulse to generate from the pointer movement when the user scrolls the Trajectory List Box 3D by dragging the pointer. |

No |

Yes |
|

Item Area Begin |

Sets the proportional offset where the part of the trajectory meant for the fully visible Trajectory List Box 3D items starts. Kanzi uses the values of the Item Area Begin and Item Area End properties to calculate the value of the Node.VisibleAmountInParent property for each list item.You can use the VisibleAmountInParent property in shaders to fade out those list items that are not fully visible. |

No |

Yes |
|

Item Area End |

Sets the proportional offset where the part of the trajectory meant for the fully visible Trajectory List Box 3D items ends. Kanzi uses the values of the Item Area Begin and Item Area End properties to calculate the value of the Node.VisibleAmountInParent property for each list item.You can use the VisibleAmountInParent property in shaders to fade out those list items that are not fully visible. |

No |

Yes |
|

Looping |

Whether to show items in the Trajectory List Box 3D from the beginning after reaching the last item. |

No |

Yes |
|

Maximum Number of Touches |

Sets the maximum number of touch points allowed on the Trajectory List Box 3D area for scrolling. |

No |

Yes |
|

Minimum Number of Touches |

Sets the minimum number of touch points required on the Trajectory List Box 3D area for scrolling. |

No |

Yes |
|

Recognition Threshold |

Sets the distance in pixels that the pointer has to move for the scrolling to start in the Trajectory List Box 3D. |

No |

Yes |
|

Reversed Scrolling |

Whether the scroll position in the Trajectory List Box node increases in relation to the direction of the pan gesture. This reverses the direction of scrolling. By default, the scroll position decreases in relation to the pan direction, which makes the list items move toward the direction of the trajectory. |

No |

Yes |
|

Scroll Position |

Sets the scroll position of the Trajectory List Box 3D along the x and y axes as a relative position within the list box area. Use this property to move the list to a scroll position immediately, without scrolling. To update the scroll position with a binding, use a two-way or to-source binding. |

No |

Yes |
|

Scroll Sensitivity |

Sets the amount that the scroll value changes relative to the movement of the pointer on the scroll view plane of the Trajectory List Box 3D. The default value 1 makes the Trajectory List Box 3D scroll the same amount as the user drags the pointer. For example, to set the Trajectory List Box 3D to scroll twice the amount that the user drags the pointer, set the value of the property to 2. |

No |

Yes |
|

Sliding Acceleration |

Sets the acceleration of the Trajectory List Box 3D after the user releases the pointer with which they scroll the Trajectory List Box 3D. The higher the value, the quicker the Trajectory List Box 3D reaches the scroll target. The default value is 40. |

No |

Yes |
|

Sliding Drag |

Sets how much drag affects the movement of the Trajectory List Box 3D after the user releases the pointer with which they scroll the Trajectory List Box 3D. The lower the value, the higher the drag and the quicker the scrolling of the Trajectory List Box 3D stops. The default value is 80. |

No |

Yes |
|

Spacing |

Sets the distance between the items in the Trajectory List Box 3D. |

No |

Yes |
|

Swipe Distance |

Sets the distance that a swipe sends the scroll value in the Trajectory List Box 3D, relative to the speed of the pointer. |

No |

Yes |
|

Trajectory |

Sets the trajectory along which the Trajectory List Box 3D arranges its items. |

No |

Yes |
|

Prefab Template |

Node to use on this prefab view. |

No |

Yes |
|

Code Behind Source |

Sets the metaclass name of the code behind class for this node. |

No |

Yes |
|

Data Context |

Source of data for this node and its descendants |

No |

Yes |
|

Primary Direction |

The direction along which the layout arranges items until the layout limit in that direction is reached. |

No |

Yes |
|

Secondary Direction |

The direction along which the flow layout arranges lines of the primary direction. |

No |

Yes |
|

Columns |

Defines the number of columns in a grid layout and how the grid layout distributes the content in columns. |

No |

Yes |
|

Layout Direction |

The direction in which the items are arranged when you add them to a grid layout. |

No |

Yes |
|

Rows |

Defines the number of rows in a grid layout and how the grid layout distributes the content in rows. |

No |

Yes |
|

Items Source |

Data object which provides data sources for list items. |

No |

Yes |
|

Cell Height |

Sets the height of each cell in the Grid List Box. |

No |

Yes |
|

Cell Width |

Sets the width of each cell in the Grid List Box. |

No |

Yes |
|

Dragging Acceleration |

Sets the acceleration of the Grid List Box when the user scrolls the Grid List Box by dragging the pointer. The higher the value, the quicker the Grid List Box reaches its final position. The default value is 80. |

No |

Yes |
|

Dragging Drag |

Sets the amount that drag affects the movement of the Grid List Box when the user scrolls the Grid List Box by dragging the pointer. The lower the value, the higher the drag and the quicker the scrolling stops. The default value is 150. |

No |

Yes |
|

Dragging Impulse |

Sets the amount of impulse to generate from the pointer movement when the user scrolls the Grid List Box by dragging the pointer. |

No |

Yes |
|

Item Area Begin |

Sets the proportional offset where the area meant for the fully visible items in the Grid List Box starts. Kanzi uses the values of the Item Area Begin and Item Area End properties to calculate the value of the Node.VisibleAmountInParent property for each list item.You can use the VisibleAmountInParent property in shaders to fade out those list items that are not fully visible. |

No |

Yes |
|

Item Area End |

Sets the proportional offset where the area meant for the fully visible items in the Grid List Box ends. Kanzi uses the values of the Item Area Begin and Item Area End properties to calculate the value of the Node.VisibleAmountInParent property for each list item.You can use the VisibleAmountInParent property in shaders to fade out those list items that are not fully visible. |

No |

Yes |
|

Layout Direction |

Sets the direction in which the Grid List Box arranges its items. When you change the layout direction you also change the scroll axis of the Grid List Box. |

No |

Yes |
|

Maximum Number of Touches |

Sets the maximum number of touch points allowed on the Grid List Box area for scrolling. |

No |

Yes |
|

Minimum Number of Touches |

Sets the minimum number of touch points required on the Grid List Box area for scrolling. |

No |

Yes |
|

Recognition Threshold |

Sets the distance in pixels that the pointer has to move for the scrolling to start in the Grid List Box. |

No |

Yes |
|

Reversed Scrolling |

Whether the scroll position in the Grid List Box node increases in relation to the direction of the pan gesture. This reverses the direction of scrolling. By default, the scroll position decreases in relation to the pan direction and items moves to same direction with the pan gesture. |

No |

Yes |
|

Scroll Position |

Sets the scroll position of the Grid List Box along the x and y axes as a relative position within the list box area. Use this property to move the list to a scroll position immediately, without scrolling. To update this property with a binding, use a to-source or two-way binding. |

No |

Yes |
|

Scroll Sensitivity |

Sets the amount that the scroll position changes relative to the movement of the pointer. The default value 1 makes the Grid List Box scroll the same amount as the user drags the pointer. For example, to set the Grid List Box to scroll twice the amount that the user drags the pointer, set the value of the property to 2. |

No |

Yes |
|

Scroll Speed |

Reports the current scroll speed of the Grid List Box. |

No |

Yes |
|

Scroll Target Position |

Reports the current target scroll value of the Grid List Box. |

No |

Yes |
|

Scrolling |

Reports whether the Grid List Box is currently scrolling. |

No |

Yes |
|

Sliding Acceleration |

Sets the acceleration of the Grid List Box after the user releases the pointer with which they scroll the Grid List Box. The higher the value, the quicker the Grid List Box reaches the scroll target. The default value is 40. |

No |

Yes |
|

Sliding Drag |

Sets how much drag affects the movement of the Grid List Box after the user releases the pointer with which they scroll the Grid List Box. The lower the value, the higher the drag and the quicker the scrolling of the Grid List Box stops. The default value is 80. |

No |

Yes |
|

Swipe Distance |

Sets the distance that a swipe sends the scroll value in the Grid List Box, relative to the speed of the pointer. |

No |

Yes |
|

Item Container Generator |

Sets the name of the item container generator type to use to provide item containers dynamically for the List Box. |

No |

Yes |
|

Item Container Template |

Sets the List Box Item Container prefab that sets the appearance and behavior of the List Box items. |

No |

Yes |
|

Item Generator |

Sets the name of the item generator type to use to provide items dynamically to the List Box. |

No |

Yes |
|

Item Template |

Sets the prefab to use for the List Box items. |

No |

Yes |
|

Keep Alive Item Count |

Sets the size of the buffer for invisible List Box items. Kanzi returns to the Item Generator those invisible items that do not fit in the buffer. |

No |

Yes |
|

Selection Behavior |

Sets how the List Box behaves when the user selects an item. âBring to Centerâ sets the List Box to bring an item to the center of the List Box area when the user selects that item. |

No |

Yes |
|

Allowed Scroll Axis |

Sets the axis on which you want to allow this Scroll View node to scroll. |

No |

Yes |
|

Dragging Acceleration |

Sets the acceleration of the node controlled by a Scroll View node while you drag that Scroll View node. Use low values when you want that node to slowly reach the final position. Use high values when you want that node to quickly reach the final position. |

No |

Yes |
|

Dragging Drag |

Sets the amount that drag affects the movement of the node controlled by a Scroll View node while you drag that Scroll View node. The lower the value the higher the drag and the faster the sliding of that node stops. |

No |

Yes |
|

Dragging Impulse |

Sets the amount of impulse generated from the pointing device movement when dragging a Scroll View node. |

No |

Yes |
|

Looping X Enabled |

Sets the node controlled by a Scroll View node to start scrolling from the beginning when the scroll reaches the scroll bounds on the x axis. When the scroll value reaches the maximum value of the bound, the value changes to the minimum value and the other way around. Use the Scroll Bounds Minimum and Scroll Bounds Maximum properties to set the scroll bounds. |

No |

Yes |
|

Looping Y Enabled |

Sets the node controlled by a Scroll View node to start scrolling from the beginning when the scroll reaches the scroll bounds on the y axis. When the scroll value reaches the maximum value of the bound, the value changes to the minimum value and the other way around. Use the Scroll Bounds Minimum and Scroll Bounds Maximum properties to set the scroll bounds. |

No |

Yes |
|

Maximum Number of Touches |

Sets the maximum number of touch points allowed for a Scroll View pan. |

No |

Yes |
|

Maximum Zoom |

Sets the maximum zoom level. |

No |

Yes |
|

Minimum Number of Touches |

Sets the required number of touch points pressed for a Scroll View node pan to start. Scroll View nodes with minimum number of touches greater than one precede the children in touch processing. |

No |

Yes |
|

Minimum Zoom |

Sets the minimum zoom level. |

No |

Yes |
|

Recognition Threshold |

Sets the amount a pointing device must move for the scrolling to start on a Scroll View node. |

No |

Yes |
|

Reversed X Axis Scroll |

Whether the scroll position of the x axis increases in relation to the direction of the pan gesture. This reverses the direction of scrolling. By default, the scroll position decreases in relation to the pan direction. |

No |

Yes |
|

Reversed Y Axis Scroll |

Whether the scroll position of the y axis increases in relation to the direction of the pan gesture. This reverses the direction of scrolling. By default, the scroll position decreases in relation to the pan direction. |

No |

Yes |
|

Scroll Bounds Maximum |

Sets the coordinates of the bottom-right corner of the scroll bounds rectangle. Scroll bounds define where the scrolling begins and ends. |

No |

Yes |
|

Scroll Bounds Minimum |

Sets the coordinates of the top-left corner of the scroll bounds rectangle. Scroll bounds define where the scrolling begins and ends. |

No |

Yes |
|

Scroll Position |

Sets the scroll position of the Scroll View along the x and y axes as a relative position within the scroll view area. Use this property to set the scroll position immediately, without scrolling. To update the scroll position with a binding, use a two-way or to-source binding. |

No |

Yes |
|

Scroll Sensitivity |

Sets the amount the position changes relative to the movement of the pointer that starts the swiping. The higher the value the more the position of the node controlled by a Scroll View node changes. The default value is 1. |

No |

Yes |
|

Scroll Speed |

The current scroll speed (read-only). |

No |

Yes |
|

Scroll Target Position |

The current target scroll value (read-only). |

No |

Yes |
|

Scrolling |

Whether a Scroll View node is currently scrolling (read-only). |

No |

Yes |
|

Sliding Acceleration |

Sets the acceleration of the node controlled by a Scroll View node after you release the pointer with which you swipe. Use low values when you want that node to slowly reach the final position. Use high values when you want that node to quickly reach the final position. |

No |

Yes |
|

Sliding Drag |

Sets the amount that drag affects the movement of the node controlled by a Scroll View node after you release the pointer with which you swipe. The lower the value the higher the drag and the faster the sliding of the object controlled by the Scroll View node stops. |

No |

Yes |
|

Step Multiplier |

Sets the smallest distance that a Scroll View scrolls. |

No |

Yes |
|

Swipe Distance |

Sets the distance that a swipe sends the scroll value, relative to the pointing device speed. |

No |

Yes |
|

Zoom |

Sets the current zoom level. |

No |

Yes |
|

Zoom Affects Scrolling |

Controls whether the scroll position is scaled, according to the zoom level. |

No |

Yes |
|

Zoom Enabled |

Sets whether to install a pinch manipulator that generates zoom messages. |

No |

Yes |
|

Align To Tangent |

Whether to align the items in this Trajectory Layout to match the tangent of the trajectory. Vertical trajectories are not supported. |

No |

Yes |
|

Item Area Begin |

Sets the starting point of the trajectory segment in which the items in this Trajectory Layout are considered fully visible. The value is in the range [0, 1], where 0 is the beginning and 1 is the end of the trajectory. The Node > Visible Amount in Parent property uses this value. |

No |

Yes |
|

Item Area End |

Sets the ending point of the trajectory segment in which the items in this Trajectory Layout are considered fully visible. The value is in the range [0, 1], where 0 is the beginning and 1 is the end of the trajectory. The Node > Visible Amount in Parent property uses this value. |

No |

Yes |
|

Override Distance |

Sets the distance between the items in this Trajectory Layout. When you do not set this property, the Trajectory Layout calculates the distance automatically. |

No |

Yes |
|

Start Offset |

Sets the offset of the starting position of the items on the trajectory in the range [0, 1], where 0 is the beginning and 1 is the end of the trajectory. |

No |

Yes |
|

Trajectory |

Sets the Trajectory along which this Trajectory Layout node arranges its items. |

No |

Yes |
|

Foreground Brush |

The foreground brush to paint the foreground of 2D nodes. |

No |

Yes |
|

Layout Height |

The height of the node when used in a layout. Overrides the default bounds of the item. |

No |

Yes |
|

Layout Width |

The width of the node when used in a layout. Overrides the default bounds of the item. |

No |

Yes |
|

Global Ambient Color |

Sets the color that is multiplied automatically with the Ambient property of the materials in the scene. Use the Intensity (I) property field to adjust the exposure of the color. |

No |

Yes |
|

Font Color |

Sets the color of the text in a 3D text node. |

No |

Yes |
|

Cubemap Texture |

Sets the cubemap texture you want the Blit render pass to blit. |

No |

Yes |
|

Texture 0 |

Sets the first texture you want the Blit render pass to blit. |

No |

Yes |
|

Texture 1 |

Sets the second texture you want the Blit render pass to blit. |

No |

Yes |
|

Texture 2 |

Sets the third texture you want the Blit render pass to blit. |

No |

Yes |
|

Texture 3 |

Sets the fourth texture you want the Blit render pass to blit. |

No |

Yes |
|

Texture 4 |

Sets the fifth texture you want the Blit render pass to blit. |

No |

Yes |
|

Texture 5 |

Sets the sixth texture you want the Blit render pass to blit. |

No |

Yes |
|

Texture 6 |

Sets the seventh texture you want the Blit render pass to blit. |

No |

Yes |
|

Texture 7 |

Sets the eighth texture you want the Blit render pass to blit. |

No |

Yes |
|

Texture 8 |

Sets the ninth texture you want the Blit render pass to blit. |

No |

Yes |
|

Texture 9 |

Sets the tenth texture you want the Blit render pass to blit. |

No |

Yes |
|

Blend Intensity |

Controls the intensity of materials that are blended on top of an existing color. Attached property enables overriding of the blend intensity of the used materials at render pass or object node level. |

No |

Yes |
|

Bloom Intensity |

Bloom intensity for the material. |

No |

Yes |
|

Bloom Intensity Texture |

Sets the bloom intensity texture. |

No |

Yes |
|

Bloom Radius |

Bloom radius for the material. |

No |

Yes |
|

Use Intensity Texture |

Enable or disable the use of the Bloom Intensity texture property. |

No |

Yes |
|

Blur Direction |

Sets the direction for the blur. |

No |

Yes |
|

Blur Radius |

Blur radius for the material. |

No |

Yes |
|

Amount |

Sets the chromatic aberration amount. |

No |

Yes |
|

Dithering Amount |

Sets the chromatic aberration dithering amount. |

No |

Yes |
|

Grading Color Highlight |

Sets the color grading highlight color. |

No |

Yes |
|

Grading Color Midtone |

Sets the color grading midtone color. |

No |

Yes |
|

Grading Color Shadow |

Sets the color grading shadow color. |

No |

Yes |
|

Grading Highlight Range |

Sets the luminance range where the highlight color is applied. |

No |

Yes |
|

Grading Hue Saturation Value |

Sets the HSV adjustment for the input color. |

No |

Yes |
|

Grading Shadow Range |

Sets the luminance range where the shadow color is applied. |

No |

Yes |
|

Alpha Cutoff |

Sets the cutoff threshold for alpha cutting. If the alpha value is less than the value of this property, Kanzi discards the fragment. The default value is 0.5. |

No |

Yes |
|

Ambient Color |

Sets the color of the material when lights are not present. Use the Intensity (I) property field to adjust the exposure of the color. |

No |

Yes |
|

Ambient Occlusion Blur Direction |

Blur direction of the ambient occlusion bilateral blur. |

No |

Yes |
|

Ambient Occlusion Focal Length |

HBAO input property for focal length. |

No |

Yes |
|

Ambient Occlusion LinMAD |

HBAO input property for LinMAD uniform. |

No |

Yes |
|

Ambient Occlusion Radius |

Screen-space ambient occlusion (SSAO) effect radius. Used to calculate the SSAO texture. |

No |

Yes |
|

Ambient Occlusion Strength |

Screen-space ambient occlusion (SSAO) strength. Used to calculate the SSAO texture. |

No |

Yes |
|

Ambient Occlusion UV to View A |

HBAO input property for UVToViewA uniform. |

No |

Yes |
|

Ambient Occlusion UV to View B |

HBAO input property for UVToViewB uniform. |

No |

Yes |
|

Base Color Factor |

Sets the base color for the material. |

No |

Yes |
|

Base Color Texture |

Sets the texture that contains the base color for the material. Use the Base Color Factor property to filter the value from this texture. |

No |

Yes |
|

BRDF Lookup Table |

Gets the Bidirectional Reflectance Distribution Function (BRDF) lookup table for the material. The BRDF table is a texture that contains precomputed information about how light reflects off a material. You can use it to improve rendering quality. |

No |

Yes |
|

Clear Coat Normal Scale |

Sets the clear coat normal scale for the material. Use the scale to set the intensity of the Clear Coat Normal Texture. |

No |

Yes |
|

Clear Coat Normal Texture |

Sets the texture that contains a clear coat normal map for the material. Use the Clear Coat Normal Scale property to scale the texture value. |

No |

Yes |
|

Clear Coat Roughness Factor |

Sets the roughness of the outer clear coat layer for the material: 0 represents a smooth, glossy surface, and 1 represents a rough, diffuse surface. |

No |

Yes |
|

Clear Coat Roughness Texture |

Sets the texture that contains a clear coat roughness map for the material. Kanzi reads the roughness from the Green channel of the texture. Use the Clear Coat Roughness Factor property to scale the roughness from this texture. |

No |

Yes |
|

Clear Coat Strength Factor |

Sets the clear coat strength for the material: 0 represents a material with no clear coat, and 1 represents a full strength clear coat. |

No |

Yes |
|

Clear Coat Strength Texture |

Sets the texture that contains a clear coat strength map for the material. Kanzi reads the strength from the Red channel of the texture. Use the Clear Coat Strength Factor property to scale the strength from this texture. |

No |

Yes |
|

Detail Base Color Factor |

Sets the detail base color for the material. The detail base color is alpha blended with the standard base color. |

No |

Yes |
|

Detail Base Color Texture |

Sets the detail texture that contains the base color for the material. Use the Detail Base Color Factor property to filter the value from this texture. The detail base color is alpha blended with the standard base color. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |
|

Detail Clear Coat Normal Scale |

Sets the detail clear coat normal scale for the material. Use the scale to set the intensity of the Detail Clear Coat Normal Texture. |

No |

Yes |
|

Detail Clear Coat Normal Texture |

Sets the detail texture that contains a clear coat normal map for the material. Use the Detail Clear Coat Normal Scale property to scale the texture value. |

No |

Yes |
|

Detail Clear Coat Roughness Texture |

Sets the detail texture that contains a clear coat roughness map for the material. Use the Clear Coat Roughness Factor and Clear Coat Roughness Texture properties to scale the roughness from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |
|

Detail Clear Coat Strength Texture |

Sets the detail texture that contains a clear coat strength map for the material. Kanzi reads the strength from the Red channel of the texture. Use the Clear Coat Strength Factor and Clear Coat Strength Texture properties to scale the strength from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |
|

Detail Diffuse Color Factor |

Sets the detail diffuse color for the material. Kanzi alpha blends the detail diffuse color with the standard diffuse color. |

No |

Yes |
|

Detail Diffuse Color Texture |

Sets the detail texture that contains the diffuse color for the material. Use the Detail Diffuse Color Factor property to filter the value from this texture. Kanzi alpha blends the detail diffuse color with the standard diffuse color. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |
|

Detail Emissive Factor |

Sets the color of the light that is emitted from a detail texture for the material. Use the Intensity (I) property field to adjust the brightness of the light. This color affects the local material rendering, but the light is not cast to other objects. The detail emissive light is alpha blended with the standard emissive light. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |
|

Detail Emissive Texture |

Sets the detail texture that contains the light emitted from the material. Use the Detail Emissive Factor property to scale the value from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |
|

Detail Glossiness Texture |

Sets the detail texture that contains a glossiness map for the material. Kanzi reads the glossiness from the Alpha channel of this texture. Use the Glossiness Factor and Glossiness Texture properties to scale the glossiness from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |
|

Detail Metallic Texture |

Sets the detail texture that contains a metallic map for the material. Kanzi reads the metalness from the Blue channel of this texture. Use the Metallic Factor and Metallic Texture properties to scale the metalness from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |
|

Detail Normal Scale |

Sets the detail normal scale for the material. Use the scale to set the intensity of the Detail Normal Texture. |

No |

Yes |
|

Detail Normal Texture |

Sets the detail texture that contains a normal map for the material. Use the Detail Normal Scale property to scale the texture value. |

No |

Yes |
|

Detail Occlusion Strength |

Sets the detail occlusion strength for the material. Use the strength to set the intensity of the Detail Occlusion Texture. |

No |

Yes |
|

Detail Occlusion Texture |

Sets the detail texture that contains an occlusion map for the material. Kanzi reads the occlusion from the Red channel of this texture. Use the Detail Occlusion Strength property to scale the occlusion from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |
|

Detail Roughness Texture |

Sets the detail texture that contains a roughness map for the material. Kanzi reads the roughness from the Green channel of the texture. Use the Roughness Factor and Roughness Texture properties to scale the roughness from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |
|

Detail Specular Color Factor |

Sets the detail specular color for the material. Kanzi alpha blends the detail specular color with the standard specular color. |

No |

Yes |
|

Detail Specular Color Texture |

Sets the detail texture that contains the specular color for the material. Use the Detail Specular Color Factor property to filter the value from this texture. Kanzi alpha blends the detail specular color with the standard specular color. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

No |

Yes |
|

Detail Texture Offset |

Sets the detail texture offset for the material. Kanzi adds this value to the UVs to produce a second set of detail UVs to use for all detail texture properties. |

No |

Yes |
|

Detail Texture Tiling |

Sets the detail texture tiling factor for the material. Kanzi multiplies this value by the UVs to produce a second set of detail UVs to use for all detail texture properties. |

No |

Yes |
|

Diffuse Color |

Sets the color of the material when it is lit by a light. |

No |

Yes |
|

Diffuse Color Factor |

Sets the diffuse color for the material. |

No |

Yes |
|

Diffuse Color Texture |

Sets the texture that contains the diffuse color for the material. Use the Diffuse Color Factor property to filter the value from this texture. |

No |

Yes |
|

Directional Light View Projection |

The premultiplied projection view matrix of a directional light. |

No |

Yes |
|

Directional Shadow Map |

Depth map used to calculate directional shadows. |

No |

Yes |
|

Emissive Color |

Sets the color of the light that is emitted from the material surface. |

No |

Yes |
|

Emissive Factor |

Sets the color of the light that is emitted from the material. Use the Intensity (I) property field to adjust the brightness of the light. This color affects the local material rendering, but the light is not cast to other objects. |

No |

Yes |
|

Emissive Texture |

Sets the texture that contains the light emitted from the material. Use the Emissive Factor property to scale the value from this texture. |

No |

Yes |
|

Environment Ambient Factor |

Sets the strength of the cubemap texture to use for ambient environment light. Use the Environment Ambient Texture property to set the cubemap texture. The ambient environment light affects diffuse lighting in image based lighting. |

No |

Yes |
|

Environment Ambient Texture |

Sets the cubemap to use for the ambient environment light for the material. This cubemap affects the diffuse lighting during image based lighting. Use the Environment Ambient Factor property to set the strength of the cubemap texture. |

No |

Yes |
|

Environment Reflection Factor |

Sets the strength of the cubemap texture to use for specular environment light. Use the Environment Reflection Texture property to set the cubemap texture. The specular environment light affects reflective lighting in image based lighting. |

No |

Yes |
|

Environment Reflection Texture |

Sets the cubemap to use for the specular environment light for the material. This cubemap affects reflective lighting during image based lighting. Use the Environment Reflection Factor property to set the strength of the cubemap texture. |

No |

Yes |
|

Exposure |

Sets the exposure compensation for the material. The exposure compensation emulates camera exposure by controlling the total amount of light rendered. Use a negative value to darken the rendered image, and a positive value to lighten the image. Exposure is exponential: 1.0 is twice as bright as 0.0, and -1.0 is half as bright as 0.0. |

No |

Yes |
|

Glossiness Factor |

Sets the glossiness of the material: 0 represents a rough, diffuse surface, and 1 represents a smooth, glossy surface. |

No |

Yes |
|

Glossiness Texture |

Sets the texture that contains a glossiness map for the material. Kanzi reads the glossiness from the Alpha channel of this texture. Use the Glossiness Factor property to scale the glossiness from this texture. |

No |

Yes |
|

Mask Texture |

Sets the texture that masks another texture or color. |

No |

Yes |
|

Mask Texture Offset |

Sets an offset for mask in materials. |

No |

Yes |
|

Mask Texture Tiling |

Determines the number of times a mask is presented in a material |

No |

Yes |
|

Metallic Factor |

Sets the metalness of the material: 0 represents a non-metallic or dielectric object, and 1 represents a metallic object. |

No |

Yes |
|

Metallic Texture |

Sets the texture that contains a metallic map for the material. Kanzi reads the metalness from the Blue channel of this texture. Use the Metallic Factor property to scale the value from this texture. |

No |

Yes |
|

Normal Scale |

Sets the normal scale for the material. Use the scale to set the intensity of the Normal Texture. |

No |

Yes |
|

Normal Texture |

Sets the texture that contains a normal map for the material. Use the Normal Scale property to scale the texture value. |

No |

Yes |
|

Occlusion Render Strength |

Sets the SSAO strength for the material. Use the strength to set the intensity of the SSAO Texture. |

No |

Yes |
|

Occlusion Render Texture |

Sets the texture that contains a SSAO computed for the scene. Use the Occlusion Render Strength property to scale the strength of the SSAO. |

No |

Yes |
|

Occlusion Strength |

Sets the occlusion strength for the material. Use the strength to set the intensity of the Occlusion Texture. |

No |

Yes |
|

Occlusion Texture |

Sets the texture that contains an occlusion map for the material. Use the Occlusion Strength property to scale the occlusion from the texture. |

No |

Yes |
|

Planar Reflection Map |

Rendered texture for planar reflections. |

No |

Yes |
|

Planar Reflection View Projection |

The premultiplied projection view matrix for planar reflections. |

No |

Yes |
|

Point Shadow Map |

Depth cubemap used to calculate point light shadows. |

No |

Yes |
|

Point Shadow Near Far |

Sets the near & far values used for point shadow calculations. |

No |

Yes |
|

Roughness Factor |

Sets the roughness of the material: 0 represents a smooth, glossy surface, and 1 represents a rough, diffuse surface. |

No |

Yes |
|

Roughness Texture |

Sets the texture that contains a roughness map for the material. Kanzi reads the roughness from the Green channel of the texture. Use the Roughness Factor property to scale the roughness from this texture. |

No |

Yes |
|

Specular Anti-Aliasing Strength |

Sets the strength of the specular anti-aliasing effect. Higher value results in blurrier specular highlights. For no specular anti-aliasing, set the value to 0. For full specular anti-aliasing, set the value to 1. The default value is 0.25. |

No |

Yes |
|

Specular Anti-Aliasing Threshold |

Sets the upper limit for the amount of specular anti-aliasing effect to apply. The default value is 0.18. |

No |

Yes |
|

Specular Color |

Sets the color of the specular reflection. |

No |

Yes |
|

Specular Color Factor |

Sets the specular color for the material. |

No |

Yes |
|

Specular Color Texture |

Sets the texture that contains the specular color for the material. Use the Specular Color Factor property to filter the value from this texture. |

No |

Yes |
|

Specular Exponent |

Sets the size of the specular highlight. |

No |

Yes |
|

Spot Light View Projection |

The premultiplied projection view matrix of a spot light. |

No |

Yes |
|

Spot Shadow Map |

Depth map used to calculate spot shadows. |

No |

Yes |
|

Texture |

Sets the texture of the material. |

No |

Yes |
|

Texture Offset |

Sets an offset for texture in materials. |

No |

Yes |
|

Texture Tiling |

Determines the number of times a texture is presented in a material. |

No |

Yes |
|

Tone Map Linear Scale |

Sets the scale for the linear tonemap option for the material. When linear tonemapping is used, Kanzi divides all output color by the value of this property. |

No |

Yes |
|

Morph Data Texture |

Data texture to use for storing morph data when the are are too many targets to use regular attribute channels. |

No |

Yes |
|

Morphing |

Add morph weights to Model3D to enable Morphing. |

No |

Yes |
|

A |

Tonemapping parameter A. |

No |

Yes |
|

B |

Tonemapping parameter B. |

No |

Yes |
|

C |

Tonemapping parameter C. |

No |

Yes |
|

D |

Tonemapping parameter D. |

No |

Yes |
|

E |

Tonemapping parameter E. |

No |

Yes |
|

F |

Tonemapping parameter F. |

No |

Yes |
|

White Scale |

Sets the value that will be tonemapped to pure white. |

No |

Yes |
|

Inner Distance |

Sets the distnace range where the vignette color transition starts. |

No |

Yes |
|

Outer Color |

Sets the vignette color. |

No |

Yes |
|

Outer Distance |

Sets the distnace range where the vignette color transition ends. |

No |

Yes |
|

Focused |

Indicates whether the node has the key focus. |

No |

Yes |
|

Actual Layout Height |

The calculated height of the node when used in a layout. |

No |

Yes |
|

Actual Layout Width |

The calculated width of the node when used in a layout. |

No |

Yes |
|

Horizontal Margin |

Sets the horizontal space between this node and other nodes that are adjacent to this node in a layout.

To access the Horizontal Margin property fields in a binding, use: * X for the **Left** property field * Y for the **Right** property field  |

No |

Yes |
|

Vertical Margin |

Sets the vertical space between this node and other nodes that are adjacent to this node in a layout.

To access the Vertical Margin property fields in a binding, use: * X for the **Bottom** property field * Y for the **Top** property field  |

No |

Yes |
|

Bottom Image |

The image to use in middle of the bottom row. |

No |

Yes |
|

Bottom-Left Image |

Image to use in the bottom-left corner. |

No |

Yes |
|

Bottom-Right Image |

The image to use in the bottom-right corner. |

No |

Yes |
|

Center Image |

The image to use in the center. |

No |

Yes |
|

Left Image |

The image to use in the center-left. |

No |

Yes |
|

Right Image |

The image to use in the center-right. |

No |

Yes |
|

Top Image |

The image to use in the middle of the top row. |

No |

Yes |
|

Top-Left Image |

The image to use in the top-left corner. |

No |

Yes |
|

Top-Right Image |

The image to use in the top-right corner. |

No |

Yes |
|

Node.Path |

Full path to the node. |

No |

Yes |
|

State Manager |

Sets the State Manager to the node. |

No |

Yes |
|

Style |

Sets a style to the node. |

No |

Yes |
|

Maximum Distance From Curve |

The distance from the curve where hit testing succeeds. |

No |

Yes |
|

Baseline |

Font baseline in 3D space units. |

No |

Yes |
|

Two Pass Rendering |

Defines whether the Text Block 3D is rendered in two passes. Disabling the two pass rendering improves performance, but can cause invalid rendering results when glyph bounds overlap. |

No |

Yes |
|

Snap Character To Pixel |

Sets whether Kanzi positions characters in 2D rendering to the nearest pixel: * When enabled, text sharpness improves, but some characters can shift a fraction of a pixel. * When disabled, certain combinations of screen resolution, use of anti-aliasing, and font size can cause the text to appear blurry. In that case, you can improve the appearance of the text with the **Fractional Character Width** and **Character Spacing** properties. |

No |

Yes |
|

Is Value Changing |

Whether the value is currently changing. |

No |

Yes |
|

Maximum Value |

The maximum value that the range allows. |

No |

Yes |
|

Minimum Value |

The minimum value that the range allows. |

No |

Yes |
|

Normalized Value |

The current value normalized to range [0, 1]. |

No |

Yes |
|

Step Value |

The minimum amount that the value of the range can change at a time. |

No |

Yes |
|

Value |

The current value. To update this property with a binding, use a to-source or two-way binding. |

No |

Yes |
|

Horizontal Fit |

Whether to horizontally scale the glyphs to make them fit into the **Layout Width** of the Text Block. To adjust the scale, use the **Horizontal Fit Scale Limits** property. |

No |

Yes |
|

Horizontal Fit Scale Limits |

When the **Horizontal Fit** property is enabled, sets the minimum and maximum scale for glyphs when the width of text in a Text Block does not match the **Layout Width** of that Text Block. For example: * **Min** property field set to 1.0 does not squeeze the glyphs, while 0.5 squeezes the glyphs to half their size. * **Max** property field set to 1.0 does not stretch the glyphs, while 2.0 stretches the glyphs to double their size. |

No |

Yes |
|

Horizontal Padding |

Sets the padding spaces between the content and the left and right boundaries of the Text node. |

No |

Yes |
|

Truncation |

Sets how Kanzi truncates text when either **Truncation** or **Overflow** property is set and the text does not fit in this node: * **None** disables text truncation. * **At character** truncates text character by character. Default value. * **At word** truncates text by entire words.

Kanzi truncates text to fit within the vertical and horizontal limits of the control. If there is not enough vertical space to fit a single line of text, Kanzi truncates all text and does not show overflow characters.  |

No |

Yes |
|

Truncation Direction |

Sets which part Kanzi truncates when either the **Truncation** or **Overflow** property is set and the text does not fit in this node: * **Trailing** truncates single- and multiline text at the end. Default value. * **Center** truncates single-line text in the middle. For multiline text, truncates entire lines from the middle, if the text does not fit in the height of this node, and clips text that does not fit in the width of this node. * **Leading** truncates single-line text in the beginning. For multiline text, truncates entire lines from the beginning, if the text does not fit in the height of this node, and clips text that does not fit in the width of this node. |

No |

Yes |
|

Vertical Padding |

Sets the padding spaces between the content and the top and bottom boundaries of the Text node. |

No |

Yes |
|

Activity Status |

Sets the possible states of the Activity when its Activity Host activates or deactivates that Activity. |

No |

Yes |
|

Active Activity Index |

The index of the active Activity in the Data-Driven Exclusive Activity Host. After instantiating all Activity from a Data Source, this property refers to the only currently active Activity in this Data-Driven Exclusive Activity Host. To deactivate all the Activities in this Data-Driven Exclusive Activity Host, set this property to -1. |

No |

Yes |
|

Activity Source |

The data object that provides the data for this Activity node. |

No |

Yes |
|

Activity Template |

If set, the Data-Driven Exclusive Activity Host uses this prefab for Activity nodes that it creates. |

No |

Yes |
|

Color Font Material |

Sets the material whose shader is used to render the text containing colored glyphs. The shader must use the ContentTexture uniform which is automatically filled with glyph data. |

No |

Yes |
|

Font Material |

Sets the material whose shader is used to render the text. The shader must use the ContentTexture uniform which is automatically filled with glyph data. |

No |

Yes |
|

Selected Item Index |

Sets the index of the item that is currently selected in the List Box node. A List Box node updates this property when the user scrolls that List Box node. To select an item in the List Box node, set this property to the index of the item that you want to select. The indexing starts from 0. To update this property with a binding, use a to-source or two-way binding. |

No |

Yes |
|

Bring Activated Activity To Front |

Sets whether to show the activated Activity in front within its Parallel Activity Host. This property affects the z-order of the activated Activity within the same Activity priority layer: * When enabled, the Activity is shown in front. * When disabled, the z-order of the activated child Activity is determined by the order in which you added that Activity to the parent Parallel Activity Host. This is the default behavior. |

No |

Yes |
|

Word Wrap |

Sets whether to break long lines into multiple lines to make the text fit within the boundaries of the Text Block node. |

No |

Yes |
|

Controller Property |

Sets the property type that the Exclusive Activity Host node uses to switch between its child Activity nodes. |

No |

Yes |
|

Data Source Controller Property Path |

Sets the path in the Data Source object of an Exclusive Activity Host node to a Data Object item that the Exclusive Activity Host node uses as the Controller Property. |

No |

Yes |
|

Character Spacing |

Sets the character spacing in pixels. |

No |

Yes |
|

Fixed Character Width |

When set, overrides the font advance widths to make each character take a fixed amount of space specified in pixels. |

No |

Yes |
|

Font Family |

The font family used to render the text. |

No |

Yes |
|

Font Hinting Preference |

Sets the hinting preference of the font. * **No hinting**: Render text without hinting the outlines of glyphs. * **Native hinting**: Prefer native hinter of the font over the auto-hinter of the rasterizer. * **Auto hinting**: Prefer auto-hinter of the rasterizer over the native hinter of the font. |

No |

Yes |
|

Font Size |

Sets the size of the font in pixels. |

No |

Yes |
|

Font Style |

Sets the style of the font. |

No |

Yes |
|

Font Weight |

Sets the weight of the font. |

No |

Yes |
|

Fractional Character Width |

Sets whether Kanzi uses fractional or rounded character widths to lay out text. In most cases fractional widths provide the best result. However, with small font sizes, fractional widths can cause the characters to run together or have too much space, making it difficult to read. * When enabled, Kanzi uses fractional character widths, which means that the spacing between characters varies and can be a fraction of a pixel. * When disabled, Kanzi uses character widths rounded to the nearest pixel. Disable fractional widths when you want to fix character spacing in whole-pixel increments and prevent characters in small font sizes from running together. |

No |

Yes |
|

Line Spacing |

Sets the line spacing in multiples of the normal line height of the selected font. |

No |

Yes |
|

Overflow |

Sets the characters that represent the truncated text when the text does not fit in this node. The default value is ââ¦â. By default, Kanzi truncates the text at the end. Use the **Truncation Direction** property to set the part of the text that you want to truncate.

Kanzi truncates text to fit within the vertical and horizontal limits of the control. If there is not enough vertical space to fit a single line of text, Kanzi truncates all text and does not show the **Overflow** characters.  |

No |

Yes |
|

Remove Side Bearings |

Whether to position the leftmost characters of left-aligned text and rightmost characters of right-aligned text exactly within the boundary of the text node. |

No |

Yes |
|

Text |

Sets the text content that the text node renders. To create a line break press Shift+Enter. |

No |

Yes |
|

Text Horizontal Alignment |

Sets the horizontal alignment of the text. |

No |

Yes |
|

Text Vertical Alignment |

Sets the vertical alignment of the text. |

No |

Yes |
|

Show Material Debug Objects |

When enabled, Kanzi Studio does not hide material debug objects. |

No |

No |
|

Opacity |

Opacity of the node. |

No |

Yes |
|

Brush Modulate Color |

Modulation color for brush. Effects brush rendering that needs color modulation. |

No |

Yes |
|

Brush Horizontal Tiling |

Horizontal Tiling for the brush. Affects the scale of texture coordinates. |

No |

Yes |
|

Brush Vertical Tiling |

Vertical Tiling for the brush. Affects the scale of texture coordinates. |

No |

Yes |
|

Custom Asset Thumbnail |

When enabled, the asset will have selected image as thumbnail instead of the generated one. |

No |

No |
|

Export in Asset Package |

When enabled, this item is exported into asset package if this project is saved as one. |

No |

No |
|

Background Brush |

The background brush to paint the background of 2D nodes. |

No |

Yes |
|

Effect |

Reports the runtime effect instance that this node uses. Kanzi sets the value of this property internally when the value of the Effect Prefab property in this node changes. |

No |

Yes |
|

Effect Prefab |

The 2D Effect to use for this node. |

No |

Yes |
|

Image |

The image to display. |

No |

Yes |
|

Content Stretch |

Sets how the content that belongs to this node is stretched (as opposed to manipulating the actual node size). |

No |

Yes |
|

Aspect Ratio |

Determines the proportion of width and height. You cannot set both the Aspect Ratio and both, Width and Height. |

No |

Yes |
|

Force Composition |

Force rendering to composing target even if not otherwise necessary. |

No |

Yes |
|

Snap to Pixel |

Snap the translation of the node and its size into pixel boundary. |

No |

Yes |
|

Cache Valid |

Indicates whether the node is cached. To disable the cache for one frame, disable this property. |

No |

Yes |
|

Caching Mode |

Sets the caching mode of this node: * **Disabled** sets Kanzi to render the node and its descendants normally, without caching. This is the default. * **Enabled** sets Kanzi to cache the node and its descendants and render the node from the cache image until you invalidate the cache by disabling the **Cache Valid** property. * **Automatic** sets Kanzi to automatically update the cache of the node whenever the content of the node or its descendants change. |

No |

Yes |
|

Disable Render Target Clear Color |

Do not clear render target buffers before rendering into it even if necessary. |

No |

Yes |
|

Mipmap Mode |

Sets the mipmap mode to use with the temporary composition targets to which Kanzi renders this node. |

No |

Yes |
|

Off-Screen Rendering |

When set and the node has an explicitly set render target, do not render the resulting framebuffer to screen. |

No |

Yes |
|

Pixel Format |

The pixel format of the node if rendering to a texture. |

No |

Yes |
|

Render Self |

Whether the node renders itself. Does not affect the rendering of child nodes. |

No |

Yes |
|

Render Target |

Forces the node to be rendered into a given render target texture. When set to âNo Targetâ, regular conditions whether node is rendered to a texture, such as opacity and rotation, are applied. |

No |

Yes |
|

Render Target Minimum Height |

Sets the minimum height of implicitly generated render targets. |

No |

Yes |
|

Render Target Minimum Width |

Sets the minimum width of implicitly generated render targets. |

No |

Yes |
|

Render Target Reallocation Limit |

The change in size that triggers reallocation of a render target. |

No |

Yes |
|

Layout Transformation |

The 2D transformation to be applied before layouting. |

No |

Yes |
|

Perspective Transformation |

The 3D transformation to be applied after layouting. |

No |

Yes |
|

Perspective Transformation FOV |

The 3D transformation field of view (degrees) to be applied after layouting. |

No |

Yes |
|

Perspective Transformation Mode |

Defines the mode of operation for the coordinate system and field of view. |

No |

Yes |
|

Perspective Transformation Origin |

The 3D transformation origin to be used for perspective transformation on this or child nodes. |

No |

Yes |
|

Perspective Transformation Pivot |

The 3D pivot point in relative coordinates. |

No |

Yes |
|

Render Transformation |

The 2D transformation to be applied after layouting. |

No |

Yes |
|

Render Transformation Origin |

Sets the render transform origin in relative coordinates. |

No |

Yes |
|

Camera |

Sets which camera to use in scenes rendered by the selected Viewport 2D. If not set, Kanzi uses the camera in the scene. |

No |

Yes |
|

Hit Test Camera |

Sets which hit test camera to use in scenes rendered by the selected Viewport 2D. If not set, Kanzi uses the camera in the scene. |

No |

Yes |
|

Render Pass Prefab |

Sets which render pass prefab will be used to instantiate the render pass tree. |

No |

Yes |
|

Direction |

Defines the axis along which the stack layout arranges its items. |

No |

Yes |
|

Reversed |

Defines whether the stack layout arranges its items in reverse order. |

No |

Yes |
|

Horizontal Alignment |

The alignment in horizontal direction the node should use when it resides under a layout. |

No |

Yes |
|

Vertical Alignment |

The alignment in vertical direction the node should use when it resides under a layout. |

No |

Yes |
|

Command |

The command executed by a UI control |

No |

Yes |
|

Item Index |

Reports the index of the item in the List Box Item Container. |

No |

Yes |
|

Selected |

Indicates whether the List Box item held by this List Box Item Container is selected. The List Box sets the value of this property. |

No |

Yes |
|

Hover |

Indicates whether a node is the foremost hit testable node under the cursor. |

No |

Yes |
|

Enabled |

Whether to apply this effect. |

No |

Yes |
|

Content Gradient |

Sets the gradient along which the content fades out: * **Start** sets the minimum intensity at which the content starts to fade out. * **Softness** sets the difference in intensity it takes for the content to disappear.

For a perfectly smooth gradient, set **Start** to 0 and **Softness** to 1. The default value [ 0.0, 0.19 ] makes the content fade out quickly before the outline fade-out starts.  |

No |

Yes |
|

Content Mask |

Sets the color that masks color components relevant to the outline calculation. The comparison value is the result of a dot product between the mask and the content RGBA color value. By default Kanzi calculates the outline only from the alpha value. |

No |

Yes |
|

Content Threshold |

Sets the threshold at which the value Kanzi calculates using the content mask is considered valid. When the value calculated from masking the content exceeds this value, that pixel is part of the outlined area. |

No |

Yes |
|

Invert Content Mask |

Whether to invert the value that Kanzi calculates using content masking. |

No |

Yes |
|

Outline Inner Softness |

Sets the softness of the outline relative to its width inside the content area. For a sharp outline, set to 0. For a fade-in that takes the complete outline width to reach maximum value, set to 1. By default, this property uses the value of the **Outline Softness** property. |

No |

Yes |
|

Outline Inner Width |

Sets the width of the outline in pixels inside the content area. By default, this property uses the value of the **Outline Width** property. |

No |

Yes |
|

Outline Method |

Sets the method for outline calculation: * **Box** uses box search which potentially consumes less memory but is slower. * **Two-pass** uses two-pass search which potentially consumes more memory but is faster. This the default. |

No |

Yes |
|

Outline Texture Offset |

Sets the relative starting offset for sampling the outline texture. The default value is 0.0. |

No |

Yes |
|

Outline Texture Tiling |

Sets the number of times the texture wraps around within the outline area. To repeat a texture, set its **Wrap Mode** to **Repeat**. The default value is 1.0 |

No |

Yes |
|

Blur Quality |

Sets the visual quality of the blur. Lower quality uses less computing and memory resources. |

No |

Yes |
|

Blur Radius |

Sets the amount of blur by defining the radius of the circular area of pixels that blend into each other. The blur radius also determines the distance in pixels that the blur expands the render area by extending outward from an edge, unless you enable the **Masked Blur** property. To disable the blur effect, set this property to 0. The default value is 8. |

No |

Yes |
|

Masked Blur |

Sets whether to blur only the pixels whose alpha channel value is not zero. When you enable this property, the blur does not spread to fully transparent pixels and the edges of the content stay sharp. The default value is false. |

No |

Yes |
|

Invert Mask |

Whether to invert the mask so that transparent areas become opaque and opaque areas become transparent. |

No |

Yes |
|

Mask Channel |

Sets the texture channel to use as the input for the mask: * **Alpha** uses the alpha channel from the texture. This is the default. * **Red** uses the red color channel from the texture. * **Green** uses the green color channel from the texture. * **Blue** uses the blue color channel from the texture. * **Luminance** uses the luminance calculated from the red, green, and blue channels. |

No |

Yes |
|

Mask Height |

Sets the height of the mask to use in a layout. This value overrides the height of the texture that you use as the mask. |

No |

Yes |
|

Mask Horizontal Alignment |

Sets the horizontal alignment of the mask effect: * **Left** aligns the left edge of the mask with the left edge of the node. This is the default. * **Right** aligns the right edge of the mask with the right edge of the node. * **Center** aligns the mask horizontally to the center of the node. * **Stretch** stretches the mask horizontally to fit the node from the left edge to the right edge. |

No |

Yes |
|

Mask Offset |

Sets the mask offset along the X and Y axes in pixels. Kanzi applies the mask offset after stretch, alignment, and scale. |

No |

Yes |
|

Mask Scale |

Sets the factor by which to scale the mask. Kanzi applies the scale after stretch and alignment. |

No |

Yes |
|

Mask Strength |

Sets the strength of the mask effect in the range from 0 to 1: * 0 disables the mask effect. * 1 applies the mask at full strength. This is the default. * Any value between 0 and 1 partially applies the mask as if the non-masked result was blended with the fully masked version. |

No |

Yes |
|

Mask Stretch |

Sets the stretch mode of the mask effect: * **None** disables stretching. This is the default. * **Fill** stretches the mask to fill the node. * **Uniform** stretches the mask using uniform scaling to fill the node in either vertical or horizontal direction, whichever requires smaller scale. * **Uniform To Fill** stretches the mask using uniform scaling to fill the node in either vertical or horizontal direction, whichever requires larger scale. * **Repeat** does not stretch the mask, and allows the mask to repeat outside of its area based on the mask texture wrap mode. |

No |

Yes |
|

Mask Texture |

Sets the mask texture. The default is no texture. |

No |

Yes |
|

Mask Vertical Alignment |

Sets the vertical alignment of the mask effect: * **Bottom** aligns the bottom edge of the mask with the bottom edge of the node. * **Top** aligns the top edge of the mask with the top edge of the node. This is the default. * **Center** aligns the mask vertically to the center of the node. * **Stretch** stretches the mask vertically to fit the node from the top edge to the bottom edge. |

No |

Yes |
|

Mask Width |

Sets the width of the mask to use in a layout. This value overrides the width of the texture that you use as the mask. |

No |

Yes |
|

Use Screen Space |

Whether to layout the mask relative to the screen instead of the node. |

No |

Yes |
|

Outline Color |

Sets the color of the outline. |

No |

Yes |
|

Outline Softness |

Sets the softness of the outline. For a sharp outline, set to 0. For a fade-in that takes the complete outline width to reach maximum value, set to 1. The default value is 0.27. |

No |

Yes |
|

Outline Texture |

Sets the texture to apply to the outline. Kanzi applies to the outline only the top row of pixels from this texture. Set **Outline Color** to the color with which you want to modulate the colors in this texture. |

No |

Yes |
|

Outline Width |

Sets the width of the outline in pixels outside the content area. The default value is 4 pixels. |

No |

Yes |
|

Override Shadow Offset |

Sets the offset of the shadow from the object along the x and y axes in pixels. When you set this property, the **Shadow Angle** and **Shadow Distance** properties have no effect. To disable the offset override, remove this property. |

No |

Yes |
|

Shadow Angle |

Sets the direction of the shadow as an angle relative to the positive x axis. The default is 45 degrees. When you set the **Override Shadow Offset** property, this property has no effect. |

No |

Yes |
|

Shadow Blur Radius |

Sets the softness of the shadow by defining the distance in pixels the shadow blur extends outward from an edge. For a shadow with sharp edges, set to 0. The default is 8 pixels. |

No |

Yes |
|

Shadow Color |

Sets the color and alpha of the shadow. |

No |

Yes |
|

Shadow Distance |

Sets how far to move the shadow from the object in the direction set by the **Shadow Angle** property. The default is 10 pixels. When you set the **Override Shadow Offset** property, this property has no effect. |

No |

Yes |
|

Shadow Only |

Whether to render only the shadow without the node contents. |

No |

Yes |
|

Shadow Quality |

Sets the visual quality of the shadow. Lower quality uses less computing and memory resources. |

No |

Yes |
|

Shadow Type |

Sets the type of the shadow: * **Drop Shadow** appears behind or below objects. * **Inner Shadow** appears inside objects. |

No |

Yes |
|

Calculated Offset |

Reports the current relative offset of an item in the Grid List Box in proportional range [0, 1]. |

No |

Yes |
|

Visible Amount in Parent |

Sets the amount the node is inside its parent. Use the value of this property in shaders to implement fades. Calculated by the parent node. |

No |

Yes |
|

Calculated Offset |

Reports the current offset of an item in a Trajectory Layout in the proportional range [0, 1]. |

No |

Yes |
|

Side |

The docking side of an item in the dock layout. |

No |

Yes |
|

Focus Order |

Sets the focus chain order of the node within the focus scope. |

No |

Yes |
|

Cyclic Focus Navigation |

Sets whether the focus chain navigation within the focus scope is cyclic. When you enable this property: * When the user navigates in the forward direction and the focus reaches the last focusable UI element of the focus scope, the focus navigation moves to the first focusable UI element. * When the user navigates in the backward direction and the focus reaches the first focusable UI element of the focus scope, the focus navigation moves to the last focusable UI element. |

No |

Yes |
|

Column |

The column into which grid layout places the item. |

No |

Yes |
|

Column Span |

Defines the number of columns an item in a grid layout occupies. |

No |

Yes |
|

Row |

The row into which grid layout places the item. |

No |

Yes |
|

Row Span |

Defines the number of rows an item in a grid layout occupies. |

No |

Yes |
|

Stretch |

Whether to scale this Trajectory Layout to match the layout size. |

No |

Yes |
|

Trajectory Override Offset |

Sets the offset of an item in a Trajectory Layout. When you do not set this property, the Trajectory Layout sets the offset. |

No |

Yes |
|

Toggle State |

Sets the toggle state of a Toggle Button. To update this property with a binding, use a to-source or two-way binding. |

No |

Yes |
|

Toggle State Count |

Sets the number of toggle states of a Toggle Button. |

No |

Yes |
|

Auto Press Interval |

Sets the time in milliseconds after which a button that the user keeps pressed down sends the Button: Click message. While the user holds the button down, the button keeps sending the Button: Click message at the time interval set by this property. To disable the behavior, set to 0. |

No |

Yes |
|

Down On Hover |

Whether holding a finger on the device screen and moving it over the button transitions the button to the down state. |

No |

Yes |
|

Hold Interval |

Sets the amount of time in milliseconds that the user must hold the button pressed down for Kanzi to recognize it as a long-press gesture. To disable the long-press gesture, set to 0. |

No |

Yes |
|

Is Down |

Indicates whether the button is pressed and in the down state. |

No |

Yes |
|

Index In Group |

Sets the index of the Toggle Button in the Toggle Button Group to which that Toggle Button is registered. If a Toggle Button does not have a local value for this property, it is not registered to the ancestor Toggle Button Group. When set to -1, the Toggle Button Group assigns an index for the Toggle Button. |

No |

Yes |
|

Focus Scope Type |

Sets the type of the focus scope node: * **Group** groups focusable nodes. * **Fence** keeps the focus chain navigation inside the scope and does not allow the focus chain navigation to enter or leave that scope. * **Modal** overlay blocks the key and touch input that originates outside of its boundaries and keeps the focus navigation within the scope boundaries. * **Auto-Closing Modal** overlay loses focus when key or touch input originates from a node that is outside of its node tree, and suppresses that input. * **Modeless** overlay propagates the key and touch input that originates outside of its boundaries to the nodes outside of its boundaries. * **Auto-Closing Modeless** overlay loses focus when key or touch input originates from a node that is outside of its boundaries, and propagates that input. |

No |

Yes |
|

Blend Mode |

Sets how to combine the color and alpha values of pixels in one layer or image with those in the underlying layer or image. |

No |

Yes |
|

Focus State |

Reports the focus state of a node: * **No focus** (0) indicates that the node is not focused. For a focus scope node indicates that none of the nodes in the scope have focus. * **Logical focus** (1) indicates that the node is the logical focus node of an overlay-type focus scope. For a focus scope node indicates that one of the nodes in that scope is the logical focus node. * **Key focus** (2) indicates that the node is the key focus node of the application and receives key input. For a focus scope node indicates that one of the nodes in that scope is the key focus node.

Use this property in state managers and bindings to implement focus states in the UI nodes.

To observe whether a node is the key focus node, you can use the boolean **Focus** > **Focused** property.  |

No |

Yes |
|

Hit Testable |

When enabled, the node can be hit tested. Enabling Hit Testable for a 2D node enables hit testing only for that node. Enabling Hit Testable for a 3D node enables hit testing also for the child nodes. Kanzi hit tests 3D nodes using the default Camera node or the Hit Test Camera node of the active Scene node. |

No |

Yes |
|

Effectively Enabled |

Indicates whether this node and its ancestor nodes are enabled. Use this property in state managers and bindings to observe whether a node is effectively enabled. To enable or disable a node, use the Enabled property. When a node is effectively disabled: * When that node is focused, it receives key input until the focus moves to another node. * When that node is not focused, it is not part of the focus chain and does not receive key input. |

No |

Yes |
|

Enabled |

Whether this node is enabled. When you disable this property in a node, that node and its descendant nodes in the same overlay focus scope are effectively disabled. Effectively disabling a node removes that node from the focus chain and cancels all the active input manipulators.Use the Effectively Enabled property to observe whether a node is effectively enabled. |

No |

Yes |
|

Clip Children |

Sets whether to clip the child nodes of this node. Kanzi clips the child nodes whose bounding box is completely outside of the bounding box of their parent node. Use this property with layout nodes. The child nodes can use only translation transformation. |

No |

Yes |
|

Visible |

When disabled, Kanzi does not render the node. |

No |

Yes |
|

Focusable |

Indicates whether the node can receive focus. |

No |

Yes |
|

Focus On Press |

Sets where to set the focus when the user presses the node that has this property: * **None** (0) keeps the focus where it was. This is the default. * **Node** (1) sets the focus to the node. * **Node or ancestor** (2) sets the focus to the node or, if that fails, to the closest focusable ancestor node. * **Node or overlay** (3) sets the focus to the node or, if that fails, to the closest ancestor overlay scope, which then forwards the focus according to its settings.

The descendants of the node where you set this property inherit value of the property.  |

No |

Yes |
|

Transition Phase |

The phase of the transition. For example, use for pixel-based effects. |

No |

Yes |
|

Multisample Level |

Sets the amount of multisample anti-aliasing to apply to the temporary composition targets to which Kanzi renders this node. |

No |

Yes |
|

Description |

Add a description of the purpose of this item. To export descriptions to a plain text file, select File > Export > Export Descriptions. When you export the kzb file, this description is not included in the exported file. |

No |

No |
|

Composition Brush |

The brush to use to compose 2D nodes to screen. |

No |

Yes |
|

Foreground Hint |

Give a hint of the type of the foreground of 2D nodes: * **None** renders the background brush after rendering the node. * **Translucent** renders the background brush before the content of the node. * **Occluding** renders the background brush. |

No |

Yes |
