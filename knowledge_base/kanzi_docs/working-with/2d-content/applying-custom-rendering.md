---
title: Applying custom rendering to 2D nodes
source: https://docs.kanzi.com/4.1.0/en/working-with/2d-content/applying-custom-rendering.html
---

# Applying custom rendering to 2D nodes

Apply custom rendering to 2D nodes to create post-processing effects.

For example, you can convert color images in a 2D node to grayscale.

To apply custom rendering to a 2D node, use the Composition Brush property to compose the node on the screen with a Material Brush, and enable the Force Composition property.

To apply custom rendering to a 2D node:

1.

Create a material with which you want to apply custom rendering.

For example, to create a material that converts color to grayscale:

  1.

In the Library, press Alt and right-click Materials and Textures and select Material Type. Kanzi Studio creates a material type and a material that uses the material type.
  2.

In the Library > Materials and Textures > Material Types, expand the material type that you created. Double-click the Vertex Shader to open it in the Shader Source Editor, replace the existing shader code with this code, and save the shader.

```
#version 310 es

in vec3 kzPosition;
in vec2 kzTextureCoordinate0;
uniform highp mat4 kzProjectionCameraWorldMatrix;

out mediump vec2 vTexCoord;

void main()
{
    precision mediump float;
    vTexCoord = kzTextureCoordinate0;
    gl_Position = kzProjectionCameraWorldMatrix * vec4(kzPosition.xyz, 1.0);
}

```

  3.

Open the Fragment Shader, replace the existing shader code with the code in this step, and save the shader.

In the shader, use these Kanzi default uniforms:

    - `ContentTexture` to define the texture that the rendered node provides when rendering
    - `RenderOpacity` to define the opacity of the rendered node

See Shader uniforms.

```
#version 310 es

uniform sampler2D ContentTexture;
in mediump vec2 vTexCoord;
uniform lowp float RenderOpacity;
layout(location = 0) out vec4 fragColor;

void main()
{
    precision mediump float;
    // Use this algorithm to convert the colors in the texture used by
    // the 2D node to grayscale.
    // To integrate to the Kanzi rendering pipeline, the shader must output
    // premultiplied alpha.
    vec4 color = texture(ContentTexture, vTexCoord);
    float grayscale = dot(color.rgb, vec3(0.21, 0.72, 0.07));
    float alpha = color.a * RenderOpacity;
    vec3 premultipliedColor = vec3(grayscale) * alpha;
    fragColor = vec4(premultipliedColor, alpha);
}

```

2.

In the Library, press Alt and right-click Materials and Textures and select Material Brush. In the Properties, set the Material property to the material that you created in the previous step.
3.

In the Node Tree, create or select a 2D node to which you want to apply the material that you created. For example, create a Stack Layout 2D node. In the Stack Layout 2D node, create an Image node.
4.

In the Properties, add and set:

  - Brush Composition Brush to the material brush that uses the material you want to apply to that node
  - Node 2D > Force Composition to enabled
  - (Optional) Render Target > Multisample Level to the number of anti-aliasing samples that you want to apply to the content
  - (Optional) Node > Opacity to control the translucency of the node
