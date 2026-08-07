---
title: Kanzi 4.0.0 migration guide
source: https://docs.kanzi.com/4.1.0/en/release-notes/kanzi-4.0/kanzi-4.0.0-migration-guide.html
---

# Kanzi 4.0.0 migration guide

Use this migration guide to update Kanzi applications from Kanzi 3.9 to Kanzi 4.0.
**Note:** Depending on your projects reliance on changes mentioned herein, it may require less effort to assemble a new project on Kanzi 4.0.0 than migrating.
## Upgrade to Visual Studio 2022

Kanzi no longer supports Kanzi Engine libraries for Visual Studio 2017 and 2019.

For Kanzi Studio projects with a Kanzi Engine plugin, rebuild the plugin with Visual Studio 2022 and import the plugin DLL to the Kanzi Studio project.
## Changes to the build system

- All platforms have been migrated to use CMake instead of SCons.

## Introduction of Kanzi Graphics

Introduction of Kanzi `Graphics` changes how Kanzi applications interact with the Kanzi rendering subsystem.

Most functions in the `Renderer` class were removed. Use the Kanzi Graphics API with the configured backend (Open GL, Open GL ES, or Vulkan) instead.

Kanzi Graphics consists of these major parts:

- Create objects with the `gfx::create` function and the `GraphicsCreateInfo` structs.
- Kanzi records `GraphicsCommands` into a command buffer, and Kanzi Graphics backend processes these commands for a specific graphics API.
- For Kanzi Studio projects with a Kanzi Engine plugin, the plugin DLL needs to be re-imported to the Kanzi Studio project.

1.

Rebuild the plugin using Kanzi 4.0.0.
2.

In the Library > Kanzi Engine Plugins, delete the Kanzi Engine plugin and import the updated Kanzi Engine plugin.

- Removed these classes, members, or functions:

  - `kanzi::acquireUniformLocation`
  - `kanzi::getUniformElementCount`
  - `kanzi::GLBufferHandle`
  - `kanzi::GLFramebufferHandle`
  - `kanzi::GlGraphicsLogScope`
  - `kanzi::GlGraphicsAdapter`
  - `kanzi::GlGraphicsAdapterCallGles`
  - `kanzi::GlGraphicsAdapterCallOpenGl`
  - `kanzi::GlGraphicsAdapterCheckForErrors`
  - `kanzi::GlGraphicsAdapterLogger`
  - `kanzi::GLGraphicsOutput`
  - `kanzi::GLProgramHandle`
  - `kanzi::GLRenderbufferHandle`
  - `kanzi::GlRenderState::acquireUniformLocation`
  - `kanzi::GlRenderState::allocateValues`
  - `kanzi::GlRenderState::RenderValueUnion`
  - `kanzi::GlRenderState::RenderValueInfo`
  - `kanzi::GlRenderState::TextureRenderValue`
  - `kanzi::GlRenderValueBase`
  - `kanzi::GLShaderHandle`
  - `kanzi::GLTextureHandle`
  - `kanzi::GlTextureRenderValue`
  - `kanzi::Mesh::bind`
  - `kanzi::Mesh::bindAttribute`
  - `kanzi::Mesh::bindAttributes`
  - `kanzi::Mesh::bindIndicies`
  - `kanzi::Renderer::getActiveGraphicsContext`
  - `kanzi::Renderer::getActiveSurfaceVendor`
  - `kanzi::Renderer::getUniformLocationSlow`
  - `kanzi::Renderer::getUniformArrayLength`
  - `kanzi::Renderer::setUniformIntArray`
  - `kanzi::Renderer::setUniformFloatArray`
  - `kanzi::Renderer::setUniformVecArray`
  - `kanzi::Renderer::setUniformColorArray`
  - `kanzi::Renderer::setUniformMatArray`
  - `kanzi::Renderer::setUniformInteger`
  - `kanzi::Renderer::setUniformFloat`
  - `kanzi::Renderer::setUniformVec2`
  - `kanzi::Renderer::setUniformVec3`
  - `kanzi::Renderer::setUniformVec4`
  - `kanzi::Renderer::setUniformColorRGBA`
  - `kanzi::Renderer::setUniformMatrix3x3`
  - `kanzi::Renderer::setUniformMatrix4x4`
  - `kanzi::Renderer::setActiveScalar`
  - `kanzi::Renderer::getActiveScalar`
  - `kanzi::Renderer::calculateProjectionCameraWorldMatrix`
  - `kanzi::Renderer::applyFixedUniformTime`
  - `kanzi::Renderer::applyFixedUniformWindowSize`
  - `kanzi::Renderer::applyTransformationUniform`
  - `kanzi::Renderer::applyTransformation`
  - `kanzi::Renderer::applyTextureSizeUniforms`
  - `kanzi::Renderer::applyTexture`
  - `kanzi::Renderer::detachTexture`
  - `kanzi::Renderer::setUniformTexture`
  - `kanzi::Renderer::generateTexture`
  - `kanzi::Renderer::deleteTexture`
  - `kanzi::Renderer::setTextureAddressingMode`
  - `kanzi::Renderer::setTextureSwizzleMask`
  - `kanzi::Renderer::setTextureSwizzleEachChannel`
  - `kanzi::Renderer::deleteShaderProgram`
  - `kanzi::Renderer::deleteShader`
  - `kanzi::Renderer::generateFramebuffer`
  - `kanzi::Renderer::deleteFramebuffer`
  - `kanzi::Renderer::invalidateFramebufferAttachments`
  - `kanzi::Renderer::framebufferRenderbuffer`
  - `kanzi::Renderer::generateRenderbuffer`
  - `kanzi::Renderer::deleteRenderbuffer`
  - `kanzi::Renderer::bindRenderbuffer`
  - `kanzi::Renderer::renderbufferStorage`
  - `kanzi::Renderer::generateBuffer`
  - `kanzi::Renderer::setVertexBufferData`
  - `kanzi::Renderer::setIndexBufferData`
  - `kanzi::Renderer::setVertexBufferSubData`
  - `kanzi::Renderer::setIndexBufferSubData`
  - `kanzi::Renderer::deleteBuffer`
  - `kanzi::Renderer::BufferAccessMode`
  - `kanzi::Renderer::mapVertexBuffer`
  - `kanzi::Renderer::unmapVertexBuffer`
  - `kanzi::Renderer::mapIndexBuffer`
  - `kanzi::Renderer::unmapIndexBuffer`
  - `kanzi::Renderer::enableVertexAttributeArray`
  - `kanzi::Renderer::disableVertexAttributeArray`
  - `kanzi::Renderer::getActiveShaderHandle`
  - `kanzi::Renderer::getActiveShaderAttributeMap`
  - `kanzi::Renderer::beginMaterialSetup`
  - `kanzi::Renderer::endMaterialSetup`
  - `kanzi::Renderer::pushStatistics`
  - `kanzi::Renderer::popStatistics`
  - `kanzi::Renderer::getIndexCount`
  - `kanzi::Renderer::getTriangleCount`
  - `kanzi::Renderer::getVertexCount`
  - `kanzi::Renderer::getInstanceCount`
  - `kanzi::Renderer::getBatchCount`
  - `kanzi::Renderer::getShaderSwitchCount`
  - `kanzi::Renderer::getUniformSendCount`
  - `kanzi::Renderer::getTextureSwitchCount`
  - `kanzi::Renderer::getFramebufferSwitchCount`
  - `kanzi::Renderer::getBufferSwitchCount`
  - `kanzi::Renderer::getHeavyweightCallCount`
  - `kanzi::Renderer::getHalfFloatVertexAttributeSupport`
  - `kanzi::Renderer::getTexStorageSupport`
  - `kanzi::Renderer::getGLFormatTriplet`
  - `kanzi::Renderer::clearUniformCaches`
  - `kanzi::Renderer::TextureUnitInfo`
  - `kanzi::Renderer::RenderingChangeStateFlag`
  - `kanzi::Renderer::refreshRenderContext`
  - `kanzi::Renderer::enableState`
  - `kanzi::Renderer::disableState`
  - `kanzi::Renderer::setState`
  - `kanzi::Renderer::getState`
  - `kanzi::Renderer::setBlendMode`
  - `kanzi::Renderer::getBlendMode`
  - `kanzi::Renderer::setCullMode`
  - `kanzi::Renderer::getCullMode`
  - `kanzi::Renderer::setDepthTest`
  - `kanzi::Renderer::getDepthTest`
  - `kanzi::Renderer::setLineWidth`
  - `kanzi::Renderer::getLineWidth`
  - `kanzi::Renderer::clear`
  - `kanzi::Renderer::resetClearTarget`
  - `kanzi::Renderer::addClearTarget`
  - `kanzi::Renderer::getClearMode`
  - `kanzi::Renderer::addClearColor`
  - `kanzi::Renderer::removeClearTarget`
  - `kanzi::Renderer::isClearEnabled`
  - `kanzi::Renderer::setClearColor`
  - `kanzi::Renderer::setClearDepthValue`
  - `kanzi::Renderer::setClearStencil`
  - `kanzi::Renderer::setColorWriteMode`
  - `kanzi::Renderer::getColorWriteMode`
  - `kanzi::Renderer::setViewport`
  - `kanzi::Renderer::getViewport`
  - `kanzi::Renderer::setScissorTest`
  - `kanzi::Renderer::getScissor`
  - `kanzi::Renderer::setVertexBuffer`
  - `kanzi::Renderer::setIndexBuffer`
  - `kanzi::Renderer::drawBuffers`
  - `kanzi::Renderer::setVertexCount`
  - `kanzi::Renderer::setIndexCount`
  - `kanzi::Renderer::setIndexData`
  - `kanzi::Renderer::setInstanceCount`
  - `kanzi::Renderer::setActiveTextureUnit`
  - `kanzi::Renderer::bindTexture`
  - `kanzi::Renderer::setTextureImage2D`
  - `kanzi::Renderer::setTextureSubImage2D`
  - `kanzi::Renderer::textureStorage`
  - `kanzi::Renderer::generateMipMaps`
  - `kanzi::Renderer::setTextureFilter`
  - `kanzi::Renderer::setTextureCompare`
  - `kanzi::Renderer::setTextureMaximumLevel`
  - `kanzi::Renderer::createShader`
  - `kanzi::Renderer::createShaderProgram`
  - `kanzi::Renderer::attachShaderToProgram`
  - `kanzi::Renderer::detachShaderFromProgram`
  - `kanzi::Renderer::bindAttributeToLocation`
  - `kanzi::Renderer::linkShaderProgram`
  - `kanzi::Renderer::compileSourceShader`
  - `kanzi::Renderer::deployBinaryShader`
  - `kanzi::Renderer::deployBinaryProgram`
  - `kanzi::Renderer::loadProgramFromCache`
  - `kanzi::Renderer::saveProgramToCache`
  - `kanzi::Renderer::getCacheFilePath`
  - `kanzi::Renderer::updateSettings`
  - `kanzi::Renderer::getProgramBinary`
  - `kanzi::Renderer::isFramebufferComplete`
  - `kanzi::Renderer::framebufferTexture2D`
  - `kanzi::Renderer::applyVertexAttributeArrays`
  - `kanzi::Renderer::setVertexBufferPointer`
  - `kanzi::Renderer::setVertexBufferPointer`
  - `kanzi::Renderer::setActiveShaderHandle`
  - `kanzi::Renderer::setActiveFramebuffer`
  - `kanzi::Renderer::setColorBufferCount`
  - `kanzi::Renderer::getActiveFramebuffer`
  - `kanzi::Renderer::beginVertexArray`
  - `kanzi::Renderer::setVertexArrayData`
  - `kanzi::Renderer::endVertexArray`
  - `kanzi::Renderer::getCurrentVertexArrayFlags`
  - `kanzi::Renderer::getCurrentVertexArrayAttributeData`
  - `kanzi::Renderer::isShaderBinaryFormatSupported`
  - `kanzi::Renderer::isProgramBinaryFormatSupported`
  - `kanzi::Renderer::applyAttributePointer`
  - `kanzi::Renderer::supportsTexStorage`
  - `kanzi::Renderer::setHasTessellationShader`
  - `kanzi::Renderer::setFillMode`
  - `kanzi::Renderer::readPixels`
  - `kanzi::Renderer::setPixelStorePack`
  - `kanzi::Renderer::setPixelStoreUnpack`
  - `kanzi::Shader::UniformProperty::uniformLocation`
  - `kanzi::Shader::hasSamplersWithoutProperties`
  - `kanzi::Shader::getTextureUniformLocation`
  - `kanzi::Texture::deployImages`
  - `kzsGlGraphicsContextCreate`
  - `kzsGlGraphicsContextDestroy`
  - `kzsGlGraphicsContextSetActive`
  - `kzsGlGraphicsContextGetAdapter`
  - `kzsGlGraphicsContextIsKhrDebugSupported`
  - `kzsGlGraphicsContextGetVendor`
  - `kzsGlGraphicsContextGetSurfaceClientAPI`
  - `kzsGlGraphicsContextGetAPI`
  - `kzsGlIsExtensionSupported`
  - `kzsGlGraphicsContextSetLogging`
  - `kzsGlGraphicsContextGetLogging`
  - `kzsGlGraphicsContextGetDumpStateOnDrawCalls`
  - `kzsGlGraphicsContextSetErrorChecking`
  - `kzsGlGraphicsContextSetDebugCallback`
  - `kzsGlGraphicsContextGetGlesSymbols`
  - `kzsGlGraphicsContextGetOpenGlSymbols`

- The `kanzi::GlRenderState` class has been renamed to `RenderState` to remove the platform-specific âGlâ prefix, as the render state abstraction is not specific to OpenGL.

The header file has also been moved from `kanzi/core.ui/graphics3d/render_state.hpp` to `kanzi/core.ui/graphics/render_state.hpp`.
- Removed these functions that have direct replacements:

Removed |

Use instead |

`kanzi::captureCurrentFramebufferToImage` |

`captureFramebuffer` |

`kanzi::captureScreenToImage` |

`captureFramebuffer` |

`kanzi::GPUBuffer::getNativeHandle` |

`GPUBuffer::getHandle` |

`kanzi::Mesh::getNativeVertexBufferHandle` |

`Mesh::getVertexBufferHandle` |

`kanzi::Mesh::getNativeIndexBufferHandle` |

`Mesh::getIndexBufferHandle` |

`kanzi::Mesh::getNativeInstanceBufferHandle` |

`Mesh::getInstanceBufferHandle` |

`kanzi::Renderbuffer::getNativeHandle` |

`Renderbuffer::getHandle` |

`kanzi::Renderer::applyFixedUniforms` |

`RenderState::updateFixedFunctionUniforms` |

`kanzi::Renderer::getMaximumVertexAttributeCount` |

`gfx::getDeviceProperty` (`gfx::DevicePropertyId::MaxVertexAttributes`) |

`kanzi::Renderer::setActiveGLGraphicsOutput` |

`Renderer::setActiveGraphicsOutput` |
- Removed the `kanzi::Geometry::drawTextured` and `kanzi::Geometry::drawUntextured` functions. If you use these functions, you can change code like this

```
if (isTextured())
{
    geometry.drawTextured(renderer, transform, GraphicsPrimitiveTypeTriangleStrip, material);
}
else
{
    geometry.drawUntextured(renderer, transform, GraphicsPrimitiveTypeTriangleStrip, material);
}

```

to

```
renderer.setMatrix(FixedMatrixWorld, transform);
renderState.updateTransformationUniforms(renderer);

renderState.draw(renderer, geometry);

```

## Changes to the Renderer API

- Removed the `Renderer3D` class. Kanzi used the `Renderer3D` class to store temporary properties during 3D rendering and provided debug functionality for the Preview.

This version of Kanzi moves:

  - The rendering to the `DebugRenderRegistry` and `DebugVisualization` classes
  - The 3D rendering specifics are now handled by render passes, such as `GatherLightsRenderPass`

In your application code, change all uses of `Renderer3D` to use `Renderer`. This includes all virtual functions that have `Renderer3D` passed as a parameter.

Moved these functions from the `Renderer3D` class to the `Renderer` class:

  - `Renderer::applyCameraMatrix`
  - `Renderer::beginFrame`
  - `Renderer::disableSubRectangleProjection`
  - `Renderer::endFrame`
  - `Renderer::getActiveGraphicsOutput`
  - `Renderer::getCompositionStack`
  - `Renderer::getInheritedAspectRatioMultiplier`
  - `Renderer::getOverrideClusterMaterial`
  - `Renderer::getOverrideMaterialCallback`
  - `Renderer::getOverrideMaterialCallbackUserData`
  - `Renderer::setActiveGraphicsOutput`
  - `Renderer::setSubRectangleProjection`
  - `Renderer::setOverrideMaterial`
  - `Renderer::setOverrideMaterialCallback`

Removed these functions because of refactoring related to the removal of the `Renderer3D` class. Most of the removed functions are related to debug rendering:

  - `Renderer::bindFramebuffer`
  - `Renderer::setActiveFramebufferCallback`
  - `Renderer::setDefaultFramebuffer`
  - `Renderer3D::addVertexAndNormalToFloatArrays`
  - `Renderer3D::addVertexToFloatArray`
  - `Renderer3D::applyBoolProperty`
  - `Renderer3D::applyColorMaterial`
  - `Renderer3D::applyColorProperty`
  - `Renderer3D::applyFloatProperty`
  - `Renderer3D::applyIntProperty`
  - `Renderer3D::applyMaterial`
  - `Renderer3D::applyMaterialStrict`
  - `Renderer3D::applyMatrix3x3Property`
  - `Renderer3D::applyMatrix4x4Property`
  - `Renderer3D::applyPropertyType`
  - `Renderer3D::applySRT2DProperty`
  - `Renderer3D::applySRT3DProperty`
  - `Renderer3D::applyStencilSettings`
  - `Renderer3D::applyTextureProperty`
  - `Renderer3D::applyVector2Property`
  - `Renderer3D::applyVector3Property`
  - `Renderer3D::applyVector4Property`
  - `Renderer3D::calculateNormal`
  - `Renderer3D::drawBoxSolidNormal`
  - `Renderer3D::drawLayerOutlineQuad`
  - `Renderer3D::drawLayerQuad`
  - `Renderer3D::drawLayerQuadWithMaterial`
  - `Renderer3D::drawLineList`
  - `Renderer3D::drawPrimitives`
  - `Renderer3D::drawOrientedBoundingBoxSolidNormal`
  - `Renderer3D::drawPrimitiveBufferTextured`
  - `Renderer3D::drawPrimitiveBufferUntextured`
  - `Renderer3D::drawPrimitivesNormal`
  - `Renderer3D::drawSelectionIndicator`
  - `Renderer3D::drawQuad`
  - `Renderer3D::drawTrajectory`
  - `Renderer3D::drawUntexturedLayerQuad`
  - `Renderer3D::drawViewportQuadWithTextureSpan`
  - `Renderer3D::getActiveGLGraphicsOutput`
  - `Renderer3D::getClearColorOverride`
  - `Renderer3D::getFloatBuffer`
  - `Renderer3D::getResourceManager`
  - `Renderer3D::isBoundingBoxVisualizationEnabled`
  - `Renderer3D::isColorWriteDisabled`
  - `Renderer3D::isSkeletonVisualizationEnabled`
  - `Renderer3D::printInfo`
  - `Renderer3D::removeClearColorOverride`
  - `Renderer3D::setActiveGLGraphicsOutput`
  - `Renderer3D::setBoundingBoxVisualizationEnabled`
  - `Renderer3D::setClearColorOverride`
  - `Renderer3D::setDefaultOrthoProjection`
  - `Renderer3D::setDisableColorWrite`
  - `Renderer3D::setFramebufferCallback`
  - `Renderer3D::setLogging`
  - `Renderer3D::setSkeletonVisualizationEnabled`
  - `Surface::attach`
  - `Surface::attachOverride`

Instead, use the `DebugVisualization` and `DebugVisualizationStorage` classes to draw and store debug visualizations for nodes.

The standard `DebugRenderRegistry::DebugObjectRenderingFunction` automatically used by `DebugComposer` changed to:

```
void (*DebugObjectRenderingFunction)(Renderer& renderer, DebugRenderStorage& storage, DebugVisualization* visualization, NodeSharedPtr object);

```

You can access `storage` to create a debug visualization structure for the `Node`. If you have done this on a previous frame, the `visualization` parameter is non-null and you can use it. Geometry stored in the `DebugVisualization` remains until you remove the `Node` from the scene graph.
- Removed the `Surface::Usage` enumeration.
- `RenderTargetMode` has been deprecated and removed from `Texture`. As a result:

  - `StatusInvalidRenderTargetMode` has been removed from `Texture::CreateInfo::Status` and `interop::TextureEnums::CreateInfo::Status`.
  - `StatusUnsupportedInternalRenderTargetSampleCount` has been renamed to `StatusUnsupportedRenderTargetSampleCount` in `Texture::CreateInfo::Status` and `interop::TextureEnums::CreateInfo::Status`.

- As consequence of the removal of the `RenderTargetMode` enumeration, modified `Texture::CreateInfo` and `Texture` to remove `GraphicsFormatFeature` and `RenderTargetMode` settings. The texture create info now uses a mask of `gfx::ImageUsageFlag` to specify texture usage intent.

  - Added `usageFlags` field to `Texture::CreateInfo`.
  - When creating composition targets, enable the `gfx::ImageUsageFlag::Attachment` flag. This is automatically enabled by `kanzi::Texture::CreateInfoNode2DRenderTarget`.
  - `gfx::ImageUsageFlag::SampledShaderResource` is enabled by default. If the texture is not sampled, remove this flag and set `gfx::ImageUsageFlag::ShaderResource` instead.
  - Other relevant flags are enabled automatically based on texture settings: - `gfx::ImageUsageFlag::CopyDestination` for MSAA textures. - You can manually enable additional flags, depending on the intended use, such as copy source and destination.

- Removed the `GlRenderValue` and `GlBlendModeRenderValue` classes, and `updateRenderValue` functions, use `kanzi::GlRenderState` instead.
- Removed the `GraphicsPrimitiveTypeLineLoop` option from the `GraphicsPrimitiveType` enumeration. Use `GraphicsPrimitiveType::GraphicsPrimitiveTypeLineStrip` instead, with the first vertex duplicated at the end of the vertex list.
- Renamed the `GlRenderValueBinding` class to `RenderValueBinding`.
- Removed the `GPUBufferType` enumeration. Use `gfx::BufferUsageFlag` instead. When creating a new GPU buffer, use either `gfx::BufferUsageFlag::VertexBuffer` or `gfx::BufferUsageFlag::IndexBuffer`.
- The type of the `nativeHandle` parameter changed to `gfx::NativeTextureHandle` in the `Texture::create`, the overloaded method which was used to create texture from a pre-existing image object.
- Removed functions left unused, because of the new graphics backend:

  - `Renderer::getColorReadFormat`
  - `Renderer::getColorReadType`

- Removed some feature detection methods from the `Renderer`.

Removed |

Use instead |

`kanzi::Renderer::checkGLSupport` |

`gfx::getBackendInformation` or `gfx::isFeatureEnabled` |

`kanzi::Renderer::checkGLESSupport` |

`gfx::getBackendInformation` or `gfx::isFeatureEnabled` |

`kanzi::Renderer::getGlesVersion` |

`gfx::getBackendInformation` |

`kanzi::Renderer::getMultisampleSupport` |

Multisampling is always supported. |

`kanzi::Multisample` |

Different multisample types no longer differentiated. |

## Consolidation of index buffers in `kanzi::Mesh`

Consolidated `kanzi::Mesh` index buffers into one in the Mesh object itself, instead of each `kanzi::Mesh::Cluster` having its own. This moves index buffer related API calls to the Mesh itself, or removes the Cluster parameter. Index buffer type and handle parameters were removed from `kanzi::Mesh::CreateInfo::Cluster` constructors, as these now form part of `kanzi::Mesh::CreateInfo` directly. Use `Mesh::getClusterIndexOffset` to get byte offset into the main index buffer, if needed.

Removed |

Use instead |

`kanzi::Mesh::getClusterIndexType` |

`Mesh::getIndexType` |

`kanzi::Mesh::getClusterIndexData` |

`Mesh::getIndexData` |

`kanzi::Mesh::CreateInfo::Cluster::setIndexCount` |

Set `kanzi::Mesh::CreateInfo::Cluster::indexCount` and `kanzi::Mesh::CreateInfo::Cluster::indexOffset` members directly. |

Cluster index parameter removed from following functions:

kanzi::Mesh::mapIndexData |

`Mesh::setIndexData` |

`Mesh::setIndexSubData` |
## Changes to the Platform API

- Several entities that refer to OpenGL context APIs have been renamed.

Removed |

Use instead |

`kanzi::platform::OpenGLPlatform` |

`kanzi::platform::GlContextApi` |

`kanzi::platform::createDefaultOpenGLPlatform` |

`kanzi::platform::createDefaultGlContextApi` |

- Win32 string utilities found inside `kanzi/core/platform/cpp/win32/string_conversion.hpp` have been moved from the `kanzi` namespace to `win32`

- All platform-dependent windowing and input code has been moved into a separate library (kzplatform).

## Changes to Data-Driven Exclusive Activity Host

Data-Driven Exclusive Activity Host now supports only Activities created from a data source and no longer supports manually added Activities. Use an Exclusive Activity Host instead.
## Changes to List Box

- In the `ListBoxConcept` class, renamed these messages and message arguments:

Kanzi 3.9 |

Kanzi 4.0 |

`ListBoxConcept::ItemHiddenMessage` |

`ListBoxConcept::ItemUnloadedMessage` |

`ListBoxConcept::ItemHiddenMessageArguments` |

`ListBoxConcept::ItemUnloadedMessageArguments` |

`ListBoxConcept::ItemVisibleMessage` |

`ListBoxConcept::ItemLoadedMessage` |

`ListBoxConcept::ItemVisibleMessageArguments` |

`ListBoxConcept::ItemLoadedMessageArguments` |
- In the `ListBoxConceptImpl` class, renamed these public member functions:

Kanzi 3.9 |

Kanzi 4.0 |

`ListBoxConceptImpl::getAliveRange` |

`ListBoxConceptImpl::getAliveItemsRange` |

`ListBoxConceptImpl::updateVisibleRangeQuiet` |

`ListBoxConceptImpl::updateAliveItemsRangeQuiet` |

`ListBoxConceptImpl::updateVisibleRange` |

`ListBoxConceptImpl::updateAliveItemsRange` |
- In the `ListBoxTrajectoryPresenter` class, renamed these protected member functions:

Kanzi 3.9 |

Kanzi 4.0 |

`ListBoxTrajectoryPresenter::calculateVisibleRange` |

`ListBoxTrajectoryPresenter::calculateAliveItemsRange` |

`ListBoxTrajectoryPresenter::updateVisibleRange` |

`ListBoxTrajectoryPresenter::updateAliveItemsRange` |

`ListBoxTrajectoryPresenter::extendVisibleItemRangeToItem` |

`ListBoxTrajectoryPresenter::extendAliveItemsRangeToItem` |
- Renamed these classes and their metaclass names:

Kanzi 3.9 |

Kanzi 4.0 |

`DataSourceListItemGenerator` |

`DataSourceListBoxItemGenerator` |

`DataSourceListItemGenerator2D` |

`DataSourceListBoxItemGenerator2D` |

`DataSourceListItemGenerator3D` |

`DataSourceListBoxItemGenerator3D` |

## Changes to the List Box nodes

In the Grid List Box nodes, the default directional navigation keys no longer move the item selection. In a List Box node, the default directional navigation keys now move the key focus between the focusable list items.

For example, to scroll a Grid List Box with the â and â keys, make the list items focusable. See Handling the key focus in a List Box node.
## Changes to the `ActivityCodeBehind` class

- In the Kanzi C++ API, in the `ActivityCodeBehind` class, replaced the `onActive`, `onInactive`, `onActivating`, and `onDeactivating` callbacks with `ActivityCodeBehind::onStatusChange`.

To migrate your Kanzi application, move the content of the `onActive`, `onInactive`, `onActivating`, and `onDeactivating` callbacks to the `ActivityCodeBehind::onStatusChange` callback. For example, if you derive from `ActivityCodeBehind`, change

```
void onActive() override
{
   kzLogInfo(KZ_LOG_CATEGORY_GENERIC, ("Activity status changed: Active"));
}

```

to

```
void onStatusChange(ActivityConcept::Status status) override
{
   switch(status)
   {
      case ActivityConcept::Status::Active:
         kzLogInfo(KZ_LOG_CATEGORY_GENERIC, ("Activity status changed: Active"));
         break;
   }
}

```

- In both Kanzi C++ (`ActivityCodeBehind`) and Kanzi Java API (`ActivityCodeBehind`), removed `registerStatusChange`, `registerStatusChangeOverride`, `unregisterStatusChange`, and `unregisterStatusChangeOverride`.

To migrate your Kanzi application, move the content of the registered status change callbacks to the `ActivityCodeBehind::onStatusChange` callback.

For example:
