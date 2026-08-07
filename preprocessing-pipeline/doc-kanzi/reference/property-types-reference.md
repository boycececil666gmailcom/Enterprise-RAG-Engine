---
title: Property types reference
source: https://docs.kanzi.com/4.1.0/en/reference/property-types-reference.html
---

# Property types reference

This table lists all default property types available in Kanzi. See Property system, Creating property types, and Node and resource reference.

Name |

Display Name |

Inherited |

Attachable |

Description |

Action.Delay |

Action Delay (ms) |

No |

No |

The time in milliseconds after which Kanzi invokes the action. |

ActivityConcept.ActivityMessageArguments.ActivityName |

Activity Name |

No |

No |   |

ActivityConcept.KeepActivityAlive |

Keep Activity Alive |

No |

Yes |

Sets how to handle the Activity node when you deactivate it: * **Detach and Destroy.** Kanzi detaches the Activity from the node tree and deletes the Activity instance. Default value. * **Hide and Disable.** Kanzi hides and disables the Activity. When you activate the Activity again, Kanzi enables and shows the same Activity. This way you skip Activity instantiation when you activate the Activity again. |

ActivityConcept.SaveLastFocusedNode |

Save Last Focused Node |

No |

Yes |

When this property is enabled, Kanzi remembers the last-focused node in this Activity and sets the key focus to that node when you activate this Activity again. This is the default. When you do not want Kanzi to remember the last-focused node in this Activity, disable this property. |

ActivityConcept.Status |

Activity Status |

No |

Yes |

Sets the possible states of the Activity when its Activity Host activates or deactivates that Activity. |

ActivityConcept.StatusChangedMessageArguments.Status |

Activity Status |

No |

No |

The possible states of an Activity when its Activity Host activates or deactivates that Activity. |

ActivityElement.PreserveHistory |

Preserve History |

No |

Yes |

Determines whether Kanzi preserves Activity property values when that Activity becomes inactive: * When enabled, Kanzi stores the values of Activity properties of this Activity and its child Activities. The default value. * When disabled, Kanzi discards the values of Activity properties of this Activity and its child Activities. |

ActivityHostConcept.ActivationMessageArguments.ActivationPath |

Activity Activation Path |

No |

No |

The relative path from the target Activity Host to the Activity that you want to activate. |

ActivityHostConcept.ActivationMessageArguments.ResetHistory |

Reset History |

No |

No |

Determines whether Kanzi resets the Activity property values when an Activity becomes active: * When enabled, Kanzi discards the serialized values of Activity properties for this Activity and its child Activities. * When disabled, Kanzi reinstates the serialized values of Activity properties of this Activity and its child Activities. The default value. |

ActivityHostConcept.ActivityPrefabMessageArguments.ActivityName |

Activity Name |

No |

No |

The name of the child Activity whose prefab was attached or detached. |

AlphaCutoff |

Alpha Cutoff |

No |

Yes |

Sets the cutoff threshold for alpha cutting. If the alpha value is less than the value of this property, Kanzi discards the fragment. The default value is 0.5. |

Ambient |

Ambient Color |

No |

Yes |

Sets the color of the material when lights are not present. Use the Intensity (I) property field to adjust the exposure of the color. |

AnimationBindingProcessor.Animation |

Animation Item Path |

No |

No |

The animation binding processor applies this animation when the binding is updated. |

AnimationPlayer.AutoplayEnabled |

Autoplay Enabled |

No |

No |

Specifies whether animation player should start playback of its timeline automatically when it is attached to the node. |

AnimationPlayer.DurationScale |

Duration Scale |

No |

No |

Specifies how much duration of the timeline is scaled during its playback. |

AnimationPlayer.PlaybackMode |

Playback Mode |

No |

No |

Specifies the mode of timeline playback (normal, reverse, pingpong). |

AnimationPlayer.PlayMessageArguments.DurationScale |

Duration Scale |

No |

No |

Specifies how much duration of the timeline is scaled during its playback. This scale is applied on top of playerâs duration scale property. |

AnimationPlayer.PlayMessageArguments.PlaybackMode |

Playback Mode |

No |

No |

Specifies the mode of timeline playback (normal, reverse, pingpong). This mode is applied on top of playerâs mode property. |

AnimationPlayer.PlayMessageArguments.RepeatCount |

Repeat Count |

No |

No |

Specifies how many times the timeline is played during its playback (1 for one time playback, 0 for infinite amount of repeats). This repeat count is applied on top of playerâs repeact count property. |

AnimationPlayer.RelativePlayback |

Relative Playback |

No |

No |

Specifies whether animations are played in relative manner by adding animated value to target property value instead of replacing the property value. |

AnimationPlayer.RepeatCount |

Repeat Count |

No |

No |

Specifies how many times the timeline is played during its playback (1 for one time playback, 0 for infinite amount of repeats). |

AnimationPlayer.RestoreOriginalValuesAfterPlayback |

Restore Original Values After Playback |

No |

No |

Specifies whether animated properties return to their initial values after playback of the timeline ends. |

AnimationPlayer.Timeline |

Target Animation Timeline |

No |

No |

The target animation timeline. |

AORadius |

Ambient Occlusion Radius |

No |

Yes |

Screen-space ambient occlusion (SSAO) effect radius. Used to calculate the SSAO texture. |

AOStrength |

Ambient Occlusion Strength |

No |

Yes |

Screen-space ambient occlusion (SSAO) strength. Used to calculate the SSAO texture. |

ApplyActivationAction.ActivationPath |

Activity Activation Path |

No |

No |

The activation path from the Activity Host, which is set as the target of this action, to the Activity node you want to activate. The activation path contains only the Activity nodes and the Activity Hosts nodes. |

ApplyActivationAction.ActivityHostPath |

Activity Host Path |

No |

No |

Path to the Activity Host node of the activated Activity node. |

BaseColorFactor |

Base Color Factor |

No |

Yes |

Sets the base color for the material. |

BaseColorTexture |

Base Color Texture |

No |

Yes |

Sets the texture that contains the base color for the material. Use the Base Color Factor property to filter the value from this texture. |

BindingItem.TargetPropertyType |

Target Property |

No |

Yes |

The binding target property |

BindingSourceItem.PropertyType |

Source Property |

No |

Yes |

The binding source property |

BlendIntensity |

Blend Intensity |

No |

Yes |

Controls the intensity of materials that are blended on top of an existing color. Attached property enables overriding of the blend intensity of the used materials at render pass or object node level. |

BlendMode |

Blend Mode |

No |

Yes |

Sets how to combine the color and alpha values of pixels in one layer or image with those in the underlying layer or image. |

BlitRenderPass.Material |

Material |

No |

Yes |

Sets to the Material that you want a Blit render pass to use to blit one or more textures. |

BlitRenderPass.Texture0 |

Texture 0 |

No |

Yes |

Sets the first texture you want the Blit render pass to blit. |

BlitRenderPass.Texture1 |

Texture 1 |

No |

Yes |

Sets the second texture you want the Blit render pass to blit. |

BlitRenderPass.Texture2 |

Texture 2 |

No |

Yes |

Sets the third texture you want the Blit render pass to blit. |

BlitRenderPass.Texture3 |

Texture 3 |

No |

Yes |

Sets the fourth texture you want the Blit render pass to blit. |

BlitRenderPass.Texture4 |

Texture 4 |

No |

Yes |

Sets the fifth texture you want the Blit render pass to blit. |

BlitRenderPass.Texture5 |

Texture 5 |

No |

Yes |

Sets the sixth texture you want the Blit render pass to blit. |

BlitRenderPass.Texture6 |

Texture 6 |

No |

Yes |

Sets the seventh texture you want the Blit render pass to blit. |

BlitRenderPass.Texture7 |

Texture 7 |

No |

Yes |

Sets the eighth texture you want the Blit render pass to blit. |

BlitRenderPass.Texture8 |

Texture 8 |

No |

Yes |

Sets the ninth texture you want the Blit render pass to blit. |

BlitRenderPass.Texture9 |

Texture 9 |

No |

Yes |

Sets the tenth texture you want the Blit render pass to blit. |

BlitRenderPass.TextureCubemap |

Cubemap Texture |

No |

Yes |

Sets the cubemap texture you want the Blit render pass to blit. |

Bloom.BloomIntensity |

Bloom Intensity |

No |

Yes |

Bloom intensity for the material. |

Bloom.BloomIntensityTexture |

Bloom Intensity Texture |

No |

Yes |

Sets the bloom intensity texture. |

Bloom.BloomRadius |

Bloom Radius |

No |

Yes |

Bloom radius for the material. |

Bloom.BloomUseIntensityTexture |

Use Intensity Texture |

No |

Yes |

Enable or disable the use of the Bloom Intensity texture property. |

BlurDirection |

Ambient Occlusion Blur Direction |

No |

Yes |

Blur direction of the ambient occlusion bilateral blur. |

BlurEffect2D.Masked |

Masked Blur |

No |

Yes |

Sets whether to blur only the pixels whose alpha channel value is not zero. When you enable this property, the blur does not spread to fully transparent pixels and the edges of the content stay sharp. The default value is false. |

BlurEffect2D.Quality |

Blur Quality |

No |

Yes |

Sets the visual quality of the blur. Lower quality uses less computing and memory resources. |

BlurEffect2D.Radius |

Blur Radius |

No |

Yes |

Sets the amount of blur by defining the radius of the circular area of pixels that blend into each other. The blur radius also determines the distance in pixels that the blur expands the render area by extending outward from an edge, unless you enable the **Masked Blur** property. To disable the blur effect, set this property to 0. The default value is 8. |

BrdfLookUpTable |

BRDF Lookup Table |

No |

Yes |

Gets the Bidirectional Reflectance Distribution Function (BRDF) lookup table for the material. The BRDF table is a texture that contains precomputed information about how light reflects off a material. You can use it to improve rendering quality. |

Brush.BrushType |

Brush Type |

No |

Yes |

The type of the brush. |

Brush.HorizontalTiling |

Brush Horizontal Tiling |

No |

Yes |

Horizontal Tiling for the brush. Affects the scale of texture coordinates. |

Brush.ModulateColor |

Brush Modulate Color |

No |

Yes |

Modulation color for brush. Effects brush rendering that needs color modulation. |

Brush.VerticalTiling |

Brush Vertical Tiling |

No |

Yes |

Vertical Tiling for the brush. Affects the scale of texture coordinates. |

BuildAccelerationStructureRenderPass.ObjectSource |

Object Source |

No |

Yes |

Sets the object source which collects the nodes that you want to use for ray tracing. To render all nodes in a Scene node (Root Object Source), do not set the value for this property. |

BuildAccelerationStructureRenderPass.OutputAccelerationStructure |

Output Acceleration Structure |

No |

Yes |

Built acceleration structure resource. |

ButtonConcept.AutoClickInterval |

Auto Press Interval |

No |

Yes |

Sets the time in milliseconds after which a button that the user keeps pressed down sends the Button: Click message. While the user holds the button down, the button keeps sending the Button: Click message at the time interval set by this property. To disable the behavior, set to 0. |

ButtonConcept.IndexInGroup |

Index In Group |

No |

Yes |

Sets the index of the Toggle Button in the Toggle Button Group to which that Toggle Button is registered. If a Toggle Button does not have a local value for this property, it is not registered to the ancestor Toggle Button Group. When set to -1, the Toggle Button Group assigns an index for the Toggle Button. |

ButtonConcept.IsPressed |

Is Down |

No |

Yes |

Indicates whether the button is pressed and in the down state. |

ButtonConcept.LongPressInterval |

Hold Interval |

No |

Yes |

Sets the amount of time in milliseconds that the user must hold the button pressed down for Kanzi to recognize it as a long-press gesture. To disable the long-press gesture, set to 0. |

ButtonConcept.PressOnHover |

Down On Hover |

No |

Yes |

Whether holding a finger on the device screen and moving it over the button transitions the button to the down state. |

ButtonConcept.ToggleState |

Toggle State |

No |

Yes |

Sets the toggle state of a Toggle Button. To update this property with a binding, use a to-source or two-way binding. |

ButtonConcept.ToggleStateCount |

Toggle State Count |

No |

Yes |

Sets the number of toggle states of a Toggle Button. |

Camera.AspectRatio |

Aspect Ratio |

No |

Yes |

Sets the aspect ratio of the camera. |

Camera.AsymmetricFov |

Asymmetric FOV |

No |

Yes |

Sets the field of view of the camera in degrees toward the left, right, up, and down. Angles to the right of the center and upwards of the center are positive.

To use this property, set the **Projection Type** to **Asymmetric perspective**.  |

Camera.DisableAspectRatio |

Use Viewport Aspect Ratio |

No |

Yes |

Whether to use the aspect ratio setting from the viewport in render pass. When disabled, you can set the aspect ratio in the camera. |

Camera.Fov |

FOV |

No |

Yes |

Sets the field of view of the camera in degrees. |

Camera.FovType |

FOV Type |

No |

Yes |

Sets the direction of the field of view: * **Y FOV** sets the field of view along the y axis. This is the default. * **X FOV** sets the field of view along the x axis. |

Camera.OrthogonalCoordinateSystemType |

Orthogonal Type |

No |

Yes |

Sets the type of the orthogonal coordinate system: * **Relative** sets the camera to display an area whose width is scaled with the value of the **Orthogonal Plane Size** property. This is the default. * **Absolute** sets the camera to use pixel coordinates. |

Camera.OrthogonalPlaneHeight |

Orthogonal Plane Size |

No |

Yes |

Sets the half width or half height of the view plane of a camera that uses the relative orthogonal coordinate system: * When **FOV Type** is **Y FOV** (default value), the height. * When **FOV Type** is **X FOV**, the width.

The default value is 1.0.  |

Camera.ProjectionType |

Projection Type |

No |

Yes |

Sets the projection type of the camera: * **Perspective** projection shows objects closer to the camera larger than those that are further away. This is the default. * **Asymmetric perspective** projection lets you use the **Asymmetric FOV** property to control the field of view of each angle of a perspective projection. * **Orthographic projection** shows a 2D view of a 3D scene without providing a sense of depth. |

Camera.ZFar |

Z Far |

No |

Yes |

Sets the distance to the far clipping plane of the camera. The camera shows only the objects that are closer than the value set in this property. |

Camera.ZNear |

Z Near |

No |

Yes |

Sets the distance to the near clipping plane of the camera. The camera shows only the objects that are farther away than the value set in this property. |

ChromaticAberration.ChromaticAberrationAmount |

Amount |

No |

Yes |

Sets the chromatic aberration amount. |

ChromaticAberration.ChromaticAberrationDitheringAmount |

Dithering Amount |

No |

Yes |

Sets the chromatic aberration dithering amount. |

ClearCoatNormalScale |

Clear Coat Normal Scale |

No |

Yes |

Sets the clear coat normal scale for the material. Use the scale to set the intensity of the Clear Coat Normal Texture. |

ClearCoatNormalTexture |

Clear Coat Normal Texture |

No |

Yes |

Sets the texture that contains a clear coat normal map for the material. Use the Clear Coat Normal Scale property to scale the texture value. |

ClearCoatRoughnessFactor |

Clear Coat Roughness Factor |

No |

Yes |

Sets the roughness of the outer clear coat layer for the material: 0 represents a smooth, glossy surface, and 1 represents a rough, diffuse surface. |

ClearCoatRoughnessTexture |

Clear Coat Roughness Texture |

No |

Yes |

Sets the texture that contains a clear coat roughness map for the material. Kanzi reads the roughness from the Green channel of the texture. Use the Clear Coat Roughness Factor property to scale the roughness from this texture. |

ClearCoatStrengthFactor |

Clear Coat Strength Factor |

No |

Yes |

Sets the clear coat strength for the material: 0 represents a material with no clear coat, and 1 represents a full strength clear coat. |

ClearCoatStrengthTexture |

Clear Coat Strength Texture |

No |

Yes |

Sets the texture that contains a clear coat strength map for the material. Kanzi reads the strength from the Red channel of the texture. Use the Clear Coat Strength Factor property to scale the strength from this texture. |

ClearRenderPass.ClearColor0 |

Clear Color 0 |

No |

Yes |

Sets the color that you want the Clear render pass to use to clear the first (default) color buffer. |

ClearRenderPass.ClearColor1 |

Clear Color 1 |

No |

Yes |

Sets the color that you want the Clear render pass to use to clear the second color buffer. |

ClearRenderPass.ClearColor2 |

Clear Color 2 |

No |

Yes |

Sets the color that you want the Clear render pass to use to clear the third color buffer. |

ClearRenderPass.ClearColor3 |

Clear Color 3 |

No |

Yes |

Sets the color that you want the Clear render pass to use to clear the fourth color buffer. |

ClearRenderPass.ClearDepth |

Clear Depth |

No |

Yes |

Sets the depth that you want the Clear render pass to use to clear the depth buffer. |

ClearRenderPass.ClearStencil |

Clear Stencil |

No |

Yes |

Sets the clear stencil that you want the Clear render pass to use to clear the stencil buffer. |

ClickConcept.DoubleClickEnabled |

Double-Click Enabled |

No |

Yes |

Whether to install a multi-click manipulator that generates double-click messages. Use this property to enable the double-click gesture for a Button node or List Box items. To enable double-click for List Box items, enable this property in the List Box Item Container. |

CodeBehind.CodeBehindSource |

Code Behind Source |

No |

Yes |

Sets the metaclass name of the code behind class for this node. |

ColorBrush.Color |

Brush Color |

No |

Yes |

Color for brush. Set alpha to 0 to disable brush. |

ColorGrading.ColorGradingHighlightColor |

Grading Color Highlight |

No |

Yes |

Sets the color grading highlight color. |

ColorGrading.ColorGradingHighlightRange |

Grading Highlight Range |

No |

Yes |

Sets the luminance range where the highlight color is applied. |

ColorGrading.ColorGradingHSV |

Grading Hue Saturation Value |

No |

Yes |

Sets the HSV adjustment for the input color. |

ColorGrading.ColorGradingMidtoneColor |

Grading Color Midtone |

No |

Yes |

Sets the color grading midtone color. |

ColorGrading.ColorGradingShadowColor |

Grading Color Shadow |

No |

Yes |

Sets the color grading shadow color. |

ColorGrading.ColorGradingShadowRange |

Grading Shadow Range |

No |

Yes |

Sets the luminance range where the shadow color is applied. |

Command.CommandMessageArguments.CommandArgumentProperty |

Command |

No |

No |

The command argument executed by a UI control |

Command.CommandProperty |

Command |

No |

Yes |

The command executed by a UI control |

ComposerFactoryName |

Engine Factory Name |

No |

Yes |

The factory name for this composer. Can be used to instantiate composer or render pass from plugin. |

CompositionTargetRenderPass.AddressingMode |

Addressing Mode |

No |

Yes |

Sets how Kanzi handles the texture coordinates of the automatically generated composition target textures outside of the [0, 0] - [1, 1] rectangle: * **Repeat** sets the texture to repeat outside of these coordinates. This is the default value. * **Mirror** sets the texture to repeat, but mirrors every other repetition. * **Clamp** confines the texture to these coordinates and outside of these texture coordinates repeats the edge texels of the texture. * **Mirror once** sets the texture to repeat once in the negative direction, and after that clamps the texture. |

CompositionTargetRenderPass.CompositionTarget0 |

Composition Target 0 |

No |

Yes |

Sets the first color target to which you want to render the result of the child render passes of this render pass. |

CompositionTargetRenderPass.CompositionTarget1 |

Composition Target 1 |

No |

Yes |

Sets the second color target to which you want to render the result of the child render passes of this render pass. |

CompositionTargetRenderPass.CompositionTarget2 |

Composition Target 2 |

No |

Yes |

Sets the third color target to which you want to render the result of the child render passes of this render pass. |

CompositionTargetRenderPass.CompositionTarget3 |

Composition Target 3 |

No |

Yes |

Sets the fourth color target to which you want to render the result of the child render passes of this render pass. |

CompositionTargetRenderPass.DepthCompareFunction |

Depth Compare Function |

No |

Yes |

Sets the comparison function to be used with comparison samplers of the Composition Target render passâ depth target. |

CompositionTargetRenderPass.DepthRenderbufferFormat |

Depth Renderbuffer Format |

No |

Yes |

Sets the format of the automatically created depth renderbuffers. When you do not set this property, Kanzi sets the depth renderbuffer format automatically to the best available format, in most cases the 32-bit float format. To create depth textures, set the **Depth Texture Format** property whose value overrides the value of this property. |

CompositionTargetRenderPass.DepthTarget |

Depth Target |

No |

Yes |

Sets the depth target to which you want to render the result of the child render passes of this render pass. |

CompositionTargetRenderPass.DepthTextureFormat |

Depth Texture Format |

No |

Yes |

Sets the format of the automatically created **Result Depth Texture**. |

CompositionTargetRenderPass.FilterMode |

Filter Mode |

No |

Yes |

Sets how Kanzi handles accessing the texture samples of the automatically generated composition target: * **Nearest** takes the color from the nearest sample. * **Linear** interpolates color from neighboring samples. This is the default value. |

CompositionTargetRenderPass.Height |

Height |

No |

Yes |

Sets the absolute height for the automatically created composition target textures. If this property is not set, the size is taken from the current composition stack state using the values of the **Resolution Multiplier** and **Resolution Divisor** properties. |

CompositionTargetRenderPass.MipmapMode |

Mipmap Mode |

No |

Yes |

Sets the mipmap mode of the automatically created composition target. To enable mipmaps, set to **Linear** or **Nearest**. Enabling mipmaps introduces the runtime cost of generating mipmaps after rendering. To disable mipmaps, remove this property. |

CompositionTargetRenderPass.MultisampleLevel |

Multisample Level |

No |

Yes |

Sets the amount of multisample anti-aliasing to apply to the automatically generated composition target textures. |

CompositionTargetRenderPass.PixelFormat0 |

Pixel Format 0 |

No |

Yes |

Sets on the GPU the target pixel format of the first automatically created composition target texture. |

CompositionTargetRenderPass.PixelFormat1 |

Pixel Format 1 |

No |

Yes |

Sets on the GPU the target pixel format of the second automatically created composition target texture. |

CompositionTargetRenderPass.PixelFormat2 |

Pixel Format 2 |

No |

Yes |

Sets on the GPU the target pixel format of the third automatically created composition target texture. |

CompositionTargetRenderPass.PixelFormat3 |

Pixel Format 3 |

No |

Yes |

Sets on the GPU the target pixel format of the fourth automatically created composition target texture. |

CompositionTargetRenderPass.ResolutionDivisor |

Resolution Divisor |

No |

Yes |

Sets the resolution divisor for the automatically created composition target textures. Together with the **Resolution Multiplier** property, this property sets the size of the composition target in relation to the size of the current Viewport 2D node. For more fine-grained control, bind from the **Render Pass** > **Input Viewport Area** property to the **Width** and **Height** properties. |

CompositionTargetRenderPass.ResolutionMultiplier |

Resolution Multiplier |

No |

Yes |

Sets the resolution multiplier for the automatically created composition target textures. Together with the **Resolution Divisor** property, this property sets the size of the composition target in relation to the size of the current Viewport 2D node. For more fine-grained control, bind from the **Render Pass** > **Input Viewport Area** property to the **Width** and **Height** properties. |

CompositionTargetRenderPass.ResolveImmediately |

Resolve Immediately |

No |

Yes |

Whether to resolve multisamples and generate mipmaps for the composition target texture immediately after rendering. By default, the Composition Target render pass resolves multisamples and generates mipmaps immediately. When you continue rendering to the composition target in another Composition Target render pass that performs the resolve, disable this property. |

CompositionTargetRenderPass.ResultDepthTexture |

Result Depth Texture |

No |

Yes |

The depth texture to which the Composition Target render pass renders its content. |

CompositionTargetRenderPass.ResultTexture0 |

Result Texture 0 |

No |

Yes |

The first color texture to which the Composition Target render pass renders its content. |

CompositionTargetRenderPass.ResultTexture1 |

Result Texture 1 |

No |

Yes |

The second color texture to which the Composition Target render pass renders its content. |

CompositionTargetRenderPass.ResultTexture2 |

Result Texture 2 |

No |

Yes |

The third color texture to which the Composition Target render pass renders its content. |

CompositionTargetRenderPass.ResultTexture3 |

Result Texture 3 |

No |

Yes |

The fourth color texture to which the Composition Target render pass renders its content. |

CompositionTargetRenderPass.Width |

Width |

No |

Yes |

Sets the absolute width for the automatically created composition target textures. If this property is not set, the size is taken from the current composition stack state using the values of the **Resolution Multiplier** and **Resolution Divisor** properties. |

ComputeRenderPass.IndirectDispatchBuffer |

Indirect Dispatch Buffer |

No |

Yes |

Sets the GPU buffer that contains the indirect dispatch parameters. |

ComputeRenderPass.IndirectDispatchOffset |

Indirect Dispatch Offset |

No |

Yes |

Sets the byte offset into the indirect dispatch buffer. |

ComputeRenderPass.InvokeCountX |

Invoke Count X |

No |

Yes |

Sets the number of shader invocations in the X dimension. The value is rounded up to a multiple of the workgroup size specified in the shader. |

ComputeRenderPass.InvokeCountY |

Invoke Count Y |

No |

Yes |

Sets the number of shader invocations in the Y dimension. The value is rounded up to a multiple of the workgroup size specified in the shader. |

ComputeRenderPass.InvokeCountZ |

Invoke Count Z |

No |

Yes |

Sets the number of shader invocations in the Z dimension. The value is rounded up to a multiple of the workgroup size specified in the shader. |

ComputeRenderPass.Material |

Material |

No |

Yes |

Sets the material that contains the compute shader program. |

ConstraintInWorldCoordinates |

Constraint In World Coordinates |

No |

Yes |

Specifies if the object constraining is done in world coordinates (when false, done in local coordinates). |

ConstraintOrientation |

Constraint Orientation |

No |

Yes |

Makes an object node where the property is attached to obtain orientation from target object |

ConstraintPosition |

Constraint Position |

No |

Yes |

Makes an object node where the property is attached to obtain position from target object |

ContentLayoutConcept.DepthPadding |

Depth Padding |

No |

Yes |

Sets the padding spaces between the content and the front and back boundaries of the Content Layout 3D node. |

ContentLayoutConcept.HorizontalPadding |

Horizontal Padding |

No |

Yes |

Sets the padding spaces between the content and the left and right boundaries of the Content Layout node. |

ContentLayoutConcept.VerticalPadding |

Vertical Padding |

No |

Yes |

Sets the padding spaces between the content and the top and bottom boundaries of the Content Layout node. |

CubeMapRenderPass.CompositionTarget |

Composition Target |

No |

Yes |

Sets the target to which you want to render the result of this Cubemap render pass. |

CubeMapRenderPass.DepthCompareFunction |

Depth Compare Function |

No |

Yes |

Sets the comparison function to be used with comparison samplers of the Cubemap render passâ depth target. |

CubeMapRenderPass.DepthFormat |

Depth Format |

No |

Yes |

Sets the format of the automatically created depth render buffer used for the cubemap rendering. If this property is not set, the depth requirement and format are autodetected. |

CubeMapRenderPass.DepthRenderbufferFormat |

Depth Renderbuffer Format |

No |

Yes |

Sets the format of the automatically created depth renderbuffers. When you do not set this property, Kanzi sets the depth renderbuffer format automatically to the best available format, in most cases the 32-bit float format. To create depth textures, set the **Depth Format** property whose value overrides the value of this property. |

CubeMapRenderPass.DepthTarget |

Depth Target |

No |

Yes |

Sets the target for depth rendering for this Cubemap render pass. |

CubeMapRenderPass.FaceUpdateRate |

Face Update Rate |

No |

Yes |

Sets the number of cubemap faces to update each frame or at the rate that you set with the Render Pass > Update Rate property. The default value is 6. |

CubeMapRenderPass.FilterMode |

Filter Mode |

No |

Yes |

Sets how Kanzi handles accessing the texture samples of the automatically generated composition cubemap target: * **Nearest** takes the color from the nearest sample. * **Linear** interpolates color from neighboring samples. This is the default value. |

CubeMapRenderPass.MipmapMode |

Mipmap Mode |

No |

Yes |

Sets the mipmap mode of the automatically created composition cubemap target. To enable mipmaps set the property value to Linear or Nearest. Enabling mipmaps introduces the runtime cost of generating mipmaps after rendering. To disable mipmaps remove the property. |

CubeMapRenderPass.OverrideCamera |

Override Camera |

No |

Yes |

Sets the Camera node that you want to use to render the nodes to the composition cubemap texture. To use the default Camera node in that Scene node, do not set the value for this property. |

CubeMapRenderPass.PixelFormat |

Pixel Format |

No |

Yes |

Sets on the GPU the target pixel format of the automatically created composition cubemap target textures. |

CubeMapRenderPass.Resolution |

Resolution |

No |

Yes |

Sets the dimensions of the automatically created composition cubemap target textures. The default value is 64. |

CubeMapRenderPass.ResolveImmediately |

Resolve Immediately |

No |

Yes |

Whether to generate mipmaps for the composition target texture immediately after rendering. By default the Cubemap render pass generates mipmaps immediately. When you continue rendering to the composition target in another Cubemap render pass that performs the resolve, disable this property. |

CubeMapRenderPass.ResultDepthTexture |

Result Depth Texture |

No |

Yes |

The cubemap depth texture to which the Cubemap render pass renders its content. |

CubeMapRenderPass.ResultTexture |

Result Texture |

No |

Yes |

The result cubemap texture that was rendered to by the Cubemap render pass. |

CustomAssetThumbnail |

Custom Asset Thumbnail |

No |

Yes |

When enabled, the asset will have selected image as thumbnail instead of the generated one. |

DataContext.DataContext |

Data Context |

No |

Yes |

Source of data for this node and its descendants |

DataContext.ItemsSource |

Items Source |

No |

Yes |

Data object which provides data sources for list items. |

DataDrivenExclusiveActivityHostConcept.ActiveActivityIndex |

Active Activity Index |

No |

Yes |

The index of the active Activity in the Data-Driven Exclusive Activity Host. After instantiating all Activity from a Data Source, this property refers to the only currently active Activity in this Data-Driven Exclusive Activity Host. To deactivate all the Activities in this Data-Driven Exclusive Activity Host, set this property to -1. |

DataDrivenExclusiveActivityHostConcept.ActivitySource |

Activity Source |

No |

Yes |

The data object that provides the data for this Activity node. |

DataDrivenExclusiveActivityHostConcept.ActivityTemplate |

Activity Template |

No |

Yes |

If set, the Data-Driven Exclusive Activity Host uses this prefab for Activity nodes that it creates. |

DataObjectValue |

Value |

No |

Yes |

The last read value of the data object |

DenoiserRenderPass.DenoiserMode |

Denoiser Mode |

No |

Yes |

Temporal clamping/rejection mode: 0 - none, 1 - reject using depth min max, 2 - reject using filter |

DenoiserRenderPass.DepthTexture |

Depth Texture |

No |

Yes |   |

DenoiserRenderPass.HistoryCertaintyThreshold |

History Certainty Threshold |

No |

Yes |   |

DenoiserRenderPass.HistoryDepthTexture |

History Depth Texture |

No |

Yes |   |

DenoiserRenderPass.MinimumUnreprojectedShadow |

Minimum Unreprojected Shadow |

No |

Yes |   |

DenoiserRenderPass.OutputDenoisedShadowMask |

Output Denoised Shadow Mask |

No |

Yes |   |

DenoiserRenderPass.ReprojectDepthSensitivity |

Reproject Depth Sensitivity |

No |

Yes |   |

DenoiserRenderPass.ShadowMask |

Shadow Mask |

No |

Yes |   |

DenoiserRenderPass.VelocityTexture |

Velocity Texture |

No |

Yes |   |

Description |

Description |

No |

Yes |

Add a description of the purpose of this item. To export descriptions to a plain text file, select File > Export > Export Descriptions. When you export the kzb file, this description is not included in the exported file. |

DetailBaseColorFactor |

Detail Base Color Factor |

No |

Yes |

Sets the detail base color for the material. The detail base color is alpha blended with the standard base color. |

DetailBaseColorTexture |

Detail Base Color Texture |

No |

Yes |

Sets the detail texture that contains the base color for the material. Use the Detail Base Color Factor property to filter the value from this texture. The detail base color is alpha blended with the standard base color. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

DetailClearCoatNormalScale |

Detail Clear Coat Normal Scale |

No |

Yes |

Sets the detail clear coat normal scale for the material. Use the scale to set the intensity of the Detail Clear Coat Normal Texture. |

DetailClearCoatNormalTexture |

Detail Clear Coat Normal Texture |

No |

Yes |

Sets the detail texture that contains a clear coat normal map for the material. Use the Detail Clear Coat Normal Scale property to scale the texture value. |

DetailClearCoatRoughnessTexture |

Detail Clear Coat Roughness Texture |

No |

Yes |

Sets the detail texture that contains a clear coat roughness map for the material. Use the Clear Coat Roughness Factor and Clear Coat Roughness Texture properties to scale the roughness from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

DetailClearCoatStrengthTexture |

Detail Clear Coat Strength Texture |

No |

Yes |

Sets the detail texture that contains a clear coat strength map for the material. Kanzi reads the strength from the Red channel of the texture. Use the Clear Coat Strength Factor and Clear Coat Strength Texture properties to scale the strength from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

DetailDiffuseFactor |

Detail Diffuse Color Factor |

No |

Yes |

Sets the detail diffuse color for the material. Kanzi alpha blends the detail diffuse color with the standard diffuse color. |

DetailDiffuseTexture |

Detail Diffuse Color Texture |

No |

Yes |

Sets the detail texture that contains the diffuse color for the material. Use the Detail Diffuse Color Factor property to filter the value from this texture. Kanzi alpha blends the detail diffuse color with the standard diffuse color. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

DetailEmissiveFactor |

Detail Emissive Factor |

No |

Yes |

Sets the color of the light that is emitted from a detail texture for the material. Use the Intensity (I) property field to adjust the brightness of the light. This color affects the local material rendering, but the light is not cast to other objects. The detail emissive light is alpha blended with the standard emissive light. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

DetailEmissiveTexture |

Detail Emissive Texture |

No |

Yes |

Sets the detail texture that contains the light emitted from the material. Use the Detail Emissive Factor property to scale the value from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

DetailGlossinessTexture |

Detail Glossiness Texture |

No |

Yes |

Sets the detail texture that contains a glossiness map for the material. Kanzi reads the glossiness from the Alpha channel of this texture. Use the Glossiness Factor and Glossiness Texture properties to scale the glossiness from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

DetailMetallicTexture |

Detail Metallic Texture |

No |

Yes |

Sets the detail texture that contains a metallic map for the material. Kanzi reads the metalness from the Blue channel of this texture. Use the Metallic Factor and Metallic Texture properties to scale the metalness from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

DetailNormalScale |

Detail Normal Scale |

No |

Yes |

Sets the detail normal scale for the material. Use the scale to set the intensity of the Detail Normal Texture. |

DetailNormalTexture |

Detail Normal Texture |

No |

Yes |

Sets the detail texture that contains a normal map for the material. Use the Detail Normal Scale property to scale the texture value. |

DetailOcclusionStrength |

Detail Occlusion Strength |

No |

Yes |

Sets the detail occlusion strength for the material. Use the strength to set the intensity of the Detail Occlusion Texture. |

DetailOcclusionTexture |

Detail Occlusion Texture |

No |

Yes |

Sets the detail texture that contains an occlusion map for the material. Kanzi reads the occlusion from the Red channel of this texture. Use the Detail Occlusion Strength property to scale the occlusion from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

DetailRoughnessTexture |

Detail Roughness Texture |

No |

Yes |

Sets the detail texture that contains a roughness map for the material. Kanzi reads the roughness from the Green channel of the texture. Use the Roughness Factor and Roughness Texture properties to scale the roughness from this texture. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

DetailSpecularFactor |

Detail Specular Color Factor |

No |

Yes |

Sets the detail specular color for the material. Kanzi alpha blends the detail specular color with the standard specular color. |

DetailSpecularTexture |

Detail Specular Color Texture |

No |

Yes |

Sets the detail texture that contains the specular color for the material. Use the Detail Specular Color Factor property to filter the value from this texture. Kanzi alpha blends the detail specular color with the standard specular color. Use the Detail Texture Tiling and Detail Texture Offset properties to set UVs for this texture. |

DetailTextureOffset |

Detail Texture Offset |

No |

Yes |

Sets the detail texture offset for the material. Kanzi adds this value to the UVs to produce a second set of detail UVs to use for all detail texture properties. |

DetailTextureTiling |

Detail Texture Tiling |

No |

Yes |

Sets the detail texture tiling factor for the material. Kanzi multiplies this value by the UVs to produce a second set of detail UVs to use for all detail texture properties. |

Diffuse |

Diffuse Color |

No |

Yes |

Sets the color of the material when it is lit by a light. |

DiffuseFactor |

Diffuse Color Factor |

No |

Yes |

Sets the diffuse color for the material. |

DiffuseTexture |

Diffuse Color Texture |

No |

Yes |

Sets the texture that contains the diffuse color for the material. Use the Diffuse Color Factor property to filter the value from this texture. |

DirectionalGaussianBlur.BlurDirection |

Blur Direction |

No |

Yes |

Sets the direction for the blur. |

DirectionalGaussianBlur.BlurRadius |

Blur Radius |

No |

Yes |

Blur radius for the material. |

DirectionalLight |

Directional Light |

No |

Yes |

Directional light settings |

DirectionalLightColor |

Directional Light Color |

No |

Yes |

Sets the color of the Directional Light. Use the Intensity (I) property field to adjust the brightness of the light. |

DirectionalLightViewProjection |

Directional Light View Projection |

No |

Yes |

The premultiplied projection view matrix of a directional light. |

DirectionalShadowBias |

Directional Shadow Bias |

No |

Yes |

Sets the directional shadow bias to reduce sampling artifacts. |

DirectionalShadowMap |

Directional Shadow Map |

No |

Yes |

Depth map used to calculate directional shadows. |

DirectionalShadowSoftness |

Directional Shadow Softness |

No |

Yes |

Sets the softness of the shadows cast by the Directional Light. |

DispatchMessageAction.DefineTargetWithProperty |

Define Target with Property |

No |

Yes |

Define Target with Property |

DispatchMessageAction.RoutingTarget |

Target Item |

No |

No |

Specifies the target item to which the message is dispatched. If the target resides within the node tree, and the message type has tunneling and bubbling enabled, the message is tunneled and bubbled through the parents of the target. |

DispatchMessageAction.RoutingTargetLookup |

Property |

No |

No |

Allows to look up the target item using this property (RoutingTarget.Property). |

DockLayoutConcept.LastItemFill |

Last Item Fill |

No |

Yes |

Whether the last item of the dock layout is given the remaining free space. |

DockLayoutConcept.Side |

Side |

No |

Yes |

The docking side of an item in the dock layout. |

DrawObjectsRenderPass.CameraMatrix |

Calculated Camera Matrix |

No |

Yes |

The camera matrix that the render pass calculates during rendering from the settings of the Camera and passes to the shader. |

DrawObjectsRenderPass.CameraPosition |

Calculated Camera Position |

No |

Yes |

The camera position that the render pass calculates during rendering from the settings of the Camera and passes to the shader. |

DrawObjectsRenderPass.DirectionalLights |

Directional Lights |

No |

Yes |

Use this property to bind the directional light set for rendering. |

DrawObjectsRenderPass.FrustumCullingEnabled |

Frustum Culling |

No |

Yes |

Enable to disable rendering objects that are not inside the view frustum. Trades GPU rendering time for CPU cull test time. |

DrawObjectsRenderPass.MaterialRequirements |

Material Requirements |

No |

Yes |

Sets the material requirements required from materials selected for rendering. |

DrawObjectsRenderPass.NearFarPlane |

Calculated Projection Near And Far Planes |

No |

Yes |

The distances to the camera near and far planes that the render pass calculates during rendering from the settings of the Camera and passes to the shader. |

DrawObjectsRenderPass.ObjectSource |

Object Source |

No |

Yes |

Sets the object source which collects the nodes that you want to render with this render pass. To render all nodes in a Scene node (Root Object Source), do not set the value for this property. |

DrawObjectsRenderPass.OutputViewport |

Output Viewport |

No |

Yes |

Viewport applied by the rendering of the render pass. |

DrawObjectsRenderPass.PointLights |

Point Lights |

No |

Yes |

Use this property to bind the point light set for rendering. |

DrawObjectsRenderPass.PreviousCameraMatrix |

Previous Camera Matrix |

No |

Yes |

Camera matrix from the previous frame, used for velocity buffer calculation. |

DrawObjectsRenderPass.PreviousProjectionMatrix |

Previous Projection Matrix |

No |

Yes |

Projection matrix from the previous frame, used for velocity buffer calculation. |

DrawObjectsRenderPass.ProjectionMatrix |

Calculated Projection Matrix |

No |

Yes |

The projection matrix that the render pass calculates during rendering from the settings of the Camera and passes to the shader. |

DrawObjectsRenderPass.SortingOrder |

Sorting Order |

No |

Yes |

Sets the sorting order for render entries. |

DrawObjectsRenderPass.SpotLights |

Spot Lights |

No |

Yes |

Use this property to bind the spot light set for rendering. |

DrawObjectsRenderPass.ViewPosition |

Calculated Homogeneous View Position |

No |

Yes |

The homogeneous view position that the render pass calculates during rendering from the settings of the Camera and passes to the shader. |

DrawObjectsWithMaterialRenderPass.Material |

Material |

No |

Yes |

Sets the material that will be used to render all nodes rendered by this DrawObjectsWithMaterialRenderPass. |

EffectStack2D.StackingMode |

Effect Stacking Mode |

No |

Yes |

Sets how to apply an effect in an Effect Stack 2D: - Chained applies the effect to the result of the previous effect, to the combined result of a sequence of layered effects, or to the node content. The next effect uses as its input the result of this effect. - Layered applies the effect to the result of a previous chained effect or to the node content. A sequence of layered effects are combined on top of each other in layers.

This property has no impact on the Mask Effect 2D and Blur Effect 2D effects, which always use the Chained mode.  |

Emissive |

Emissive Color |

No |

Yes |

Sets the color of the light that is emitted from the material surface. |

EmissiveFactor |

Emissive Factor |

No |

Yes |

Sets the color of the light that is emitted from the material. Use the Intensity (I) property field to adjust the brightness of the light. This color affects the local material rendering, but the light is not cast to other objects. |

EmissiveTexture |

Emissive Texture |

No |

Yes |

Sets the texture that contains the light emitted from the material. Use the Emissive Factor property to scale the value from this texture. |

EnvironmentAmbientFactor |

Environment Ambient Factor |

No |

Yes |

Sets the strength of the cubemap texture to use for ambient environment light. Use the Environment Ambient Texture property to set the cubemap texture. The ambient environment light affects diffuse lighting in image based lighting. |

EnvironmentAmbientTexture |

Environment Ambient Texture |

No |

Yes |

Sets the cubemap to use for the ambient environment light for the material. This cubemap affects the diffuse lighting during image based lighting. Use the Environment Ambient Factor property to set the strength of the cubemap texture. |

EnvironmentReflectionFactor |

Environment Reflection Factor |

No |

Yes |

Sets the strength of the cubemap texture to use for specular environment light. Use the Environment Reflection Texture property to set the cubemap texture. The specular environment light affects reflective lighting in image based lighting. |

EnvironmentReflectionTexture |

Environment Reflection Texture |

No |

Yes |

Sets the cubemap to use for the specular environment light for the material. This cubemap affects reflective lighting during image based lighting. Use the Environment Reflection Factor property to set the strength of the cubemap texture. |

ExclusiveActivityHostConcept.FocusOnActivatingActivity |

Focus On Activating Activity |

No |

Yes |

Sets the policy that this Exclusive Activity Host uses to decide whether it tries to set the key focus to its activating Activity: * **When Host Has Focus**: If the Activity Host has the focus, it tries to set the focus to the Activity. This is the default. * **Always**: The Activity Host always tries to set the focus to the Activity. * **Never**: The Activity Host never tries to set the focus to the Activity. |

ExclusiveActivityHostConcept.ImplicitActivityChangeRequestMessageArguments.LoopActivity |

Loop Activity |

No |

No |

Sets how an Exclusive Activity Host reacts to the âNavigate To Next Activityâ and âNavigate To Previous Activityâ messages when it reaches its last and first Activities. When set to true and an Exclusive Activity Host reaches: * The last Activity, the Exclusive Activity Host reacts to the âNavigate To Next Activityâ message by activating the first Activity in that Exclusive Activity Host. * The first Activity, the Exclusive Activity Host reacts to the âNavigate To Previous Activityâ message by activating the last Activity in that Exclusive Activity Host. |

ExecuteLuaAction.ScriptUrlProperty |

Lua Script |

No |

No |

The Lua script to execute. |

Exposure |

Exposure |

No |

Yes |

Sets the exposure compensation for the material. The exposure compensation emulates camera exposure by controlling the total amount of light rendered. Use a negative value to darken the rendered image, and a positive value to lighten the image. Exposure is exponential: 1.0 is twice as bright as 0.0, and -1.0 is half as bright as 0.0. |

ExpressionBindingProcessor.Argument1 |

Argument 1 |

No |

No |

The first argument in the binding expression. |

ExpressionBindingProcessor.Argument1Field |

Argument 1 Field |

No |

No |

The property attribute for the first argument. |

ExpressionBindingProcessor.Argument2 |

Argument 2 |

No |

No |

The second argument in the binding expression. |

ExpressionBindingProcessor.Argument2Field |

Argument 2 Field |

No |

No |

The property attribute for the second argument. |

ExpressionBindingProcessor.Argument3 |

Argument 3 |

No |

No |

The third argument in the binding expression. |

ExpressionBindingProcessor.Argument3Field |

Argument 3 Field |

No |

No |

The property attribute for the third argument. |

ExpressionBindingProcessor.Operation |

Operation |

No |

No |

The operation in the expression. |

ExpressionBindingProcessor.Output |

Output |

No |

No |

The temporary register to write the result to. |

ExpressionBindingProcessor.OutputField |

Output Field |

No |

No |

The property attribute of the output register. |

FaceToCameraMode |

Face to Camera Mode |

No |

Yes |

Sets how to rotate the 3D node towards a camera: * **Disabled** does not make the node turn to the camera. * **Look at** rotates the node along all axes to turn to the camera. * **Billboarding** keeps the node perpendicular to the camera FOV. * **Cylindrical** rotates the node along the y axis to turn to the camera.

By default, the node turns to the Scene default camera. To use a different camera, set the **Face to Camera Target Camera** property.  |

FaceToCameraTargetCamera |

Face to Camera Target Camera |

No |

Yes |

Sets the camera towards which the 3D node turns when you set the **Face to Camera Mode** property. The default is the Scene default camera. |

FloatValueAccumulator.IncrementSize |

Increment Size |

No |

No |

The size of the increments of this Float Value Accumulator. |

FloatValueAccumulator.IncrementSizeSource |

Increment Size Source |

No |

No |

The property type set on this node that determines the increment size of this Float Value Accumulator. |

FloatValueAccumulator.MaximumAccumulatedValue |

Maximum Value |

No |

No |

The maximum total accumulated float value. |

FloatValueAccumulator.MinimumAccumulatedValue |

Minimum Value |

No |

No |

The minimum total accumulated float value. |

FloatValueAccumulator.TargetPropertyField |

Target Property Field |

No |

No |

The field of the target property on a node which where the values of the input property are accumulated. |

FloatValueAccumulator.TargetPropertyType |

Target Property Type |

No |

No |

The property type on this node that this Float Value Accumulator updates. |

FlowLayoutConcept.PrimaryDirection |

Primary Direction |

No |

Yes |

The direction along which the layout arranges items until the layout limit in that direction is reached. |

FlowLayoutConcept.SecondaryDirection |

Secondary Direction |

No |

Yes |

The direction along which the flow layout arranges lines of the primary direction. |

FocalLen |

Ambient Occlusion Focal Length |

No |

Yes |

HBAO input property for focal length. |

FocusManager.CyclicFocusNavigation |

Cyclic Focus Navigation |

No |

Yes |

Sets whether the focus chain navigation within the focus scope is cyclic. When you enable this property: * When the user navigates in the forward direction and the focus reaches the last focusable UI element of the focus scope, the focus navigation moves to the first focusable UI element. * When the user navigates in the backward direction and the focus reaches the first focusable UI element of the focus scope, the focus navigation moves to the last focusable UI element. |

FocusManager.FocusOnPress |

Focus On Press |

No |

Yes |

Sets where to set the focus when the user presses the node that has this property: * **None** (0) keeps the focus where it was. This is the default. * **Node** (1) sets the focus to the node. * **Node or ancestor** (2) sets the focus to the node or, if that fails, to the closest focusable ancestor node. * **Node or overlay** (3) sets the focus to the node or, if that fails, to the closest ancestor overlay scope, which then forwards the focus according to its settings.

The descendants of the node where you set this property inherit value of the property.  |

FocusManager.FocusOrder |

Focus Order |

No |

Yes |

Sets the focus chain order of the node within the focus scope. |

FocusManager.FocusScopeType |

Focus Scope Type |

No |

Yes |

Sets the type of the focus scope node: * **Group** groups focusable nodes. * **Fence** keeps the focus chain navigation inside the scope and does not allow the focus chain navigation to enter or leave that scope. * **Modal** overlay blocks the key and touch input that originates outside of its boundaries and keeps the focus navigation within the scope boundaries. * **Auto-Closing Modal** overlay loses focus when key or touch input originates from a node that is outside of its node tree, and suppresses that input. * **Modeless** overlay propagates the key and touch input that originates outside of its boundaries to the nodes outside of its boundaries. * **Auto-Closing Modeless** overlay loses focus when key or touch input originates from a node that is outside of its boundaries, and propagates that input. |

FocusManager.ScopeStateChangeMessageArguments.ReasonValue |

Reason Value |

No |

No |

The reason the modal or popup focus scope state is changed: * Force Focus specifies that the focus scope is explicitly brought to front or sent to back. |

FontStyleConcept.CharacterSpacing |

Character Spacing |

No |

Yes |

Sets the character spacing in pixels. |

FontStyleConcept.FixedCharacterWidth |

Fixed Character Width |

No |

Yes |

When set, overrides the font advance widths to make each character take a fixed amount of space specified in pixels. |

FontStyleConcept.FontHintingPreference |

Font Hinting Preference |

No |

Yes |

Sets the hinting preference of the font. * **No hinting**: Render text without hinting the outlines of glyphs. * **Native hinting**: Prefer native hinter of the font over the auto-hinter of the rasterizer. * **Auto hinting**: Prefer auto-hinter of the rasterizer over the native hinter of the font. |

FontStyleConcept.FractionalCharacterWidth |

Fractional Character Width |

No |

Yes |

Sets whether Kanzi uses fractional or rounded character widths to lay out text. In most cases fractional widths provide the best result. However, with small font sizes, fractional widths can cause the characters to run together or have too much space, making it difficult to read. * When enabled, Kanzi uses fractional character widths, which means that the spacing between characters varies and can be a fraction of a pixel. * When disabled, Kanzi uses character widths rounded to the nearest pixel. Disable fractional widths when you want to fix character spacing in whole-pixel increments and prevent characters in small font sizes from running together. |

FontStyleConcept.LineSpacing |

Line Spacing |

No |

Yes |

Sets the line spacing in multiples of the normal line height of the selected font. |

FontStyleConcept.Size |

Font Size |

No |

Yes |

Sets the size of the font in pixels. |

FontStyleConcept.SnapCharacterToPixelProperty |

Snap Character To Pixel |

No |

Yes |

Sets whether Kanzi positions characters in 2D rendering to the nearest pixel: * When enabled, text sharpness improves, but some characters can shift a fraction of a pixel. * When disabled, certain combinations of screen resolution, use of anti-aliasing, and font size can cause the text to appear blurry. In that case, you can improve the appearance of the text with the **Fractional Character Width** and **Character Spacing** properties. |

FontStyleConcept.Style |

Font Style |

No |

Yes |

Sets the style of the font. |

FontStyleConcept.Weight |

Font Weight |

No |

Yes |

Sets the weight of the font. |

FrustumCullMargin |

Frustum Cull Margin |

No |

Yes |

The margin of the frustum cull radius of the node. For example, set the margin when a vertex shader modifies the geometry of the node. To use this property, enable the Frustum Culling property in the Draw Objects Render Pass you use to render the node. |

GatherLightsRenderPass.OutputDirectionalLights |

Output Directional Lights |

No |

Yes |

Kanzi uses this property to allow binding to directional light set. |

GatherLightsRenderPass.OutputPointLights |

Output Point Lights |

No |

Yes |

Kanzi uses this property to allow binding to point light set. |

GatherLightsRenderPass.OutputSpotLights |

Output Spot Lights |

No |

Yes |

Kanzi uses this property to allow binding to spot light set. |

GlobalAmbient |

Global Ambient Color |

No |

Yes |

Sets the color that is multiplied automatically with the Ambient property of the materials in the scene. Use the Intensity (I) property field to adjust the exposure of the color. |

GlossinessFactor |

Glossiness Factor |

No |

Yes |

Sets the glossiness of the material: 0 represents a rough, diffuse surface, and 1 represents a smooth, glossy surface. |

GlossinessTexture |

Glossiness Texture |

No |

Yes |

Sets the texture that contains a glossiness map for the material. Kanzi reads the glossiness from the Alpha channel of this texture. Use the Glossiness Factor property to scale the glossiness from this texture. |

GridLayoutConcept.Column |

Column |

No |

Yes |

The column into which grid layout places the item. |

GridLayoutConcept.ColumnDefinitions |

Columns |

No |

Yes |

Defines the number of columns in a grid layout and how the grid layout distributes the content in columns. |

GridLayoutConcept.ColumnSpan |

Column Span |

No |

Yes |

Defines the number of columns an item in a grid layout occupies. |

GridLayoutConcept.Direction |

Layout Direction |

No |

Yes |

The direction in which the items are arranged when you add them to a grid layout. |

GridLayoutConcept.Row |

Row |

No |

Yes |

The row into which grid layout places the item. |

GridLayoutConcept.RowDefinitions |

Rows |

No |

Yes |

Defines the number of rows in a grid layout and how the grid layout distributes the content in rows. |

GridLayoutConcept.RowSpan |

Row Span |

No |

Yes |

Defines the number of rows an item in a grid layout occupies. |

GridListBoxConcept.CalculatedOffset |

Calculated Offset |

No |

Yes |

Reports the current relative offset of an item in the Grid List Box in proportional range [0, 1]. |

GridListBoxConcept.CellHeight |

Cell Height |

No |

Yes |

Sets the height of each cell in the Grid List Box. |

GridListBoxConcept.CellWidth |

Cell Width |

No |

Yes |

Sets the width of each cell in the Grid List Box. |

GridListBoxConcept.Direction |

Layout Direction |

No |

Yes |

Sets the direction in which the Grid List Box arranges its items. When you change the layout direction you also change the scroll axis of the Grid List Box. |

GridListBoxConcept.ItemAreaBegin |

Item Area Begin |

No |

Yes |

Sets the proportional offset where the area meant for the fully visible items in the Grid List Box starts. Kanzi uses the values of the Item Area Begin and Item Area End properties to calculate the value of the Node.VisibleAmountInParent property for each list item.You can use the VisibleAmountInParent property in shaders to fade out those list items that are not fully visible. |

GridListBoxConcept.ItemAreaEnd |

Item Area End |

No |

Yes |

Sets the proportional offset where the area meant for the fully visible items in the Grid List Box ends. Kanzi uses the values of the Item Area Begin and Item Area End properties to calculate the value of the Node.VisibleAmountInParent property for each list item.You can use the VisibleAmountInParent property in shaders to fade out those list items that are not fully visible. |

GridListBoxConcept.ReversedScrolling |

Reversed Scrolling |

No |

Yes |

Whether the scroll position in the Grid List Box node increases in relation to the direction of the pan gesture. This reverses the direction of scrolling. By default, the scroll position decreases in relation to the pan direction and items moves to same direction with the pan gesture. |

GridListBoxConcept.Scrolling |

Scrolling |

No |

Yes |

Reports whether the Grid List Box is currently scrolling. |

GridListBoxConcept.ScrollPosition |

Scroll Position |

No |

Yes |

Sets the scroll position of the Grid List Box along the x and y axes as a relative position within the list box area. Use this property to move the list to a scroll position immediately, without scrolling. To update this property with a binding, use a to-source or two-way binding. |

GridListBoxConcept.ScrollSpeed |

Scroll Speed |

No |

Yes |

Reports the current scroll speed of the Grid List Box. |

GridListBoxConcept.ScrollTargetPosition |

Scroll Target Position |

No |

Yes |

Reports the current target scroll value of the Grid List Box. |

GridListBoxDraggingAccelerationCoefficient |

Dragging Acceleration |

No |

Yes |

Sets the acceleration of the Grid List Box when the user scrolls the Grid List Box by dragging the pointer. The higher the value, the quicker the Grid List Box reaches its final position. The default value is 80. |

GridListBoxDraggingDragCoefficient |

Dragging Drag |

No |

Yes |

Sets the amount that drag affects the movement of the Grid List Box when the user scrolls the Grid List Box by dragging the pointer. The lower the value, the higher the drag and the quicker the scrolling stops. The default value is 150. |

GridListBoxDraggingImpulseFactor |

Dragging Impulse |

No |

Yes |

Sets the amount of impulse to generate from the pointer movement when the user scrolls the Grid List Box by dragging the pointer. |

GridListBoxMaximumNumberOfTouches |

Maximum Number of Touches |

No |

Yes |

Sets the maximum number of touch points allowed on the Grid List Box area for scrolling. |

GridListBoxMinimumNumberOfTouches |

Minimum Number of Touches |

No |

Yes |

Sets the minimum number of touch points required on the Grid List Box area for scrolling. |

GridListBoxRecognitionThreshold |

Recognition Threshold |

No |

Yes |

Sets the distance in pixels that the pointer has to move for the scrolling to start in the Grid List Box. |

GridListBoxSensitivity |

Scroll Sensitivity |

No |

Yes |

Sets the amount that the scroll position changes relative to the movement of the pointer. The default value 1 makes the Grid List Box scroll the same amount as the user drags the pointer. For example, to set the Grid List Box to scroll twice the amount that the user drags the pointer, set the value of the property to 2. |

GridListBoxSlidingAccelerationCoefficient |

Sliding Acceleration |

No |

Yes |

Sets the acceleration of the Grid List Box after the user releases the pointer with which they scroll the Grid List Box. The higher the value, the quicker the Grid List Box reaches the scroll target. The default value is 40. |

GridListBoxSlidingDragCoefficient |

Sliding Drag |

No |

Yes |

Sets how much drag affects the movement of the Grid List Box after the user releases the pointer with which they scroll the Grid List Box. The lower the value, the higher the drag and the quicker the scrolling of the Grid List Box stops. The default value is 80. |

GridListBoxSwipeDistance |

Swipe Distance |

No |

Yes |

Sets the distance that a swipe sends the scroll value in the Grid List Box, relative to the speed of the pointer. |

Image2D.Image |

Image |

No |

Yes |

The image to display. |

ImageClampPixelsValue |

Clamp Pixels |

No |

Yes |

Clamp the color channel maximum to the value. For SDR images the effective range is 0 to 1, and for HDR images any non-negative value. If one color channel needs to be clamped, then all other color channels are scaled down by the same ratio. |

ImageFileNativePixelFormat |

Native Pixel Format |

No |

Yes |

Sets the native image format to use when exporting this image to the kzb file. Make sure that the graphics backend of your target device supports the format. |

Input.MessageArgument.CapsLock |

Caps Lock |

No |

No |

Sets whether Caps Lock is on during the key event. |

Input.MessageArgument.Key |

Key |

No |

No |

Sets the target logical key to handle. |

Input.MessageArgument.KeyModifiers |

Key Modifiers |

No |

No |

Sets the target key modifiers to handle. |

Input.MessageArgument.NavigationDirection |

Navigation Direction |

No |

No |

The navigation direction. |

InputManipulator.InputMessageArguments.HitTestPoint |

Hit Test Point |

No |

No |   |

InputManipulator.InputMessageArguments.HitTestRayDirection |

Hit Test Ray Direction |

No |

No |   |

InputManipulator.InputMessageArguments.HitTestRayDistance |

Hit Test Ray Distance |

No |

No |   |

InputManipulator.InputMessageArguments.HitTestRayOrigin |

Hit Test Ray Origin |

No |

No |   |

InputManipulator.InputMessageArguments.ManipulatorPoint |

Manipulator Point |

No |

No |   |

InputManipulator.InputMessageArguments.ManipulatorRayDirection |

Manipulator Ray Direction |

No |

No |   |

InputManipulator.InputMessageArguments.ManipulatorRayOrigin |

Manipulator Ray Origin |

No |

No |   |

Instantiator3D.Node |

Instantiated Node |

No |

No |

Sets the node that this Instantiator node replicates. |

IntValueAccumulator.IncrementSize |

Increment Size |

No |

No |

The size of the increments of this Int Value Accumulator. |

IntValueAccumulator.IncrementSizeSource |

Increment Size Source |

No |

No |

The property type set on this node that determines the increment size of this Int Value Accumulator. |

IntValueAccumulator.MaximumAccumulatedValue |

Maximum Value |

No |

No |

The maximum total accumulated integer value. |

IntValueAccumulator.MinimumAccumulatedValue |

Minimum Value |

No |

No |

The minimum total accumulated integer value. |

IntValueAccumulator.TargetPropertyType |

Target Property Type |

No |

No |

The property type on this node that this Int Value Accumulator updates. |

IsAssetInAssetPackage |

Export in Asset Package |

No |

Yes |

When enabled, this item is exported into asset package if this project is saved as one. |

IsDisabled |

Disable KZB Export |

No |

Yes |

Disables the exporting of the item into KZB. Can be used for, e.g. letting items out from certain profiles. The disabled items are always included in preview. |

IsUsedByCode |

Is Used by Code |

No |

Yes |

Whether or not the application code uses this asset. Used for determining unused assets. |

KeyManipulatorComponent.CapsLock |

Caps Lock |

No |

Yes |

Sets the Caps Lock value of the key manipulator. If the value is not set, Caps Lock state is ignored. |

KeyManipulatorComponent.KeyModifier |

Key Modifiers |

No |

Yes |

Sets the key modifiers of the key manipulator. The default value is Undefined. |

KeyManipulatorComponent.LogicalKey |

Logical Key |

No |

No |

Sets the logical key value of the key manipulator. |

LightPropertyType |

Light Type Name |

No |

Yes |

The property type name of the light. |

LinMAD |

Ambient Occlusion LinMAD |

No |

Yes |

HBAO input property for LinMAD uniform. |

ListBoxConcept.ItemContainerGeneratorTypeName |

Item Container Generator |

No |

Yes |

Sets the name of the item container generator type to use to provide item containers dynamically for the List Box. |

ListBoxConcept.ItemContainerTemplate |

Item Container Template |

No |

Yes |

Sets the List Box Item Container prefab that sets the appearance and behavior of the List Box items. |

ListBoxConcept.ItemCount |

Item Count |

No |

Yes |

Reports the number of items in the List Box, including virtual items. |

ListBoxConcept.ItemGeneratorTypeName |

Item Generator |

No |

Yes |

Sets the name of the item generator type to use to provide items dynamically to the List Box. |

ListBoxConcept.ItemMessageArguments.ItemIndex |

Item Index |

No |

No |

Reports the index of the List Box item. |

ListBoxConcept.ItemSelectedMessageArguments.PreviousSelectedItemIndex |

Previous Selection |

No |

No |

Reports the index of the previously selected List Box item. The value -1 indicates that no item was selected. |

ListBoxConcept.ItemSelectedMessageArguments.SelectedItemIndex |

Selection |

No |

No |

Reports the index of the selected List Box item. The value -1 indicates that no item is selected. |

ListBoxConcept.ItemTemplate |

Item Template |

No |

Yes |

Sets the prefab to use for the List Box items. |

ListBoxConcept.KeepAliveItemCount |

Keep Alive Item Count |

No |

Yes |

Sets the size of the buffer for invisible List Box items. Kanzi returns to the Item Generator those invisible items that do not fit in the buffer. |

ListBoxConcept.MoveFocusMessageArguments.FocusMoveTargetProperty |

Focus Move Target |

No |

No |

Sets the target where the focus moves. |

ListBoxConcept.SelectedItemIndex |

Selected Item Index |

No |

Yes |

Sets the index of the item that is currently selected in the List Box node. A List Box node updates this property when the user scrolls that List Box node. To select an item in the List Box node, set this property to the index of the item that you want to select. The indexing starts from 0. To update this property with a binding, use a to-source or two-way binding. |

ListBoxConcept.SelectionBehavior |

Selection Behavior |

No |

Yes |

Sets how the List Box behaves when the user selects an item. âBring to Centerâ sets the List Box to bring an item to the center of the List Box area when the user selects that item. |

ListBoxConcept.TrySetFocusToItemMessageArguments.FallbackProperty |

Fallback |

No |

No |

Whether to set the focus to the List Box node if the list item cannot receive the focus. |

ListBoxConcept.TrySetFocusToItemMessageArguments.ItemIndexProperty |

Item Index |

No |

No |

Sets the index of the item to which to set the focus. |

ListBoxItemContainer.ItemIndex |

Item Index |

No |

Yes |

Reports the index of the item in the List Box Item Container. |

ListBoxItemContainer.Selected |

Selected |

No |

Yes |

Indicates whether the List Box item held by this List Box Item Container is selected. The List Box sets the value of this property. |

ListBoxScrollingConcept.ScrollMessageArguments.ScrollPosition |

Scroll Position |

No |

No |

Reports the scroll position in the Scroll View within the List Box. |

ListBoxScrollingConcept.ScrollMessageArguments.ScrollSpeed |

Scroll Speed |

No |

No |

Reports the scroll speed in the Scroll View within the List Box. |

ListBoxScrollingConcept.UserScrollStartedMessageArguments.ItemIndex |

Item Index |

No |

No |

Reports the index of the List Box item where the user started scrolling. |

LongPressManipulatorComponent.LongPressDuration |

Long Press Duration |

No |

No |

Sets the duration of the press required for the installed long-press manipulator to recognize the long-press gesture and to set off the Long Press trigger. |

LookAt |

Look At |

No |

Yes |

Makes a node to always face the node set in this property. |

LuaDataSource.DataScriptUrlProperty |

Lua Data Script |

No |

No |

The Lua script to provide data to DataSource. |

MaskEffect2D.Channel |

Mask Channel |

No |

Yes |

Sets the texture channel to use as the input for the mask: * **Alpha** uses the alpha channel from the texture. This is the default. * **Red** uses the red color channel from the texture. * **Green** uses the green color channel from the texture. * **Blue** uses the blue color channel from the texture. * **Luminance** uses the luminance calculated from the red, green, and blue channels. |

MaskEffect2D.Height |

Mask Height |

No |

Yes |

Sets the height of the mask to use in a layout. This value overrides the height of the texture that you use as the mask. |

MaskEffect2D.HorizontalAlignment |

Mask Horizontal Alignment |

No |

Yes |

Sets the horizontal alignment of the mask effect: * **Left** aligns the left edge of the mask with the left edge of the node. This is the default. * **Right** aligns the right edge of the mask with the right edge of the node. * **Center** aligns the mask horizontally to the center of the node. * **Stretch** stretches the mask horizontally to fit the node from the left edge to the right edge. |

MaskEffect2D.Invert |

Invert Mask |

No |

Yes |

Whether to invert the mask so that transparent areas become opaque and opaque areas become transparent. |

MaskEffect2D.Mask |

Mask Texture |

No |

Yes |

Sets the mask texture. The default is no texture. |

MaskEffect2D.Offset |

Mask Offset |

No |

Yes |

Sets the mask offset along the X and Y axes in pixels. Kanzi applies the mask offset after stretch, alignment, and scale. |

MaskEffect2D.Scale |

Mask Scale |

No |

Yes |

Sets the factor by which to scale the mask. Kanzi applies the scale after stretch and alignment. |

MaskEffect2D.ScreenSpace |

Use Screen Space |

No |

Yes |

Whether to layout the mask relative to the screen instead of the node. |

MaskEffect2D.Strength |

Mask Strength |

No |

Yes |

Sets the strength of the mask effect in the range from 0 to 1: * 0 disables the mask effect. * 1 applies the mask at full strength. This is the default. * Any value between 0 and 1 partially applies the mask as if the non-masked result was blended with the fully masked version. |

MaskEffect2D.Stretch |

Mask Stretch |

No |

Yes |

Sets the stretch mode of the mask effect: * **None** disables stretching. This is the default. * **Fill** stretches the mask to fill the node. * **Uniform** stretches the mask using uniform scaling to fill the node in either vertical or horizontal direction, whichever requires smaller scale. * **Uniform To Fill** stretches the mask using uniform scaling to fill the node in either vertical or horizontal direction, whichever requires larger scale. * **Repeat** does not stretch the mask, and allows the mask to repeat outside of its area based on the mask texture wrap mode. |

MaskEffect2D.VerticalAlignment |

Mask Vertical Alignment |

No |

Yes |

Sets the vertical alignment of the mask effect: * **Bottom** aligns the bottom edge of the mask with the bottom edge of the node. * **Top** aligns the top edge of the mask with the top edge of the node. This is the default. * **Center** aligns the mask vertically to the center of the node. * **Stretch** stretches the mask vertically to fit the node from the top edge to the bottom edge. |

MaskEffect2D.Width |

Mask Width |

No |

Yes |

Sets the width of the mask to use in a layout. This value overrides the width of the texture that you use as the mask. |

MaskTexture |

Mask Texture |

No |

Yes |

Sets the texture that masks another texture or color. |

MaskTextureOffset |

Mask Texture Offset |

No |

Yes |

Sets an offset for mask in materials. |

MaskTextureTiling |

Mask Texture Tiling |

No |

Yes |

Determines the number of times a mask is presented in a material |

Material.MaterialVariationMapping |

Material Variation Mapping |

No |

No |

Sets the variation mapping for selecting material variations for rendering. |

MaterialBrush.Material |

Material |

No |

Yes |

Material used when drawing with the brush |

MaterialSetupRenderPass.Material |

Material |

No |

Yes |

Sets the material that will have all other Material Setup render pass properties set to. |

MaterialTypeShaderVersion |

Shader Version |

No |

Yes |

Sets the OpenGL ES version in the shaders of this material type. The value of this property overrides the #version directive in the shader source files. When you do not set this property, Kanzi uses the #version directive in the shader source files. |

MeshMorphTargetWeight |

Weight |

No |

No |

A weight value for a morph target |

Message.IsRepeat |

Is Repeat |

No |

No |

Whether the key press is a repeat caused by the user holding down a keyboard key. |

Message.ToggleState |

Toggle State |

No |

No |

Reports the toggle state of a Toggle Button. |

MessageArgument.FloatValueAccumulator.SetAccumulatedValueBoundaries.MaximumAccumulatedValue |

Maximum Value |

No |

No |

Sets the maximum total accumulated float value. |

MessageArgument.FloatValueAccumulator.SetAccumulatedValueBoundaries.MinimumAccumulatedValue |

Minimum Value |

No |

No |

Sets the minimum total accumulated float value. |

MessageArgument.FocusReason |

Focus Reason |

No |

No |

Sets the focus reason: * Force Focus. Focus was forced on the node. * Focus Chain Navigation. Focus was moved as a result of navigation in the focus chain. * Node Hidden. The Visible property of the focused node was disabled. * Force Focus to Root. Focus was forced on the root node of the focus scope. |

MessageArgument.IntValueAccumulator.SetAccumulatedValueBoundaries.MaximumAccumulatedValue |

Maximum Accumulated Value |

No |

No |

Sets the maximum total accumulated integer value. |

MessageArgument.IntValueAccumulator.SetAccumulatedValueBoundaries.MinimumAccumulatedValue |

Minimum Accumulated Value |

No |

No |

Sets the minimum total accumulated integer value. |

MessageArgument.Page.Navigate.Immediate |

Immediate (deprecated) |

No |

No |

Whether to navigate to the page instantly, without playing a transition animation. |

MessageArgument.PropertyTargetEasingInterpolator.SetEnabled.Enabled |

Enabled |

No |

No |

Sets whether the Property Target Easing Interpolator attached to the Target Item interpolates the value of the Interpolated Property Type. |

MessageArgument.Screen.ActivateThemeMessageArguments.Theme |

Theme |

No |

No |

Theme to activate |

MessageArgument.ScrollView.ScrollPosition |

Position |

No |

No |

Sets the x and y axis coordinates for the new scroll position of a Scroll View node. |

MessageArgument.ScrollView.ScrollPositionX |

Position X |

No |

No |

Sets the x axis coordinate for the new scroll position of a Scroll View node. |

MessageArgument.ScrollView.ScrollPositionY |

Position Y |

No |

No |

Sets the y axis coordinate for the new scroll position of a Scroll View node. |

MessageArgument.ScrollView.ScrollSpeed |

Speed |

No |

No |

Sets the scrolling speed of a Scroll View node. |

MessageArgument.ScrollView.ScrollTarget |

Scroll Target |

No |

No |

Sets the target position for a Scroll View node. |

MessageArgument.ScrollView.SnapDirection |

Snap Direction |

No |

No |

Sets the direction of a snap request. |

MessageArgument.ScrollView.SnapPosition |

Snap Position |

No |

No |

Sets the target of a snap request. |

MessageArgument.ScrollView.Zoom |

Zoom |

No |

No |

Sets the zoom level for a Scroll View node. |

MessageArgument.StateManager.EnteredState |

State |

No |

No |

State Manager State Entered |

MessageArgument.StateManager.Immediate |

Immediate |

No |

No |

Whether to change the state instantly, without playing a transition animation. |

MessageArgument.StateManager.LeftState |

State |

No |

No |

State Manager State Left |

MessageArgument.StateManager.LoopStates |

Loop State |

No |

No |

Whether to go back to the first state after reaching the last state. |

MessageArgument.StateManager.ShowStateManagerOnly |

Show only items that have state manager |

No |

Yes |

Show only items that have state manager |

MessageArgument.StateManager.SourceState |

Source State |

No |

No |

Source State for the transition |

MessageArgument.StateManager.State |

State |

No |

No |

State Manager State |

MessageArgument.StateManager.StateDefinedInCode |

State defined in code |

No |

Yes |

State defined in code |

MessageArgument.StateManager.StateGroup |

State Group |

No |

No |

The state group that contains the state to which you want to transition. |

MessageArgument.StateManager.StateSelectorPlaceholder |

State |

No |

Yes |

Target state for dispatched message action |

MessageArgument.StateManager.TargetState |

Target State |

No |

No |

Target State for the transition |

MessageTrigger.MessageSource |

Message Source |

No |

No |

A filter that makes possible to intercept events only for a certain source node. Empty string intercepts messages from all sources. |

MessageTrigger.RoutingMode |

Routing Mode |

No |

No |

The routing phase where the message is going to be intercepted. |

MessageTrigger.SetHandled |

Set Message Handled |

No |

No |

When enabled the trigger intercepts the message, marks it as handled, and prevents further message delivery. |

MetallicFactor |

Metallic Factor |

No |

Yes |

Sets the metalness of the material: 0 represents a non-metallic or dielectric object, and 1 represents a metallic object. |

MetallicTexture |

Metallic Texture |

No |

Yes |

Sets the texture that contains a metallic map for the material. Kanzi reads the metalness from the Blue channel of this texture. Use the Metallic Factor property to scale the value from this texture. |

MipmapGenerationConcept.ColorMipmapMaterial0 |

Color Mipmap Material 0 |

No |

Yes |

Sets the material to use to generate the mipmaps for the first color result texture (Result Texture 0) of a Composition Target Render Pass. To use the default mipmap generation, remove the property or set it to the default value â< No Material >â. |

MipmapGenerationConcept.ColorMipmapMaterial1 |

Color Mipmap Material 1 |

No |

Yes |

Sets the material to use to generate the mipmaps for the second color result texture (Result Texture 1) of a Composition Target Render Pass. To use the default mipmap generation, remove the property or set it to the default value â< No Material >â. |

MipmapGenerationConcept.ColorMipmapMaterial2 |

Color Mipmap Material 2 |

No |

Yes |

Sets the material to use to generate the mipmaps for the third color result texture (Result Texture 2) of a Composition Target Render Pass. To use the default mipmap generation, remove the property or set it to the default value â< No Material >â. |

MipmapGenerationConcept.ColorMipmapMaterial3 |

Color Mipmap Material 3 |

No |

Yes |

Sets the material to use to generate the mipmaps for the fourth color result texture (Result Texture 3) of a Composition Target Render Pass. To use the default mipmap generation, remove the property or set it to the default value â< No Material >â. |

MipmapGenerationConcept.CubemapMipmapMaterial |

Cubemap Mipmap Material |

No |

Yes |

Sets the material to use to generate the mipmaps for the color Result Texture of a Cubemap Render Pass. To use the default mipmap generation, remove the property or set it to the default value â< No Material >â. |

MipmapGenerationConcept.CurrentMipmapLevel |

Current Mipmap Level |

No |

Yes |

Reports the mipmap level that Kanzi is generating. Use this property in a material that you use to customize how Kanzi generates mipmaps for the composition targets of a Composition Target Render Pass or Cubemap Render Pass.The value of this property is valid only while Kanzi generates the mipmaps. |

MipmapGenerationConcept.DepthMipmapMaterial |

Depth Mipmap Material |

No |

Yes |

Sets the material to use to generate the mipmaps for the Result Depth Texture of a Composition Target Render Pass. To use the default mipmap generation, remove the property or set it to the default value â< No Material >â. |

MipmapGenerationConcept.MipmapSourceTexture |

Mipmap Source Texture |

No |

Yes |

Reports the texture that contains the render target texture for which Kanzi creates mipmaps. Use this property as the source texture in a material that you use to customize how Kanzi generates mipmaps for the composition targets of a Composition Target Render Pass or Cubemap Render Pass. The default value is < No Texture > |

Model3D.DrawnAsBoundingBox |

Drawn as Bounding Box |

No |

Yes |

When enabled the object is drawn its solid bounding box. |

Model3D.Material |

Material |

No |

Yes |

Use this material to override the materials defined in the clusters of the mesh. |

Model3D.Mesh |

Mesh |

No |

No |

The mesh resource used by the model. |

Model3D.MorphDataTexture |

Morph Data Texture |

No |

Yes |

Data texture to use for storing morph data when the are are too many targets to use regular attribute channels. |

Model3D.Morphing |

Morphing |

No |

Yes |

Add morph weights to Model3D to enable Morphing. |

MoveFocusAction.Direction |

Direction |

No |

No |

Direction to which the focus is transferred in the focus navigation chain. |

MultiClickManipulatorComponent.ClickCount |

Click Count |

No |

No |

Sets the number of clicks or taps required for the installed multi-click manipulator to recognize the multi-click gesture and to set off the Multi-Click trigger. The default value is 2. |

MultiClickManipulatorComponent.SendIntermediateClickMessages |

Send Intermediate Click Messages |

No |

Yes |

Sets whether to send Intermediate Click messages until the desired click count is reached. |

MultiClickManipulatorComponent.Timeout |

Multi-Click Timeout |

No |

No |

Sets the time in milliseconds within which two consecutive clicks or taps must occur for the multi-click manipulator to continue recognizing them as the multi-click gesture. The default value is 250 ms. |

NavigationManipulatorComponent.DownNavigationKey |

Down Navigation Key |

No |

Yes |

Sets the logical key value of the down navigation. |

NavigationManipulatorComponent.DownNavigationKeyModifier |

Down Navigation Key Modifier |

No |

Yes |

Sets the key modifiers of the down navigation. The default value is Undefined. |

NavigationManipulatorComponent.EndNavigationKey |

End Navigation Key |

No |

Yes |

Sets the logical key value of the end navigation. |

NavigationManipulatorComponent.EndNavigationKeyModifier |

End Navigation Key Modifier |

No |

Yes |

Sets the key modifiers of the end navigation. The default value is Undefined. |

NavigationManipulatorComponent.HomeNavigationKey |

Home Navigation Key |

No |

Yes |

Sets the logical key value of the home navigation. |

NavigationManipulatorComponent.HomeNavigationKeyModifier |

Home Navigation Key Modifier |

No |

Yes |

Sets the key modifiers of the home navigation. The default value is Undefined. |

NavigationManipulatorComponent.LeftNavigationKey |

Left Navigation Key |

No |

Yes |

Sets the logical key value of the left direction navigation. |

NavigationManipulatorComponent.LeftNavigationKeyModifier |

Left Navigation Key Modifier |

No |

Yes |

Sets the key modifiers of the left direction navigation. The default value is Undefined. |

NavigationManipulatorComponent.PageDownNavigationKey |

Page Down Navigation Key |

No |

Yes |

Sets the logical key value of the page-down navigation. |

NavigationManipulatorComponent.PageDownNavigationKeyModifier |

Page Down Navigation Key Modifier |

No |

Yes |

Sets the key modifiers of the page-down navigation. The default value is Undefined. |

NavigationManipulatorComponent.PageUpNavigationKey |

Page Up Navigation Key |

No |

Yes |

Sets the logical key value of the page-up navigation. |

NavigationManipulatorComponent.PageUpNavigationKeyModifier |

Page Up Navigation Key Modifier |

No |

Yes |

Sets the key modifiers of the page-up navigation. The default value is Undefined. |

NavigationManipulatorComponent.RightNavigationKey |

Right Navigation Key |

No |

Yes |

Sets the logical key value of the right direction navigation. |

NavigationManipulatorComponent.RightNavigationKeyModifier |

Right Navigation Key Modifier |

No |

Yes |

Sets the key modifiers of the right direction navigation. The default value is Undefined. |

NavigationManipulatorComponent.UpNavigationKey |

Up Navigation Key |

No |

Yes |

Sets the logical key value of the up navigation. |

NavigationManipulatorComponent.UpNavigationKeyModifier |

Up Navigation Key Modifier |

No |

Yes |

Sets the key modifiers of the up navigation. The default value is Undefined. |

NinePatchImage2D.ImageBottom |

Bottom Image |

No |

Yes |

The image to use in middle of the bottom row. |

NinePatchImage2D.ImageBottomLeft |

Bottom-Left Image |

No |

Yes |

Image to use in the bottom-left corner. |

NinePatchImage2D.ImageBottomRight |

Bottom-Right Image |

No |

Yes |

The image to use in the bottom-right corner. |

NinePatchImage2D.ImageCenter |

Center Image |

No |

Yes |

The image to use in the center. |

NinePatchImage2D.ImageLeft |

Left Image |

No |

Yes |

The image to use in the center-left. |

NinePatchImage2D.ImageRight |

Right Image |

No |

Yes |

The image to use in the center-right. |

NinePatchImage2D.ImageTop |

Top Image |

No |

Yes |

The image to use in the middle of the top row. |

NinePatchImage2D.ImageTopLeft |

Top-Left Image |

No |

Yes |

The image to use in the top-left corner. |

NinePatchImage2D.ImageTopRight |

Top-Right Image |

No |

Yes |

The image to use in the top-right corner. |

NinePatchImage2D.StretchTypeBottom |

Stretch Type Bottom |

No |

Yes |

Sets how to display the bottom image: * **Stretch**: Scales the image to fill the space between the bottom-left and bottom-right images. * **Wrap**: When the width of the space between the bottom-left and bottom-right images exceeds the width of the image, either extends the last column of pixels in the image or tiles the image. Depends on the value of the **Wrap Mode** property of the texture. |

NinePatchImage2D.StretchTypeCenter |

Stretch Type Center |

No |

Yes |

Sets how to display the center image: * **Stretch**: Scales the image to fill the width and height of the center of the nine patch image. * **Wrap**: When the height and width of the center exceed the size of the image, either extends the last row or column of pixels in the image or tiles the image. Depends on the value of the **Wrap Mode** property of the texture. |

NinePatchImage2D.StretchTypeLeft |

Stretch Type Left |

No |

Yes |

Sets how to display the left image: * **Stretch**: Scales the image to fill the space between the top-left and bottom-left images. * **Wrap**: When the height of the space between the top-left and bottom-left images exceeds the height of the image, either extends the last row of pixels in the image or tiles the image. Depends on the value of the **Wrap Mode** property of the texture. |

NinePatchImage2D.StretchTypeRight |

Stretch Type Right |

No |

Yes |

Sets how to display the right image: * **Stretch**: Scales the image to fill the space between the top-right and bottom-right images. * **Wrap**: When the height of the space between the top-right and bottom-right images exceeds the height of the image, either extends the last row of pixels in the image or tiles the image. Depends on the value of the **Wrap Mode** property of the texture. |

NinePatchImage2D.StretchTypeTop |

Stretch Type Top |

No |

Yes |

Sets how to display the top image: * **Stretch**: Scales the image to fill the space between the top-left and top-right images. * **Wrap**: When the width of the space between the top-left and top-right images exceeds the width of the image, either extends the last column of pixels in the image or tiles the image. Depends on the value of the **Wrap Mode** property of the texture. |

Node.ActualDepth |

Actual Layout Depth |

No |

Yes |

The calculated size of the node in depth direction when used in a layout. |

Node.ActualHeight |

Actual Layout Height |

No |

Yes |

The calculated height of the node when used in a layout. |

Node.ActualWidth |

Actual Layout Width |

No |

Yes |

The calculated width of the node when used in a layout. |

Node.ClipChildren |

Clip Children |

No |

Yes |

Sets whether to clip the child nodes of this node. Kanzi clips the child nodes whose bounding box is completely outside of the bounding box of their parent node. Use this property with layout nodes. The child nodes can use only translation transformation. |

Node.ContentStretch |

Content Stretch |

No |

Yes |

Sets how the content that belongs to this node is stretched (as opposed to manipulating the actual node size). |

Node.Depth |

Layout Depth |

No |

Yes |

The size of the node in depth direction when used in a layout. Overrides the default bounds of the item. |

Node.DepthAlignment |

Depth Alignment |

No |

Yes |

The alignment in depth direction the node should use when it resides under a layout. |

Node.DepthMargin |

Depth Margin |

No |

Yes |

Sets the depth distance between this node and other nodes that are adjacent to this node in a layout.

To access the Depth Margin property fields in a binding, use: * X for the **Back** property field * Y for the **Front** property field  |

Node.EffectivelyEnabled |

Effectively Enabled |

No |

Yes |

Indicates whether this node and its ancestor nodes are enabled. Use this property in state managers and bindings to observe whether a node is effectively enabled. To enable or disable a node, use the Enabled property. When a node is effectively disabled: * When that node is focused, it receives key input until the focus moves to another node. * When that node is not focused, it is not part of the focus chain and does not receive key input. |

Node.Enabled |

Enabled |

No |

Yes |

Whether this node is enabled. When you disable this property in a node, that node and its descendant nodes in the same overlay focus scope are effectively disabled. Effectively disabling a node removes that node from the focus chain and cancels all the active input manipulators.Use the Effectively Enabled property to observe whether a node is effectively enabled. |

Node.Focusable |

Focusable |

No |

Yes |

Indicates whether the node can receive focus. |

Node.Focused |

Focused |

No |

Yes |

Indicates whether the node has the key focus. |

Node.FocusState |

Focus State |

No |

Yes |

Reports the focus state of a node: * **No focus** (0) indicates that the node is not focused. For a focus scope node indicates that none of the nodes in the scope have focus. * **Logical focus** (1) indicates that the node is the logical focus node of an overlay-type focus scope. For a focus scope node indicates that one of the nodes in that scope is the logical focus node. * **Key focus** (2) indicates that the node is the key focus node of the application and receives key input. For a focus scope node indicates that one of the nodes in that scope is the key focus node.

Use this property in state managers and bindings to implement focus states in the UI nodes.

To observe whether a node is the key focus node, you can use the boolean **Focus** > **Focused** property.  |

Node.FontFamily |

Font Family |

No |

Yes |

The font family used to render the text. |

Node.Height |

Layout Height |

No |

Yes |

The height of the node when used in a layout. Overrides the default bounds of the item. |

Node.HitTestable |

Hit Testable |

No |

Yes |

When enabled, the node can be hit tested. Enabling Hit Testable for a 2D node enables hit testing only for that node. Enabling Hit Testable for a 3D node enables hit testing also for the child nodes. Kanzi hit tests 3D nodes using the default Camera node or the Hit Test Camera node of the active Scene node. |

Node.HitTestableContainer |

Hit Testable Container |

No |

Yes |

When enabled, Kanzi uses the layout bounds as geometry for hit testing. |

Node.HorizontalAlignment |

Horizontal Alignment |

No |

Yes |

The alignment in horizontal direction the node should use when it resides under a layout. |

Node.HorizontalMargin |

Horizontal Margin |

No |

Yes |

Sets the horizontal space between this node and other nodes that are adjacent to this node in a layout.

To access the Horizontal Margin property fields in a binding, use: * X for the **Left** property field * Y for the **Right** property field  |

Node.Hover |

Hover |

No |

Yes |

Indicates whether a node is the foremost hit testable node under the cursor. |

Node.Locale |

Locale |

No |

No |

The locale of the node. |

Node.Opacity |

Opacity |

No |

Yes |

Opacity of the node. |

Node.Path |

Node.Path |

No |

Yes |

Full path to the node. |

Node.Projection2DTo3DScale |

2D to 3D Projection Scale |

No |

Yes |

Sets the scale factor to project pixels to 3D size. When scale is 1, then the size of one pixel is one 3D space unit. |

Node.StateManager |

State Manager |

No |

Yes |

Sets the State Manager to the node. |

Node.Style |

Style |

No |

Yes |

Sets a style to the node. |

Node.VerticalAlignment |

Vertical Alignment |

No |

Yes |

The alignment in vertical direction the node should use when it resides under a layout. |

Node.VerticalMargin |

Vertical Margin |

No |

Yes |

Sets the vertical space between this node and other nodes that are adjacent to this node in a layout.

To access the Vertical Margin property fields in a binding, use: * X for the **Bottom** property field * Y for the **Top** property field  |

Node.Visible |

Visible |

No |

Yes |

When disabled, Kanzi does not render the node. |

Node.VisibleAmountInParent |

Visible Amount in Parent |

No |

Yes |

Sets the amount the node is inside its parent. Use the value of this property in shaders to implement fades. Calculated by the parent node. |

Node.Width |

Layout Width |

No |

Yes |

The width of the node when used in a layout. Overrides the default bounds of the item. |

Node2D.AspectRatio |

Aspect Ratio |

No |

Yes |

Determines the proportion of width and height. You cannot set both the Aspect Ratio and both, Width and Height. |

Node2D.BackgroundBrush |

Background Brush |

No |

Yes |

The background brush to paint the background of 2D nodes. |

Node2D.CacheValid |

Cache Valid |

No |

Yes |

Indicates whether the node is cached. To disable the cache for one frame, disable this property. |

Node2D.CachingMode |

Caching Mode |

No |

Yes |

Sets the caching mode of this node: * **Disabled** sets Kanzi to render the node and its descendants normally, without caching. This is the default. * **Enabled** sets Kanzi to cache the node and its descendants and render the node from the cache image until you invalidate the cache by disabling the **Cache Valid** property. * **Automatic** sets Kanzi to automatically update the cache of the node whenever the content of the node or its descendants change. |

Node2D.CompositionBrush |

Composition Brush |

No |

Yes |

The brush to use to compose 2D nodes to screen. |

Node2D.DisableRenderTargetClear |

Disable Render Target Clear Color |

No |

Yes |

Do not clear render target buffers before rendering into it even if necessary. |

Node2D.Effect |

Effect |

No |

Yes |

Reports the runtime effect instance that this node uses. Kanzi sets the value of this property internally when the value of the Effect Prefab property in this node changes. |

Node2D.EffectPrefab |

Effect Prefab |

No |

Yes |

The 2D Effect to use for this node. |

Node2D.ForceComposition |

Force Composition |

No |

Yes |

Force rendering to composing target even if not otherwise necessary. |

Node2D.ForegroundBrush |

Foreground Brush |

No |

Yes |

The foreground brush to paint the foreground of 2D nodes. |

Node2D.ForegroundHint |

Foreground Hint |

No |

Yes |

Give a hint of the type of the foreground of 2D nodes: * **None** renders the background brush after rendering the node. * **Translucent** renders the background brush before the content of the node. * **Occluding** renders the background brush. |

Node2D.LayoutTransformation |

Layout Transformation |

No |

Yes |

The 2D transformation to be applied before layouting. |

Node2D.MipmapMode |

Mipmap Mode |

No |

Yes |

Sets the mipmap mode to use with the temporary composition targets to which Kanzi renders this node. |

Node2D.MultisampleLevel |

Multisample Level |

No |

Yes |

Sets the amount of multisample anti-aliasing to apply to the temporary composition targets to which Kanzi renders this node. |

Node2D.OffscreenRendering |

Off-Screen Rendering |

No |

Yes |

When set and the node has an explicitly set render target, do not render the resulting framebuffer to screen. |

Node2D.PerspectiveTransformation |

Perspective Transformation |

No |

Yes |

The 3D transformation to be applied after layouting. |

Node2D.PerspectiveTransformationFov |

Perspective Transformation FOV |

No |

Yes |

The 3D transformation field of view (degrees) to be applied after layouting. |

Node2D.PerspectiveTransformationMode |

Perspective Transformation Mode |

No |

Yes |

Defines the mode of operation for the coordinate system and field of view. |

Node2D.PerspectiveTransformationOrigin |

Perspective Transformation Origin |

No |

Yes |

The 3D transformation origin to be used for perspective transformation on this or child nodes. |

Node2D.PerspectiveTransformationPivot |

Perspective Transformation Pivot |

No |

Yes |

The 3D pivot point in relative coordinates. |

Node2D.PixelFormat |

Pixel Format |

No |

Yes |

The pixel format of the node if rendering to a texture. |

Node2D.RenderSelf |

Render Self |

No |

Yes |

Whether the node renders itself. Does not affect the rendering of child nodes. |

Node2D.RenderTarget |

Render Target |

No |

Yes |

Forces the node to be rendered into a given render target texture. When set to âNo Targetâ, regular conditions whether node is rendered to a texture, such as opacity and rotation, are applied. |

Node2D.RenderTargetMinimumHeight |

Render Target Minimum Height |

No |

Yes |

Sets the minimum height of implicitly generated render targets. |

Node2D.RenderTargetMinimumWidth |

Render Target Minimum Width |

No |

Yes |

Sets the minimum width of implicitly generated render targets. |

Node2D.RenderTargetReallocationLimit |

Render Target Reallocation Limit |

No |

Yes |

The change in size that triggers reallocation of a render target. |

Node2D.RenderTransformation |

Render Transformation |

No |

Yes |

The 2D transformation to be applied after layouting. |

Node2D.RenderTransformationOrigin |

Render Transformation Origin |

No |

Yes |

Sets the render transform origin in relative coordinates. |

Node2D.SnapToPixel |

Snap to Pixel |

No |

Yes |

Snap the translation of the node and its size into pixel boundary. |

Node3D.FinalTransformation |

Final Transformation |

No |

Yes |

The combined location, orientation and scale of the node and its ancestor nodes. Automatically calculated by the system. |

Node3D.LayoutTransformation |

Layout Transformation |

No |

Yes |

The location, orientation and scale of the node relative to its parent node. Layout Transformation affects the layout. If you do not want to affect the layout, use Render Transformation. |

Node3D.PreviousFinalTransformation |

Previous Final Transformation |

No |

Yes |

Final transformation (world matrix) from the previous frame, used for velocity buffer calculation. |

Node3D.RenderTransformation |

Render Transformation |

No |

Yes |

The location, orientation, and scale of the node relative to its parent node. Render transformation does not affect the layout of the node. |

NodeComponent.NodeComponentMessageArguments.TargetName |

Target Node Component Name |

No |

No |

Sets the name of the node component that receives this message. To send this message to every node component in this node, use an empty string. |

NodeComponent.NodeComponentSourceMessageArguments.SourceName |

Source Node Component Name |

No |

No |

Name of the node component that sent the message. |

NodeEffect2D.Enabled |

Enabled |

No |

Yes |

Whether to apply this effect. |

NodeListRenderPass.Filter |

Filter |

No |

Yes |

Sets the filter that the Node List render pass uses to filter or sort a list of incoming nodes. |

NodeListRenderPass.NodeList |

Node List |

No |

Yes |

Input node list range. Set by a binding from nearest parent node list. |

NodeListRenderPass.OutputNodeList |

Output Node List |

No |

Yes |

Output node list range. Set by Node List render pass as result of filtering the Input Node List. |

NormalScale |

Normal Scale |

No |

Yes |

Sets the normal scale for the material. Use the scale to set the intensity of the Normal Texture. |

NormalTexture |

Normal Texture |

No |

Yes |

Sets the texture that contains a normal map for the material. Use the Normal Scale property to scale the texture value. |

OcclusionRenderStrength |

Occlusion Render Strength |

No |

Yes |

Sets the SSAO strength for the material. Use the strength to set the intensity of the SSAO Texture. |

OcclusionRenderTexture |

Occlusion Render Texture |

No |

Yes |

Sets the texture that contains a SSAO computed for the scene. Use the Occlusion Render Strength property to scale the strength of the SSAO. |

OcclusionStrength |

Occlusion Strength |

No |

Yes |

Sets the occlusion strength for the material. Use the strength to set the intensity of the Occlusion Texture. |

OcclusionTexture |

Occlusion Texture |

No |

Yes |

Sets the texture that contains an occlusion map for the material. Use the Occlusion Strength property to scale the occlusion from the texture. |

OnPropertyChangedTrigger.IgnoreIdenticalValue |

Ignore Identical Value |

No |

No |

Invoke the trigger only on change in the monitored propertyâs value. |

OnPropertyChangedTrigger.IgnoreInitialValue |

Ignore Initial Value |

No |

No |

Invoke the trigger only when the value of the monitored property changes after the trigger is already attached. |

OnPropertyChangedTrigger.SourceNode |

Node |

No |

No |

The node for which this trigger monitors property changes. |

OnPropertyChangedTrigger.SourcePropertyType |

Property Type |

No |

No |

The property type the changes of which trigger this trigger. |

OutlineEffect2D.BlendMode |

Outline Blend Mode |

No |

Yes |

Sets the blend mode to use for rendering the outline.

Color Blending: - Additive adds the source pixels to the destination pixels. - Multiply multiplies the source and destination pixels. - Screen adds the source and destination pixels and subtracts from the result the product of the source and destination. - Alpha: Automatic uses premultiplied or non-premultiplied alpha depending on the value of the âPremultiply Alphaâ property in the project or an image. - Alpha: Non-premultiplied is a legacy mode. For non-premultiplied input use the Alpha: Mixed mode. - Alpha: Premultiplied expects premultiplied alpha RGBA in the source pixels and blends the source pixels on top of the destination pixels. This is the default and recommended mode for alpha blending. - Alpha: Mixed expects non-premultiplied alpha RGBA in the source pixels, and blends the source pixels with the destination framebuffer.

Alpha Compositing: - Opaque disables blending and replaces the destination pixels with the source pixels. - Clear sets the destination pixels to transparent black. - Exclusive Or draws the non-overlapping source and destination pixels. - Source Atop discards those source pixels that do not cover destination pixels and draws the rest of the source pixels over destination pixels. - Source In draws those source pixels that cover destination pixels and discards all destination pixels. - Source Out draws the source pixels with alpha reduced by the inverse of the destination alpha, and discards all destination pixels. - Destination Atop discards those destination pixels that are not covered by source pixels, and draws the rest of the destination pixels over source pixels. - Destination In draws only those destination pixels that intersect with the source pixels, and discards all source pixels. - Destination Out draws the destination pixels with alpha reduced by the inverse of the source alpha, and discards all source pixels. - Destination Over draws the destination pixels over the source pixels.

Advanced Color Blending: - Multiply (advanced khr) is similar to the Multiply mode but it screens the alpha. - Overlay multiplies dark pixels and screens light pixels. - Darken compares the destination and source pixels and selects the darker one. - Lighten compares the destination and source pixels and selects the lighter one. - Color Burn darkens the destination to reflect the color of the source. - Color Dodge lightens the destination to reflect the color of the source. - Hard Light multiplies with dark source color and screens with light source color. - Soft Light burns with dark source color and dodges with light source color. - Difference uses the difference of the source and destination pixels. - Exclusion is similar to difference but the result is lower in contrast. - HSL Hue uses the hue of the source, and the luminosity and saturation of the destination. - HSL Saturation uses the saturation of the source, and the hue and luminosity of the destination. - HSL Color uses the hue and saturation of the source, and the luminosity of the destination. - HSL Luminosity uses luminosity of the source, and the jue and saturation of the destination.

The advanced color blending modes require the GL_KHR_blend_equation_advanced and GL_KHR_blend_equation_advanced_coherent OpengGL extensions.  |

OutlineEffect2D.Color |

Outline Color |

No |

Yes |

Sets the color of the outline. |

OutlineEffect2D.ContentGradient |

Content Gradient |

No |

Yes |

Sets the gradient along which the content fades out: * **Start** sets the minimum intensity at which the content starts to fade out. * **Softness** sets the difference in intensity it takes for the content to disappear.

For a perfectly smooth gradient, set **Start** to 0 and **Softness** to 1. The default value [ 0.0, 0.19 ] makes the content fade out quickly before the outline fade-out starts.  |

OutlineEffect2D.ContentMask |

Content Mask |

No |

Yes |

Sets the color that masks color components relevant to the outline calculation. The comparison value is the result of a dot product between the mask and the content RGBA color value. By default Kanzi calculates the outline only from the alpha value. |

OutlineEffect2D.ContentThreshold |

Content Threshold |

No |

Yes |

Sets the threshold at which the value Kanzi calculates using the content mask is considered valid. When the value calculated from masking the content exceeds this value, that pixel is part of the outlined area. |

OutlineEffect2D.InnerSoftness |

Outline Inner Softness |

No |

Yes |

Sets the softness of the outline relative to its width inside the content area. For a sharp outline, set to 0. For a fade-in that takes the complete outline width to reach maximum value, set to 1. By default, this property uses the value of the **Outline Softness** property. |

OutlineEffect2D.InnerWidth |

Outline Inner Width |

No |

Yes |

Sets the width of the outline in pixels inside the content area. By default, this property uses the value of the **Outline Width** property. |

OutlineEffect2D.InvertContentMask |

Invert Content Mask |

No |

Yes |

Whether to invert the value that Kanzi calculates using content masking. |

OutlineEffect2D.Method |

Outline Method |

No |

Yes |

Sets the method for outline calculation: * **Box** uses box search which potentially consumes less memory but is slower. * **Two-pass** uses two-pass search which potentially consumes more memory but is faster. This the default. |

OutlineEffect2D.Softness |

Outline Softness |

No |

Yes |

Sets the softness of the outline. For a sharp outline, set to 0. For a fade-in that takes the complete outline width to reach maximum value, set to 1. The default value is 0.27. |

OutlineEffect2D.Texture |

Outline Texture |

No |

Yes |

Sets the texture to apply to the outline. Kanzi applies to the outline only the top row of pixels from this texture. Set **Outline Color** to the color with which you want to modulate the colors in this texture. |

OutlineEffect2D.TextureOffset |

Outline Texture Offset |

No |

Yes |

Sets the relative starting offset for sampling the outline texture. The default value is 0.0. |

OutlineEffect2D.TextureTiling |

Outline Texture Tiling |

No |

Yes |

Sets the number of times the texture wraps around within the outline area. To repeat a texture, set its **Wrap Mode** to **Repeat**. The default value is 1.0 |

OutlineEffect2D.Width |

Outline Width |

No |

Yes |

Sets the width of the outline in pixels outside the content area. The default value is 4 pixels. |

Page.AutoActivate |

Keep Active |

No |

No |

Always activate this Page node when its parent is active. |

Page.RotationOffset |

Rotation Offset |

No |

Yes |

The angle in degrees by which to rotate a Page node. |

Page.ScaleOffset |

Scale Offset |

No |

Yes |

The factor by which to scale a Page node. |

Page.SlideOffset |

Slide Offset |

No |

Yes |

The offset to slide a Page node in horizontal or vertical direction:nX [-1, 1] to move the Page node horizontallynY [-1, 1] to move the Page node vertically |

Page.State |

Activation State |

No |

Yes |

The state of this Page node: false (inactive and invisible) or true (active and visible) (read-only). |

Page.TransitionPhase |

Transition Phase |

No |

Yes |

The phase of the transition. For example, use for pixel-based effects. |

PageHost.DefaultSubPage |

Default Subpage |

No |

No |

The default or the currently active subpage, which Kanzi automatically activates whenever this PageHost node becomes active. |

PageHost.LoopSubPages |

Loop Subpages |

No |

No |

Loop the subpages when navigating to the next or previous subpage. |

PageHost.Transitions |

Transitions |

No |

Yes |

Transitions to be used within this PageHost node. |

PageTransition.Direction |

Direction |

No |

No |

Defines whether the transition is unidirectional (one way) or bidirectional (two way). |

PageTransition.Duration |

Duration |

No |

No |

The duration of a Page node transition (in milliseconds). |

PageTransition.From |

From |

No |

No |

The selection criteria for the source Page node. Use * for any Page node. |

PageTransition.To |

To |

No |

No |

The selection criteria for the target Page node. Use * for any Page node. |

PageTransitionAnimation.AnimationTarget |

Animation Target |

No |

No |

Defines the animation target, either page transitioning in or page transitioning out. |

PageTransitionAnimation.EndValue |

End Value |

No |

No |

The ending value for the animation. |

PageTransitionAnimation.PropertyType |

Transition Property |

No |

No |

Defines which property to animate. |

PageTransitionAnimation.StartValue |

Start Value |

No |

No |

The starting value for the animation. |

PanManipulator.PanDelta |

Pan Delta |

No |

No |

Holds the change in pan position since the last update in global screen coordinates. |

PanManipulator.PanVelocity |

Pan Velocity |

No |

No |

Holds the current estimate of the pan velocity in global screen coordinates. |

PanManipulatorComponent.MaximumTouchPoints |

Maximum Touch Points |

No |

Yes |

Sets the maximum number of touches allowed on the node area for the installed pan manipulator to recognize the pan gesture and to set off the Pan Started trigger. The default value is 10. The value cannot be lower than the value of the Minimum Touch Points property. |

PanManipulatorComponent.MinimumTouchPoints |

Minimum Touch Points |

No |

Yes |

Sets the minimum number of touches required on the node area for the installed pan manipulator to recognize the pan gesture and to set off the Pan Started trigger. The default value is 1. |

PanManipulatorComponent.RecognitionThreshold |

Recognition Threshold |

No |

Yes |

Sets the threshold in pixels on the horizontal and vertical axis that the finger must move before Kanzi recognizes it as a pan gesture. The default value is 5 pixels on both axes. To disable the pan gesture along either axis, set the threshold on that axis to -1. |

PanManipulatorComponent.RoutingMode |

Routing Mode |

No |

No |

Routing mode determines when the input manipulator recognizes input events: * **Bubbling** sets the installed manipulator to recognize input events that are traversing from the hit test node or the focus node to the root node. * **Tunneling** sets the installed manipulator to recognize input events that are traversing from the root node to the hit test node or to the focus node. |

ParallelActivityHostConcept.BringActivatedToFront |

Bring Activated Activity To Front |

No |

Yes |

Sets whether to show the activated Activity in front within its Parallel Activity Host. This property affects the z-order of the activated Activity within the same Activity priority layer: * When enabled, the Activity is shown in front. * When disabled, the z-order of the activated child Activity is determined by the order in which you added that Activity to the parent Parallel Activity Host. This is the default behavior. |

ParallelActivityHostConcept.FocusOnActivation |

Focus On Activation |

No |

Yes |

Sets the policy that a Parallel Activity Host uses to decide whether it tries to set the key focus to an activating Activity: * **When Host Has Focus**: If the Activity Host has the focus, it tries to set the focus to the Activity. This is the default. * **Always**: The Activity Host always tries to set the focus to the Activity. * **Never**: The Activity Host never tries to set the focus to the Activity.

Set this property in an Activity in a Parallel Activity Host.  |

PinchManipulator.PinchPositionDelta |

Pinch Position Delta |

No |

No |   |

PinchManipulator.PinchRotation |

Pinch Rotation |

No |

No |   |

PinchManipulator.PinchScale |

Pinch Scale |

No |

No |   |

PipelineStateRenderPass.AlphaToCoverageEnabled |

Alpha To Coverage Enabled |

No |

Yes |

Sets whether Alpha To Coverage is enabled or not. |

PipelineStateRenderPass.BlendMode |

Blend Mode |

No |

Yes |

Overrides the blend mode set in each node that this render pass renders. |

PipelineStateRenderPass.ColorWriteMode |

Color Write Mode |

No |

Yes |

Sets which channels the render pass writes to the color buffer. To disable the color write, set the property to None. |

PipelineStateRenderPass.CullMode |

Cull Mode |

No |

Yes |

Sets the culling of the triangle faces in the rendered meshes: * **Back** renders the triangles whose normal points towards a Camera node. * **Front** renders the triangles whose normal points away from a Camera node. |

PipelineStateRenderPass.DepthTestFunction |

Depth Test Function |

No |

Yes |

Controls whether the depth test discards a fragment. |

PipelineStateRenderPass.DepthWriteEnabled |

Depth Write Enabled |

No |

Yes |

Sets whether the render pass writes to the depth buffer. |

PipelineStateRenderPass.PolygonDepthOffset |

Polygon Depth Offset |

No |

Yes |

Sets the polygon depth offset to apply to the element that the Pipeline State render pass renders: * **Derivative multiplier** sets the multiplier for the depth change derivative for the fragment. * **Constant multiplier** multiplies the smallest measurable unit of depth, dependent on the target platform.

You can use the offset to render decals on the surfaces of filled polygons. Kanzi typically shows nearer the camera those polygons that have a negative offset.  |

PipelineStateRenderPass.Scissor |

Scissor Area |

No |

Yes |

Sets the scissor test in the current rendering **Viewport 2D** node. You can define the scissor in either relative or absolute coordinates, the default is relative. Use the **Scissor Mode** property to set the coordinate type. |

PipelineStateRenderPass.ScissorMode |

Scissor Mode |

No |

Yes |

Sets the scissor test coordinate mode. |

PipelineStateRenderPass.StencilFailOperation |

Stencil Fail Operation |

No |

Yes |

Sets the operation that the render pass performs when the stencil test fails. |

PipelineStateRenderPass.StencilMask |

Stencil Function Mask |

No |

Yes |

Sets a mask on which the AND operation is executed with both the reference value and the stored stencil value when the test is done. |

PipelineStateRenderPass.StencilPassDepthFailOperation |

Stencil Pass Depth Fail Operation |

No |

Yes |

Sets the operation that the render pass performs when the stencil test passes, but the depth test fails. |

PipelineStateRenderPass.StencilPassDepthPassOperation |

Stencil Pass Depth Pass Operation |

No |

Yes |

Sets the operation that the render pass performs when both, the stencil and the depth test, pass. |

PipelineStateRenderPass.StencilReferenceValue |

Stencil Function Reference Value |

No |

Yes |

Sets the reference value for the stencil test. |

PipelineStateRenderPass.StencilTestFunction |

Stencil Test Function |

No |

Yes |

Controls whether the stencil test discards a fragment. |

PipelineStateRenderPass.StencilWriteEnabled |

Stencil Write Enabled |

No |

Yes |

Sets whether to enable writing to the stencil buffer. |

PipelineStateRenderPass.Viewport |

Viewport Area |

No |

Yes |

Modifies the current rendering Viewport node. You can define the Viewport in either relative or absolute coordinates, the default is relative. Use the **Viewport Mode** property to set the coordinate type. |

PipelineStateRenderPass.ViewportMode |

Viewport Mode |

No |

Yes |

Sets the coordinate type for the Viewport node. |

PlanarReflectionMap |

Planar Reflection Map |

No |

Yes |

Rendered texture for planar reflections. |

PlanarReflectionViewProjection |

Planar Reflection View Projection |

No |

Yes |

The premultiplied projection view matrix for planar reflections. |

PointLight |

Point Light |

No |

Yes |

Point light settings |

PointLightAttenuation |

Point Light Attenuation |

No |

Yes |

Sets the effect that this Point Light has on nodes that are farther away. Distance of light from the lighted surface is input in a quadratic function, the 3 components are the constant, linear and quadratic coefficients for the distance variable. |

PointLightColor |

Point Light Color |

No |

Yes |

Sets the color of the Point Light. Use the Intensity (I) property field to adjust the brightness of the light. |

PointLightRadius |

Point Light Radius |

No |

Yes |

Sets the distance at which the intensity of the Point Light reaches zero. For infinite distance, set the property value to 0. |

PointShadowBias |

Point Shadow Bias |

No |

Yes |

Sets the point shadow bias to reduce sampling artifacts. |

PointShadowMap |

Point Shadow Map |

No |

Yes |

Depth cubemap used to calculate point light shadows. |

PointShadowNearFar |

Point Shadow Near Far |

No |

Yes |

Sets the near & far values used for point shadow calculations. |

PointShadowSoftness |

Point Shadow Softness |

No |

Yes |

Sets the softness of the shadows cast by the Point Light. |

PrefabViewConcept.AsynchronousLoadCompletedMessageArguments.PrefabTemplate |

Prefab Template |

No |

No |

The prefab whose resources finished loading asynchronously. |

PrefabViewConcept.LoadAsynchronouslyMessageArguments.PrefabTemplate |

Prefab Template |

No |

No |

The prefab whose resources you want to load asynchronously. |

PrefabViewConcept.Prefab |

Prefab Template |

No |

Yes |

Node to use on this prefab view. |

PreviewBackgroundColor |

Preview Background Color |

No |

Yes |

Sets the background color of the Preview for this project.

When you do not set this property, the project uses the color that you set in **Edit** > **User Preferences** > **Preview** > **Background Color**.  |

ProgressiveRenderingViewport2D.Animation |

Timeline |

No |

Yes |

The animation timeline to play in Progressive Rendering Viewport 2D |

ProjectCustomThumbnail |

Thumbnail |

No |

Yes |

Sets the thumbnail that Kanzi Studio shows in the Quick Start window. |

ProjectResourceDefaultCrossProjectVisibility |

Resource Visibility Across Projects |

No |

Yes |

Sets whether the resources of this project are available to referencing projects: * Private makes the resources available only to this project. This is the default value. * Public makes the resources available in the dropdown menus of referencing projects. To override this setting for an individual resource, add and set the Visibility Across Projects property for that resource. |

PropertyDrivenAnimationPlayer.Enabled |

Enabled |

No |

No |

Specifies whether animation timeline is applied. |

PropertyDrivenAnimationPlayer.RelativePlayback |

Relative Playback |

No |

No |

Specifies whether animations are applied in relative manner by adding animated value to target property value instead of replacing the property value. |

PropertyDrivenAnimationPlayer.Timeline |

Target Animation Timeline |

No |

No |

The target animation timeline for property driven animation. |

PropertyDrivenAnimationPlayer.TimePropertyTypeProperty |

Time Controller Property Type |

No |

No |

The type of property on the node whose value is taken by the player as input time for timeline playback. |

PropertyTargetEasingInterpolator.EasingFunction |

Easing Function |

No |

No |

Sets the easing function that defines the curve of the interpolation. |

PropertyTargetEasingInterpolator.EasingMode |

Easing Mode |

No |

No |

Sets how to apply the easing function to the interpolation. |

PropertyTargetEasingInterpolator.Enabled |

Enabled |

No |

Yes |

Sets whether the Property Target Easing Interpolator interpolates the value of the Interpolated Property Type. |

PropertyTargetEasingInterpolator.InterpolatedPropertyField |

Interpolated Field |

No |

No |

The property field of the Interpolated Property Type you want to interpolate from its previous value to a new value using this Property Target Easing Interpolator. |

PropertyTargetEasingInterpolator.InterpolatedPropertyType |

Interpolated Property Type |

No |

No |

The property type you want to interpolate from its previous value to a new value using this Property Target Easing Interpolator. |

PropertyTargetEasingInterpolator.InterpolationDuration |

Interpolation Duration |

No |

No |

Sets the duration of the interpolation in milliseconds. |

PropertyTargetEasingInterpolator.InterpolationIfInterrupted |

Interpolation If Interrupted |

No |

No |   Sets what happens if a new value is set to the interpolated property before interpolation to its previous value completes:

- Start from current interpolated value uses the current value of the ongoing interpolation as the start value of the new interpolation.
- Start from current target value uses the target value of the ongoing interpolation as the start value of the new interpolation.

PropertyTargetEasingInterpolator.NotifyInterpolationCompleted |

Notify Interpolation Completed |

No |

Yes |

Sets whether the Property Target Easing Interpolator dispatches a Completed message every time it completes interpolation. |

PropertyTargetInterpolator.Acceleration |

Acceleration |

No |

No |

Acceleration coefficient of property interpolation. Larger acceleration leads to faster reaching new property value. |

PropertyTargetInterpolator.Drag |

Drag |

No |

No |

Drag coefficient of property interpolation. Larger drag lowers maximum speed of interpolation. |

PropertyTargetInterpolator.InterpolatedPropertyField |

Interpolated Field |

No |

No |

The field of a property on a node which is interpolated from its previous value to new one by property target interpolator. |

PropertyTargetInterpolator.InterpolatedPropertyType |

Interpolated Property Type |

No |

No |

The property type of a property on a node which is interpolated from its previous value to new one by property target interpolator. |

RangeConcept.CommonMessageArguments.Value |

Range Value |

No |

No |

Range Value |

RangeConcept.IsValueChanging |

Is Value Changing |

No |

Yes |

Whether the value is currently changing. |

RangeConcept.MaximumValue |

Maximum Value |

No |

Yes |

The maximum value that the range allows. |

RangeConcept.MinimumValue |

Minimum Value |

No |

Yes |

The minimum value that the range allows. |

RangeConcept.NormalizedValue |

Normalized Value |

No |

Yes |

The current value normalized to range [0, 1]. |

RangeConcept.Step |

Step Value |

No |

Yes |

The minimum amount that the value of the range can change at a time. |

RangeConcept.Value |

Value |

No |

Yes |

The current value. To update this property with a binding, use a to-source or two-way binding. |

RaytracedReflectionRenderPass.AccelerationStructure |

Acceleration Structure |

No |

Yes |   |

RaytracedReflectionRenderPass.EnvironmentAmbientTexture |

Environment Ambient Texture |

No |

Yes |   |

RaytracedReflectionRenderPass.GBufferDepth |

GBuffer Depth |

No |

Yes |   |

RaytracedReflectionRenderPass.GBufferNormal |

GBuffer Normal |

No |

Yes |   |

RaytracedReflectionRenderPass.GBufferRoughness |

GBuffer Roughness |

No |

Yes |   |

RaytracedReflectionRenderPass.Material |

Material |

No |

Yes |

Sets the material that will be used to render all nodes rendered by this RaytracedReflectionRenderPass. |

RaytracedReflectionRenderPass.OutputReflection |

Output Reflection Texture |

No |

Yes |   |

RaytracedReflectionRenderPass.RayTMax |

Ray Maximum Trace Distance |

No |

Yes |   |

RaytracedReflectionRenderPass.RaytracedReflectionMaxRoughness |

Raytraced Reflection Maximum Roughness |

No |

Yes |   |

RaytracedReflectionRenderPass.ResolutionScale |

Reflection Resolution Scale |

No |

Yes |   |

RaytracedShadowRenderPass.AccelerationStructure |

Acceleration Structure |

No |

Yes |   |

RaytracedShadowRenderPass.BlueNoise |

Blue Noise |

No |

Yes |   |

RaytracedShadowRenderPass.GBufferDepth |

GBuffer Depth |

No |

Yes |   |

RaytracedShadowRenderPass.GBufferNormal |

GBuffer Normal |

No |

Yes |   |

RaytracedShadowRenderPass.Light |

Light |

No |

Yes |   |

RaytracedShadowRenderPass.Material |

Material |

No |

Yes |

Sets the material that will be used to render all nodes rendered by this RaytracedShadowRenderPass. |

RaytracedShadowRenderPass.OutputShadowMask |

Output Shadow Mask Texture |

No |

Yes |   |

RaytracedShadowRenderPass.RayTMax |

Ray Maximum Trace Distance |

No |

Yes |   |

RaytracedShadowRenderPass.ResolutionScale |

Shadow Map Resolution Scale |

No |

Yes |   |

RenderPass.Camera |

Camera |

No |

Yes |

Sets the Camera node that you want to use to render the nodes. To use the default Camera node in that Scene node, do not set the value for this property. |

RenderPass.Enabled |

Enabled |

No |

Yes |

Whether Kanzi executes this render pass and its child render pass tree. |

RenderPass.InputViewportArea |

Input Viewport Area |

No |

Yes |

Reports the viewport area relative to the composition space as passed from the parent render pass.

To access the Input Viewport Area property fields in a binding, use: * X for the offset along the x axis relative to the composition space * Y for the offset along the y axis relative to the composition space * Z for the width of the viewport * W for the height of the viewport  |

RenderPass.ShadowProjectionFittingEnabled |

Shadow Projection Fitting Enabled |

No |

Yes |

Controls how the directional light shadow projection is calculated Enabling this will fit the lights projection to the area covered by the main camera. |

RenderPass.ShadowProjectionMargin |

Shadow Projection Margin |

No |

Yes |

Use to add extra margin by scaling the area of the projection |

RenderPass.ShadowProjectionRange |

Shadow Projection Range |

No |

Yes |

Use to limit the projection to a smaller proportional slice (X: near, Y: far) of the main camera frustum. For example if X: 0.0, Y: 0.5 means only the closest half of the camera frustum is guaranteed to be included in the shadow projection. |

RenderPass.UpdateOffset |

Update Rate Offset |

No |

Yes |

Sets a frame offset to the rendering rate that you set with the Update Rate property. This lets you cascade multiple updating render passes to different frames. |

RenderPass.UpdateRate |

Update Rate |

No |

Yes |

Sets the rate at which to render the render pass. To render every frame, set to 1. To render every second frame, set to 2, and so on. To render only once, set to 0. |

RenderPassView.RenderPassPrefab |

Render Pass Prefab |

No |

Yes |

Sets the Render Pass Prefab that this Render Pass View instantiates. |

ResourceCrossProjectVisibility |

Visibility Across Projects |

No |

Yes |

Sets whether this resource is available to referencing projects: * Project setting uses the value of the Resource Visibility Across Projects property of the project. * Private makes the resource available only to this project. * Public makes the resource available in the dropdown menus of referencing projects. |

ResourceDictionarySelector.SelectedDictionary |

Selected Theme |

No |

No |

The currently selected theme in the theme group. In Kanzi Studio you can change the current theme with the ActivateTheme action. |

ResourceKeepAliveBehavior |

Keep Alive Behavior |

No |

Yes |

The keep-alive behavior of this resource. Can be used to deny unloading of the resource. |

RoughnessFactor |

Roughness Factor |

No |

Yes |

Sets the roughness of the material: 0 represents a smooth, glossy surface, and 1 represents a rough, diffuse surface. |

RoughnessTexture |

Roughness Texture |

No |

Yes |

Sets the texture that contains a roughness map for the material. Kanzi reads the roughness from the Green channel of the texture. Use the Roughness Factor property to scale the roughness from this texture. |

Scene.Camera |

Camera |

No |

Yes |

Sets the camera through which the Kanzi application shows the Scene. |

Scene.HitTestCamera |

Hit Testing Camera |

No |

Yes |

Sets the camera to use to hit test the objects in the Scene. The default is the camera that you set with the **Camera** property. |

Screen.ClearColor |

Screen Clear Color |

No |

Yes |

If screen has a clear color, screen will be cleared with the specified color before all other rendering. Depth will be cleared to 1.0f and stencil will be cleared to 0. |

Screen.HostName |

Host Name |

No |

Yes |

Contains the name of the host the node originates from. |

ScrollViewConcept.AllowedScrollAxis |

Allowed Scroll Axis |

No |

Yes |

Sets the axis on which you want to allow this Scroll View node to scroll. |

ScrollViewConcept.DraggingAccelerationCoefficient |

Dragging Acceleration |

No |

Yes |

Sets the acceleration of the node controlled by a Scroll View node while you drag that Scroll View node. Use low values when you want that node to slowly reach the final position. Use high values when you want that node to quickly reach the final position. |

ScrollViewConcept.DraggingDragCoefficient |

Dragging Drag |

No |

Yes |

Sets the amount that drag affects the movement of the node controlled by a Scroll View node while you drag that Scroll View node. The lower the value the higher the drag and the faster the sliding of that node stops. |

ScrollViewConcept.DraggingImpulseFactor |

Dragging Impulse |

No |

Yes |

Sets the amount of impulse generated from the pointing device movement when dragging a Scroll View node. |

ScrollViewConcept.LoopingXEnabled |

Looping X Enabled |

No |

Yes |

Sets the node controlled by a Scroll View node to start scrolling from the beginning when the scroll reaches the scroll bounds on the x axis. When the scroll value reaches the maximum value of the bound, the value changes to the minimum value and the other way around. Use the Scroll Bounds Minimum and Scroll Bounds Maximum properties to set the scroll bounds. |

ScrollViewConcept.LoopingYEnabled |

Looping Y Enabled |

No |

Yes |

Sets the node controlled by a Scroll View node to start scrolling from the beginning when the scroll reaches the scroll bounds on the y axis. When the scroll value reaches the maximum value of the bound, the value changes to the minimum value and the other way around. Use the Scroll Bounds Minimum and Scroll Bounds Maximum properties to set the scroll bounds. |

ScrollViewConcept.MaximumNumberOfTouches |

Maximum Number of Touches |

No |

Yes |

Sets the maximum number of touch points allowed for a Scroll View pan. |

ScrollViewConcept.MinimumNumberOfTouches |

Minimum Number of Touches |

No |

Yes |

Sets the required number of touch points pressed for a Scroll View node pan to start. Scroll View nodes with minimum number of touches greater than one precede the children in touch processing. |

ScrollViewConcept.RecognitionThreshold |

Recognition Threshold |

No |

Yes |

Sets the amount a pointing device must move for the scrolling to start on a Scroll View node. |

ScrollViewConcept.ReversedXAxisScroll |

Reversed X Axis Scroll |

No |

Yes |

Whether the scroll position of the x axis increases in relation to the direction of the pan gesture. This reverses the direction of scrolling. By default, the scroll position decreases in relation to the pan direction. |

ScrollViewConcept.ReversedYAxisScroll |

Reversed Y Axis Scroll |

No |

Yes |

Whether the scroll position of the y axis increases in relation to the direction of the pan gesture. This reverses the direction of scrolling. By default, the scroll position decreases in relation to the pan direction. |

ScrollViewConcept.ScrollBoundsMaximum |

Scroll Bounds Maximum |

No |

Yes |

Sets the coordinates of the bottom-right corner of the scroll bounds rectangle. Scroll bounds define where the scrolling begins and ends. |

ScrollViewConcept.ScrollBoundsMinimum |

Scroll Bounds Minimum |

No |

Yes |

Sets the coordinates of the top-left corner of the scroll bounds rectangle. Scroll bounds define where the scrolling begins and ends. |

ScrollViewConcept.Scrolling |

Scrolling |

No |

Yes |

Whether a Scroll View node is currently scrolling (read-only). |

ScrollViewConcept.ScrollPosition |

Scroll Position |

No |

Yes |

Sets the scroll position of the Scroll View along the x and y axes as a relative position within the scroll view area. Use this property to set the scroll position immediately, without scrolling. To update the scroll position with a binding, use a two-way or to-source binding. |

ScrollViewConcept.ScrollSpeed |

Scroll Speed |

No |

Yes |

The current scroll speed (read-only). |

ScrollViewConcept.ScrollTargetPosition |

Scroll Target Position |

No |

Yes |

The current target scroll value (read-only). |

ScrollViewConcept.Sensitivity |

Scroll Sensitivity |

No |

Yes |

Sets the amount the position changes relative to the movement of the pointer that starts the swiping. The higher the value the more the position of the node controlled by a Scroll View node changes. The default value is 1. |

ScrollViewConcept.SlidingAccelerationCoefficient |

Sliding Acceleration |

No |

Yes |

Sets the acceleration of the node controlled by a Scroll View node after you release the pointer with which you swipe. Use low values when you want that node to slowly reach the final position. Use high values when you want that node to quickly reach the final position. |

ScrollViewConcept.SlidingDragCoefficient |

Sliding Drag |

No |

Yes |

Sets the amount that drag affects the movement of the node controlled by a Scroll View node after you release the pointer with which you swipe. The lower the value the higher the drag and the faster the sliding of the object controlled by the Scroll View node stops. |

ScrollViewConcept.StepMultiplier |

Step Multiplier |

No |

Yes |

Sets the smallest distance that a Scroll View scrolls. |

ScrollViewConcept.SwipeDistance |

Swipe Distance |

No |

Yes |

Sets the distance that a swipe sends the scroll value, relative to the pointing device speed. |

ScrollViewConcept.Zoom |

Zoom |

No |

Yes |

Sets the current zoom level. |

ScrollViewConcept.ZoomAffectsScrolling |

Zoom Affects Scrolling |

No |

Yes |

Controls whether the scroll position is scaled, according to the zoom level. |

ScrollViewConcept.ZoomEnabled |

Zoom Enabled |

No |

Yes |

Sets whether to install a pinch manipulator that generates zoom messages. |

ScrollViewConcept.ZoomMaximum |

Maximum Zoom |

No |

Yes |

Sets the maximum zoom level. |

ScrollViewConcept.ZoomMinimum |

Minimum Zoom |

No |

Yes |

Sets the minimum zoom level. |

ShadowEffect2D.Angle |

Shadow Angle |

No |

Yes |

Sets the direction of the shadow as an angle relative to the positive x axis. The default is 45 degrees. When you set the **Override Shadow Offset** property, this property has no effect. |

ShadowEffect2D.BlendMode |

Shadow Blend Mode |

No |

Yes |

Sets the blend mode to use for rendering the shadow.

Color Blending: - Additive adds the source pixels to the destination pixels. - Multiply multiplies the source and destination pixels. - Screen adds the source and destination pixels and subtracts from the result the product of the source and destination. - Alpha: Automatic uses premultiplied or non-premultiplied alpha depending on the value of the âPremultiply Alphaâ property in the project or an image. - Alpha: Non-premultiplied is a legacy mode. For non-premultiplied input use the Alpha: Mixed mode. - Alpha: Premultiplied expects premultiplied alpha RGBA in the source pixels and blends the source pixels on top of the destination pixels. This is the default and recommended mode for alpha blending. - Alpha: Mixed expects non-premultiplied alpha RGBA in the source pixels, and blends the source pixels with the destination framebuffer.

Alpha Compositing: - Opaque disables blending and replaces the destination pixels with the source pixels. - Clear sets the destination pixels to transparent black. - Exclusive Or draws the non-overlapping source and destination pixels. - Source Atop discards those source pixels that do not cover destination pixels and draws the rest of the source pixels over destination pixels. - Source In draws those source pixels that cover destination pixels and discards all destination pixels. - Source Out draws the source pixels with alpha reduced by the inverse of the destination alpha, and discards all destination pixels. - Destination Atop discards those destination pixels that are not covered by source pixels, and draws the rest of the destination pixels over source pixels. - Destination In draws only those destination pixels that intersect with the source pixels, and discards all source pixels. - Destination Out draws the destination pixels with alpha reduced by the inverse of the source alpha, and discards all source pixels. - Destination Over draws the destination pixels over the source pixels.

Advanced Color Blending: - Multiply (advanced khr) is similar to the Multiply mode but it screens the alpha. - Overlay multiplies dark pixels and screens light pixels. - Darken compares the destination and source pixels and selects the darker one. - Lighten compares the destination and source pixels and selects the lighter one. - Color Burn darkens the destination to reflect the color of the source. - Color Dodge lightens the destination to reflect the color of the source. - Hard Light multiplies with dark source color and screens with light source color. - Soft Light burns with dark source color and dodges with light source color. - Difference uses the difference of the source and destination pixels. - Exclusion is similar to difference but the result is lower in contrast. - HSL Hue uses the hue of the source, and the luminosity and saturation of the destination. - HSL Saturation uses the saturation of the source, and the hue and luminosity of the destination. - HSL Color uses the hue and saturation of the source, and the luminosity of the destination. - HSL Luminosity uses luminosity of the source, and the jue and saturation of the destination.

The advanced color blending modes require the GL_KHR_blend_equation_advanced and GL_KHR_blend_equation_advanced_coherent OpengGL extensions.  |

ShadowEffect2D.BlurRadius |

Shadow Blur Radius |

No |

Yes |

Sets the softness of the shadow by defining the distance in pixels the shadow blur extends outward from an edge. For a shadow with sharp edges, set to 0. The default is 8 pixels. |

ShadowEffect2D.Color |

Shadow Color |

No |

Yes |

Sets the color and alpha of the shadow. |

ShadowEffect2D.Distance |

Shadow Distance |

No |

Yes |

Sets how far to move the shadow from the object in the direction set by the **Shadow Angle** property. The default is 10 pixels. When you set the **Override Shadow Offset** property, this property has no effect. |

ShadowEffect2D.OverrideOffset |

Override Shadow Offset |

No |

Yes |

Sets the offset of the shadow from the object along the x and y axes in pixels. When you set this property, the **Shadow Angle** and **Shadow Distance** properties have no effect. To disable the offset override, remove this property. |

ShadowEffect2D.Quality |

Shadow Quality |

No |

Yes |

Sets the visual quality of the shadow. Lower quality uses less computing and memory resources. |

ShadowEffect2D.ShadowOnly |

Shadow Only |

No |

Yes |

Whether to render only the shadow without the node contents. |

ShadowEffect2D.Type |

Shadow Type |

No |

Yes |

Sets the type of the shadow: * **Drop Shadow** appears behind or below objects. * **Inner Shadow** appears inside objects. |

ShowMaterialDebugObjects |

Show Material Debug Objects |

No |

Yes |

When enabled, Kanzi Studio does not hide material debug objects. |

SliderConcept.MaxDistanceFromCurve |

Maximum Distance From Curve |

No |

Yes |

The distance from the curve where hit testing succeeds. |

SpecularAntiAliasingStrength |

Specular Anti-Aliasing Strength |

No |

Yes |

Sets the strength of the specular anti-aliasing effect. Higher value results in blurrier specular highlights. For no specular anti-aliasing, set the value to 0. For full specular anti-aliasing, set the value to 1. The default value is 0.25. |

SpecularAntiAliasingThreshold |

Specular Anti-Aliasing Threshold |

No |

Yes |

Sets the upper limit for the amount of specular anti-aliasing effect to apply. The default value is 0.18. |

SpecularColor |

Specular Color |

No |

Yes |

Sets the color of the specular reflection. |

SpecularExponent |

Specular Exponent |

No |

Yes |

Sets the size of the specular highlight. |

SpecularFactor |

Specular Color Factor |

No |

Yes |

Sets the specular color for the material. |

SpecularTexture |

Specular Color Texture |

No |

Yes |

Sets the texture that contains the specular color for the material. Use the Specular Color Factor property to filter the value from this texture. |

SpotLight |

Spot Light |

No |

Yes |

Spot light settings |

SpotLightAttenuation |

Spot Light Attenuation |

No |

Yes |

Sets the effect that this Spot Light has on nodes that are farther away. Distance of light from the lighted surface is input in a quadratic function, the 3 components are the constant, linear and quadratic coefficients for the distance variable. |

SpotLightColor |

Spot Light Color |

No |

Yes |

Sets the color of the Spot Light. Use the Intensity (I) property field to adjust the brightness of the light. |

SpotLightCutoffAngle |

Cutoff |

No |

Yes |

Sets the angle of the light cone in degrees. |

SpotLightExponent |

Exponent |

No |

Yes |

Defines how fast a fully lit area at the center of the light cone turns into an unlit area. |

SpotLightInnerAngle |

Inner Angle |

No |

Yes |

Sets the inner angle of the light cone in degrees. |

SpotLightRadius |

Spot Light Radius |

No |

Yes |

Sets the distance at which the intensity of the Spot Light reaches zero. For infinite distance, set the property value to 0. |

SpotLightViewProjection |

Spot Light View Projection |

No |

Yes |

The premultiplied projection view matrix of a spot light. |

SpotShadowBias |

Spot Shadow Bias |

No |

Yes |

Sets the spot shadow bias to reduce sampling artifacts. |

SpotShadowMap |

Spot Shadow Map |

No |

Yes |

Depth map used to calculate spot shadows. |

SpotShadowSoftness |

Spot Shadow Softness |

No |

Yes |

Sets the softness of the shadows cast by the Spot Light. |

StackLayoutConcept.Direction |

Direction |

No |

Yes |

Defines the axis along which the stack layout arranges its items. |

StackLayoutConcept.Reversed |

Reversed |

No |

Yes |

Defines whether the stack layout arranges its items in reverse order. |

StateGroupInitialState |

Initial State |

No |

Yes |

Allows to define a startup state for a group, if there is no controller property defined. |

Tags |

Tags |

No |

Yes |

List of tags attached to the item |

TextBlock3D.Baseline |

Baseline |

No |

Yes |

Font baseline in 3D space units. |

TextBlock3D.TwoPassRendering |

Two Pass Rendering |

No |

Yes |

Defines whether the Text Block 3D is rendered in two passes. Disabling the two pass rendering improves performance, but can cause invalid rendering results when glyph bounds overlap. |

TextBlockConcept.WordWrap |

Word Wrap |

No |

Yes |

Sets whether to break long lines into multiple lines to make the text fit within the boundaries of the Text Block node. |

TextBox3D.CompositionBackgroundColor |

Composition Background Color |

No |

Yes |

Sets the color that highlights the text that the user composes using an input method editor (IME). |

TextBox3D.CompositionFontColor |

Composition Font Color |

No |

Yes |

Sets the color of the text that the user composes using an input method editor (IME). |

TextBox3D.SelectionBackgroundColor |

Selection Background Color |

No |

Yes |

Sets the color that highlights the selected text. |

TextBox3D.SelectionFontColor |

Selection Font Color |

No |

Yes |

Sets the color of the selected text. |

TextBoxConcept.CompositionText |

Composition Text |

No |

Yes |

Reports the text that the user composes in the Text Box using an input method editor (IME). |

TextBoxConcept.CompositionTextBackgroundBrush |

Composition Text Background Brush |

No |

Yes |

Sets the brush that highlights the text that the user composes using an input method editor (IME). |

TextBoxConcept.CompositionTextForegroundBrush |

Composition Text Foreground Brush |

No |

Yes |

Sets the brush for the text that the user composes using an input method editor (IME). |

TextBoxConcept.CursorPosition |

Cursor Position |

No |

Yes |

Sets the position of the cursor in the text shown in the Text Box node. |

TextBoxConcept.CursorPositionMessageArguments.CursorPosition |

Current Position |

No |

No |

Contains the current position of the cursor. |

TextBoxConcept.CursorPrefab |

Cursor Prefab |

No |

Yes |

Sets the prefab template that defines the appearance of the cursor instead of the default cursor. |

TextBoxConcept.DisplayText |

Display Text |

No |

Yes |

Reports the text that the Text Box displays. |

TextBoxConcept.EchoMode |

Echo Mode |

No |

Yes |

Sets how the Text Box node shows text: * **Normal** makes the inserted characters visible. * **No Echo** makes the inserted characters invisible. * **Password** makes the inserted character visible for a certain amount of time and then masks the character. Use the **Password Masking Character** property to set the masking character. The default is a bullet symbol. Use the **Password Echo Timeout** property to set the time in milliseconds that an inserted character is visible before masking. |

TextBoxConcept.EditMode |

Edit Mode |

No |

Yes |

Sets how the Text Box node enters the editing state: * **Automatic** makes the Text Box enter the editing state when focused, and leave the editing state when focus is lost. * **Triggered** requires the user to trigger the Text Box to enter and leave the editing state. |

TextBoxConcept.HasSelection |

Has Selection |

No |

Yes |

Indicates whether any of the text in the Text Box node is selected. |

TextBoxConcept.HideTextHintWhenEditing |

Hide Text Hint When Editing |

No |

Yes |

Sets whether to hide the placeholder content, which you set using the **Text Hint Prefab** property, when the Text Box node is in the editing state. To hide the placeholder content only when the user enters text in the Text Box node, disable this property. |

TextBoxConcept.InputMethodAction |

Input Method Action |

No |

Yes |

Sets the label of the user action button on the on-screen keyboard for this Text Box. By default uses the label of the default input method of the operating system. |

TextBoxConcept.InputType |

Input Type |

No |

Yes |

Sets the input type of the input methods that provide the input layout to let the user enter and edit text of specific type in the Text Box node: * **Default** for the default input type of the input method editor * **Numeric** for numbers * **Email** for email addresses * **URL** for URL addresses |

TextBoxConcept.IsComposingText |

Is Composing Text |

No |

Yes |

Reports the text composition state of the Text Box node. |

TextBoxConcept.IsEditing |

Is Editing |

No |

Yes |

Reports the editing state of the Text Box node. |

TextBoxConcept.MaximumTextLength |

Maximum Text Length |

No |

Yes |

Sets the maximum length of text that the user can insert in the Text Box node. The unit is a UTF-8 character and the buffer byte length can be greater for multi-byte characters. |

TextBoxConcept.PasswordEchoTimeout |

Password Echo Timeout |

No |

Yes |

When the **Echo Mode** property is set to **Password**, this property sets the time in milliseconds that an inserted character is visible before being masked. |

TextBoxConcept.PasswordMaskingCharacter |

Password Masking Character |

No |

Yes |

When the **Echo Mode** property is set to **Password**, this property sets the character that masks each character that the application user enters. |

TextBoxConcept.ReadOnly |

Read Only |

No |

Yes |

Sets whether the Text Box node is editable. When you enable this property, you can set the text only through the **Text** property and the user cannot edit the text in the Text Box node. |

TextBoxConcept.SelectedTextMessageArguments.SelectionEnd |

Selection End |

No |

No |

Contains the end index of the selection. |

TextBoxConcept.SelectedTextMessageArguments.SelectionStart |

Selection Start |

No |

No |

Contains the index of the character in the beginning of the text selection. |

TextBoxConcept.SelectionBackgroundBrush |

Selection Background Brush |

No |

Yes |

Sets the brush that highlights the selected text. |

TextBoxConcept.SelectionEndCursorPosition |

Selection End Cursor Position |

No |

Yes |

The position of the cursor that marks the end of text selection in the Text Box node. |

TextBoxConcept.SelectionEndPrefab |

Selection End Prefab |

No |

Yes |

Sets the prefab template that defines the appearance of the selection handle at the end of text selection instead of the default handle. |

TextBoxConcept.SelectionForegroundBrush |

Selection Foreground Brush |

No |

Yes |

Sets the brush for the selected text. |

TextBoxConcept.SelectionStartCursorPosition |

Selection Start Cursor Position |

No |

Yes |

The position of the cursor that marks the beginning of text selection in the Text Box node. |

TextBoxConcept.SelectionStartPrefab |

Selection Start Prefab |

No |

Yes |

Sets the prefab template that defines the appearance of the selection handle at the beginning of text selection instead of the default handle. |

TextBoxConcept.TextContentMessageArguments.TextFieldContent |

Text |

No |

No |

Contains the content of a Text Box node. |

TextBoxConcept.TextHintPrefab |

Text Hint Prefab |

No |

Yes |

Sets the prefab template for showing placeholder content when the Text Box node is empty. |

TextBoxConcept.TextInsertionMessageArguments.Position |

Position |

No |

No |

The character index at which to insert text. |

TextBoxConcept.TextInsertionMessageArguments.Text |

Text |

No |

No |

Sets the text to insert in the Text Box node. |

TextBoxConcept.TextKeyNavigationDirection |

Text Key Navigation Direction |

No |

Yes |

Sets the text key navigation direction. |

TextBoxConcept.TextRangeMessageArguments.EndPosition |

End Position |

No |

No |

Sets the index of the last character in the text range. |

TextBoxConcept.TextRangeMessageArguments.StartPosition |

Start Position |

No |

No |

Sets the index of the first character in the text range. |

TextConcept.ColorFontMaterial |

Color Font Material |

No |

Yes |

Sets the material whose shader is used to render the text containing colored glyphs. The shader must use the ContentTexture uniform which is automatically filled with glyph data. |

TextConcept.FontColor |

Font Color |

No |

Yes |

Sets the color of the text in a 3D text node. |

TextConcept.FontMaterial |

Font Material |

No |

Yes |

Sets the material whose shader is used to render the text. The shader must use the ContentTexture uniform which is automatically filled with glyph data. |

TextConcept.HorizontalFit |

Horizontal Fit |

No |

Yes |

Whether to horizontally scale the glyphs to make them fit into the **Layout Width** of the Text Block. To adjust the scale, use the **Horizontal Fit Scale Limits** property. |

TextConcept.HorizontalFitScaleLimits |

Horizontal Fit Scale Limits |

No |

Yes |

When the **Horizontal Fit** property is enabled, sets the minimum and maximum scale for glyphs when the width of text in a Text Block does not match the **Layout Width** of that Text Block. For example: * **Min** property field set to 1.0 does not squeeze the glyphs, while 0.5 squeezes the glyphs to half their size. * **Max** property field set to 1.0 does not stretch the glyphs, while 2.0 stretches the glyphs to double their size. |

TextConcept.HorizontalPadding |

Horizontal Padding |

No |

Yes |

Sets the padding spaces between the content and the left and right boundaries of the Text node. |

TextConcept.Overflow |

Overflow |

No |

Yes |

Sets the characters that represent the truncated text when the text does not fit in this node. The default value is ââ¦â. By default, Kanzi truncates the text at the end. Use the **Truncation Direction** property to set the part of the text that you want to truncate.

Kanzi truncates text to fit within the vertical and horizontal limits of the control. If there is not enough vertical space to fit a single line of text, Kanzi truncates all text and does not show the **Overflow** characters.  |

TextConcept.RemoveSideBearings |

Remove Side Bearings |

No |

Yes |

Whether to position the leftmost characters of left-aligned text and rightmost characters of right-aligned text exactly within the boundary of the text node. |

TextConcept.Text |

Text |

No |

Yes |

Sets the text content that the text node renders. To create a line break press Shift+Enter. |

TextConcept.TextHorizontalAlignment |

Text Horizontal Alignment |

No |

Yes |

Sets the horizontal alignment of the text. |

TextConcept.TextVerticalAlignment |

Text Vertical Alignment |

No |

Yes |

Sets the vertical alignment of the text. |

TextConcept.Truncation |

Truncation |

No |

Yes |

Sets how Kanzi truncates text when either **Truncation** or **Overflow** property is set and the text does not fit in this node: * **None** disables text truncation. * **At character** truncates text character by character. Default value. * **At word** truncates text by entire words.

Kanzi truncates text to fit within the vertical and horizontal limits of the control. If there is not enough vertical space to fit a single line of text, Kanzi truncates all text and does not show overflow characters.  |

TextConcept.TruncationDirection |

Truncation Direction |

No |

Yes |

Sets which part Kanzi truncates when either the **Truncation** or **Overflow** property is set and the text does not fit in this node: * **Trailing** truncates single- and multiline text at the end. Default value. * **Center** truncates single-line text in the middle. For multiline text, truncates entire lines from the middle, if the text does not fit in the height of this node, and clips text that does not fit in the width of this node. * **Leading** truncates single-line text in the beginning. For multiline text, truncates entire lines from the beginning, if the text does not fit in the height of this node, and clips text that does not fit in the width of this node. |

TextConcept.VerticalPadding |

Vertical Padding |

No |

Yes |

Sets the padding spaces between the content and the top and bottom boundaries of the Text node. |

Texture |

Texture |

No |

Yes |

Sets the texture of the material. |

TextureBrush.RenderTexture |

Brush Texture |

No |

Yes |

Texture for brush. |

TextureNativeDeploymentTarget |

Native Deployment Target |

No |

Yes |

Sets the memory in which to store this texture on your target device. |

TextureOffset |

Texture Offset |

No |

Yes |

Sets an offset for texture in materials. |

TextureTiling |

Texture Tiling |

No |

Yes |

Determines the number of times a texture is presented in a material. |

TimerTrigger.Interval |

Timer Interval (ms) |

No |

No |

The interval in milliseconds on which the trigger is triggered. |

ToggleButtonGroupConcept.CurrentButtonIndex |

Current Button Index |

No |

Yes |

The index of the Toggle Button that is toggled on in the Toggle Button Group. To update this property with a binding, use a to-source or two-way binding. |

Tonemap.A |

A |

No |

Yes |

Tonemapping parameter A. |

Tonemap.B |

B |

No |

Yes |

Tonemapping parameter B. |

Tonemap.C |

C |

No |

Yes |

Tonemapping parameter C. |

Tonemap.D |

D |

No |

Yes |

Tonemapping parameter D. |

Tonemap.E |

E |

No |

Yes |

Tonemapping parameter E. |

Tonemap.F |

F |

No |

Yes |

Tonemapping parameter F. |

Tonemap.WhiteScale |

White Scale |

No |

Yes |

Sets the value that will be tonemapped to pure white. |

ToneMapLinearScale |

Tone Map Linear Scale |

No |

Yes |

Sets the scale for the linear tonemap option for the material. When linear tonemapping is used, Kanzi divides all output color by the value of this property. |

TrajectoryLayoutConcept.AlignToTangent |

Align To Tangent |

No |

Yes |

Whether to align the items in this Trajectory Layout to match the tangent of the trajectory. Vertical trajectories are not supported. |

TrajectoryLayoutConcept.CalculatedOffset |

Calculated Offset |

No |

Yes |

Reports the current offset of an item in a Trajectory Layout in the proportional range [0, 1]. |

TrajectoryLayoutConcept.ItemAreaBegin |

Item Area Begin |

No |

Yes |

Sets the starting point of the trajectory segment in which the items in this Trajectory Layout are considered fully visible. The value is in the range [0, 1], where 0 is the beginning and 1 is the end of the trajectory. The Node > Visible Amount in Parent property uses this value. |

TrajectoryLayoutConcept.ItemAreaEnd |

Item Area End |

No |

Yes |

Sets the ending point of the trajectory segment in which the items in this Trajectory Layout are considered fully visible. The value is in the range [0, 1], where 0 is the beginning and 1 is the end of the trajectory. The Node > Visible Amount in Parent property uses this value. |

TrajectoryLayoutConcept.OverrideDistance |

Override Distance |

No |

Yes |

Sets the distance between the items in this Trajectory Layout. When you do not set this property, the Trajectory Layout calculates the distance automatically. |

TrajectoryLayoutConcept.OverrideOffset |

Trajectory Override Offset |

No |

Yes |

Sets the offset of an item in a Trajectory Layout. When you do not set this property, the Trajectory Layout sets the offset. |

TrajectoryLayoutConcept.StartOffset |

Start Offset |

No |

Yes |

Sets the offset of the starting position of the items on the trajectory in the range [0, 1], where 0 is the beginning and 1 is the end of the trajectory. |

TrajectoryLayoutConcept.Stretch |

Stretch |

No |

Yes |

Whether to scale this Trajectory Layout to match the layout size. |

TrajectoryLayoutConcept.Trajectory |

Trajectory |

No |

Yes |

Sets the Trajectory along which this Trajectory Layout node arranges its items. |

TrajectoryListBox.AllowedScrollAxis |

Allowed Scroll Axis |

No |

Yes |

Sets the axis on which you want to allow this Trajectory List Box 3D node to scroll. |

TrajectoryListBox.Looping |

Looping |

No |

Yes |

Whether to show items in the Trajectory List Box 3D from the beginning after reaching the last item. |

TrajectoryListBox.ReversedScrolling |

Reversed Scrolling |

No |

Yes |

Whether the scroll position in the Trajectory List Box node increases in relation to the direction of the pan gesture. This reverses the direction of scrolling. By default, the scroll position decreases in relation to the pan direction, which makes the list items move toward the direction of the trajectory. |

TrajectoryListBoxConcept.AlignToTangent |

Align To Tangent |

No |

Yes |

Whether to align the Trajectory List Box 3D items to match the tangent of the trajectory. |

TrajectoryListBoxConcept.CursorOffset |

Cursor Offset |

No |

Yes |

Sets the offset of the position to use to select the active item, in proportional range [0,1]. |

TrajectoryListBoxConcept.ItemAreaBegin |

Item Area Begin |

No |

Yes |

Sets the proportional offset where the part of the trajectory meant for the fully visible Trajectory List Box 3D items starts. Kanzi uses the values of the Item Area Begin and Item Area End properties to calculate the value of the Node.VisibleAmountInParent property for each list item.You can use the VisibleAmountInParent property in shaders to fade out those list items that are not fully visible. |

TrajectoryListBoxConcept.ItemAreaEnd |

Item Area End |

No |

Yes |

Sets the proportional offset where the part of the trajectory meant for the fully visible Trajectory List Box 3D items ends. Kanzi uses the values of the Item Area Begin and Item Area End properties to calculate the value of the Node.VisibleAmountInParent property for each list item.You can use the VisibleAmountInParent property in shaders to fade out those list items that are not fully visible. |

TrajectoryListBoxConcept.ScrollPosition |

Scroll Position |

No |

Yes |

Sets the scroll position of the Trajectory List Box 3D along the x and y axes as a relative position within the list box area. Use this property to move the list to a scroll position immediately, without scrolling. To update the scroll position with a binding, use a two-way or to-source binding. |

TrajectoryListBoxConcept.Spacing |

Spacing |

No |

Yes |

Sets the distance between the items in the Trajectory List Box 3D. |

TrajectoryListBoxConcept.Trajectory |

Trajectory |

No |

Yes |

Sets the trajectory along which the Trajectory List Box 3D arranges its items. |

TrajectoryListBoxDraggingAccelerationCoefficient |

Dragging Acceleration |

No |

Yes |

Sets the acceleration of the Trajectory List Box 3D when the user scrolls the Trajectory List Box 3D by dragging the pointer. The higher the value, the quicker the Trajectory List Box 3D reaches its final position. The default value is 80. |

TrajectoryListBoxDraggingDragCoefficient |

Dragging Drag |

No |

Yes |

Sets the amount that drag affects the movement of the Trajectory List Box 3D when the user scrolls the Trajectory List Box 3D by dragging the pointer. The lower the value, the higher the drag and the quicker the scrolling stops. The default value is 150. |

TrajectoryListBoxDraggingImpulseFactor |

Dragging Impulse |

No |

Yes |

Sets the amount of impulse to generate from the pointer movement when the user scrolls the Trajectory List Box 3D by dragging the pointer. |

TrajectoryListBoxMaximumNumberOfTouches |

Maximum Number of Touches |

No |

Yes |

Sets the maximum number of touch points allowed on the Trajectory List Box 3D area for scrolling. |

TrajectoryListBoxMinimumNumberOfTouches |

Minimum Number of Touches |

No |

Yes |

Sets the minimum number of touch points required on the Trajectory List Box 3D area for scrolling. |

TrajectoryListBoxRecognitionThreshold |

Recognition Threshold |

No |

Yes |

Sets the distance in pixels that the pointer has to move for the scrolling to start in the Trajectory List Box 3D. |

TrajectoryListBoxSensitivity |

Scroll Sensitivity |

No |

Yes |

Sets the amount that the scroll value changes relative to the movement of the pointer on the scroll view plane of the Trajectory List Box 3D. The default value 1 makes the Trajectory List Box 3D scroll the same amount as the user drags the pointer. For example, to set the Trajectory List Box 3D to scroll twice the amount that the user drags the pointer, set the value of the property to 2. |

TrajectoryListBoxSlidingAccelerationCoefficient |

Sliding Acceleration |

No |

Yes |

Sets the acceleration of the Trajectory List Box 3D after the user releases the pointer with which they scroll the Trajectory List Box 3D. The higher the value, the quicker the Trajectory List Box 3D reaches the scroll target. The default value is 40. |

TrajectoryListBoxSlidingDragCoefficient |

Sliding Drag |

No |

Yes |

Sets how much drag affects the movement of the Trajectory List Box 3D after the user releases the pointer with which they scroll the Trajectory List Box 3D. The lower the value, the higher the drag and the quicker the scrolling of the Trajectory List Box 3D stops. The default value is 80. |

TrajectoryListBoxSwipeDistance |

Swipe Distance |

No |

Yes |

Sets the distance that a swipe sends the scroll value in the Trajectory List Box 3D, relative to the speed of the pointer. |

TriggerActionItem.ForwardedMessageArguments |

Forwarded Arguments |

No |

Yes |

The arguments of the message to forward |

TrySetFocusAction.TargetItem |

Target Item |

No |

No |

Target item to be focused |

UVToViewA |

Ambient Occlusion UV to View A |

No |

Yes |

HBAO input property for UVToViewA uniform. |

UVToViewB |

Ambient Occlusion UV to View B |

No |

Yes |

HBAO input property for UVToViewB uniform. |

ValueAccumulator.Autoplay |

Autoplay |

No |

Yes |

Sets whether the Value Accumulator starts automatically when it is attached to the node. |

ValueAccumulator.BoundType |

Bound Type |

No |

Yes |

Sets how the Value Accumulator limits the total accumulated value between the minimum and maximum value boundaries. |

ValueAccumulator.IncrementMode |

Increment Mode |

No |

Yes |

Sets how the Value Accumulator increments the accumulated value.: * Time Based increments at fixed time intervals. This is the default. * Per Frame increments once every frame, ignoring time. |

ValueAccumulator.IncrementTimeInterval |

Increment Time Interval |

No |

Yes |

Sets the frequency of increments in milliseconds. This property is only used when Increment Mode is set to Time Based. |

ValueControlledExclusiveActivityHostConcept.ControllerProperty |

Controller Property |

No |

Yes |

Sets the property type that the Exclusive Activity Host node uses to switch between its child Activity nodes. |

ValueControlledExclusiveActivityHostConcept.DataSourceControllerPropertyPath |

Data Source Controller Property Path |

No |

Yes |

Sets the path in the Data Source object of an Exclusive Activity Host node to a Data Object item that the Exclusive Activity Host node uses as the Controller Property. |

Viewport2D.Camera |

Camera |

No |

Yes |

Sets which camera to use in scenes rendered by the selected Viewport 2D. If not set, Kanzi uses the camera in the scene. |

Viewport2D.HitTestCamera |

Hit Test Camera |

No |

Yes |

Sets which hit test camera to use in scenes rendered by the selected Viewport 2D. If not set, Kanzi uses the camera in the scene. |

Viewport2D.RenderPass |

Render Pass |

No |

Yes |

The RenderPass used for rendering the Scene for the Viewport. Instantiated from the RenderPassPrefab. Set internally by Kanzi whenever RenderPassPrefabProperty changes. |

Viewport2D.RenderPassPrefab |

Render Pass Prefab |

No |

Yes |

Sets which render pass prefab will be used to instantiate the render pass tree. |

Viewport3D.OverrideMaterial |

Override Material |

No |

Yes |

Sets the override material to use to render the content of the 2D prefab in the Viewport 3D node. In the Viewport 3D node, bind a texture property of the override material to the Viewport3D.PrefabTexture property. |

Viewport3D.Prefab |

Prefab Template |

No |

Yes |

Sets the 2D prefab whose content the Viewport 3D node renders in 3D space. |

Viewport3D.PrefabTexture |

Prefab Texture |

No |

Yes |

The read-only texture to which the Viewport 3D renders the content of the 2D prefab. When you set the Override Material property, you must bind a texture property of that material to this property. |

Vignette.InnerDistance |

Inner Distance |

No |

Yes |

Sets the distnace range where the vignette color transition starts. |

Vignette.OuterColor |

Outer Color |

No |

Yes |

Sets the vignette color. |

Vignette.OuterDistance |

Outer Distance |

No |

Yes |

Sets the distnace range where the vignette color transition ends. |

Window.MetricsType |

Metrics Type |

No |

No |

Defines the type of the coordinate system for the window metrics. |

Window.Orientation |

Orientation |

No |

No |

Sets the orientation of the application window. |

WriteLogAction.LogText |

Log Text |

No |

No |

The text to write to the Kanzi Studio Log window when a trigger executes this action. |
