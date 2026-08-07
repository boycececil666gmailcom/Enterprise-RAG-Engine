---
title: Using the Shadow Effect 2D effect
source: https://docs.kanzi.com/4.1.0/en/working-with/effects/shadow-effect-2d.html
---

# Using the Shadow Effect 2D effect

Use the Shadow Effect 2D effect to apply a shadow to the content of a 2D node.
## Creating a shadow effect for a 2D node

To create a shadow effect for a 2D node:

1.

In the Library press Alt and right-click Effects and select Shadow Effect 2D.
2.

In the Node Tree or Prefabs create a 2D node to which you want to apply the shadow effect.
3.

From the Library > Effects > 2D Effects drag the Shadow Effect 2D effect to the Node Tree or Prefabs and drop it on the 2D node to which you want to apply the shadow effect.

This way you set in that 2D node the Effect Prefab property to the Shadow Effect 2D effect.

Kanzi applies to the visual shape of the content in the 2D node a partially transparent black drop shadow directed at a 45-degree angle relative to the positive x axis.
4.

To adjust the appearance of the shadow, in the Library select the Shadow Effect 2D effect and in the Properties add and set the Shadow Effect 2D properties.

Shadow Blend Mode sets the blend mode that Kanzi uses to render the shadow.

The default is Alpha: Premultiplied.

For example, use the Multiply (advanced khr) blend mode to create a more realistic shadow.

See Blending and compositing 2D nodes.  |

Shadow Blur Radius sets the softness of the shadow by defining the distance in pixels that the shadow blur extends outward from each edge of the shadow. The higher the value, the blurrier the shadow is. The default radius is 8 pixels.  |    |

Shadow Type sets the type of the shadow:

  - Drop Shadow appears behind or below an object. This is the default.
  - Inner Shadow appears inside an object.

Shadow Distance sets how far from an object the shadow falls. The default distance is 10 pixels.  |    |

Shadow Angle sets the direction of the shadow as an angle relative to the positive x axis in the clockwise direction. The default angle is 45 degrees.  |    |

Override Shadow Offset sets the offset of the shadow from the object along the x and y axes. The default offset is 7 pixels along both axes.

When you set this property, the Shadow Distance and Shadow Angle properties have no effect.  |    |

Shadow Color sets the color of the shadow.  |    |

Shadow Only sets whether to render only the shadow without the visual content of the node.  |    |

Shadow Quality sets the visual quality of the shadow. Lower quality uses less computing and memory resources.  |    |

## Customizing an instance of a shadow effect

When you edit the properties of an effect in the Library > Effects, you change the appearance of that effect for all nodes that use it. You can customize each effect instance by overriding the effect property values. For example:

- When you create a Shadow Effect 2D effect, you can vary the softness of the shadow in different instances of that effect.
- When you create a Mask Effect 2D effect, you can vary the size of the mask in different instances of that effect.
- When you create a Blur Effect 2D effect, you can vary the amount of blur in different instances of that effect.
- When you create an Outline Effect 2D effect, you can vary the color of the outline in different instances of that effect.

To customize an instance of an effect:

1.

Create an effect and set a node to use it.

For example, create a Shadow Effect 2D effect and set an Image node to use it. See Creating a shadow effect for a 2D node.
2.

Customize a property in the effect:

  1.

In the Library, select the effect that you created. In the Properties, next to the property that you want to customize, click .

Kanzi Studio creates from that property a custom property, adds it to the root of the effect prefab, and creates a `##Template` binding to the property in the 2D effect.

For example, click  next to Shadow Blur Radius property. Kanzi Studio creates a custom Shadow Blur Radius property, adds it to the root effect prefab, and creates in the Shadow Effect 2D effect prefab a `##Template` binding to the custom Shadow Blur Radius property.
  2.

In the Node Tree or Prefabs, select the 2D node that uses the effect that you created. In the Properties, click  next to the property that you customized and set the value of the property.

Kanzi Studio adds to the 2D node a To Source binding which pushes the value of that property to the effect instance made available through the `Node2D.Effect` property of the node.

You can set multiple 2D nodes to use the same effect and in each 2D node, you can add and set the property to have different values.

For example, in the Properties, add the Shadow Effect 2D Properties > ShadowEffect2D.BlurRadius property and use it to adjust the softness of the shadow only in the Image node.

3.

(Optional) Repeat the previous step for each effect property that you want to customize.
**Tip:** When you want to remove from a node a property and its To Source binding, right-click that property and select Remove Property And Binding.

## Using the Shadow Effect 2D effect in the API

To create a shadow effect:

```
// Create an effect template.
NodeEffectTemplate2DSharedPtr shadowEffectTemplate =
    NodeEffectTemplate2D::create(ShadowEffect2D::getStaticMetaclass()->getName(), "DropShadow");

// Set the value of the AngleProperty in the template. This value serves as the default value
// of the property in instances of the effect prefab.
shadowEffectTemplate->addPropertyValue(ShadowEffect2D::AngleProperty, Variant(35.f));

// Create an effect prefab.
NodeEffectPrefab2DSharedPtr shadowEffectPrefab =
    NodeEffectPrefab2D::create(getDomain(), "DropShadow prefab", shadowEffectTemplate);

// Assign the effect to a 2D node.
node2d->setEffectPrefab(shadowEffectPrefab);

// Get the node-specific effect instance created from the assigned prefab.
ShadowEffect2DSharedPtr shadowEffect = dynamic_pointer_cast<ShadowEffect2D>(node2d->getEffect());

// Set the shadow distance to 15 pixels for this node only. This overrides
// the property default value defined by the ShadowEffect2D metaclass.
shadowEffect->setDistance(15.f);

// Set the direction of the shadow to 55 degrees relative to the positive x axis.
// This overrides the default value of 35 degrees set in the shadow effect template.
shadowEffect->setAngle(55.f);

```

For details, see the `ShadowEffect2D` class.
