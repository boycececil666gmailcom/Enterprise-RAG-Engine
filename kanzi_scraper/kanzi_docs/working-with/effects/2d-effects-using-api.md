---
title: Using effects in the Kanzi Engine API
source: https://docs.kanzi.com/4.1.0/en/working-with/effects/2d-effects-using-api.html
---

# Using effects in the Kanzi Engine API


You can use the Kanzi Engine API to create effects for 2D nodes.
## Assigning effects to nodes


To create an effect:

```
// An effect that is assigned to a 2D node is an effect prefab.
// Before you can construct an effect prefab, you must create an effect template.
// This example creates an effect template for the ShadowEffect2D effect prefab.
NodeEffectTemplate2DSharedPtr shadowEffectTemplate =
    NodeEffectTemplate2D::create(ShadowEffect2D::getStaticMetaclass()->getName(), "DropShadow");

// Create a node effect prefab from the effect template.
NodeEffectPrefab2DSharedPtr shadowEffectPrefab =
    NodeEffectPrefab2D::create(getDomain(), "DropShadow prefab", shadowEffectTemplate);

```


To set a 2D node to use an effect:

```
// To assign an effect prefab to a 2D node, set the Node2D::EffectPrefabProperty.
node2d->setProperty(Node2D::EffectPrefabProperty, shadowEffectPrefab);

```


```
// To assign an effect prefab to a 2D node, call the Node2D::setEffectPrefab method.
node2d->setEffectPrefab(shadowEffectPrefab);

```


To disable an effect:

```
// Enable an effect on a 2D node by assigning an effect prefab.
node2d->setEffectPrefab(shadowEffectPrefab);
// Disable an effect by assigning a nullptr or an empty shared pointer.
node2d->setEffectPrefab(nullptr);

```


To set multiple 2D nodes to use the same effect:

```
// Create an effect template.
NodeEffectTemplate2DSharedPtr shadowEffectTemplate =
    NodeEffectTemplate2D::create(ShadowEffect2D::getStaticMetaclass()->getName(), "DropShadow");

// Create an effect prefab from the effect template.
NodeEffectPrefab2DSharedPtr shadowEffectPrefab =
    NodeEffectPrefab2D::create(getDomain(), "DropShadow prefab", shadowEffectTemplate);

// Set two nodes to use the same effect prefab. The nodes create separate instances
// of NodeEffect2D but share the same NodeEffectPrefab2D instance.
node1->setEffectPrefab(shadowEffectPrefab);
node2->setEffectPrefab(shadowEffectPrefab);

```

## Creating a blur effect


Use the Blur Effect 2D effect to apply a Gaussian blur to a 2D node.

To create a blur effect for a 2D node using the Kanzi Engine API:

```
// Create a blur effect template.
NodeEffectTemplate2DSharedPtr blurEffectTemplate =
    NodeEffectTemplate2D::create(BlurEffect2D::getStaticMetaclass()->getName(), "BlurEffect");

// Set the value of the RadiusProperty in the blur effect template.
// RadiusProperty defines the amount of blur.
blurEffectTemplate->addPropertyValue(BlurEffect2D::RadiusProperty, Variant(6.f));

// Create a blur effect prefab.
NodeEffectPrefab2DSharedPtr blurEffectPrefab =
    NodeEffectPrefab2D::create(getDomain(), "BlurEffect prefab", blurEffectTemplate);

// Assign the blur effect to a 2D node.
node2d->setEffectPrefab(blurEffectPrefab);

// Get the node-specific effect instance created from the assigned prefab.
BlurEffect2DSharedPtr blurEffect = dynamic_pointer_cast<BlurEffect2D>(node2d->getEffect());

// Set the MaskedProperty to true. Masked mode maintains the original alpha channel and
// prevents the blur from spreading to fully transparent pixels.
blurEffect->setMasked(true);

```


For details, see the `BlurEffect2D` class.
## Creating a mask effect


Use the Mask Effect 2D effect to apply a mask to a 2D node.

To create a mask effect for a 2D node using the Kanzi Engine API:

```
// Create an effect template.
NodeEffectTemplate2DSharedPtr maskEffectTemplate =
    NodeEffectTemplate2D::create(MaskEffect2D::getStaticMetaclass()->getName(), "MaskEffect");

// Set the value of the MaskProperty in the template.
// The MaskProperty defines the mask texture which you must set before you can use the mask effect.
TextureSharedPtr maskTexture = acquireMaskTexture(getDomain());
maskEffectTemplate->addPropertyValue(MaskEffect2D::MaskProperty, Variant(maskTexture));

// Create a mask effect prefab.
NodeEffectPrefab2DSharedPtr maskEffectPrefab =
    NodeEffectPrefab2D::create(getDomain(), "MaskEffect prefab", maskEffectTemplate);

// Assign the mask effect to a 2D node.
node2d->setEffectPrefab(maskEffectPrefab);

// Get the node-specific effect instance created from the assigned prefab.
MaskEffect2DSharedPtr maskEffect = dynamic_pointer_cast<MaskEffect2D>(node2d->getEffect());

// Set the mask stretch mode to uniform.
maskEffect->setStretch(MaskEffect2D::Stretch::Uniform);

```


For details, see the `MaskEffect2D` class.
## Creating an outline effect


Use the Outline Effect 2D effect to apply an outline to the content of a 2D node.

To create an outline effect for a 2D node using the Kanzi Engine API:

```
// Create an outline effect template.
NodeEffectTemplate2DSharedPtr outlineEffectTemplate =
    NodeEffectTemplate2D::create(OutlineEffect2D::getStaticMetaclass()->getName(), "OutlineEffect");

// Set the value of the WidthProperty in the outline effect template.
// The WidthProperty defines the maximum width of the outline outside the content area.
outlineEffectTemplate->addPropertyValue(OutlineEffect2D::WidthProperty, Variant(8));

// Create an outline effect prefab.
NodeEffectPrefab2DSharedPtr outlineEffectPrefab =
    NodeEffectPrefab2D::create(getDomain(), "OutlineEffect prefab", outlineEffectTemplate);

// Assign the outline effect to a 2D node.
node2d->setEffectPrefab(outlineEffectPrefab);

// Get the node-specific effect instance created from the assigned prefab.
OutlineEffect2DSharedPtr outlineEffect = dynamic_pointer_cast<OutlineEffect2D>(node2d->getEffect());

// Set the SoftnessProperty to 0.7 for this node only. This overrides
// the property default value defined by the OutlineEffect2D metaclass.
outlineEffect->setSoftness(0.7f);

```


For details, see the `OutlineEffect2D` class.
## Creating a shadow effect


Use the Shadow Effect 2D effect to apply a shadow to the content of a 2D node.

To create a shadow effect for a 2D node using the Kanzi Engine API:

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
## Assigning multiple effects to a 2D node


To assign multiple effects to a 2D node using the Kanzi Engine API:

```
// Create an outline effect template.
NodeEffectTemplate2DSharedPtr outlineEffectTemplate =
    NodeEffectTemplate2D::create(OutlineEffect2D::getStaticMetaclass()->getName(), "OutlineEffect");

// Set the value of the WidthProperty in the outline effect template.
// The WidthProperty defines the maximum width of the outline outside the content area.
outlineEffectTemplate->addPropertyValue(OutlineEffect2D::WidthProperty, Variant(8));

// Create an effect stack template.
NodeEffectTemplate2DSharedPtr effectStackTemplate = NodeEffectTemplate2D::create(EffectStack2D::getStaticMetaclass()->getName(), "Group");

// Add the outline effect template to the effect stack template.
effectStackTemplate->addChild(outlineEffectTemplate);

// Create a shadow effect template and add it to the effect stack template.
effectStackTemplate->addChild(NodeEffectTemplate2D::create(ShadowEffect2D::getStaticMetaclass()->getName(), "DropShadow"));

// Create a prefab from the effect stack template.
NodeEffectPrefab2DSharedPtr effectStackPrefab =
    NodeEffectPrefab2D::create(getDomain(), "Effect Stack prefab", effectStackTemplate);

// Set a 2D node to use the effect stack prefab.
// This way, you apply to the node both the outline and the shadow effect.
node->setEffectPrefab(effectStackPrefab);

```


For details, see the `EffectStack2D` class.
## Using bindings with effects


To use bindings with effects:

```
// Create an outline effect template.
NodeEffectTemplate2DSharedPtr outlineEffectTemplate =
    NodeEffectTemplate2D::create(OutlineEffect2D::getStaticMetaclass()->getName(), "OutlineEffect");

// Create a shadow effect template.
NodeEffectTemplate2DSharedPtr shadowEffectTemplate =
    NodeEffectTemplate2D::create(ShadowEffect2D::getStaticMetaclass()->getName(), "DropShadow");

// Add to the shadow effect a binding that binds the shadow distance to a value in the root
// of the effect template.
shadowEffectTemplate->addBinding(BindingLoadInfo(Binding::create("##Template", ShadowEffect2D::DistanceProperty), ShadowEffect2D::DistanceProperty));

// Add to the host node a binding that binds the shadow distance value in the effect template root
// to the value in the node.
node->setBinding(
    ToSourceBinding::create(
        ObjectPropertyBindingSource::create(".", ShadowEffect2D::DistanceProperty),
        ObjectPropertyBindingSource::create(".Node2D.Effect", ShadowEffect2D::DistanceProperty)));

// Create an effect stack template
NodeEffectTemplate2DSharedPtr effectStackTemplate = NodeEffectTemplate2D::create(EffectStack2D::getStaticMetaclass()->getName(), "Group");

// Add the outline effect template to the effect stack template.
effectStackTemplate->addChild(outlineEffectTemplate);

// Add the shadow effect template to the effect stack template.
effectStackTemplate->addChild(shadowEffectTemplate);

// Create a prefab from the effect stack template.
NodeEffectPrefab2DSharedPtr effectStackPrefab =
    NodeEffectPrefab2D::create(getDomain(), "Effect Stack prefab", effectStackTemplate);

// Assign the effect stack to a 2D node.
node->setEffectPrefab(effectStackPrefab);

// In the host node, set the shadow distance.
node->setProperty(ShadowEffect2D::DistanceProperty, 20.f);

```

## Creating a custom effect


You can use the Kanzi Engine API to create your own effects for 2D nodes.

To create a custom effect for a 2D node using the Kanzi Engine API:

```
// To create an effect resource type, inherit a new class from NodeEffect2D
// and define a new associated metaclass. Each effect resource class must
// have an associated renderer class inherited from NodeEffectRenderer2D.

class EmptyEffectRenderer2D;
using EmptyEffectRenderer2DUniquePtr = unique_ptr<EmptyEffectRenderer2D>;

class EmptyEffect2D;
using EmptyEffect2DSharedPtr = shared_ptr<EmptyEffect2D>;

// EmptyEffect2D defines a new effect that defines no properties
// nor padding.
class EmptyEffect2D : public NodeEffect2D
{
public:
    KZ_METACLASS_BEGIN(EmptyEffect2D, NodeEffect2D, "Kanzi.EmptyEffect2D")
    KZ_METACLASS_END()

    // Create an instance of EmptyEffect2D.
    static EmptyEffect2DSharedPtr create(Domain* domain, string_view name)
    {
        return make_polymorphic_shared_ptr<Resource>(new EmptyEffect2D(domain, name));
    }

protected:
    // Constructor.
    explicit EmptyEffect2D(Domain* domain, string_view name) :
        NodeEffect2D(domain, name)
    {
    }

    // NodeEffect2D::createRendererOverride implementation.
    NodeEffectRenderer2DUniquePtr createRendererOverride() override;

    // NodeEffect2D::initializeRendererOverride implementation.
    void initializeRendererOverride() override
    {
    }
};

// EmptyEffectRenderer2D implements the rendering of the effect.
// Because this example effect does not render anything, Kanzi renders
// the original node as is.
class EmptyEffectRenderer2D : public NodeEffectRenderer2D
{
public:
    // Creates an instance of MinimalEffectRenderer2D. Never call this
    // function directly. Instead, use NodeEffect2D::createRenderer().
    static EmptyEffectRenderer2DUniquePtr create(EmptyEffect2DSharedPtr effect)
    {
        return unique_ptr<EmptyEffectRenderer2D>(new EmptyEffectRenderer2D(effect));
    }

private:
    // Constructor.
    explicit EmptyEffectRenderer2D(EmptyEffect2DSharedPtr effect) :
        NodeEffectRenderer2D(effect)
    {
    }

    // Implementation of NodeEffectRenderer2D::beginEffectOverride.
    void beginEffectOverride(Renderer& /*renderer*/, CompositionManager* /*compositionManager*/,
                             const Matrix3x3& /*worldTransform*/, const CompositionContentRequirements& /*requirements*/) override
    {
    }

    // Implementation of NodeEffectRenderer2D::endEffectOverride.
    void endEffectOverride(Renderer& /*renderer*/, CompositionManager* /*compositionManager*/) override
    {
    }

    // Implementation of NodeEffectRenderer2D::blitEffectOverride.
    void blitEffectOverride(Renderer& /*renderer*/, CompositionManager* /*compositionManager*/,
                            const QuadDescription& /*effectQuad*/, const Matrix3x3& /*transform*/, const Matrix4x4* /*perspectiveMatrix*/,
                            const Matrix4x4* /*projectionMatrix*/, int /*blendMode*/, bool /*needsClear*/) override
    {
    }

    // Implementation of NodeEffectRenderer2D::restoreResourcesOverride.
    virtual void restoreResourcesOverride() override
    {
    }
};

NodeEffectRenderer2DUniquePtr EmptyEffect2D::createRendererOverride()
{
    return EmptyEffectRenderer2D::create(static_pointer_cast<EmptyEffect2D>(shared_from_this()));
}

```


For details, see the `NodeEffect2D` class.
