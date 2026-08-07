---
title: All node and resource properties and messages
source: https://docs.kanzi.com/4.1.0/en/reference/all-node-and-resource-properties-messages.html
---

# All node and resource properties and messages

Here you can find all properties and messages for nodes and resources. See individual node an resource reference to find out whether a property or message is available for a specific node or resource type.
## Properties

|

2D to 3D Projection Scale |

Sets the scale factor to project pixels to 3D size. When scale is 1, then the size of one pixel is one 3D space unit. |

No |

Yes |
|

A |

Tonemapping parameter A. |

No |

Yes |
|

Acceleration Structure |   |

No |

Yes |
|

Activation State |

The state of this Page node: false (inactive and invisible) or true (active and visible) (read-only). |

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

Activity Status |

Sets the possible states of the Activity when its Activity Host activates or deactivates that Activity. |

No |

Yes |
|

Activity Template |

If set, the Data-Driven Exclusive Activity Host uses this prefab for Activity nodes that it creates. |

No |

Yes |
|

Actual Layout Depth |

The calculated size of the node in depth direction when used in a layout. |

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

Addressing Mode |

Sets how Kanzi handles the texture coordinates of the automatically generated composition target textures outside of the [0, 0] - [1, 1] rectangle: * **Repeat** sets the texture to repeat outside of these coordinates. This is the default value. * **Mirror** sets the texture to repeat, but mirrors every other repetition. * **Clamp** confines the texture to these coordinates and outside of these texture coordinates repeats the edge texels of the texture. * **Mirror once** sets the texture to repeat once in the negative direction, and after that clamps the texture. |

No |

Yes |
|

Align To Tangent |

Whether to align the items in this Trajectory Layout to match the tangent of the trajectory. Vertical trajectories are not supported. |

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

Allowed Scroll Axis |

Sets the axis on which you want to allow this Scroll View node to scroll. |

No |

Yes |
|

Alpha Cutoff |

Sets the cutoff threshold for alpha cutting. If the alpha value is less than the value of this property, Kanzi discards the fragment. The default value is 0.5. |

No |

Yes |
|

Alpha To Coverage Enabled |

Sets whether Alpha To Coverage is enabled or not. |

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

Amount |

Sets the chromatic aberration amount. |

No |

Yes |
|

Angle |

Angle of the center point of the arc |

No |

No |
|

Angle |

The angle in which the trajectory opens |

No |

No |
|

Angle |

Angle of the center point of the ellipse |

No |

No |
|

Angle |

The angle of the circleâs starting point |

No |

No |
|

Animated Object |

The target node for the animation, relative to where the sequence is invoked. To use an absolute path, set the scope from the sequence properties (Reference for Absolute paths). |

No |

No |
|

Anisotropy |

Anisotropy of texture. |

No |

No |
|

Application Export Directory |

Directory into which KZB Player version of the project is exported. |

No |

No |
|

Arc Angle |

The angle of the arc |

No |

No |
|

Aspect Ratio |

Sets the aspect ratio of the camera. |

No |

Yes |
|

Aspect Ratio |

Determines the proportion of width and height. You cannot set both the Aspect Ratio and both, Width and Height. |

No |

Yes |
|

ASTC Block Size |

The block size in pixels when compressing the image. The less pixels in the block, the better the quality of the compressed image and the bigger the file size. |

No |

No |
|

ASTC Compression Speed |

The compression speed when compressing the image. Use faster compression for fast and good results and slower compression for better quality. |

No |

No |
|

ASTC Profile |

The ASTC profile to be used. |

No |

No |
|

Asymmetric FOV |

Sets the field of view of the camera in degrees toward the left, right, up, and down. Angles to the right of the center and upwards of the center are positive. To use this property, set the **Projection Type** to **Asymmetric perspective**. |

No |

Yes |
|

Attributes |

The vertex attributes that the shader expects to find in the vertex buffer of the models that use materials of this material type. For example, this includes the position, normal, and texture coordinates of the vertices. If the names of the attributes in models do not match the names of the attributes in the shader, you must map the names manually. |

No |

No |
|

Auto Press Interval |

Sets the time in milliseconds after which a button that the user keeps pressed down sends the Button: Click message. While the user holds the button down, the button keeps sending the Button: Click message at the time interval set by this property. To disable the behavior, set to 0. |

No |

Yes |
|

Auto Size to Content |

When the setting is on, clip is automatically resized to cover all the keyframes in the member animations when keyframes are added and removed |

No |

No |
|

B |

Tonemapping parameter B. |

No |

Yes |
|

Back Length |

Back length of the trapezoid trajectory |

No |

No |
|

Background Brush |

The background brush to paint the background of 2D nodes. |

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

Baseline |

Font baseline in 3D space units. |

No |

Yes |
|

Basis Universal Texture Mode |

The Basis Universal texture mode to be used. |

No |

No |
|

Binary Export Directory |

Directory name for the KZB files |

No |

No |
|

Binary File Name |

Name for the binary (KZB) file. <projectname>.kzb by default |

No |

No |
|

Bit Depth |

The bit depth of the image on disk (Read-only) |

No |

No |
|

Blend Intensity |

Controls the intensity of materials that are blended on top of an existing color. Attached property enables overriding of the blend intensity of the used materials at render pass or object node level. |

No |

Yes |
|

Blend Mode |

Sets how to combine the color and alpha values of pixels in one layer or image with those in the underlying layer or image. |

No |

Yes |
|

Blend Mode |

Overrides the blend mode set in each node that this render pass renders. |

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

Blue Noise |   |

No |

Yes |
|

Blur Direction |

Sets the direction for the blur. |

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

Blur Radius |

Blur radius for the material. |

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

BRDF Lookup Table |

Gets the Bidirectional Reflectance Distribution Function (BRDF) lookup table for the material. The BRDF table is a texture that contains precomputed information about how light reflects off a material. You can use it to improve rendering quality. |

No |

Yes |
|

Bring Activated Activity To Front |

Sets whether to show the activated Activity in front within its Parallel Activity Host. This property affects the z-order of the activated Activity within the same Activity priority layer: * When enabled, the Activity is shown in front. * When disabled, the z-order of the activated child Activity is determined by the order in which you added that Activity to the parent Parallel Activity Host. This is the default behavior. |

No |

Yes |
|

Brush Color |

Color for brush. Set alpha to 0 to disable brush. |

No |

Yes |
|

Brush Horizontal Tiling |

Horizontal Tiling for the brush. Affects the scale of texture coordinates. |

No |

Yes |
|

Brush Modulate Color |

Modulation color for brush. Effects brush rendering that needs color modulation. |

No |

Yes |
|

Brush Texture |

Texture for brush. |

No |

Yes |
|

Brush Type |

The type of the brush. |

No |

No |
|

Brush Vertical Tiling |

Vertical Tiling for the brush. Affects the scale of texture coordinates. |

No |

Yes |
|

C |

Tonemapping parameter C. |

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

Calculated Camera Matrix |

The camera matrix that the render pass calculates during rendering from the settings of the Camera and passes to the shader. |

No |

Yes |
|

Calculated Camera Position |

The camera position that the render pass calculates during rendering from the settings of the Camera and passes to the shader. |

No |

Yes |
|

Calculated Homogeneous View Position |

The homogeneous view position that the render pass calculates during rendering from the settings of the Camera and passes to the shader. |

No |

Yes |
|

Calculated Offset |

Reports the current relative offset of an item in the Grid List Box in proportional range [0, 1]. |

No |

Yes |
|

Calculated Offset |

Reports the current offset of an item in a Trajectory Layout in the proportional range [0, 1]. |

No |

Yes |
|

Calculated Projection Matrix |

The projection matrix that the render pass calculates during rendering from the settings of the Camera and passes to the shader. |

No |

Yes |
|

Calculated Projection Near And Far Planes |

The distances to the camera near and far planes that the render pass calculates during rendering from the settings of the Camera and passes to the shader. |

No |

Yes |
|

Camera |

Sets which camera to use in scenes rendered by the selected Viewport 2D. If not set, Kanzi uses the camera in the scene. |

No |

Yes |
|

Camera |

Sets the camera through which the Kanzi application shows the Scene. |

No |

Yes |
|

Camera |

Sets the Camera node that you want to use to render the nodes. To use the default Camera node in that Scene node, do not set the value for this property. |

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

Center Image |

The image to use in the center. |

No |

Yes |
|

Character Spacing |

Sets the character spacing in pixels. |

No |

Yes |
|

Clamp Pixels |

Clamp the color channel maximum to the value. For SDR images the effective range is 0 to 1, and for HDR images any non-negative value. If one color channel needs to be clamped, then all other color channels are scaled down by the same ratio. |

No |

No |
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

Clear Color 0 |

Sets the color that you want the Clear render pass to use to clear the first (default) color buffer. |

No |

Yes |
|

Clear Color 1 |

Sets the color that you want the Clear render pass to use to clear the second color buffer. |

No |

Yes |
|

Clear Color 2 |

Sets the color that you want the Clear render pass to use to clear the third color buffer. |

No |

Yes |
|

Clear Color 3 |

Sets the color that you want the Clear render pass to use to clear the fourth color buffer. |

No |

Yes |
|

Clear Depth |

Sets the depth that you want the Clear render pass to use to clear the depth buffer. |

No |

Yes |
|

Clear Stencil |

Sets the clear stencil that you want the Clear render pass to use to clear the stencil buffer. |

No |

Yes |
|

Clip Children |

Sets whether to clip the child nodes of this node. Kanzi clips the child nodes whose bounding box is completely outside of the bounding box of their parent node. Use this property with layout nodes. The child nodes can use only translation transformation. |

No |

Yes |
|

Cluster Materials |

Materials for each of the clusters in the model. |

No |

No |
|

Code Behind Source |

Sets the metaclass name of the code behind class for this node. |

No |

Yes |
|

Color Font Material |

Sets the material whose shader is used to render the text containing colored glyphs. The shader must use the ContentTexture uniform which is automatically filled with glyph data. |

No |

Yes |
|

Color Format in Raw |

The color format of the image in the kzb file when using the raw target format. |

No |

No |
|

Color Mipmap Material 0 |

Sets the material to use to generate the mipmaps for the first color result texture (Result Texture 0) of a Composition Target Render Pass. To use the default mipmap generation, remove the property or set it to the default value â< No Material >â. |

No |

Yes |
|

Color Mipmap Material 1 |

Sets the material to use to generate the mipmaps for the second color result texture (Result Texture 1) of a Composition Target Render Pass. To use the default mipmap generation, remove the property or set it to the default value â< No Material >â. |

No |

Yes |
|

Color Mipmap Material 2 |

Sets the material to use to generate the mipmaps for the third color result texture (Result Texture 2) of a Composition Target Render Pass. To use the default mipmap generation, remove the property or set it to the default value â< No Material >â. |

No |

Yes |
|

Color Mipmap Material 3 |

Sets the material to use to generate the mipmaps for the fourth color result texture (Result Texture 3) of a Composition Target Render Pass. To use the default mipmap generation, remove the property or set it to the default value â< No Material >â. |

No |

Yes |
|

Color Workflow |

The color workflow used when Kanzi Studio embeds color into the kzb file: * In Linear mode Kanzi Studio converts all color values to linear color space before exporting them to the kzb file. This is the default. * In Standard mode Kanzi Studio does not modify the color values. When you change the value of this property, the Preview restarts. |

No |

No |
|

Color Write Mode |

Sets which channels the render pass writes to the color buffer. To disable the color write, set the property to None. |

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

Columns |

Defines the number of columns in a grid layout and how the grid layout distributes the content in columns. |

No |

Yes |
|

Command |

The command executed by a UI control |

No |

Yes |
|

Component Type |

The component type of this component node |

No |

No |
|

Composition Background Color |

Sets the color that highlights the text that the user composes using an input method editor (IME). |

No |

Yes |
|

Composition Brush |

The brush to use to compose 2D nodes to screen. |

No |

Yes |
|

Composition Font Color |

Sets the color of the text that the user composes using an input method editor (IME). |

No |

Yes |
|

Composition Target |

Sets the target to which you want to render the result of this Cubemap render pass. |

No |

Yes |
|

Composition Target 0 |

Sets the first color target to which you want to render the result of the child render passes of this render pass. |

No |

Yes |
|

Composition Target 1 |

Sets the second color target to which you want to render the result of the child render passes of this render pass. |

No |

Yes |
|

Composition Target 2 |

Sets the third color target to which you want to render the result of the child render passes of this render pass. |

No |

Yes |
|

Composition Target 3 |

Sets the fourth color target to which you want to render the result of the child render passes of this render pass. |

No |

Yes |
|

Composition Text |

Reports the text that the user composes in the Text Box using an input method editor (IME). |

No |

Yes |
|

Composition Text Background Brush |

Sets the brush that highlights the text that the user composes using an input method editor (IME). |

No |

Yes |
|

Composition Text Foreground Brush |

Sets the brush for the text that the user composes using an input method editor (IME). |

No |

Yes |
|

Constraint In World Coordinates |

Specifies if the object constraining is done in world coordinates (when false, done in local coordinates). |

No |

Yes |
|

Constraint Orientation |

Makes an object node where the property is attached to obtain orientation from target object |

No |

Yes |
|

Constraint Position |

Makes an object node where the property is attached to obtain position from target object |

No |

Yes |
|

Contains ICC Profile |

Whether the image contains the ICC profile. If the image contains an invalid ICC profile, in the Project > Properties enable the Remove ICC Profiles of PNG Images property to remove the ICC profiles from the PNG images during kzb file export. (Read-only) |

No |

No |
|

Contains Transparency |

Whether the image contains transparency. (Read-only) |

No |

No |
|

Content Gradient |

Sets the gradient along which the content fades out: * **Start** sets the minimum intensity at which the content starts to fade out. * **Softness** sets the difference in intensity it takes for the content to disappear. For a perfectly smooth gradient, set **Start** to 0 and **Softness** to 1. The default value [ 0.0, 0.19 ] makes the content fade out quickly before the outline fade-out starts. |

No |

Yes |
|

Content Mask |

Sets the color that masks color components relevant to the outline calculation. The comparison value is the result of a dot product between the mask and the content RGBA color value. By default Kanzi calculates the outline only from the alpha value. |

No |

Yes |
|

Content Stretch |

Sets how the content that belongs to this node is stretched (as opposed to manipulating the actual node size). |

No |

Yes |
|

Content Threshold |

Sets the threshold at which the value Kanzi calculates using the content mask is considered valid. When the value calculated from masking the content exceeds this value, that pixel is part of the outlined area. |

No |

Yes |
|

Controller Property |

Sets the property type that the Exclusive Activity Host node uses to switch between its child Activity nodes. |

No |

Yes |
|

Cubemap Mipmap Material |

Sets the material to use to generate the mipmaps for the color Result Texture of a Cubemap Render Pass. To use the default mipmap generation, remove the property or set it to the default value â< No Material >â. |

No |

Yes |
|

Cubemap Texture |

Sets the cubemap texture you want the Blit render pass to blit. |

No |

Yes |
|

Cull Mode |

Sets the culling of the triangle faces in the rendered meshes: * **Back** renders the triangles whose normal points towards a Camera node. * **Front** renders the triangles whose normal points away from a Camera node. |

No |

Yes |
|

Current Button Index |

The index of the Toggle Button that is toggled on in the Toggle Button Group. To update this property with a binding, use a to-source or two-way binding. |

No |

Yes |
|

Current Mipmap Level |

Reports the mipmap level that Kanzi is generating. Use this property in a material that you use to customize how Kanzi generates mipmaps for the composition targets of a Composition Target Render Pass or Cubemap Render Pass.The value of this property is valid only while Kanzi generates the mipmaps. |

No |

Yes |
|

Cursor Offset |

Sets the offset of the position to use to select the active item, in proportional range [0,1]. |

No |

Yes |
|

Cursor Position |

Sets the position of the cursor in the text shown in the Text Box node. |

No |

Yes |
|

Cursor Prefab |

Sets the prefab template that defines the appearance of the cursor instead of the default cursor. |

No |

Yes |
|

Curve Tesselation Detail |

The number of subdivisions when importing NURBS curves and tesselating them as Kanzi splines |

No |

No |
|

Custom Asset Thumbnail |

When enabled, the asset will have selected image as thumbnail instead of the generated one. |

No |

No |
|

Cutoff |

Sets the angle of the light cone in degrees. |

No |

Yes |
|

Cyclic Focus Navigation |

Sets whether the focus chain navigation within the focus scope is cyclic. When you enable this property: * When the user navigates in the forward direction and the focus reaches the last focusable UI element of the focus scope, the focus navigation moves to the first focusable UI element. * When the user navigates in the backward direction and the focus reaches the first focusable UI element of the focus scope, the focus navigation moves to the last focusable UI element. |

No |

Yes |
|

D |

Tonemapping parameter D. |

No |

Yes |
|

Data Context |

Source of data for this node and its descendants |

No |

Yes |
|

Data Source Controller Property Path |

Sets the path in the Data Source object of an Exclusive Activity Host node to a Data Object item that the Exclusive Activity Host node uses as the Controller Property. |

No |

Yes |
|

Default Build Configuration |

Kanzi Studio uses this configuration to build the project. You can add new build configurations in the Library > Build Configurations. |

No |

No |
|

Default Cubemap Texture |

The cubemap texture that Kanzi Studio uses for new materials that use cubemaps. |

No |

No |
|

Default Material |

The material that is used in newly created models and imported models without a material. |

No |

No |
|

Default Subpage |

The default or the currently active subpage, which Kanzi automatically activates whenever this PageHost node becomes active. |

No |

Yes |
|

Default Texture |

The texture that is used for new Image nodes and materials that use textures. |

No |

No |
|

Default Vertex Attribute Data Type |

The default data type used in model vertex buffers. Half-float decreases mesh data size by half, but decreases the accuracy too. |

No |

No |
|

Denoiser Mode |

Temporal clamping/rejection mode: 0 - none, 1 - reject using depth min max, 2 - reject using filter |

No |

Yes |
|

Depth |

Depth of the trapezoid trajectory |

No |

No |
|

Depth |

The depth of the box (along Z axis) |

No |

No |
|

Depth / Stencil Attachment |

Defines which attachment(s) the render target contains in addition to color. |

No |

No |
|

Depth Alignment |

The alignment in depth direction the node should use when it resides under a layout. |

No |

Yes |
|

Depth Compare Function |

Sets the comparison function to be used with comparison samplers of the Cubemap render passâ depth target. |

No |

Yes |
|

Depth Compare Function |

Sets the comparison function to be used with comparison samplers of the Composition Target render passâ depth target. |

No |

Yes |
|

Depth Format |

Sets the format of the automatically created depth render buffer used for the cubemap rendering. If this property is not set, the depth requirement and format are autodetected. |

No |

Yes |
|

Depth Margin |

Sets the depth distance between this node and other nodes that are adjacent to this node in a layout. To access the Depth Margin property fields in a binding, use: * X for the **Back** property field * Y for the **Front** property field |

No |

Yes |
|

Depth Mipmap Material |

Sets the material to use to generate the mipmaps for the Result Depth Texture of a Composition Target Render Pass. To use the default mipmap generation, remove the property or set it to the default value â< No Material >â. |

No |

Yes |
|

Depth Padding |

Sets the padding spaces between the content and the front and back boundaries of the Content Layout 3D node. |

No |

Yes |
|

Depth Renderbuffer Format |

Sets the format of the automatically created depth renderbuffers. When you do not set this property, Kanzi sets the depth renderbuffer format automatically to the best available format, in most cases the 32-bit float format. To create depth textures, set the **Depth Format** property whose value overrides the value of this property. |

No |

Yes |
|

Depth Renderbuffer Format |

Sets the format of the automatically created depth renderbuffers. When you do not set this property, Kanzi sets the depth renderbuffer format automatically to the best available format, in most cases the 32-bit float format. To create depth textures, set the **Depth Texture Format** property whose value overrides the value of this property. |

No |

Yes |
|

Depth Target |

Sets the target for depth rendering for this Cubemap render pass. |

No |

Yes |
|

Depth Target |

Sets the depth target to which you want to render the result of the child render passes of this render pass. |

No |

Yes |
|

Depth Test Function |

Controls whether the depth test discards a fragment. |

No |

Yes |
|

Depth Texture |   |

No |

Yes |
|

Depth Texture Format |

Sets the format of the automatically created **Result Depth Texture**. |

No |

Yes |
|

Depth Write Enabled |

Sets whether the render pass writes to the depth buffer. |

No |

Yes |
|

Description |

Add a description of the purpose of this item. To export descriptions to a plain text file, select File > Export > Export Descriptions. When you export the kzb file, this description is not included in the exported file. |

No |

No |
|

Descriptions File Name |

Name for the file into which item descriptions are exported by default |

No |

No |
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

Direction |

The direction of the line |

No |

No |
|

Direction |

Defines the axis along which the stack layout arranges its items. |

No |

Yes |
|

Direction |

A hidden property that identifies spotlight direction and contains related metadata. |

No |

Yes |
|

Directional Light |

Directional light settings |

No |

No |
|

Directional Light Color |

Sets the color of the Directional Light. Use the Intensity (I) property field to adjust the brightness of the light. |

No |

Yes |
|

Directional Light Direction |

A hidden property that identifies directional light direction and contains related metadata. |

No |

Yes |
|

Directional Light View Projection |

The premultiplied projection view matrix of a directional light. |

No |

Yes |
|

Directional Lights |

Use this property to bind the directional light set for rendering. |

No |

Yes |
|

Directional Shadow Bias |

Sets the directional shadow bias to reduce sampling artifacts. |

No |

Yes |
|

Directional Shadow Map |

Depth map used to calculate directional shadows. |

No |

Yes |
|

Directional Shadow Softness |

Sets the softness of the shadows cast by the Directional Light. |

No |

Yes |
|

Disable KZB Export |

Disables the exporting of the item into KZB. Can be used for, e.g. letting items out from certain profiles. The disabled items are always included in preview. |

No |

No |
|

Disable Render Target Clear Color |

Do not clear render target buffers before rendering into it even if necessary. |

No |

Yes |
|

Display Text |

Reports the text that the Text Box displays. |

No |

Yes |
|

Dithering Amount |

Sets the chromatic aberration dithering amount. |

No |

Yes |
|

Double-Click Enabled |

Whether to install a multi-click manipulator that generates double-click messages. Use this property to enable the double-click gesture for a Button node or List Box items. To enable double-click for List Box items, enable this property in the List Box Item Container. |

No |

Yes |
|

Down On Hover |

Whether holding a finger on the device screen and moving it over the button transitions the button to the down state. |

No |

Yes |
|

Dragging Acceleration |

Sets the acceleration of the Grid List Box when the user scrolls the Grid List Box by dragging the pointer. The higher the value, the quicker the Grid List Box reaches its final position. The default value is 80. |

No |

Yes |
|

Dragging Acceleration |

Sets the acceleration of the Trajectory List Box 3D when the user scrolls the Trajectory List Box 3D by dragging the pointer. The higher the value, the quicker the Trajectory List Box 3D reaches its final position. The default value is 80. |

No |

Yes |
|

Dragging Acceleration |

Sets the acceleration of the node controlled by a Scroll View node while you drag that Scroll View node. Use low values when you want that node to slowly reach the final position. Use high values when you want that node to quickly reach the final position. |

No |

Yes |
|

Dragging Drag |

Sets the amount that drag affects the movement of the Grid List Box when the user scrolls the Grid List Box by dragging the pointer. The lower the value, the higher the drag and the quicker the scrolling stops. The default value is 150. |

No |

Yes |
|

Dragging Drag |

Sets the amount that drag affects the movement of the Trajectory List Box 3D when the user scrolls the Trajectory List Box 3D by dragging the pointer. The lower the value, the higher the drag and the quicker the scrolling stops. The default value is 150. |

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

Dragging Impulse |

Sets the amount of impulse to generate from the pointer movement when the user scrolls the Grid List Box by dragging the pointer. |

No |

Yes |
|

Dragging Impulse |

Sets the amount of impulse to generate from the pointer movement when the user scrolls the Trajectory List Box 3D by dragging the pointer. |

No |

Yes |
|

Drawn as Bounding Box |

When enabled the object is drawn its solid bounding box. |

No |

Yes |
|

Duration |

The duration of the sequence in seconds. The value is read-only and calculated from the member entries. |

No |

No |
|

Duration Scaling |

Scales the length of animation in the way that small values (< 1) speed the animation up and large values (> 1) slow it down |

No |

No |
|

E |

Tonemapping parameter E. |

No |

Yes |
|

Echo Mode |

Sets how the Text Box node shows text: * **Normal** makes the inserted characters visible. * **No Echo** makes the inserted characters invisible. * **Password** makes the inserted character visible for a certain amount of time and then masks the character. Use the **Password Masking Character** property to set the masking character. The default is a bullet symbol. Use the **Password Echo Timeout** property to set the time in milliseconds that an inserted character is visible before masking. |

No |

Yes |
|

Edit Mode |

Sets how the Text Box node enters the editing state: * **Automatic** makes the Text Box enter the editing state when focused, and leave the editing state when focus is lost. * **Triggered** requires the user to trigger the Text Box to enter and leave the editing state. |

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

Effect Stacking Mode |

Sets how to apply an effect in an Effect Stack 2D: - Chained applies the effect to the result of the previous effect, to the combined result of a sequence of layered effects, or to the node content. The next effect uses as its input the result of this effect. - Layered applies the effect to the result of a previous chained effect or to the node content. A sequence of layered effects are combined on top of each other in layers. This property has no impact on the Mask Effect 2D and Blur Effect 2D effects, which always use the Chained mode. |

No |

Yes |
|

Effective Activity Source |

The data source for this Activity node. |

No |

No |
|

Effective Data Context |

The data context in the current node that is resolved from data context properties and bindings |

No |

No |
|

Effective Screen Size |

Screen Size based on current window settings (Read-only, requires running Preview) |

No |

No |
|

Effectively Enabled |

Indicates whether this node and its ancestor nodes are enabled. Use this property in state managers and bindings to observe whether a node is effectively enabled. To enable or disable a node, use the Enabled property. When a node is effectively disabled: * When that node is focused, it receives key input until the focus moves to another node. * When that node is not focused, it is not part of the focus chain and does not receive key input. |

No |

Yes |
|

Effort |

Quality of the ETC2 compression, 100 for the highest quality. |

No |

No |
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

Enabled |

Whether Kanzi executes this render pass and its child render pass tree. |

No |

Yes |
|

Enabled |

Whether this node is enabled. When you disable this property in a node, that node and its descendant nodes in the same overlay focus scope are effectively disabled. Effectively disabling a node removes that node from the focus chain and cancels all the active input manipulators.Use the Effectively Enabled property to observe whether a node is effectively enabled. |

No |

Yes |
|

Enabled |

Whether to apply this effect. |

No |

Yes |
|

End Radius |

End radius of the spiral |

No |

No |
|

End Time |

The ending time of the clip. |

No |

No |
|

End Time |

The ending time of the global timeline. |

No |

No |
|

Engine Factory Name |

The factory name for this composer. Can be used to instantiate composer or render pass from plugin. |

No |

No |
|

Entry Weight |

The weight ratio of this entry among all entries |

No |

No |
|

Environment Ambient Factor |

Sets the strength of the cubemap texture to use for ambient environment light. Use the Environment Ambient Texture property to set the cubemap texture. The ambient environment light affects diffuse lighting in image based lighting. |

No |

Yes |
|

Environment Ambient Texture |   |

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

ETC1S Encoding Level |

Set ETC1S encoding level. Use faster compression for fast and good results and slower compression for better quality. |

No |

No |
|

Exclusive Activity Host Content |

Describes the content of an Exclusive Activity Host node. An Exclusive Activity Host uses the value of this property to instantiate Activity prefabs and control the status and lifetime of its child Activities. Kanzi Studio user cannot directly edit this property. The ActivityBrowserController sets the value of this property according to the changes done to the state of the Activity Tree in the ActivityBrowser. The expected format for the property value is the name of the Activity that the Exclusive Activity Host initially activates, followed by a list of Activity descriptions. Each of this Activity description contains: The name of the Activity * The ControllerProperty reference value of the Activity * The path to the prefab of that Activity. The values in this property must be separated by a comma. For example, {name0,{name1,666,path1},{name2,123,path2}}. |

No |

Yes |
|

Exponent |

Defines how fast a fully lit area at the center of the light cone turns into an unlit area. |

No |

Yes |
|

Export Behavior |

Whether to export the image always or only when it is used by other assets in the Kanzi Studio project. Set this as âExport Alwaysâ when the image is used by the application code. |

No |

No |
|

Export Empty When File Is Missing |

Whether to export empty or default image when file is missing. |

No |

No |
|

Export in Asset Package |

When enabled, this item is exported into asset package if this project is saved as one. |

No |

No |
|

Export Shader Source Code |

If all shaders in the project are binary shaders and you do not use the shader binary cache, you can reduce the size of the kzb file by disabling this property. |

No |

No |
|

Exposure |

Sets the exposure compensation for the material. The exposure compensation emulates camera exposure by controlling the total amount of light rendered. Use a negative value to darken the rendered image, and a positive value to lighten the image. Exposure is exponential: 1.0 is twice as bright as 0.0, and -1.0 is half as bright as 0.0. |

No |

Yes |
|

F |

Tonemapping parameter F. |

No |

Yes |
|

Face to Camera Mode |

Sets how to rotate the 3D node towards a camera: * **Disabled** does not make the node turn to the camera. * **Look at** rotates the node along all axes to turn to the camera. * **Billboarding** keeps the node perpendicular to the camera FOV. * **Cylindrical** rotates the node along the y axis to turn to the camera. By default, the node turns to the Scene default camera. To use a different camera, set the **Face to Camera Target Camera** property. |

No |

Yes |
|

Face to Camera Target Camera |

Sets the camera towards which the 3D node turns when you set the **Face to Camera Mode** property. The default is the Scene default camera. |

No |

Yes |
|

Face Update Rate |

Sets the number of cubemap faces to update each frame or at the rate that you set with the Render Pass > Update Rate property. The default value is 6. |

No |

Yes |
|

Filter |

Sets the filter that the Node List render pass uses to filter or sort a list of incoming nodes. |

No |

Yes |
|

Filter Mode |

Sets how Kanzi handles accessing the texture samples of the automatically generated composition cubemap target: * **Nearest** takes the color from the nearest sample. * **Linear** interpolates color from neighboring samples. This is the default value. |

No |

Yes |
|

Filter Mode |

Sets how Kanzi handles accessing the texture samples of the automatically generated composition target: * **Nearest** takes the color from the nearest sample. * **Linear** interpolates color from neighboring samples. This is the default value. |

No |

Yes |
|

Final Transformation |

The combined location, orientation and scale of the node and its ancestor nodes. Automatically calculated by the system. |

No |

Yes |
|

Fixed Character Width |

When set, overrides the font advance widths to make each character take a fixed amount of space specified in pixels. |

No |

Yes |
|

Focus On Activating Activity |

Sets the policy that this Exclusive Activity Host uses to decide whether it tries to set the key focus to its activating Activity: * **When Host Has Focus**: If the Activity Host has the focus, it tries to set the focus to the Activity. This is the default. * **Always**: The Activity Host always tries to set the focus to the Activity. * **Never**: The Activity Host never tries to set the focus to the Activity. |

No |

Yes |
|

Focus On Activation |

Sets the policy that a Parallel Activity Host uses to decide whether it tries to set the key focus to an activating Activity: * **When Host Has Focus**: If the Activity Host has the focus, it tries to set the focus to the Activity. This is the default. * **Always**: The Activity Host always tries to set the focus to the Activity. * **Never**: The Activity Host never tries to set the focus to the Activity. Set this property in an Activity in a Parallel Activity Host. |

No |

Yes |
|

Focus On Press |

Sets where to set the focus when the user presses the node that has this property: * **None** (0) keeps the focus where it was. This is the default. * **Node** (1) sets the focus to the node. * **Node or ancestor** (2) sets the focus to the node or, if that fails, to the closest focusable ancestor node. * **Node or overlay** (3) sets the focus to the node or, if that fails, to the closest ancestor overlay scope, which then forwards the focus according to its settings. The descendants of the node where you set this property inherit value of the property. |

No |

Yes |
|

Focus Order |

Sets the focus chain order of the node within the focus scope. |

No |

Yes |
|

Focus Scope Type |

Sets the type of the focus scope node: * **Group** groups focusable nodes. * **Fence** keeps the focus chain navigation inside the scope and does not allow the focus chain navigation to enter or leave that scope. * **Modal** overlay blocks the key and touch input that originates outside of its boundaries and keeps the focus navigation within the scope boundaries. * **Auto-Closing Modal** overlay loses focus when key or touch input originates from a node that is outside of its node tree, and suppresses that input. * **Modeless** overlay propagates the key and touch input that originates outside of its boundaries to the nodes outside of its boundaries. * **Auto-Closing Modeless** overlay loses focus when key or touch input originates from a node that is outside of its boundaries, and propagates that input. |

No |

Yes |
|

Focus State |

Reports the focus state of a node: * **No focus** (0) indicates that the node is not focused. For a focus scope node indicates that none of the nodes in the scope have focus. * **Logical focus** (1) indicates that the node is the logical focus node of an overlay-type focus scope. For a focus scope node indicates that one of the nodes in that scope is the logical focus node. * **Key focus** (2) indicates that the node is the key focus node of the application and receives key input. For a focus scope node indicates that one of the nodes in that scope is the key focus node. Use this property in state managers and bindings to implement focus states in the UI nodes. To observe whether a node is the key focus node, you can use the boolean **Focus** > **Focused** property. |

No |

Yes |
|

Focusable |

Indicates whether the node can receive focus. |

No |

Yes |
|

Focused |

Indicates whether the node has the key focus. |

No |

Yes |
|

Font Color |

Sets the color of the text in a 3D text node. |

No |

Yes |
|

Font Engine |

Sets the font engine that Kanzi Studio Preview uses to render text: * FreeType uses the FreeType rasterizer, HarfBuzz shaper, and ICU bidirectional library, and libunibreak for line breaking. This is the default value. * iType uses the Monotype iType rasterizer and WorldTypeÂ® Shaperâ¢ for shaping. * None to not load a font engine. When you do not load a font engine, the Preview does not render the text in your application. |

No |

No |
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

Font Material |

Sets the material whose shader is used to render the text. The shader must use the ContentTexture uniform which is automatically filled with glyph data. |

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

Force Composition |

Force rendering to composing target even if not otherwise necessary. |

No |

Yes |
|

Foreground Brush |

The foreground brush to paint the foreground of 2D nodes. |

No |

Yes |
|

Foreground Hint |

Give a hint of the type of the foreground of 2D nodes: * **None** renders the background brush after rendering the node. * **Translucent** renders the background brush before the content of the node. * **Occluding** renders the background brush. |

No |

Yes |
|

Format |

Defines the target pixel format on the GPU |

No |

No |
|

FOV |

Sets the field of view of the camera in degrees. |

No |

Yes |
|

FOV Type |

Sets the direction of the field of view: * **Y FOV** sets the field of view along the y axis. This is the default. * **X FOV** sets the field of view along the x axis. |

No |

Yes |
|

Fractional Character Width |

Sets whether Kanzi uses fractional or rounded character widths to lay out text. In most cases fractional widths provide the best result. However, with small font sizes, fractional widths can cause the characters to run together or have too much space, making it difficult to read. * When enabled, Kanzi uses fractional character widths, which means that the spacing between characters varies and can be a fraction of a pixel. * When disabled, Kanzi uses character widths rounded to the nearest pixel. Disable fractional widths when you want to fix character spacing in whole-pixel increments and prevent characters in small font sizes from running together. |

No |

Yes |
|

Frustum Cull Margin |

The margin of the frustum cull radius of the node. For example, set the margin when a vertex shader modifies the geometry of the node. To use this property, enable the Frustum Culling property in the Draw Objects Render Pass you use to render the node. |

No |

Yes |
|

Frustum Culling |

Enable to disable rendering objects that are not inside the view frustum. Trades GPU rendering time for CPU cull test time. |

No |

Yes |
|

Full Screen Preview Layer |

Whether or not to display the preview root layer as fullscreen |

No |

No |
|

GBuffer Depth |   |

No |

Yes |
|

GBuffer Normal |   |

No |

Yes |
|

GBuffer Roughness |   |

No |

Yes |
|

Generate Mesh Inside Out |

Whether to flip the windings and normals of the mesh faces. Enable this property when you want to use the mesh as a skybox. |

No |

No |
|

Generate Mipmaps |

Whether or not to generate mipmaps. If the image has mipmaps inside, those will take precedence over generated ones. |

No |

No |
|

Generate Normals |

Generate normals for this primitive |

No |

No |
|

Generate Tangents |

Generate tangents for this primitive |

No |

No |
|

Global Ambient Color |

Sets the color that is multiplied automatically with the Ambient property of the materials in the scene. Use the Intensity (I) property field to adjust the exposure of the color. |

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

GPU Memory Type |

Determines which kind of GPU memory will be used. |

No |

No |
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

Has Selection |

Indicates whether any of the text in the Text Box node is selected. |

No |

Yes |
|

Height |

Height of the spiral trajectory |

No |

No |
|

Height |

Relative height of the window (0,1] |

No |

No |
|

Height |

The height of the box (along Y axis) |

No |

No |
|

Height |

Absolute height of the window in pixels |

No |

No |
|

Height |

The height of the plane (along Y axis) |

No |

No |
|

Height |

Height of the texture |

No |

No |
|

Height |

Sets the absolute height for the automatically created composition target textures. If this property is not set, the size is taken from the current composition stack state using the values of the **Resolution Multiplier** and **Resolution Divisor** properties. |

No |

Yes |
|

Hide Text Hint When Editing |

Sets whether to hide the placeholder content, which you set using the **Text Hint Prefab** property, when the Text Box node is in the editing state. To hide the placeholder content only when the user enters text in the Text Box node, disable this property. |

No |

Yes |
|

History Certainty Threshold |   |

No |

Yes |
|

History Depth Texture |   |

No |

Yes |
|

Hit Test Camera |

Sets which hit test camera to use in scenes rendered by the selected Viewport 2D. If not set, Kanzi uses the camera in the scene. |

No |

Yes |
|

Hit Testable |

When enabled, the node can be hit tested. Enabling Hit Testable for a 2D node enables hit testing only for that node. Enabling Hit Testable for a 3D node enables hit testing also for the child nodes. Kanzi hit tests 3D nodes using the default Camera node or the Hit Test Camera node of the active Scene node. |

No |

Yes |
|

Hit Testable Container |

When enabled, Kanzi uses the layout bounds as geometry for hit testing. |

No |

Yes |
|

Hit Testing Camera |

Sets the camera to use to hit test the objects in the Scene. The default is the camera that you set with the **Camera** property. |

No |

Yes |
|

Hold Interval |

Sets the amount of time in milliseconds that the user must hold the button pressed down for Kanzi to recognize it as a long-press gesture. To disable the long-press gesture, set to 0. |

No |

Yes |
|

Horizontal Alignment |

The alignment in horizontal direction the node should use when it resides under a layout. |

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

Horizontal Margin |

Sets the horizontal space between this node and other nodes that are adjacent to this node in a layout. To access the Horizontal Margin property fields in a binding, use: * X for the **Left** property field * Y for the **Right** property field |

No |

Yes |
|

Horizontal Padding |

Sets the padding spaces between the content and the left and right boundaries of the Text node. |

No |

Yes |
|

Horizontal Padding |

Sets the padding spaces between the content and the left and right boundaries of the Content Layout node. |

No |

Yes |
|

Host Name |

Contains the name of the host the node originates from. |

No |

Yes |
|

Hover |

Indicates whether a node is the foremost hit testable node under the cursor. |

No |

Yes |
|

Ignore Embedded Color Profile |

Whether to ignore color conversions for this image. When you enable this property, Kanzi Studio removes the ICC profile from the image file and does not perform gamma correction. |

No |

No |
|

Image |

The image file to be used in the texture |

No |

No |
|

Image |

A thumbnail preview of the selected image (Read-only) |

No |

No |
|

Image |

The image to display. |

No |

Yes |
|

Import Axis Transform |

Transformation that is applied to all the imported object nodes |

No |

No |
|

Import Material Type |

The material type under which the materials are imported from 3D asset files, such as COLLADA. âAutomaticâ option assigns imported materials under different material types depending on their material effect. Note that only basic effects such as Phong and textured Phong are recognized. |

No |

No |
|

Import Scale |

Scaling that is applied to all the imported object nodes |

No |

No |
|

Import Source ID |   |

No |

No |
|

Import Source Override |

Use this setting in cases where you want to combine the contents of multiple Asset 3D files into a one hierarchy. When importing the existing items are matched based on their import source, therefore overriding the import source of one Asset 3D file will import items into the same hierarchy as the items imported earlier from the override target Asset 3D file. |

No |

No |
|

Imported from |

The source, the project reference or the 3D asset source file from where the item was imported into this project |

No |

No |
|

Index In Group |

Sets the index of the Toggle Button in the Toggle Button Group to which that Toggle Button is registered. If a Toggle Button does not have a local value for this property, it is not registered to the ancestor Toggle Button Group. When set to -1, the Toggle Button Group assigns an index for the Toggle Button. |

No |

Yes |
|

Inner Angle |

Sets the inner angle of the light cone in degrees. |

No |

Yes |
|

Inner Distance |

Sets the distnace range where the vignette color transition starts. |

No |

Yes |
|

Input Method Action |

Sets the label of the user action button on the on-screen keyboard for this Text Box. By default uses the label of the default input method of the operating system. |

No |

Yes |
|

Input Property |

The property on the input property host project item from which the input is read from |

No |

No |
|

Input Property Field |

The property field from which the input (float value) is read. For example, WHOLE_PROPERTY for float properties and TRANSLATE_X for matrix properties. |

No |

No |
|

Input Property Host |

The project item that contains the property from which the input is read from |

No |

No |
|

Input Type |

The type of the input for the target animation: time (default) / property |

No |

No |
|

Input Type |

Sets the input type of the input methods that provide the input layout to let the user enter and edit text of specific type in the Text Box node: * **Default** for the default input type of the input method editor * **Numeric** for numbers * **Email** for email addresses * **URL** for URL addresses |

No |

Yes |
|

Input Viewport Area |

Reports the viewport area relative to the composition space as passed from the parent render pass. To access the Input Viewport Area property fields in a binding, use: * X for the offset along the x axis relative to the composition space * Y for the offset along the y axis relative to the composition space * Z for the width of the viewport * W for the height of the viewport |

No |

Yes |
|

Instantiated Node |

Sets the node that this Instantiator node replicates. |

No |

Yes |
|

Invert Content Mask |

Whether to invert the value that Kanzi calculates using content masking. |

No |

Yes |
|

Invert Mask |

Whether to invert the mask so that transparent areas become opaque and opaque areas become transparent. |

No |

Yes |
|

Invert U |

Whether or not to invert the texture coordinate U. Can be used for mirroring the possible displayed texture vertically. |

No |

No |
|

Invert V |

Whether or not to invert the texture coordinate V. Can be used for mirroring the possible displayed texture horizontally. |

No |

No |
|

Is Asset Package |

When enabled, saving this project will export a manifest file that is used for locating importable assets in this project. Mark the assets to be exported with âExport In Asset Packageâ property. |

No |

No |
|

Is Checked |

When enabled, the toggle button is in On state. Works only when a toggle button has two states. |

No |

No |
|

Is Composing Text |

Reports the text composition state of the Text Box node. |

No |

Yes |
|

Is Down |

Indicates whether the button is pressed and in the down state. |

No |

Yes |
|

Is Editing |

Reports the editing state of the Text Box node. |

No |

Yes |
|

Is Used by Code |

Whether or not the application code uses this asset. Used for determining unused assets. |

No |

No |
|

Is Value Changing |

Whether the value is currently changing. |

No |

Yes |
|

Item Area Begin |

Sets the proportional offset where the part of the trajectory meant for the fully visible Trajectory List Box 3D items starts. Kanzi uses the values of the Item Area Begin and Item Area End properties to calculate the value of the Node.VisibleAmountInParent property for each list item.You can use the VisibleAmountInParent property in shaders to fade out those list items that are not fully visible. |

No |

Yes |
|

Item Area Begin |

Sets the starting point of the trajectory segment in which the items in this Trajectory Layout are considered fully visible. The value is in the range [0, 1], where 0 is the beginning and 1 is the end of the trajectory. The Node > Visible Amount in Parent property uses this value. |

No |

Yes |
|

Item Area Begin |

Sets the proportional offset where the area meant for the fully visible items in the Grid List Box starts. Kanzi uses the values of the Item Area Begin and Item Area End properties to calculate the value of the Node.VisibleAmountInParent property for each list item.You can use the VisibleAmountInParent property in shaders to fade out those list items that are not fully visible. |

No |

Yes |
|

Item Area End |

Sets the proportional offset where the part of the trajectory meant for the fully visible Trajectory List Box 3D items ends. Kanzi uses the values of the Item Area Begin and Item Area End properties to calculate the value of the Node.VisibleAmountInParent property for each list item.You can use the VisibleAmountInParent property in shaders to fade out those list items that are not fully visible. |

No |

Yes |
|

Item Area End |

Sets the proportional offset where the area meant for the fully visible items in the Grid List Box ends. Kanzi uses the values of the Item Area Begin and Item Area End properties to calculate the value of the Node.VisibleAmountInParent property for each list item.You can use the VisibleAmountInParent property in shaders to fade out those list items that are not fully visible. |

No |

Yes |
|

Item Area End |

Sets the ending point of the trajectory segment in which the items in this Trajectory Layout are considered fully visible. The value is in the range [0, 1], where 0 is the beginning and 1 is the end of the trajectory. The Node > Visible Amount in Parent property uses this value. |

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

Item Count |

Reports the number of items in the List Box, including virtual items. |

No |

Yes |
|

Item Generator |

Sets the name of the item generator type to use to provide items dynamically to the List Box. |

No |

Yes |
|

Item Index |

Reports the index of the item in the List Box Item Container. |

No |

Yes |
|

Item Template |

Sets the prefab to use for the List Box items. |

No |

Yes |
|

Items Source |

Data object which provides data sources for list items. |

No |

Yes |
|

Java Project |

Whether the project contains Java plugins |

No |

No |
|

Keep Active |

Always activate this Page node when its parent is active. |

No |

Yes |
|

Keep Activity Alive |

Sets how to handle the Activity node when you deactivate it: * **Detach and Destroy.** Kanzi detaches the Activity from the node tree and deletes the Activity instance. Default value. * **Hide and Disable.** Kanzi hides and disables the Activity. When you activate the Activity again, Kanzi enables and shows the same Activity. This way you skip Activity instantiation when you activate the Activity again. |

No |

Yes |
|

Keep Alive Behavior |

The keep-alive behavior of this resource. Can be used to deny unloading of the resource. |

No |

No |
|

Keep Alive Item Count |

Sets the size of the buffer for invisible List Box items. Kanzi returns to the Item Generator those invisible items that do not fit in the buffer. |

No |

Yes |
|

KZB Endianness |

Endianness of the KZB data. Use the endianness of the target device for optimal performance. |

No |

No |
|

Last Item Fill |

Whether the last item of the dock layout is given the remaining free space. |

No |

Yes |
|

Layout Depth |

The size of the node in depth direction when used in a layout. Overrides the default bounds of the item. |

No |

Yes |
|

Layout Direction |

The direction in which the items are arranged when you add them to a grid layout. |

No |

Yes |
|

Layout Direction |

Sets the direction in which the Grid List Box arranges its items. When you change the layout direction you also change the scroll axis of the Grid List Box. |

No |

Yes |
|

Layout Height |

The height of the node when used in a layout. Overrides the default bounds of the item. |

No |

Yes |
|

Layout Transformation |

The location, orientation and scale of the node relative to its parent node. Layout Transformation affects the layout. If you do not want to affect the layout, use Render Transformation. |

No |

Yes |
|

Layout Transformation |

The 2D transformation to be applied before layouting. |

No |

Yes |
|

Layout Width |

The width of the node when used in a layout. Overrides the default bounds of the item. |

No |

Yes |
|

Left Image |

The image to use in the center-left. |

No |

Yes |
|

Length |

The length of the line |

No |

No |
|

Length |

Length of the trapezoid trajectory |

No |

No |
|

Length |

The length of the angle |

No |

No |
|

Light |   |

No |

Yes |
|

Light Type |

A reference to a light property type that defines the type of the light. |

No |

No |
|

Light Type Name |

The property type name of the light. |

No |

Yes |
|

Line Spacing |

Sets the line spacing in multiples of the normal line height of the selected font. |

No |

Yes |
|

Linear Premultiply |

Premultiply the alpha channel in a linear color space. For sRGB images, using a linear color space for premultiplication results in the fewest artifacts. If source image was created for standard mode, disabling this option may give better results. |

No |

No |
|

Locale |

The locale of the node. |

No |

Yes |
|

Look At |

Makes a node to always face the node set in this property. |

No |

Yes |
|

Loop Subpages |

Loop the subpages when navigating to the next or previous subpage. |

No |

Yes |
|

Looping |

Whether to show items in the Trajectory List Box 3D from the beginning after reaching the last item. |

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

Magnification Filter |

Controls the texture sampling together with the **Mipmap Mode** property when the texture is magnified: * **Nearest** sample uses the nearest texel in the texture. * **Linear** sample interpolates between the four nearest texels in the texture. |

No |

No |
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

Sets the texture that masks another texture or color. |

No |

Yes |
|

Mask Texture |

Sets the mask texture. The default is no texture. |

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

Masked Blur |

Sets whether to blur only the pixels whose alpha channel value is not zero. When you enable this property, the blur does not spread to fully transparent pixels and the edges of the content stay sharp. The default value is false. |

No |

Yes |
|

Material |

Sets the material that will have all other Material Setup render pass properties set to. |

No |

Yes |
|

Material |

Material used when drawing with the brush |

No |

Yes |
|

Material |

Sets to the Material that you want a Blit render pass to use to blit one or more textures. |

No |

Yes |
|

Material |

Sets the material that will be used to render all nodes rendered by this RaytracedReflectionRenderPass. |

No |

Yes |
|

Material |

Sets the material that will be used to render all nodes rendered by this RaytracedShadowRenderPass. |

No |

Yes |
|

Material |

Use this material to override the materials defined in the clusters of the mesh. |

No |

Yes |
|

Material |

Sets the material that will be used to render all nodes rendered by this DrawObjectsWithMaterialRenderPass. |

No |

Yes |
|

Material Requirements |

Sets the material requirements required from materials selected for rendering. |

No |

Yes |
|

Material Type |

Material type of this material |

Yes |

No |
|

Material Type Keep Alive Behavior |

The keep-alive behavior to be inherited by material types in project. Can be used to deny unloading of material types. |

No |

No |
|

Maximum Distance From Curve |

The distance from the curve where hit testing succeeds. |

No |

Yes |
|

Maximum Number of Touches |

Sets the maximum number of touch points allowed on the Grid List Box area for scrolling. |

No |

Yes |
|

Maximum Number of Touches |

Sets the maximum number of touch points allowed on the Trajectory List Box 3D area for scrolling. |

No |

Yes |
|

Maximum Number of Touches |

Sets the maximum number of touch points allowed for a Scroll View pan. |

No |

Yes |
|

Maximum Text Length |

Sets the maximum length of text that the user can insert in the Text Box node. The unit is a UTF-8 character and the buffer byte length can be greater for multi-byte characters. |

No |

Yes |
|

Maximum Value |

The maximum value that the range allows. |

No |

Yes |
|

Maximum Zoom |

Sets the maximum zoom level. |

No |

Yes |
|

Mesh Material |

The material to be used for rendering the mesh |

No |

No |
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

Metrics Type |

Defines the type of the coordinate system for the window metrics. |

No |

Yes |
|

Minification Filter |

Controls the texture sampling together with the **Mipmap Mode** property when the texture is minified: * **Nearest** sample uses the nearest texel in the texture. * **Linear** sample interpolates between the four nearest texels in the texture. |

No |

No |
|

Minimum Number of Touches |

Sets the minimum number of touch points required on the Trajectory List Box 3D area for scrolling. |

No |

Yes |
|

Minimum Number of Touches |

Sets the required number of touch points pressed for a Scroll View node pan to start. Scroll View nodes with minimum number of touches greater than one precede the children in touch processing. |

No |

Yes |
|

Minimum Number of Touches |

Sets the minimum number of touch points required on the Grid List Box area for scrolling. |

No |

Yes |
|

Minimum Unreprojected Shadow |   |

No |

Yes |
|

Minimum Value |

The minimum value that the range allows. |

No |

Yes |
|

Minimum Zoom |

Sets the minimum zoom level. |

No |

Yes |
|

Mipmap Mode |

Sets the mipmap mode of the automatically created composition target. To enable mipmaps, set to **Linear** or **Nearest**. Enabling mipmaps introduces the runtime cost of generating mipmaps after rendering. To disable mipmaps, remove this property. |

No |

Yes |
|

Mipmap Mode |

Sets the mipmap mode of the automatically created composition cubemap target. To enable mipmaps set the property value to Linear or Nearest. Enabling mipmaps introduces the runtime cost of generating mipmaps after rendering. To disable mipmaps remove the property. |

No |

Yes |
|

Mipmap Mode |

Sets how to use mipmaps: * **Base** uses only the base texture and does not use mipmaps. It uses either point sample or bilinear sampling. * **Nearest** uses mipmaps and samples one mipmap level. It uses either point sample or bilinear sampling from a single nearest mipmap level. It selects the operation based on the **Minification Filter** or **Magnification Filter** property values. * **Linear** uses mipmaps, and samples and interpolates two mipmap levels. It selects the operation based on the **Minification Filter** or **Magnification Filter** property values. |

No |

No |
|

Mipmap Mode |

Sets the mipmap mode to use with the temporary composition targets to which Kanzi renders this node. |

No |

Yes |
|

Mipmap Source Texture |

Reports the texture that contains the render target texture for which Kanzi creates mipmaps. Use this property as the source texture in a material that you use to customize how Kanzi generates mipmaps for the composition targets of a Composition Target Render Pass or Cubemap Render Pass. The default value is < No Texture > |

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

Multisample Level |

Sets the amount of multisample anti-aliasing to apply to the automatically generated composition target textures. |

No |

Yes |
|

Multisample Level |

Sets the amount of multisample anti-aliasing to apply to the temporary composition targets to which Kanzi renders this node. |

No |

Yes |
|

Name |

Name of the project item |

No |

No |
|

Name |

Description |

Inherited |

Exported to Kanzi Engine |
|

Native Deployment Target |

Sets the memory in which to store this texture on your target device. |

No |

No |
|

Native Pixel Format |

Sets the native image format to use when exporting this image to the kzb file. Make sure that the graphics backend of your target device supports the format. |

No |

No |
|

NegX Image |

Negative X image |

No |

No |
|

NegY Image |

Negative Y image |

No |

No |
|

NegZ Image |

Negative Z image |

No |

No |
|

Node List |

Input node list range. Set by a binding from nearest parent node list. |

No |

Yes |
|

Node.Path |

Full path to the node. |

No |

Yes |
|

Normal |

The normal vector of the normal of the rectangle |

No |

No |
|

Normal |

The normal vector of the ellipse |

No |

No |
|

Normal |

The normal vector of the arc |

No |

No |
|

Normal |

The normal vector of the normal of the spiral |

No |

No |
|

Normal |

The normal vector of the normal of the circle |

No |

No |
|

Normal |

Normal vector of the trapezoid trajectory orientation |

No |

No |
|

Normal |

The normal vector of the normal of the angle |

No |

No |
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

Normalized Value |

The current value normalized to range [0, 1]. |

No |

Yes |
|

Object Source |

Sets the object source which collects the nodes that you want to render with this render pass. To render all nodes in a Scene node (Root Object Source), do not set the value for this property. |

No |

Yes |
|

Object Source |

Sets the object source which collects the nodes that you want to use for ray tracing. To render all nodes in a Scene node (Root Object Source), do not set the value for this property. |

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

Off-Screen Rendering |

When set and the node has an explicitly set render target, do not render the resulting framebuffer to screen. |

No |

Yes |
|

Opacity |

Opacity of the node. |

No |

Yes |
|

Optimize Meshes |

Whether to perform the vertex cache optimization for exported meshes. Kanzi Studio sets the vertex cache of the meshes to the value you set in the Target Vertex Cache Size property. |

No |

No |
|

Orientation |

Sets the orientation of the application window. |

No |

Yes |
|

Original Name |

The name of the item in the import source |

No |

No |
|

Orthogonal Plane Size |

Sets the half width or half height of the view plane of a camera that uses the relative orthogonal coordinate system: * When **FOV Type** is **Y FOV** (default value), the height. * When **FOV Type** is **X FOV**, the width. The default value is 1.0. |

No |

Yes |
|

Orthogonal Type |

Sets the type of the orthogonal coordinate system: * **Relative** sets the camera to display an area whose width is scaled with the value of the **Orthogonal Plane Size** property. This is the default. * **Absolute** sets the camera to use pixel coordinates. |

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

Outline Color |

Sets the color of the outline. |

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

Outline Width |

Sets the width of the outline in pixels outside the content area. The default value is 4 pixels. |

No |

Yes |
|

Output Acceleration Structure |

Built acceleration structure resource. |

No |

Yes |
|

Output Denoised Shadow Mask |   |

No |

Yes |
|

Output Directional Lights |

Kanzi uses this property to allow binding to directional light set. |

No |

Yes |
|

Output Node List |

Output node list range. Set by Node List render pass as result of filtering the Input Node List. |

No |

Yes |
|

Output Point Lights |

Kanzi uses this property to allow binding to point light set. |

No |

Yes |
|

Output Reflection Texture |   |

No |

Yes |
|

Output Shadow Mask Texture |   |

No |

Yes |
|

Output Spot Lights |

Kanzi uses this property to allow binding to spot light set. |

No |

Yes |
|

Output Viewport |

Viewport applied by the rendering of the render pass. |

No |

Yes |
|

Overflow |

Sets the characters that represent the truncated text when the text does not fit in this node. The default value is ââ¦â. By default, Kanzi truncates the text at the end. Use the **Truncation Direction** property to set the part of the text that you want to truncate. Kanzi truncates text to fit within the vertical and horizontal limits of the control. If there is not enough vertical space to fit a single line of text, Kanzi truncates all text and does not show the **Overflow** characters. |

No |

Yes |
|

Override Camera |

Sets the Camera node that you want to use to render the nodes to the composition cubemap texture. To use the default Camera node in that Scene node, do not set the value for this property. |

No |

Yes |
|

Override Distance |

Sets the distance between the items in this Trajectory Layout. When you do not set this property, the Trajectory Layout calculates the distance automatically. |

No |

Yes |
|

Override Material |

Sets the override material to use to render the content of the 2D prefab in the Viewport 3D node. In the Viewport 3D node, bind a texture property of the override material to the Viewport3D.PrefabTexture property. |

No |

Yes |
|

Override Shadow Offset |

Sets the offset of the shadow from the object along the x and y axes in pixels. When you set this property, the **Shadow Angle** and **Shadow Distance** properties have no effect. To disable the offset override, remove this property. |

No |

Yes |
|

Parallel Activity Host Content |

Describes the content of a Parallel Activity Host. The Parallel Activity Host uses this content to instantiate Activity prefabs and control the status and lifetime of its child Activities. This property is not directly editable by a Kanzi Studio user. The ActivityBrowserController sets the value of this property according to the changes done to the state of the Activity Tree in the ActivityBrowser. The expected format for the property value is a list of Activity descriptions. Each of this Activity description contains: * The name of the Activity. * A boolean value describing whether the Activity is going to be active on the Parallel Activity Host activation. When set to true the Activity is going to be active, when set to false, the Activity is not going to be active. * The path to the prefab of the Activity. * The priority layer value of the Activity. The priority layer value decides the z-order of the child Activity. The child Activity with a higher priority value, is displayed on the top of a child Activity with the lower priority value. The z-order of the child Activities with the same priority value depends on their order of addition to the Activity Host. The latest added child Activity is always displayed on top on the existing child Activities with the same priority value. The values in this property must be separated by a comma. For example, {{name1,1,path1,0},{name2,0,path2,1}}. |

No |

Yes |
|

Password Echo Timeout |

When the **Echo Mode** property is set to **Password**, this property sets the time in milliseconds that an inserted character is visible before being masked. |

No |

Yes |
|

Password Masking Character |

When the **Echo Mode** property is set to **Password**, this property sets the character that masks each character that the application user enters. |

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

Pixel Format |

The pixel format of the node if rendering to a texture. |

No |

Yes |
|

Pixel Format |

Sets on the GPU the target pixel format of the automatically created composition cubemap target textures. |

No |

Yes |
|

Pixel Format 0 |

Sets on the GPU the target pixel format of the first automatically created composition target texture. |

No |

Yes |
|

Pixel Format 1 |

Sets on the GPU the target pixel format of the second automatically created composition target texture. |

No |

Yes |
|

Pixel Format 2 |

Sets on the GPU the target pixel format of the third automatically created composition target texture. |

No |

Yes |
|

Pixel Format 3 |

Sets on the GPU the target pixel format of the fourth automatically created composition target texture. |

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

Playback Mode |

Normal plays the animation as it is defined in the animation clip. Ping pong first plays the animation as it is defined in the animation clip and then plays the animation in reverse. Reverse plays the animation defined in the animation clip in reverse. |

No |

No |
|

Plot Animations |

Whether to plot non-linear animations into linear animations during export. |

No |

No |
|

PNG Compression Level |

Affects how PNG images are compressed when exported to kzb |

No |

No |
|

PNG Compression Level |

Affects how PNG images are compressed when exported to kzb. Can be overridden per image. |

No |

No |
|

Point Light |

Point light settings |

No |

No |
|

Point Light Attenuation |

Sets the effect that this Point Light has on nodes that are farther away. Distance of light from the lighted surface is input in a quadratic function, the 3 components are the constant, linear and quadratic coefficients for the distance variable. |

No |

Yes |
|

Point Light Color |

Sets the color of the Point Light. Use the Intensity (I) property field to adjust the brightness of the light. |

No |

Yes |
|

Point Light Radius |

Sets the distance at which the intensity of the Point Light reaches zero. For infinite distance, set the property value to 0. |

No |

Yes |
|

Point Lights |

Use this property to bind the point light set for rendering. |

No |

Yes |
|

Point Shadow Bias |

Sets the point shadow bias to reduce sampling artifacts. |

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

Point Shadow Softness |

Sets the softness of the shadows cast by the Point Light. |

No |

Yes |
|

Polygon Depth Offset |

Sets the polygon depth offset to apply to the element that the Pipeline State render pass renders: * **Derivative multiplier** sets the multiplier for the depth change derivative for the fragment. * **Constant multiplier** multiplies the smallest measurable unit of depth, dependent on the target platform. You can use the offset to render decals on the surfaces of filled polygons. Kanzi typically shows nearer the camera those polygons that have a negative offset. |

No |

Yes |
|

Position |

A hidden property that identifies point light position and related metata. |

No |

Yes |
|

Position |

A hidden property that identifies spotlight position and contains related metadata. |

No |

Yes |
|

PosX Image |

Positive X image |

No |

No |
|

PosY Image |

Positive Y image |

No |

No |
|

PosZ Image |

Positive Z image |

No |

No |
|

Prefab Template |

The prefab template to use for this 3D prefab placeholder |

No |

No |
|

Prefab Template |

Node to use on this prefab view. |

No |

Yes |
|

Prefab Template |

Sets the 2D prefab whose content the Viewport 3D node renders in 3D space. |

No |

Yes |
|

Prefab Template |

The prefab template to use for this prefab placeholder |

No |

No |
|

Prefab Texture |

The read-only texture to which the Viewport 3D renders the content of the 2D prefab. When you set the Override Material property, you must bind a texture property of that material to this property. |

No |

Yes |
|

Premultiply Alpha |

Whether to premultiply alpha for images during .kzb file export. You can override this project-wide setting in the Properties of each image. |

No |

No |
|

Premultiply Alpha |

Whether to premultiply the alpha channel into color channels in images that have an alpha channel. If you want to control the value of this property in the Project > Properties with the Premultiply Alpha property, select Project default. |

No |

No |
|

Preprocessor Definitions |

Use preprocessor definitions to set values for shader preprocessor directives. |

No |

No |
|

Preserve History |

Determines whether Kanzi preserves Activity property values when that Activity becomes inactive: * When enabled, Kanzi stores the values of Activity properties of this Activity and its child Activities. The default value. * When disabled, Kanzi discards the values of Activity properties of this Activity and its child Activities. |

No |

Yes |
|

Preview Background Color |

Sets the background color of the Preview for this project. When you do not set this property, the project uses the color that you set in **Edit** > **User Preferences** > **Preview** > **Background Color**. |

No |

No |
|

Preview Build Configuration |

Use release setting for performance and debug setting for debugging Kanzi engine plugins. Kanzi engine plugins must have a DLL available with the same ES wrapper, build configuration and Visual Studio version as specified for the preview. |

No |

No |
|

Preview Camera |

Sets the camera through which Kanzi Studio Preview shows the Scene. |

No |

No |
|

Preview Graphics API Configuration |

Preview Graphics API Configuration is used to select the graphics API used for rendering within Preview. |

No |

No |
|

Preview Visual Studio Version |

Preview Visual Studio version setting is required for Kanzi engine plugin compatibility. Kanzi engine plugins must have a DLL available with the same ES wrapper, build configuration and Visual Studio version as specified for the preview. |

No |

No |
|

Preview Working Directory |

The working directory of preview. Accepts relative path from Kanzi Studio project directory or an absolute path. |

No |

No |
|

Previous Camera Matrix |

Camera matrix from the previous frame, used for velocity buffer calculation. |

No |

Yes |
|

Previous Final Transformation |

Final transformation (world matrix) from the previous frame, used for velocity buffer calculation. |

No |

Yes |
|

Previous Projection Matrix |

Projection matrix from the previous frame, used for velocity buffer calculation. |

No |

Yes |
|

Primary Direction |

The direction along which the layout arranges items until the layout limit in that direction is reached. |

No |

Yes |
|

Projection Type |

Sets the projection type of the camera: * **Perspective** projection shows objects closer to the camera larger than those that are further away. This is the default. * **Asymmetric perspective** projection lets you use the **Asymmetric FOV** property to control the field of view of each angle of a perspective projection. * **Orthographic projection** shows a 2D view of a 3D scene without providing a sense of depth. |

No |

Yes |
|

Property Field |

The property field (See Property Data Types) on the target property to be animated. |

No |

No |
|

Property Namespace |

The property namespace to prepend to the newly created custom property types in this project. When you change the value of this property, Kanzi Studio asks you whether you want to change the existing custom property type names which use this namespace. |

No |

No |
|

Property Types |

Sets the property types that you can use in the materials of this material type. |

No |

No |
|

Radius |

The radius of the sphere |

No |

No |
|

Radius |

The radius of the arc |

No |

No |
|

Radius |

The radius of the circle |

No |

No |
|

Radius A |

The radius along the x-axis |

No |

No |
|

Radius B |

The radius along the y-axis |

No |

No |
|

Ray Maximum Trace Distance |   |

No |

Yes |
|

Raytraced Reflection Maximum Roughness |   |

No |

Yes |
|

Read Only |

Sets whether the Text Box node is editable. When you enable this property, you can set the text only through the **Text** property and the user cannot edit the text in the Text Box node. |

No |

Yes |
|

Recognition Threshold |

Sets the distance in pixels that the pointer has to move for the scrolling to start in the Trajectory List Box 3D. |

No |

Yes |
|

Recognition Threshold |

Sets the distance in pixels that the pointer has to move for the scrolling to start in the Grid List Box. |

No |

Yes |
|

Recognition Threshold |

Sets the amount a pointing device must move for the scrolling to start on a Scroll View node. |

No |

Yes |
|

Reference for Absolute Paths |

Required if using absolute paths for animation targets in timeline entries. Defines the scope of nodes that can be referenced. |

No |

No |
|

Reference for Targeting |

Required if using absolute paths for animation targets in animation child clips. Defines the scope of nodes that can be referenced. |

No |

No |
|

Reflection Resolution Scale |   |

No |

Yes |
|

Remove ICC Profile From PNG Images |

Whether to remove the ICC profile from the PNG images files during kzb file export. |

No |

No |
|

Remove Side Bearings |

Whether to position the leftmost characters of left-aligned text and rightmost characters of right-aligned text exactly within the boundary of the text node. |

No |

Yes |
|

Render Pass |

The RenderPass used for rendering the Scene for the Viewport. Instantiated from the RenderPassPrefab. Set internally by Kanzi whenever RenderPassPrefabProperty changes. |

No |

Yes |
|

Render Pass Prefab |

Sets which render pass prefab will be used to instantiate the render pass tree. |

No |

Yes |
|

Render Pass Prefab |

Sets the Render Pass Prefab that this Render Pass View instantiates. |

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

Render Target Type |

Defines which kind of data the texture is to contain: COLOR / DEPTH |

No |

No |
|

Render Transformation |

The 2D transformation to be applied after layouting. |

No |

Yes |
|

Render Transformation |

The location, orientation, and scale of the node relative to its parent node. Render transformation does not affect the layout of the node. |

No |

Yes |
|

Render Transformation Origin |

Sets the render transform origin in relative coordinates. |

No |

Yes |
|

Repeat Count |

The amount of times the target animation will be played (1 for one time playback). Endless loop can be defined using âInfiniteâ checkbox. |

No |

No |
|

Reproject Depth Sensitivity |   |

No |

Yes |
|

Resolution |

Sets the dimensions of the automatically created composition cubemap target textures. The default value is 64. |

No |

Yes |
|

Resolution Divisor |

Sets the resolution divisor for the automatically created composition target textures. Together with the **Resolution Multiplier** property, this property sets the size of the composition target in relation to the size of the current Viewport 2D node. For more fine-grained control, bind from the **Render Pass** > **Input Viewport Area** property to the **Width** and **Height** properties. |

No |

Yes |
|

Resolution Multiplier |

Sets the resolution multiplier for the automatically created composition target textures. Together with the **Resolution Divisor** property, this property sets the size of the composition target in relation to the size of the current Viewport 2D node. For more fine-grained control, bind from the **Render Pass** > **Input Viewport Area** property to the **Width** and **Height** properties. |

No |

Yes |
|

Resolve Immediately |

Whether to resolve multisamples and generate mipmaps for the composition target texture immediately after rendering. By default, the Composition Target render pass resolves multisamples and generates mipmaps immediately. When you continue rendering to the composition target in another Composition Target render pass that performs the resolve, disable this property. |

No |

Yes |
|

Resolve Immediately |

Whether to generate mipmaps for the composition target texture immediately after rendering. By default the Cubemap render pass generates mipmaps immediately. When you continue rendering to the composition target in another Cubemap render pass that performs the resolve, disable this property. |

No |

Yes |
|

Resource Keep Alive Behavior |

The keep-alive behavior to be inherited by resources in the project. Can be used to deny unloading of resources. |

No |

No |
|

Resource Visibility Across Projects |

Sets whether the resources of this project are available to referencing projects: * Private makes the resources available only to this project. This is the default value. * Public makes the resources available in the dropdown menus of referencing projects. To override this setting for an individual resource, add and set the Visibility Across Projects property for that resource. |

No |

No |
|

Result Depth Texture |

The depth texture to which the Composition Target render pass renders its content. |

No |

Yes |
|

Result Depth Texture |

The cubemap depth texture to which the Cubemap render pass renders its content. |

No |

Yes |
|

Result Texture |

The result cubemap texture that was rendered to by the Cubemap render pass. |

No |

Yes |
|

Result Texture 0 |

The first color texture to which the Composition Target render pass renders its content. |

No |

Yes |
|

Result Texture 1 |

The second color texture to which the Composition Target render pass renders its content. |

No |

Yes |
|

Result Texture 2 |

The third color texture to which the Composition Target render pass renders its content. |

No |

Yes |
|

Result Texture 3 |

The fourth color texture to which the Composition Target render pass renders its content. |

No |

Yes |
|

Reversed |

Defines whether the stack layout arranges its items in reverse order. |

No |

Yes |
|

Reversed Scrolling |

Whether the scroll position in the Trajectory List Box node increases in relation to the direction of the pan gesture. This reverses the direction of scrolling. By default, the scroll position decreases in relation to the pan direction, which makes the list items move toward the direction of the trajectory. |

No |

Yes |
|

Reversed Scrolling |

Whether the scroll position in the Grid List Box node increases in relation to the direction of the pan gesture. This reverses the direction of scrolling. By default, the scroll position decreases in relation to the pan direction and items moves to same direction with the pan gesture. |

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

Revolutions |

Revolutions of the spiral trajectory |

No |

No |
|

Right Image |

The image to use in the center-right. |

No |

Yes |
|

Rotation Offset |

The angle in degrees by which to rotate a Page node. |

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

Round up Image Dimensions to Nearest Power of Two |

Whether to round up the width and height of images to the nearest power of two during kzb file export. For example, when you enable this property, Kanzi Studio exports a 40 x 30 pixel image to the kzb file in the size 64 x 32 pixels. |

No |

No |
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

Rows |

Defines the number of rows in a grid layout and how the grid layout distributes the content in rows. |

No |

Yes |
|

Rules |

Use material rules to automate the definition of preprocessors for material inputs, vertex attributes, and lights. |

No |

No |
|

Samples |

The number of multisample samples used for each pixel for this render target. |

No |

No |
|

Save Last Focused Node |

When this property is enabled, Kanzi remembers the last-focused node in this Activity and sets the key focus to that node when you activate this Activity again. This is the default. When you do not want Kanzi to remember the last-focused node in this Activity, disable this property. |

No |

Yes |
|

Scale Offset |

The factor by which to scale a Page node. |

No |

Yes |
|

Scissor Area |

Sets the scissor test in the current rendering **Viewport 2D** node. You can define the scissor in either relative or absolute coordinates, the default is relative. Use the **Scissor Mode** property to set the coordinate type. |

No |

Yes |
|

Scissor Mode |

Sets the scissor test coordinate mode. |

No |

Yes |
|

Screen Clear Color |

If screen has a clear color, screen will be cleared with the specified color before all other rendering. Depth will be cleared to 1.0f and stencil will be cleared to 0. |

No |

Yes |
|

Screen Resolution |

A selection of pre-defined absolute screen resolutions / a custom resolution |

No |

No |
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

Scroll Position |

Sets the scroll position of the Grid List Box along the x and y axes as a relative position within the list box area. Use this property to move the list to a scroll position immediately, without scrolling. To update this property with a binding, use a to-source or two-way binding. |

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

Scroll Sensitivity |

Sets the amount the position changes relative to the movement of the pointer that starts the swiping. The higher the value the more the position of the node controlled by a Scroll View node changes. The default value is 1. |

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

Scroll Speed |

The current scroll speed (read-only). |

No |

Yes |
|

Scroll Target Position |

Reports the current target scroll value of the Grid List Box. |

No |

Yes |
|

Scroll Target Position |

The current target scroll value (read-only). |

No |

Yes |
|

Scrolling |

Reports whether the Grid List Box is currently scrolling. |

No |

Yes |
|

Scrolling |

Whether a Scroll View node is currently scrolling (read-only). |

No |

Yes |
|

Secondary Direction |

The direction along which the flow layout arranges lines of the primary direction. |

No |

Yes |
|

Selected |

Indicates whether the List Box item held by this List Box Item Container is selected. The List Box sets the value of this property. |

No |

Yes |
|

Selected Item Index |

Sets the index of the item that is currently selected in the List Box node. A List Box node updates this property when the user scrolls that List Box node. To select an item in the List Box node, set this property to the index of the item that you want to select. The indexing starts from 0. To update this property with a binding, use a to-source or two-way binding. |

No |

Yes |
|

Selection Background Brush |

Sets the brush that highlights the selected text. |

No |

Yes |
|

Selection Background Color |

Sets the color that highlights the selected text. |

No |

Yes |
|

Selection Behavior |

Sets how the List Box behaves when the user selects an item. âBring to Centerâ sets the List Box to bring an item to the center of the List Box area when the user selects that item. |

No |

Yes |
|

Selection End Cursor Position |

The position of the cursor that marks the end of text selection in the Text Box node. |

No |

Yes |
|

Selection End Prefab |

Sets the prefab template that defines the appearance of the selection handle at the end of text selection instead of the default handle. |

No |

Yes |
|

Selection Font Color |

Sets the color of the selected text. |

No |

Yes |
|

Selection Foreground Brush |

Sets the brush for the selected text. |

No |

Yes |
|

Selection Start Cursor Position |

The position of the cursor that marks the beginning of text selection in the Text Box node. |

No |

Yes |
|

Selection Start Prefab |

Sets the prefab template that defines the appearance of the selection handle at the beginning of text selection instead of the default handle. |

No |

Yes |
|

Shader Version |

Sets the OpenGL ES version in the shaders of this material type. The value of this property overrides the #version directive in the shader source files. When you do not set this property, Kanzi uses the #version directive in the shader source files. |

No |

No |
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

Shadow Map Resolution Scale |   |

No |

Yes |
|

Shadow Mask |   |

No |

Yes |
|

Shadow Only |

Whether to render only the shadow without the node contents. |

No |

Yes |
|

Shadow Projection Fitting Enabled |

Controls how the directional light shadow projection is calculated Enabling this will fit the lights projection to the area covered by the main camera. |

No |

Yes |
|

Shadow Projection Margin |

Use to add extra margin by scaling the area of the projection |

No |

Yes |
|

Shadow Projection Range |

Use to limit the projection to a smaller proportional slice (X: near, Y: far) of the main camera frustum. For example if X: 0.0, Y: 0.5 means only the closest half of the camera frustum is guaranteed to be included in the shadow projection. |

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

Show Children in Layer Thumbnails |

Whether to show the child items in the thumbnails of the layer view that have direct content, such as image and viewport. |

No |

No |
|

Show Material Debug Objects |

When enabled, Kanzi Studio does not hide material debug objects. |

No |

No |
|

Side |

The docking side of an item in the dock layout. |

No |

Yes |
|

Size |

The size of the rectangle trajectory |

No |

No |
|

Size |

The size of the image on disk in pixels (Read-only) |

No |

No |
|

Slice Count |

The number of depth slices this image contains. The total height of the source height must be evenly divisible by Slice Count |

No |

No |
|

Slide Offset |

The offset to slide a Page node in horizontal or vertical direction:nX [-1, 1] to move the Page node horizontallynY [-1, 1] to move the Page node vertically |

No |

Yes |
|

Sliding Acceleration |

Sets the acceleration of the Trajectory List Box 3D after the user releases the pointer with which they scroll the Trajectory List Box 3D. The higher the value, the quicker the Trajectory List Box 3D reaches the scroll target. The default value is 40. |

No |

Yes |
|

Sliding Acceleration |

Sets the acceleration of the Grid List Box after the user releases the pointer with which they scroll the Grid List Box. The higher the value, the quicker the Grid List Box reaches the scroll target. The default value is 40. |

No |

Yes |
|

Sliding Acceleration |

Sets the acceleration of the node controlled by a Scroll View node after you release the pointer with which you swipe. Use low values when you want that node to slowly reach the final position. Use high values when you want that node to quickly reach the final position. |

No |

Yes |
|

Sliding Drag |

Sets how much drag affects the movement of the Grid List Box after the user releases the pointer with which they scroll the Grid List Box. The lower the value, the higher the drag and the quicker the scrolling of the Grid List Box stops. The default value is 80. |

No |

Yes |
|

Sliding Drag |

Sets the amount that drag affects the movement of the node controlled by a Scroll View node after you release the pointer with which you swipe. The lower the value the higher the drag and the faster the sliding of the object controlled by the Scroll View node stops. |

No |

Yes |
|

Sliding Drag |

Sets how much drag affects the movement of the Trajectory List Box 3D after the user releases the pointer with which they scroll the Trajectory List Box 3D. The lower the value, the higher the drag and the quicker the scrolling of the Trajectory List Box 3D stops. The default value is 80. |

No |

Yes |
|

Smoothness |

The smoothness of the trapezoid trajectory |

No |

No |
|

Snap Character To Pixel |

Sets whether Kanzi positions characters in 2D rendering to the nearest pixel: * When enabled, text sharpness improves, but some characters can shift a fraction of a pixel. * When disabled, certain combinations of screen resolution, use of anti-aliasing, and font size can cause the text to appear blurry. In that case, you can improve the appearance of the text with the **Fractional Character Width** and **Character Spacing** properties. |

No |

Yes |
|

Snap to Pixel |

Snap the translation of the node and its size into pixel boundary. |

No |

Yes |
|

Sorting Order |

Sets the sorting order for render entries. |

No |

Yes |
|

Spacing |

Sets the distance between the items in the Trajectory List Box 3D. |

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

Sphere Type |

Sets the tessellation type of the sphere: * UV Sphere consists of fans of triangles at the poles and quad faces elsewhere. This is the default. * Icosphere is a subdivided icosahedron that consists of triangles. * Quad Sphere is a subdivided box consisting of quads projected to a sphere. |

No |

No |
|

Spline |

The spline to use in the spline trajectory |

No |

No |
|

Spot Light |

Spot light settings |

No |

No |
|

Spot Light Attenuation |

Sets the effect that this Spot Light has on nodes that are farther away. Distance of light from the lighted surface is input in a quadratic function, the 3 components are the constant, linear and quadratic coefficients for the distance variable. |

No |

Yes |
|

Spot Light Color |

Sets the color of the Spot Light. Use the Intensity (I) property field to adjust the brightness of the light. |

No |

Yes |
|

Spot Light Radius |

Sets the distance at which the intensity of the Spot Light reaches zero. For infinite distance, set the property value to 0. |

No |

Yes |
|

Spot Light View Projection |

The premultiplied projection view matrix of a spot light. |

No |

Yes |
|

Spot Lights |

Use this property to bind the spot light set for rendering. |

No |

Yes |
|

Spot Shadow Bias |

Sets the spot shawow bias to reduce sampling artifacts. |

No |

Yes |
|

Spot Shadow Bias |

Sets the spot shadow bias to reduce sampling artifacts. |

No |

Yes |
|

Spot Shadow Map |

Depth map used to calculate spot shadows. |

No |

Yes |
|

Spot Shadow Softness |

Sets the softness of the shadows cast by the Spot Light. |

No |

Yes |
|

sRGB Content |

Whether to use the sRGB color space for the image format. |

No |

No |
|

Start Offset |

Sets the offset of the starting position of the items on the trajectory in the range [0, 1], where 0 is the beginning and 1 is the end of the trajectory. |

No |

Yes |
|

Start Radius |

Start radius of the spiral |

No |

No |
|

Start Time |

The starting time of the global timeline. |

No |

No |
|

Start Time |

The starting time of the target on the hosting sequence |

No |

No |
|

Start Time |

The starting time of the clip. |

No |

No |
|

State Manager |

Sets the State Manager to the node. |

No |

Yes |
|

Stencil Fail Operation |

Sets the operation that the render pass performs when the stencil test fails. |

No |

Yes |
|

Stencil Function Mask |

Sets a mask on which the AND operation is executed with both the reference value and the stored stencil value when the test is done. |

No |

Yes |
|

Stencil Function Reference Value |

Sets the reference value for the stencil test. |

No |

Yes |
|

Stencil Pass Depth Fail Operation |

Sets the operation that the render pass performs when the stencil test passes, but the depth test fails. |

No |

Yes |
|

Stencil Pass Depth Pass Operation |

Sets the operation that the render pass performs when both, the stencil and the depth test, pass. |

No |

Yes |
|

Stencil Test Function |

Controls whether the stencil test discards a fragment. |

No |

Yes |
|

Stencil Write Enabled |

Sets whether to enable writing to the stencil buffer. |

No |

Yes |
|

Step Multiplier |

Sets the smallest distance that a Scroll View scrolls. |

No |

Yes |
|

Step Value |

The minimum amount that the value of the range can change at a time. |

No |

Yes |
|

Stretch |

Whether to scale this Trajectory Layout to match the layout size. |

No |

Yes |
|

Stretch Type Bottom |

Sets how to display the bottom image: * **Stretch**: Scales the image to fill the space between the bottom-left and bottom-right images. * **Wrap**: When the width of the space between the bottom-left and bottom-right images exceeds the width of the image, either extends the last column of pixels in the image or tiles the image. Depends on the value of the **Wrap Mode** property of the texture. |

No |

Yes |
|

Stretch Type Center |

Sets how to display the center image: * **Stretch**: Scales the image to fill the width and height of the center of the nine patch image. * **Wrap**: When the height and width of the center exceed the size of the image, either extends the last row or column of pixels in the image or tiles the image. Depends on the value of the **Wrap Mode** property of the texture. |

No |

Yes |
|

Stretch Type Left |

Sets how to display the left image: * **Stretch**: Scales the image to fill the space between the top-left and bottom-left images. * **Wrap**: When the height of the space between the top-left and bottom-left images exceeds the height of the image, either extends the last row of pixels in the image or tiles the image. Depends on the value of the **Wrap Mode** property of the texture. |

No |

Yes |
|

Stretch Type Right |

Sets how to display the right image: * **Stretch**: Scales the image to fill the space between the top-right and bottom-right images. * **Wrap**: When the height of the space between the top-right and bottom-right images exceeds the height of the image, either extends the last row of pixels in the image or tiles the image. Depends on the value of the **Wrap Mode** property of the texture. |

No |

Yes |
|

Stretch Type Top |

Sets how to display the top image: * **Stretch**: Scales the image to fill the space between the top-left and top-right images. * **Wrap**: When the width of the space between the top-left and top-right images exceeds the width of the image, either extends the last column of pixels in the image or tiles the image. Depends on the value of the **Wrap Mode** property of the texture. |

No |

Yes |
|

Style |

Sets a style to the node. |

No |

Yes |
|

Style Type |

Defines how the style is applied: * Named styles are applied to the objects that set the style in their Style property. * Target styles are applied to the descendant objects of all object types set in the style Target Type property and have the style in their resource dictionary. * Global styles are applied to all object types set in the Target Type property. |

No |

No |
|

Subdivisions |

Sets the number of subdivisions to apply on top of the most basic sphere. Each subdivision increases the number of faces in the sphere. The default is 6. |

No |

No |
|

Subdivisions |

Sets the number of subdivisions to apply to the plane. With the default value 0, the plane consist of one tile. Each subdivision increases the number of tiles in the plane quadratically: the number of tiles equals (subdivisions + 1)^2. |

No |

No |
|

Subdivisions |

Sets the number of subdivisions to apply to the box. With the default value 0, each face of the box consist of one tile. Each subdivision increases the number of tiles in each face quadratically: the number of tiles per face equals (subdivisions + 1)^2. |

No |

No |
|

Support Simple RenderTarget |

Allow rendering to the texture without using a render pass. |

No |

No |
|

Swipe Distance |

Sets the distance that a swipe sends the scroll value in the Grid List Box, relative to the speed of the pointer. |

No |

Yes |
|

Swipe Distance |

Sets the distance that a swipe sends the scroll value, relative to the pointing device speed. |

No |

Yes |
|

Swipe Distance |

Sets the distance that a swipe sends the scroll value in the Trajectory List Box 3D, relative to the speed of the pointer. |

No |

Yes |
|

Tags |

List of tags attached to the item |

No |

No |
|

Tangent Generation Mode |

Sets how Kanzi generates vertex tangents for the meshes in this asset: * **Automatic** chooses the method based on the material that the mesh uses. * **Legacy** calculates the tangents using a legacy algorithm. * **MikkTSpace** calculates the tangents using the MikkTSpace tangent space algorithm. |

No |

No |
|

Target |

The target of the bookmark |

No |

No |
|

Target Animation |

The animation clip or timeline sequence to be inserted into the hosting timeline. Can include animation overrides (See Animation Sharing) that are mappings from the target project items of the target animation into arbitrary other project items. |

No |

No |
|

Target Format |

The format of the image in the exported kzb file. |

No |

No |
|

Target Graphics API |

The version of OpenGL used when exporting shader parameters. |

No |

No |
|

Target Property |

The property on the target item that is to be animated. When animating parts of array or struct properties a path to the sub-property can be given as an expression. |

No |

No |
|

Target Shader Family |

The shader family used when exporting shaders. When Target Graphics API is Vulkan 1.2, only Vulkan shaders are exported. |

No |

No |
|

Target Type |

The node type to which the style applies. |

No |

No |
|

Target Vertex Cache Size |

The size in bytes of the vertex cache on the target hardware. Kanzi Studio uses this value when you enable the Optimize Meshes property. |

No |

No |
|

Text |

Sets the text content that the text node renders. To create a line break press Shift+Enter. |

No |

Yes |
|

Text Hint Prefab |

Sets the prefab template for showing placeholder content when the Text Box node is empty. |

No |

Yes |
|

Text Horizontal Alignment |

Sets the horizontal alignment of the text. |

No |

Yes |
|

Text Key Navigation Direction |

Sets the text key navigation direction. |

No |

Yes |
|

Text Vertical Alignment |

Sets the vertical alignment of the text. |

No |

Yes |
|

Texture |

Sets the texture of the material. |

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

Thumbnail |

Sets the thumbnail that Kanzi Studio shows in the Quick Start window. |

No |

No |
|

Timeline |

The animation timeline to play in Progressive Rendering Viewport 2D |

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

Tone Map Linear Scale |

Sets the scale for the linear tonemap option for the material. When linear tonemapping is used, Kanzi divides all output color by the value of this property. |

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

Trajectory |

Sets the trajectory along which the Trajectory List Box 3D arranges its items. |

No |

Yes |
|

Trajectory |

Sets the Trajectory along which this Trajectory Layout node arranges its items. |

No |

Yes |
|

Trajectory Override Offset |

Sets the offset of an item in a Trajectory Layout. When you do not set this property, the Trajectory Layout sets the offset. |

No |

Yes |
|

Transition Phase |

The phase of the transition. For example, use for pixel-based effects. |

No |

Yes |
|

Transitions |

Transitions to be used within this PageHost node. |

No |

Yes |
|

Truncation |

Sets how Kanzi truncates text when either **Truncation** or **Overflow** property is set and the text does not fit in this node: * **None** disables text truncation. * **At character** truncates text character by character. Default value. * **At word** truncates text by entire words. Kanzi truncates text to fit within the vertical and horizontal limits of the control. If there is not enough vertical space to fit a single line of text, Kanzi truncates all text and does not show overflow characters. |

No |

Yes |
|

Truncation Direction |

Sets which part Kanzi truncates when either the **Truncation** or **Overflow** property is set and the text does not fit in this node: * **Trailing** truncates single- and multiline text at the end. Default value. * **Center** truncates single-line text in the middle. For multiline text, truncates entire lines from the middle, if the text does not fit in the height of this node, and clips text that does not fit in the width of this node. * **Leading** truncates single-line text in the beginning. For multiline text, truncates entire lines from the beginning, if the text does not fit in the height of this node, and clips text that does not fit in the width of this node. |

No |

Yes |
|

Two Pass Rendering |

Defines whether the Text Block 3D is rendered in two passes. Disabling the two pass rendering improves performance, but can cause invalid rendering results when glyph bounds overlap. |

No |

Yes |
|

UASTC Encoding Level |

Set UASTC LDR/HDR 4x4 encoding level. Use faster compression for fast and good results and slower compression for better quality. |

No |

No |
|

Uniforms |

The uniform attributes that the shader uses to render the material: * Uniforms with FIXED_UNIFORM source type have reserved names and are supplied to the shader by Kanzi Engine. * Uniforms with PROPERTY_TYPE source type are specified using the properties in the materials. * Uniforms with NO_SOURCE source type do not have a source specified. To fix that, click Sync with Uniforms. |

No |

No |
|

Update Rate |

Sets the rate at which to render the render pass. To render every frame, set to 1. To render every second frame, set to 2, and so on. To render only once, set to 0. |

No |

Yes |
|

Update Rate Offset |

Sets a frame offset to the rendering rate that you set with the Update Rate property. This lets you cascade multiple updating render passes to different frames. |

No |

Yes |
|

Use Camera Aspect Ratio |

Whether to use the **Aspect Ratio** of the active Camera node to render this asset. By default Kanzi ignores the aspect ratio of the camera. |

No |

No |
|

Use Free Camera Interest Position |

When enabled, Kanzi creates a camera target node at the interest position of the Free Camera nodes and adds corresponding look at constraint. This is disabled by default as free cameras are not normally constrained to interest position. Enabling this may fix erroneous camera orientations on certain FBX files. |

No |

No |
|

Use Intensity Texture |

Enable or disable the use of the Bloom Intensity texture property. |

No |

Yes |
|

Use Original Image |

Whether or not to use original image in images folder directly instead of compressing it when exporting kzb. Note that use of the original image is not always possible. |

No |

No |
|

Use Screen Space |

Whether to layout the mask relative to the screen instead of the node. |

No |

Yes |
|

Use Viewport Aspect Ratio |

Whether to use the aspect ratio setting from the viewport in render pass. When disabled, you can set the aspect ratio in the camera. |

No |

Yes |
|

Value |

The current value. To update this property with a binding, use a to-source or two-way binding. |

No |

Yes |
|

Velocity Texture |   |

No |

Yes |
|

Vertical Alignment |

The alignment in vertical direction the node should use when it resides under a layout. |

No |

Yes |
|

Vertical Margin |

Sets the vertical space between this node and other nodes that are adjacent to this node in a layout. To access the Vertical Margin property fields in a binding, use: * X for the **Bottom** property field * Y for the **Top** property field |

No |

Yes |
|

Vertical Padding |

Sets the padding spaces between the content and the top and bottom boundaries of the Content Layout node. |

No |

Yes |
|

Vertical Padding |

Sets the padding spaces between the content and the top and bottom boundaries of the Text node. |

No |

Yes |
|

Viewport Area |

Modifies the current rendering Viewport node. You can define the Viewport in either relative or absolute coordinates, the default is relative. Use the **Viewport Mode** property to set the coordinate type. |

No |

Yes |
|

Viewport Mode |

Sets the coordinate type for the Viewport node. |

No |

Yes |
|

Visibility Across Projects |

Sets whether this resource is available to referencing projects: * Project setting uses the value of the Resource Visibility Across Projects property of the project. * Private makes the resource available only to this project. * Public makes the resource available in the dropdown menus of referencing projects. |

No |

No |
|

Visible |

When disabled, Kanzi does not render the node. |

No |

Yes |
|

Visible Amount in Parent |

Sets the amount the node is inside its parent. Use the value of this property in shaders to implement fades. Calculated by the parent node. |

No |

Yes |
|

White Scale |

Sets the value that will be tonemapped to pure white. |

No |

Yes |
|

Width |

Sets the absolute width for the automatically created composition target textures. If this property is not set, the size is taken from the current composition stack state using the values of the **Resolution Multiplier** and **Resolution Divisor** properties. |

No |

Yes |
|

Width |

Absolute width of the window in pixels |

No |

No |
|

Width |

Relative width of the window (0,1] |

No |

No |
|

Width |

The width of the box (along X axis) |

No |

No |
|

Width |

Width of the texture |

No |

No |
|

Width |

The width of the plane (along X axis) |

No |

No |
|

Word Wrap |

Sets whether to break long lines into multiple lines to make the text fit within the boundaries of the Text Block node. |

No |

Yes |
|

Wrap Mode |

How the 3D hardware handles the texture mapping when the UV coordinates are outside of the 0 to 1 range. |

No |

No |
|

Z Far |

Sets the distance to the far clipping plane of the camera. The camera shows only the objects that are closer than the value set in this property. |

No |

Yes |
|

Z Near |

Sets the distance to the near clipping plane of the camera. The camera shows only the objects that are farther away than the value set in this property. |

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
## Messages

|

Activity Host: Activity Prefab Attached |

An Activity Host sends this message when it attaches the prefab of the Activity that is activated. |

No |

Yes |
|

Activity Host: Activity Prefab Detached |

An Activity Host sends this message when it detaches the prefab of the Activity that is deactivated. |

No |

Yes |
|

Activity: Activated |

An Activity sends this message when it is activated. |

No |

Yes |
|

Activity: Activating |

An Activity sends this message when it is in the activating state. |

No |

Yes |
|

Activity: Deactivated |

An Activity sends this message when it is deactivated. |

No |

Yes |
|

Activity: Deactivating |

An Activity sends this message when it is in the deactivating state. |

No |

Yes |
|

Activity: Status Changed |

An Activity sends this message when the value of its Activity Status property changes. |

No |

Yes |
|

Animation Player: Completed |

Occurs when an Animation Player completes animation playback. |

No |

Yes |
|

Animation Player: Started |

Occurs when an Animation Player starts animation playback. |

No |

Yes |
|

Animation Player: Stopped |

Occurs when an Animation Player stops animation playback. |

No |

Yes |
|

Button: Cancel |

Occurs when a user lifts their finger outside of a Button that they previously pressed. |

No |

Yes |
|

Button: Click |

Occurs when a user lifts their finger on top of a Button that they previously pressed and when the time set by the Auto Press Interval property in the pressed Button expires. |

No |

Yes |
|

Button: Down |

Occurs when the user presses down the Button. |

No |

Yes |
|

Button: Enter |

Button: Enter trigger is set off: * When the user presses down the button. * When the user presses down the button, moves the pointer outside of the button area, and then moves the pointer back to the button area while still holding down the pointer. |

No |

Yes |
|

Button: Leave |

Button: Leave trigger is set off: * When the user presses down the button and then lifts the pointer. * When the user presses down the button and then moves the pointer outside of the button area. * When the user sets off a **Button: Long Press** trigger. |

No |

Yes |
|

Button: Long Press |

Occurs when the user presses down a Button and holds the Button pressed for the amount of milliseconds defined in the Hold Interval property of that Button. |

No |

Yes |
|

Click: Begin |

Occurs when the user presses a hit-testable node with a Click Manipulator. You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes. |

No |

Yes |
|

Click: Cancel |

Occurs when the user first presses a hit-testable node with a Click Manipulator, then moves the pointer outside of the node area, and lifts the pointer. You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes. |

No |

Yes |
|

Click: Click |

Occurs when the user presses and releases a hit-testable node with a Click Manipulator, while the pointer is still within the node area and Kanzi does not recognize another gesture. You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes. |

No |

Yes |
|

Click: Enter |

Occurs when the user presses a hit-testable node with a Click Manipulator and then every time the user moves the pointer on top of that node while still holding down the pointer. You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes. |

No |

Yes |
|

Click: Leave |

Occurs when the user presses a hit-testable node with a Click Manipulator and then every time the user moves the pointer outside of that node. You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes. |

No |

Yes |
|

Command: Command |

Command message arguments |

No |

Yes |
|

Data Trigger |

Monitors changes in properties and data source values. Use a Data Trigger to apply an action to either set a property value of a target node or activate an Activity node. |

No |

Yes |
|

Drag and Drop: Drag and Drop Canceled |

Occurs when focus moves away from the node during the drag-and-drop gesture. |

No |

Yes |
|

Drag and Drop: Drag and Drop Finished |

Occurs when the user lifts their finger after starting the drag-and-drop gesture. |

No |

Yes |
|

Drag and Drop: Drag and Drop Moved |

Occurs when the user moves their finger after starting the drag-and-drop gesture. |

No |

Yes |
|

Drag and Drop: Drag and Drop Started |

Occurs when the user holds their finger for 500ms on the node. |

No |

Yes |
|

Focus: About To Gain Focus |

Kanzi sends this message before a focusable node receives focus. |

No |

Yes |
|

Focus: About To Lose Focus |

Kanzi sends this message before the focused node loses focus. |

No |

Yes |
|

Focus: Focus Entered Focus Scope |

When focus enters a focus scope, Kanzi sends this message to the focus scope node that contains the node that gains focus. |

No |

Yes |
|

Focus: Focus Gained |

Kanzi sends this message to the node that received focus. |

No |

Yes |
|

Focus: Focus Left Focus Scope |

When focus leaves a focus scope, Kanzi sends this message to the focus scope node that contains the node that loses focus. |

No |

Yes |
|

Focus: Focus Lost |

Kanzi sends this message to the node that lost focus. |

No |

Yes |
|

Focus: Input Outside Overlay |

Kanzi sends this message to an overlay focus scope when the application area outside the boundaries of that overlay receives input. |

No |

Yes |
|

Focus: Overlay Brought To Front |

Occurs when an overlay focus scope becomes the foremost overlay scope in the overlay focus scope stack. |

No |

Yes |
|

Focus: Overlay Gained Focus |

When an overlay scope gains focus, Kanzi sends this message to the overlay scope node that contains the node that gains focus. |

No |

Yes |
|

Focus: Overlay Lost Focus |

When an overlay scope loses focus, Kanzi sends this message to the overlay scope node that contains the node that loses focus. |

No |

Yes |
|

Focus: Overlay Sent To Back |

Occurs when an overlay focus scope is no longer the foremost overlay scope in the overlay focus scope stack. |

No |

Yes |
|

Key Input: Key Canceled |

Occurs when Kanzi recognizes a key-canceled gesture. A key-canceled gesture occurs when Kanzi recognizes that the user canceled a gesture. |

No |

Yes |
|

Key Input: Key Pressed |

Occurs when Kanzi recognizes a key-pressed gesture. A key-pressed gesture occurs when Kanzi recognizes a key event that contains all the elements that compose that gesture. |

No |

Yes |
|

Key Input: Key Released |

Occurs when Kanzi recognizes a key-released gesture. A key-released gesture occurs when Kanzi recognizes the release of one of the elements that compose that gesture. |

No |

Yes |
|

Key Navigation: Key Navigation Canceled |

Occurs when the key-pressed gesture is canceled for the navigation direction. |

No |

Yes |
|

Key Navigation: Key Navigation Finished |

Occurs when Kanzi recognizes the key-released gesture for the navigation direction. To capture key navigation gestures for a node, create a Navigation Manipulator component in that node. |

No |

Yes |
|

Key Navigation: Key Navigation Started |

Occurs when Kanzi recognizes the key-pressed and key repeat gestures for the navigation direction. To capture key navigation gestures for a node, create a Navigation Manipulator component in that node. |

No |

Yes |
|

List Box: Item Loaded |

Occurs when an item is loaded to the working memory. To set how many items you want to keep loaded in the working memory at a time, use the Keep Alive Item Count property. |

No |

Yes |
|

List Box: Item Selected |

Occurs when an item is selected. |

No |

Yes |
|

List Box: Item Unloaded |

Occurs when an item is unloaded from the working memory. To set how many items you want to keep loaded in the working memory at a time, use the Keep Alive Item Count property. |

No |

Yes |
|

List Box: Scroll Finished |

Occurs when the List Box stops scrolling. |

No |

Yes |
|

List Box: Scroll Started |

Occurs when the List Box starts to scroll. |

No |

Yes |
|

List Box: Scrolled |

Occurs when the List Box scrolls. |

No |

Yes |
|

List Box: Target Changed |

Occurs when List Box gets a new target item. |

No |

Yes |
|

List Box: User Scroll Finished |

Occurs when the application user stops scrolling the List Box. |

No |

Yes |
|

List Box: User Scroll Started |

Occurs when the application user starts to scroll the List Box. |

No |

Yes |
|

Long Press: Long Press |

Occurs when the user presses a hit-testable node with a Long-Press Manipulator and holds the press for the time that you set in the Long-Press Manipulator. You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes. |

No |

Yes |
|

Long Press: Long Press Cancel |

Occurs during the long-press gesture when the user moves the focus away from a hit-testable node with a Long-Press Manipulator. You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes. |

No |

Yes |
|

Message Trigger |   |

No |

Yes |
|

Multi-Click: Intermediate Click |

Occurs when the user presses and releases a hit-testable node with a Multi-Click Manipulator that is set to send messages for intermediate clicks. To set a Multi-Click Manipulator to send messages for intermediate clicks, in the Multi-Click Manipulator enable the Send Intermediate Click Messages property. You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes. |

No |

Yes |
|

Multi-Click: Multi-Click |

Occurs when the user presses and releases a hit-testable node with a Multi-Click Manipulator a specified number of times (default 2) within a set amount of time (default 250 ms) between presses. You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes. |

No |

Yes |
|

Multi-Click: Multi-Click Canceled |

Occurs during the multi-click gesture when the user moves the focus away from a hit-testable node with a Multi-Click Manipulator. You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes. |

No |

Yes |
|

On Attached |

This trigger is set off when the item is initialized. For example, when you add a node to the node tree, or enter a state that contains this trigger. |

No |

Yes |
|

On Property Change |

Occurs when a property is changed |

No |

Yes |
|

On Timer |

Occurs when timer interval is elapsed |

No |

Yes |
|

Page (deprecated): Activated (deprecated) |

Page has been activated. |

No |

Yes |
|

Page (deprecated): Deactivated (deprecated) |

Page has been deactivated. |

No |

Yes |
|

Page Host (deprecated): Page Navigation Finished (deprecated) |

Page host has finished navigation process. |

No |

Yes |
|

Page Host (deprecated): Page Navigation Started (deprecated) |

Page host has started navigation process. |

No |

Yes |
|

Pan: Pan Canceled |

Occurs when focus moves away from the node during the pan gesture. |

No |

Yes |
|

Pan: Pan Entered |

Occurs when the pan gesture enters the node to which the Pan Manipulator is attached. |

No |

Yes |
|

Pan: Pan Finished |

Occurs when the user lifts their finger after Kanzi recognizes a pan gesture. |

No |

Yes |
|

Pan: Pan Left |

Occurs when the pan gesture leaves the node to which the Pan Manipulator is attached. |

No |

Yes |
|

Pan: Pan Moved |

Occurs when the user changes the position of their finger and that change exceeds the recognition thresholds. |

No |

Yes |
|

Pan: Pan Started |

Occurs when the user presses down their finger on the node. If the user lifts their finger before exceeding the position change threshold, Kanzi cancels the pan gesture. |

No |

Yes |
|

Pinch: Pinch Canceled |

Occurs when focus moves away from the node during the pinch gesture. |

No |

Yes |
|

Pinch: Pinch Finished |

Occurs when the user lifts their finger after Kanzi recognizes a pinch gesture. |

No |

Yes |
|

Pinch: Pinch Moved |

Occurs when the user changes the position of their finger and that change exceed the scale or rotation threshold. |

No |

Yes |
|

Pinch: Pinch Started |

Occurs when the user presses down their finger. If the user lifts their finger before it exceeds the scale or rotate threshold, Kanzi cancels the pinch. |

No |

Yes |
|

Prefab View: Asynchronous Load Completed |

Occurs when asynchronous loading of resources from a prefab has been finished. |

No |

Yes |
|

Property Target Easing Interpolator: Easing Interpolation Completed |

Occurs when Property Target Easing Interpolator completes its interpolation. |

No |

Yes |
|

Property Target Interpolator: Interpolation Completed |

Occurs when property target interpolator completes interpolation. |

No |

Yes |
|

Range: Value Change Finished |

Occurs when the range value stops changing. |

No |

Yes |
|

Range: Value Change Started |

Occurs when the range value starts changing. |

No |

Yes |
|

Range: Value Changed |

Occurs when the range value has changed. |

No |

Yes |
|

Scroll View: Scroll Ended |

Occurs when the scroll position of a Scroll View node stops changing. |

No |

Yes |
|

Scroll View: Scroll Started |

Occurs when the scroll position of a Scroll View node starts changing. |

No |

Yes |
|

Scroll View: Scroll Zoomed |

Occurs when the zoom level of a Scroll View node changes. |

No |

Yes |
|

Scroll View: Scrolled |

Occurs when the scroll position of a Scroll View node changes. |

No |

Yes |
|

Scroll View: Snap Request |

Occurs when a Scroll View node requests snapping target from the hosting component. |

No |

Yes |
|

Scroll View: User Scroll Ended |

Occurs when the user stops scrolling a Scroll View node. |

No |

Yes |
|

Scroll View: User Scroll Started |

Occurs when the user starts scrolling a Scroll View node. |

No |

Yes |
|

State Manager: Entered State |

Occurs when a state manager has entered a state. |

No |

Yes |
|

State Manager: Left State |

Occurs when a state manager has left a state. |

No |

Yes |
|

State Manager: Transition Finished |

Occurs when a state manager finishes a transition to a state. |

No |

Yes |
|

State Manager: Transition Started |

Occurs when a state manager begins a transition to a state. |

No |

Yes |
|

Text Box: Composition Text Changed |

Occurs when the text produced in an Input Method Editor is updated in a Text Box node. |

No |

Yes |
|

Text Box: Composition Text Committed |

Occurs: * When the text produced in an Input Method Editor is committed to the cached text in a Text Box node. * When a trigger executes the **Text Box: Commit Composition Text** action. |

No |

Yes |
|

Text Box: Cursor Moved |

Occurs when the user moves the cursor in a Text Box node. |

No |

Yes |
|

Text Box: Editing Finished |

Occurs when a Text Box node leaves the editing state after the user modified the text content. |

No |

Yes |
|

Text Box: Editing Started |

Occurs when the user makes the first modification to the text in a Text Box node that is in the editing state. |

No |

Yes |
|

Text Box: Entered Editing State |

Occurs when a Text Box node enters the editing state. |

No |

Yes |
|

Text Box: Input Method Action |

Occurs when the user taps the action button on their on-screen keyboard while editing the text in a Text Box node. |

No |

Yes |
|

Text Box: Input Method Available |

Occurs when an input method becomes available to a Text Box node. For example, an on-screen keyboard becomes available when it appears on the screen. |

No |

Yes |
|

Text Box: Input Method Unavailable |

Occurs when the input method that is composing text in a Text Box node becomes unavailable. For example, an on-screen keyboard becomes unavailable when the user hides it. |

No |

Yes |
|

Text Box: Left Editing State |

Occurs when a Text Box node leaves the editing state |

No |

Yes |
|

Text Box: Selection Changed |

Occurs when the user changes the text selection in a Text Box node. |

No |

Yes |
|

Text Box: Selection Cleared |

Occurs when the user clears or resets the text selection in a Text Box node. |

No |

Yes |
|

Text Box: Selection Started |

Occurs when the user starts selecting text in a Text Box node. |

No |

Yes |
|

Text Box: Text Changed |

Occurs when the user changes the text in a Text Box node. |

No |

Yes |
|

Text Box: Text Composition Canceled |

Occurs: * When the text composition in a Text Box node is canceled by Input Method that is in text composition state. * When a trigger executes the **Text Box: Cancel Text Composition** action. |

No |

Yes |
|

Toggle Button Group: Toggled |

Occurs when the toggle state of a **Toggle Button** node in a **Toggle Button Group** node changes. |

No |

Yes |
|

Toggle Button: State Toggled |

Occurs when the toggle state of a Toggle Button changes. |

No |

Yes |
|

Toggle Button: Toggled Off |

Occurs when a Toggle Button is toggled off. |

No |

Yes |
|

Toggle Button: Toggled On |

Occurs when a Toggle Button is toggled on. |

No |

Yes |
