---
title: Asset Toolkit
source: https://docs.kanzi.com/4.1.0/en/working-with/asset-toolkit/asset-toolkit.html
---

# Asset Toolkit

The Asset Toolkit contains easy, ready-made components and materials with a similar structure and set of properties, that you can use to create Kanzi applications faster.

Here you can find all the Asset Toolkit content:

- A high quality placeholder car model that you can use in your prototype application. See Car.
- Materials that you can apply to 3D content in your project. See Materials.
- Environment Textures that you can use to give perspective to your scene. See Environments.
- Flipbook and Transition Material types that you can use to present content in your application. See Material types.
- Interactive User Interface Components that you can use to receive user input. See Interactivity Control components.
- Radial UI Components that you can show progress in a circular arc. See Radial UI Components.
- Simple shapes to use in your application. See Simple Shape UI Components.
- Scrollable lists that can present collections of items. See Scroll list UI Components.
- Example components that shows ways to combine these assets into more complex, reusable components. See Examples.

To use the Asset Toolkit assets in your Kanzi Studio project, from the Asset Packages drag an asset to a node in the Node Tree, to the Prefabs, or to the Preview. See Using the Asset Toolkit assets.
## Car

Use the Car to add a car model into your scene.

To position the car, in the Preview use either the Node tool or the Camera tool. See Editing your application in the Preview and Using the Camera node.

To set the material for the different parts of the car, you can drag materials from the Assets window to the Car in the Preview window, or on the part of the car in the Node Tree. See Using the Asset Toolkit assets.
## Materials

The Asset Toolkit includes Physically Based Rendering (PBR) materials that you can apply to 3D content in your project.

PBR Carpaint-blue

PBR Carpaint-orange

PBR Chrome

PBR Glass

PBR Plastic

To learn about using materials from the Asset Toolkit in your Kanzi application, see Using Asset Toolkit materials in your project.
## Environments

The Asset Toolkit includes two environment textures which are also included in the car and PBR materials, but provided independently for use with your own materials or models.

- Use Environment Studio Irradiance to provide diffused ambient lighting to materials in your scene, as is done with glass and plastics in the assets.

Environment Studio Irradiance

- Use Environment Studio Specular to provide a sharp, smooth reflective surface to materials in your scene, as is done with metals and paint in the assets.

Environment Studio Specular

To use an environment texture in your project, from the Assets window right-click and import, and apply to your materials by setting it as the Ambient and/or Reflection texture in the material properties. Control its strength by adjusting the Factor slider.

To learn more about environment textures, see Using environment textures.
## Material types

The Asset Toolkit includes two Material Types that can be used to animate display of content in your application:

- The Flipbook Material Type allows you to use a texture atlas that contains multiple images arranged in a grid layout. Use it to selectively display images from that texture atlas, or to play out an animated sequence. This is useful for example, to set the state of navigation arrow in a cluster, or to animate a simple pedestrian figure walking.

Flipbook Material Type

To use the Flipbook Material Type in your project:

  - Right-click to import or drag it into your preview or node tree.
  - Apply it as a brush to 2D or 3D nodes in your scene.
  - In the Flipbook Material Type properties window, set the grid to correspond to the layout of the images in the texture atlas.
  - Set the static image to display by setting the Static Image Index property.
  - Play out an animated flipbook sequence by advancing the Time property value.

To learn about using tile atlases, see Using a tile atlas.
- The Transition Material Type allows you to transition between nodes in either a Fade, Sweep or Noise motion.

Transition Material Type

To use the Transition Material Type in your project:

  - Right-click to import or drag it into your preview or node tree.
  - Apply it as a brush to 2D or 3D nodes in your scene.
  - In the Transition Material Type properties window,

    - Set the Transition Type to apply to the transition.
    - Select textures between which to transition as the Transition Texture Start and Transition Texture End properties.

  - To apply a Fade transition, set the Transition type property to Fade.

    - Control the progression of the fade by advancing the Transition Progress property value.

  - To apply a Sweep transition, set the Transition type property to Sweep.

    - Control the smoothing intensity by setting the Transition Smoothing property
    - Set orientation of the sweep motion using the Transition Rotation property.

  - To apply a Noise transition, set the Transition type property to Noise.

    - Additionally, control the granularity of the noise by setting the Transition Noise Scale property.

## Interactivity Control components

Use the UI Components provided in the Asset Toolkit to receive user input, and provide an interactive user experience in your application.

The interactive UI components included in the Asset Toolkit all share a set of similar properties and behaviors, exposed and named the same way. This makes it easier to apply consistent styling, and to combine them in your project.

When you import a UI component, Kanzi Studio adds to your project Library and Prefabs, the required shaders and materials to render that component.

It uses the FillStrokeBrush material, applied as BackgroundBrush to all the UI components, to expose properties that control their appearance and behavior.

For example, to adjust the appearance and behavior of the Button, after you add the Button to your project, in the Properties set:

- UI - Appearance to set the Corner Radius value that adjust the roundness of the button corners.
- UI - Fill to set the Fill Color of the button background.
- UI - Fill Gradient to set the Fill Gradient Color of the button background and its Rotation.
- UI - Fill Texture to apply a texture to the button background and set how it should be applied.
- UI - Progress to apply a progress bar state across the background of the button.
- UI - Segments to divide the button background into segments, and set its number and weight.
- UI - Stroke to apply an outline to the button, and set its color and weight.

Use any combination of these properties to adjust the appearance of the UI components. Each are enabled individually by marking the property Active.

You can use bindings to control the UI - Progress property. See Using bindings.

To learn more about the interactivity controls, see Interactivity controls.
## Radial UI Components

Use the Radial UI Components provided in the Asset Toolkit display values to progress in a round control.

The Radial UI components included in the Asset Toolkit all share a set of similar properties and behaviors, exposed and named the same way.

When you import a UI component, Kanzi Studio adds to your project Library and Prefabs, the required shaders and materials to render that component.

It uses the FillStrokeRadialBrush material, applied as BackgroundBrush to all the UI components, to expose properties that control their appearance and behavior.

For example, to adjust the appearance and behavior of the Gauge Progress control, after you add it to your project, in the Properties set:

- UI - Appearance to set the angle at which to apply progress, its radial weight and cap shape.
- UI - Fill to set the Fill Color of the UI background.
- UI - Progress to apply progression state across the background of the dial, and its color.
- UI - Segments to divide the gauge into segments, and set its number and weight.
- UI - Stroke to apply an outline to the gauge, and set its color and weight.

Use any combination of these properties to adjust the appearance of the Radial UI components. Each are enabled individually by marking the property Active.

You can use bindings to control the UI - Progress property. See Using bindings.
## Simple Shape UI Components

Use the simple shape UI components provided in the Asset Toolkit to add basic shapes to your application without the need of a plugin.

- On the Box with Rounded Corners, set the Corner Radius property to square or round out the shape.
- On the Circle, set the UI - Fill property values to apply color.

## Scroll list UI Components

Use the scroll list UI components provided in the Asset Toolkit to add scrollable lists to your application in one of a four layout patterns.

- Use the Scroll List Vertical to present items two dimensionally in a vertical scrollable list.
- Use the Horizontal List Vertical to present items two dimensionally in a horizontally scrollable list.
- Use the Scroll Trajectory 3D Horizontal to present the items three dimensionally in on horizontal plane.
- Use the Scroll Trajectory 3D Arc to present the items three dimensionally in an arc.

To learn more about list, see List Box nodes.

To use a data source to display your own data in a list component, see Using a data source, and Tutorial: Get application data from a data source.
## Examples

Expand the Asset Toolkit to find a folder with example components that show possible ways to combine these assets into more complex, reusable components.

Explore these example components for practical ideas on assembling your own custom controls by combining them.
