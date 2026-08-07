---
title: Render Pass
source: https://docs.kanzi.com/4.1.0/en/reference/node-and-resource-reference/render-pass-reference.html
---

# Render Pass

## Render Pass available properties

|

Name |

Description |

Inherited |

Exported to Kanzi Engine |
|

Acceleration Structure |   |

No |

Yes |
|

Acceleration Structure |   |

No |

Yes |
|

Addressing Mode |

Sets how Kanzi handles the texture coordinates of the automatically generated composition target textures outside of the [0, 0] - [1, 1] rectangle: * **Repeat** sets the texture to repeat outside of these coordinates. This is the default value. * **Mirror** sets the texture to repeat, but mirrors every other repetition. * **Clamp** confines the texture to these coordinates and outside of these texture coordinates repeats the edge texels of the texture. * **Mirror once** sets the texture to repeat once in the negative direction, and after that clamps the texture. |

No |

Yes |
|

Alpha To Coverage Enabled |

Sets whether Alpha To Coverage is enabled or not. |

No |

Yes |
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

Blue Noise |   |

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

Sets the Camera node that you want to use to render the nodes. To use the default Camera node in that Scene node, do not set the value for this property. |

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

Color Write Mode |

Sets which channels the render pass writes to the color buffer. To disable the color write, set the property to None. |

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

Current Mipmap Level |

Reports the mipmap level that Kanzi is generating. Use this property in a material that you use to customize how Kanzi generates mipmaps for the composition targets of a Composition Target Render Pass or Cubemap Render Pass.The value of this property is valid only while Kanzi generates the mipmaps. |

No |

Yes |
|

Denoiser Mode |

Temporal clamping/rejection mode: 0 - none, 1 - reject using depth min max, 2 - reject using filter |

No |

Yes |
|

Depth Compare Function |

Sets the comparison function to be used with comparison samplers of the Composition Target render passâ depth target. |

No |

Yes |
|

Depth Compare Function |

Sets the comparison function to be used with comparison samplers of the Cubemap render passâ depth target. |

No |

Yes |
|

Depth Format |

Sets the format of the automatically created depth render buffer used for the cubemap rendering. If this property is not set, the depth requirement and format are autodetected. |

No |

Yes |
|

Depth Mipmap Material |

Sets the material to use to generate the mipmaps for the Result Depth Texture of a Composition Target Render Pass. To use the default mipmap generation, remove the property or set it to the default value â< No Material >â. |

No |

Yes |
|

Depth Renderbuffer Format |

Sets the format of the automatically created depth renderbuffers. When you do not set this property, Kanzi sets the depth renderbuffer format automatically to the best available format, in most cases the 32-bit float format. To create depth textures, set the **Depth Texture Format** property whose value overrides the value of this property. |

No |

Yes |
|

Depth Renderbuffer Format |

Sets the format of the automatically created depth renderbuffers. When you do not set this property, Kanzi sets the depth renderbuffer format automatically to the best available format, in most cases the 32-bit float format. To create depth textures, set the **Depth Format** property whose value overrides the value of this property. |

No |

Yes |
|

Depth Target |

Sets the depth target to which you want to render the result of the child render passes of this render pass. |

No |

Yes |
|

Depth Target |

Sets the target for depth rendering for this Cubemap render pass. |

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

Directional Lights |

Use this property to bind the directional light set for rendering. |

No |

Yes |
|

Disable KZB Export |

Disables the exporting of the item into KZB. Can be used for, e.g. letting items out from certain profiles. The disabled items are always included in preview. |

No |

No |
|

Enabled |

Whether Kanzi executes this render pass and its child render pass tree. |

No |

Yes |
|

Engine Factory Name |

The factory name for this composer. Can be used to instantiate composer or render pass from plugin. |

No |

No |
|

Environment Ambient Texture |   |

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

Sets how Kanzi handles accessing the texture samples of the automatically generated composition target: * **Nearest** takes the color from the nearest sample. * **Linear** interpolates color from neighboring samples. This is the default value. |

No |

Yes |
|

Filter Mode |

Sets how Kanzi handles accessing the texture samples of the automatically generated composition cubemap target: * **Nearest** takes the color from the nearest sample. * **Linear** interpolates color from neighboring samples. This is the default value. |

No |

Yes |
|

Frustum Culling |

Enable to disable rendering objects that are not inside the view frustum. Trades GPU rendering time for CPU cull test time. |

No |

Yes |
|

GBuffer Depth |   |

No |

Yes |
|

GBuffer Depth |   |

No |

Yes |
|

GBuffer Normal |   |

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

Height |

Sets the absolute height for the automatically created composition target textures. If this property is not set, the size is taken from the current composition stack state using the values of the **Resolution Multiplier** and **Resolution Divisor** properties. |

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

Input Viewport Area |

Reports the viewport area relative to the composition space as passed from the parent render pass.

To access the Input Viewport Area property fields in a binding, use: * X for the offset along the x axis relative to the composition space * Y for the offset along the y axis relative to the composition space * Z for the width of the viewport * W for the height of the viewport  |

No |

Yes |
|

Light |   |

No |

Yes |
|

Material |

Sets to the Material that you want a Blit render pass to use to blit one or more textures. |

No |

Yes |
|

Material |

Sets the material that will be used to render all nodes rendered by this DrawObjectsWithMaterialRenderPass. |

No |

Yes |
|

Material |

Sets the material that will have all other Material Setup render pass properties set to. |

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

Material Requirements |

Sets the material requirements required from materials selected for rendering. |

No |

Yes |
|

Minimum Unreprojected Shadow |   |

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

Mipmap Source Texture |

Reports the texture that contains the render target texture for which Kanzi creates mipmaps. Use this property as the source texture in a material that you use to customize how Kanzi generates mipmaps for the composition targets of a Composition Target Render Pass or Cubemap Render Pass. The default value is < No Texture > |

No |

Yes |
|

Multisample Level |

Sets the amount of multisample anti-aliasing to apply to the automatically generated composition target textures. |

No |

Yes |
|

Node List |

Input node list range. Set by a binding from nearest parent node list. |

No |

Yes |
|

Object Source |

Sets the object source which collects the nodes that you want to use for ray tracing. To render all nodes in a Scene node (Root Object Source), do not set the value for this property. |

No |

Yes |
|

Object Source |

Sets the object source which collects the nodes that you want to render with this render pass. To render all nodes in a Scene node (Root Object Source), do not set the value for this property. |

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

Override Camera |

Sets the Camera node that you want to use to render the nodes to the composition cubemap texture. To use the default Camera node in that Scene node, do not set the value for this property. |

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

Point Lights |

Use this property to bind the point light set for rendering. |

No |

Yes |
|

Polygon Depth Offset |

Sets the polygon depth offset to apply to the element that the Pipeline State render pass renders: * **Derivative multiplier** sets the multiplier for the depth change derivative for the fragment. * **Constant multiplier** multiplies the smallest measurable unit of depth, dependent on the target platform.

You can use the offset to render decals on the surfaces of filled polygons. Kanzi typically shows nearer the camera those polygons that have a negative offset.  |

No |

Yes |
|

Previous Camera Matrix |

Camera matrix from the previous frame, used for velocity buffer calculation. |

No |

Yes |
|

Previous Projection Matrix |

Projection matrix from the previous frame, used for velocity buffer calculation. |

No |

Yes |
|

Ray Maximum Trace Distance |   |

No |

Yes |
|

Ray Maximum Trace Distance |   |

No |

Yes |
|

Raytraced Reflection Maximum Roughness |   |

No |

Yes |
|

Reflection Resolution Scale |   |

No |

Yes |
|

Render Pass Prefab |

Sets the Render Pass Prefab that this Render Pass View instantiates. |

No |

Yes |
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

Shadow Map Resolution Scale |   |

No |

Yes |
|

Shadow Mask |   |

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

Sorting Order |

Sets the sorting order for render entries. |

No |

Yes |
|

Spot Lights |

Use this property to bind the spot light set for rendering. |

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

Velocity Texture |   |

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

Width |

Sets the absolute width for the automatically created composition target textures. If this property is not set, the size is taken from the current composition stack state using the values of the **Resolution Multiplier** and **Resolution Divisor** properties. |

No |

Yes |
## Render Pass messages

|

Name |

Description |

Inherited |

Exported to Kanzi Engine |
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

Occurs when the user presses a hit-testable node with a Click Manipulator.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Click: Cancel |

Occurs when the user first presses a hit-testable node with a Click Manipulator, then moves the pointer outside of the node area, and lifts the pointer.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Click: Click |

Occurs when the user presses and releases a hit-testable node with a Click Manipulator, while the pointer is still within the node area and Kanzi does not recognize another gesture.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Click: Enter |

Occurs when the user presses a hit-testable node with a Click Manipulator and then every time the user moves the pointer on top of that node while still holding down the pointer.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Click: Leave |

Occurs when the user presses a hit-testable node with a Click Manipulator and then every time the user moves the pointer outside of that node.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

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

Occurs when the user presses a hit-testable node with a Long-Press Manipulator and holds the press for the time that you set in the Long-Press Manipulator.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Long Press: Long Press Cancel |

Occurs during the long-press gesture when the user moves the focus away from a hit-testable node with a Long-Press Manipulator.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Message Trigger |   |

No |

Yes |
|

Multi-Click: Intermediate Click |

Occurs when the user presses and releases a hit-testable node with a Multi-Click Manipulator that is set to send messages for intermediate clicks.

To set a Multi-Click Manipulator to send messages for intermediate clicks, in the Multi-Click Manipulator enable the Send Intermediate Click Messages property.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Multi-Click: Multi-Click |

Occurs when the user presses and releases a hit-testable node with a Multi-Click Manipulator a specified number of times (default 2) within a set amount of time (default 250 ms) between presses.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Multi-Click: Multi-Click Canceled |

Occurs during the multi-click gesture when the user moves the focus away from a hit-testable node with a Multi-Click Manipulator.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

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
