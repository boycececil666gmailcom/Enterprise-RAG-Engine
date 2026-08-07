---
title: Kanzi Studio property editors for property types declared in Kanzi Engine plugins
source: https://docs.kanzi.com/4.1.0/en/working-with/plugins/studio-editors.html
---

# Kanzi Studio property editors for property types declared in Kanzi Engine plugins

Kanzi Studio property type editors enable users to set the values for the property types you declare in a Kanzi Engine plugin. This table lists the available Kanzi Studio editors you can declare for a property type in a Kanzi Engine plugin. If you do not set an editor, Kanzi assigns a default editor.
|

Editor display name |

Editor name |

Supported data types |

Multi-edit support |

Project item target type |
|

< No editor > |

NoEditor.PropertyGridEditor |

- COLOR
- STRING
- INT32
- FLOAT
- VECTOR2D
- VECTOR3D
- VECTOR4D
- MATRIX2x2
- MATRIX3x3
- MATRIX4x4
- ENUM
- GROUP_PROPERTY
- LIGHT_PROPERTY
- CAMERA_PROPERTY
- TEXTURE
- BOOLEAN
- RESOURCE_ID
- CONTENT_REFERENCE
- SRT2D
- SRT3D
-  PROJECT_ITEM _REFERENCE
-  PROJECT_ITEM _REFERENCE_LIST
- TYPE
-  PROPERTY_HOST _TYPES
-  PROPERTY_TYPE _GROUP
- ENUM_OPTIONS
- ATTRIBUTE_MAPPINGS
- ARRAY_PROPERTY
- EVENT
-  PROPERTY_TYPE _REFERENCE
- EVENT_HANDLER_LIST
-  COMPONENT _CALLBACK_LIST
- STRING_LIST
-  TIMELINE_ENTRY _TARGET
-  SHADER_VARIABLE _INFO_LIST
-  COLUMN_DEFINITION _LIST
- DATE_TIME
-  PROPERTY_BINDING _LIST
-  TIMELINEENTRY _WEIGHT
-  TIMELINEENTRY _WEIGHT_SINGLE
-  STATE_TRANSITION _LIST
-  RESOURCE _DICTIONARY
-  MULTI_EXPRESSION _PROPERTY _BINDING_LIST
-  LOCALIZATION _TABLE _DICTIONARY
- COMPOSITION_LIST
- DATA_CONTEXT
- VARIANT
- QUATERNION
- NODE_REFERENCE
- BINDING_TARGET
- NONE
  |

True |

ProjectItem |
|

2D prefab template selector |   LayerPrefabSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Node2DPrefabTemplate |
|

2D Transformation editor |   Transformation2DEditor. PropertyGridEditor   |

- MATRIX3x3
- SRT2D
  |

False |

N/A |
|

2D vector field editor |   Vector2dFieldEditor. PropertyGridEditor   |

VECTOR2D |

False |

N/A |
|

2D vector slider editor |   Vector2dSliderEditor. PropertyGridEditor   |

VECTOR2D |

False |

N/A |
|

3D prefab template selector |   ScenePrefabSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Node3DPrefabTemplate |
|

3D Transformation editor |   MatrixFieldEditor. PropertyGridEditor   |

- MATRIX4x4
- SRT3D
  |

False |

N/A |
|

3D vector field editor |   Vector3dFieldEditor. PropertyGridEditor   |

VECTOR3D |

False |

N/A |
|

3D vector slider editor |   Vector3dSliderEditor. PropertyGridEditor   |

VECTOR3D |

False |

N/A |
|

4D field-of-view editor |   Vector4dSliderEditor. FovEditor   |

VECTOR4D |

False |

N/A |
|

4D vector area editor |   Vector4dSliderEditor. AreaEditor   |

VECTOR4D |

False |

N/A |
|

4D vector field editor |   Vector4dFieldEditor. PropertyGridEditor   |

VECTOR4D |

False |

N/A |
|

4D vector slider editor |   Vector4dSliderEditor. PropertyGridEditor   |

VECTOR4D |

False |

N/A |
|

Animable property type selector |   PropertyTypeNameSelector. AnimablePropertyEditor   |   PROPERTY_TYPE _REFERENCE   |

False |

N/A |
|

Animation clip dropdown |   AnimationClipSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

AnimationClip |
|

Animation dropdown |   AnimationSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Animation |
|

Animation list selector |   AnimationEntryTargetList Selector.PropertyGridEditor   |   PROJECT_ITEM _REFERENCE_LIST   |

False |   |
|

Boolean dropdown |   BooleanValueSelector. PropertyGridEditor   |

BOOLEAN |

False |

N/A |
|

Boolean property type selector |   PropertyTypeNameSelector. ExportedBoolean PropertyEditor   |   PROPERTY_TYPE _REFERENCE   |

False |

N/A |
|

Browse file text editor |

BrowseFileTextEditor |

STRING |

False |

N/A |
|

Browse folder text editor |

BrowseFolderTextEditor |

STRING |

False |

N/A |
|

Browse plugin text editor |

BrowsePluginTextEditor |

STRING |

False |

N/A |
|

Brush dropdown |   BrushSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Brush |
|

Camera dropdown |   CameraComboBox. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

CameraNode |
|

Checkbox |   CheckboxValueSelector. PropertyGridEditor   |

BOOLEAN |

False |

N/A |
|

Color editor |   ColorSliderEditor. PropertyGridEditor   |

COLOR |

False |

N/A |
|

Composer dropdown |   ComposerComboBox. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

AbstractComposer |
|

Compute material dropdown |   MaterialComboBox. ComputeMaterialSelector   |   PROJECT_ITEM _REFERENCE   |

True |

Material |
|

Cube map texture dropdown |   TextureSelector.CubeMap TexturePropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

CubemapTextureInterface |
|

Data source selector |   DataSourceSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

DataSource |
|

Dispatch message action state selector |   DispatchMessageAction StateSelector   |   PROJECT_ITEM _REFERENCE   |

True |

State |
|

Enum property member selector |   EnumPropertyMember Selector.PropertyGrid Editor   |   PROPERTY_TYPE _GROUP   |

False |

N/A |
|

Enumeration dropdown |   EnumValueSelector. PropertyGridEditor   |

ENUM |

False |

N/A |
|

File list editor |   StringListEditor. FileListEditor   |

STRING_LIST |

False |

N/A |
|

Flags dropdown |   FlagsValueSelector. PropertyGridEditor   |

FLAGS |

False |

N/A |
|

Font dropdown |   FontSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

FontFile |
|

Font Family dropdown |   FontFamilySelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

FontFamily |
|

Forwarded message argument selector |   PropertyTypeNameSelector. ForwardedMessage ArgumentPropertyEditor   |   PROPERTY_TYPE _REFERENCE   |

False |

N/A |
|

Forwarded trigger host property value selector |   PropertyTypeNameSelector. ForwardedPropertyOf TriggerHostPropertyEditor   |   PROPERTY_TYPE _REFERENCE   |

False |

N/A |
|

Generic resource dropdown |   GenericResourceFileSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

GenericResourceFile |
|

HDR Color editor |   ColorSliderEditor. HDRPropertyGridEditor   |

COLOR |

False |

N/A |
|

Image format dropdown |   ImageFormatSelector. PropertyGridEditor   |

ENUM |

False |

N/A |
|

Image selector |   ImageFileComboBox. ImageOnly   |   PROJECT_ITEM _REFERENCE   |

True |

ImageFile |
|

Kzb dependency editor |   KzbDependenciesListEditor. PropertyGridEditor   |

STRING |

False |

N/A |
|

List box item template selector |   PrefabTemplateSelector. ListBoxItemTemplateSelector   |   PROJECT_ITEM _REFERENCE   |

True |

PrefabTemplate |
|

Locale selector |   CultureSelector. PropertyGridEditor   |

STRING |

False |

N/A |
|

Localization table selector |   LocalizationTableSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

LocalizationTable |
|

Main collada file dropdown |   MainAsset3DSourceFile Selector.PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Asset3DSourceFile |
|

Material dropdown |   MaterialComboBox. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Material |
|

Material type dropdown |   MaterialTypeSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

MaterialType |
|

Mesh dropdown |   MeshComboBox. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

MeshNodeMesh |
|

Mesh dropdown (allow null) |

MeshComboBox.AllowNull |   PROJECT_ITEM _REFERENCE   |

True |

Mesh |
|

Multi-line text editor |

TextEditor.TextAreaEditor |

STRING |

False |

N/A |
|

No Default Render Pass Prefab dropdown |   RenderPassPrefabComboBox. NoDefaultRenderPass PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

RenderPassPrefab |
|

Node 2D selector |   Node2DSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Node2D |
|

Node 3D dropdown |   Node3dSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Node3D |
|

Node 3D dropdown (allow null) |   Node3dSelector.Property GridEditorAllowNull   |   PROJECT_ITEM _REFERENCE   |

True |

Node3D |
|

Node 3D dropdown (immediate children) |   NodeSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Node3D |
|

Node dropdown |   NodeSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Node |
|

Object list selector |   SceneGraphNodeListSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE_LIST   |

False |

N/A |
|

Object source dropdown |   ObjectSourceSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

ObjectSource |
|

Object source list selector |   ObjectSourceListSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE_LIST   |

False |

N/A |
|

Page selector |   PageSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Node2D |
|

Page Transition Collection dropdown |   PageTransitionCollection Selector.PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

PageTransitionCollection |
|

Path Editor |   PathEditor. PropertyGridEditor   |

STRING |

False |

N/A |
|

Prefab template selector |   PrefabTemplateSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

PrefabTemplate |
|

Project item dropdown |   DefaultProjectObjectSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

ProjectItemInterface |
|

Property type selector |   PropertyTypeNameSelector. ExportedPropertyEditor   |   PROPERTY_TYPE _REFERENCE   |

False |

N/A |
|

Property Type List Selector |   GroupPropertyMember Selector.PropertyGridEditor   |   PROPERTY_TYPE _GROUP   |

False |

N/A |
|

Property type without object selector |   PropertyTypeNameSelector. ExportedPropertyWithout ObjectReferenceEditor   |   PROPERTY_TYPE _REFERENCE   |

False |

N/A |
|

Reference visualizer |   ReferenceVisualizer. PropertyGridEditor   |

-  PROJECT_ITEM _REFERENCE
-  PROPERTY_TYPE _REFERENCE
  |

True |

ProjectItemInterface |
|

Render Pass Prefab dropdown |   RenderPassPrefabComboBox. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

RenderPassPrefab |
|

Render target depth dropdown |   RenderTargetDepthTexture Selector.PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

DepthTargetTexture |
|

Render target dropdown |   RenderTargetTextureSelector. RenderTargetSelector   |   PROJECT_ITEM _REFERENCE   |

True |

RenderTarget |
|

Render target texture dropdown |   RenderTargetTextureSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

RenderTargetTexture |
|

Rich text editor |   RichTextEditor. PropertyGridEditor   |

STRING |

False |

N/A |
|

Scene dropdown |   SceneSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Scene |
|

Screen dropdown |   ScreenSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Screen |
|

Shader file dropdown |   ShaderSourceFileSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

ShaderSourceFile |
|

Single texture dropdown |   TextureSelector. SingleTextureSelector   |   PROJECT_ITEM _REFERENCE   |

True |

SingleTexture |
|

Slider |

Slider.PropertyGridEditor |

- INT32
- FLOAT
  |

False |

N/A |
|

Spline dropdown |   SplineSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Spline |
|

State manager selector |

StateManagerSelector |   PROJECT_ITEM _REFERENCE   |

True |

StateManager |
|

State selector |

StateSelector |   PROJECT_ITEM _REFERENCE   |

True |

State |
|

String list editor |   StringListEditor. PropertyGridEditor   |

STRING_LIST |

False |

N/A |
|

Style selector |

StyleSelector |   PROJECT_ITEM _REFERENCE   |

True |

StyleItem |
|

Sub-Page selector |

PageSelector.SubPageEditor |   PROJECT_ITEM _REFERENCE   |

True |

Node2D |
|

Sub page path Editor |

PathEditor.SubPagePathEditor |

STRING |

False |

N/A |
|

Text editor |

TextEditor.PropertyGridEditor |

STRING |

False |

N/A |
|

Text editor (float) |

TextEditor.FloatTextBoxEditor |

FLOAT |

False |

N/A |
|

Text editor (integer) |

TextEditor.IntTextBoxEditor |

INT32 |

False |

N/A |
|

Text editor (localizable) |

LocalizableTextSelector |   PROJECT_ITEM _REFERENCE   |

True |

NodeResource |
|

Text editor (value required) |   TextEditor.RequiredValue PropertyGridEditor   |

STRING |

False |

N/A |
|

Text label |   TextVisualizer. PropertyGridEditor   |

- STRING
- INT32
- FLOAT
- BOOLEAN
- ENUM
- DATE_TIME
- DATA_CONTEXT
  |

False |

N/A |
|

Texture dropdown |   TextureSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Texture |
|

Texture property type selector |   PropertyTypeNameSelector. ExportedTexturePropertyEditor   |   PROPERTY_TYPE _REFERENCE   |

False |

N/A |
|

Texture Source dropdown |   TextureSelector. TextureSourceSelector   |   PROJECT_ITEM _REFERENCE   |

True |

SingleTextureInterface |
|

Theme group selector |   ThemeGroupSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

ThemeGroup |
|

Timeline sequence dropdown |   TimelineSequenceSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

TimelineSequence |
|

Trajectory dropdown |   TrajectorySelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Trajectory |
|

Transition dropdown |   TransitionSelector. PropertyGridEditor   |   PROJECT_ITEM _REFERENCE   |

True |

Transition |
|

Trigger term source type dropdown |   TriggerTermSourceTypeSelector. PropertyGridEditor   |

ENUM |

False |

N/A |
|

Unordered string list editor |   StringListEditor. PropertyGridEditorNoOrdering   |

STRING_LIST |

False |

N/A |
