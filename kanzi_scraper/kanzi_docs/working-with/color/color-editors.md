---
title: Color editors in Kanzi Studio
source: https://docs.kanzi.com/4.1.0/en/working-with/color/color-editors.html
---

# Color editors in Kanzi Studio


Use the color editors to set the values of color properties in Kanzi Studio.
## Color editor


The color editor has these modes:

- HSLA color:

  - H property field sets the hue of the color.
  - S property field sets the saturation of the color.
  - L property field sets the lightness of the color.
  - A property field sets the alpha of the color.


This is the default color editor mode in Kanzi Studio.

The color editor defines the values of the HSLA channels in the range from 0 to 255.
- RGBA color:

  - R property field sets the red color channel.
  - G property field sets the green color channel.
  - B property field sets the blue color channel.
  - A property field sets the alpha channel.


To use this mode, below the color swatch, click To RGB.

The color editor defines the values of the RGBA channels in the range from 0 to 255.


In bindings, create color values using the `Color4()` constant, which defines the RGBA values in the range from 0 to 1. See Color4.

> **Tip:** You can use bindings to convert between the HSL and sRGB color spaces. See hslToSrgb and srgbToHsl.
## HDR color editor


Use the HDR color editor to set:

- The color of lights. See Using the light nodes.
- Ambient and emissive color properties, such as Ambient Color or Emissive Factor.


The HDR color editor works like the Color editor, but has an additional I property field that enables you to set the intensity of the color.

Color intensity in Kanzi works like exposure in photography:

- Increase of intensity by one unit doubles the exposure.
- Decrease of intensity by one unit halves the exposure.


For example, when you change the intensity:

- From 0 to +2, you quadruple the color brightness.
- From 0 to -3, you decrease the color brightness to 1/8.

## Applying color in hexadecimal format


In the Kanzi Studio color editors, to apply a color in hexadecimal format, set the # field to `RRGGBBAA`, where:

- `RR` sets the red color channel.
- `GG` sets the green color channel.
- `BB` sets the blue color channel.
- (Optional) `AA` sets the alpha channel.


The hexadecimal field defines the values of the RGBA channels in the range from 00 to ff.
