---
title: Creating meshes using the Kanzi Engine API
source: https://docs.kanzi.com/4.1.0/en/working-with/meshes/meshes-api.html
---

# Creating meshes using the Kanzi Engine API


`Mesh` stores the geometry data for rendering a `Model3D` node. A mesh has one or more clusters. Each cluster has a material and primitives. Primitives are typically triangles stored as vertex data and index data.

You can load a mesh resource from a kzb file or use the `Mesh::create` function to create a mesh. After you create a `Mesh` with the constructor, Kanzi uploads all primitive data to GPU memory instead of storing the data in CPU memory in the `Mesh`.

To define a mesh, you need:

- Vertex format definition.

This definition describes the components that define a vertex. This includes information about the vertex position, texture coordinates, normal, and tangent.
- List of vertices.

Each vertex contains components that the format definition describes.
- List of indices.

Indices describe polygons by referring to each vertex by index. When triangles describe a polygon, three indices describe a triangle. You can use several index listings, each of which uses a material.


To enable the Kanzi Studio Preview to visualize the bounding volume of a mesh, set the bounding box for that mesh. See Analyzing your application in the Preview.
## Creating a mesh


To create a cube mesh using the Kanzi Engine API:

```
// Define a CreateInfo structure and set it to not keep the data after uploading it to the GPU.
Mesh::CreateInfo createInfo;
createInfo.memoryType = GPUResource::GpuOnly;

// Describe the format for each vertex. In this example, every vertex has a position in 3D space,
// texture coordinates pointing to 2D texture space, and normal and tangent data in 3D space.

// Add a three-component position to the vertex format description.
// Use the standard Kanzi name kzPosition.
MeshVertexAttribute position("kzPosition", VertexAttribute::SemanticPosition, 0, gfx::Format::RGB32_Float, ~0u);
createInfo.vertexFormat.attributes.push_back(position);

// Add a two-component texture coordinate to the vertex format description.
// Texture coordinates enable you to use textures on a mesh.
// Use the standard Kanzi name kzTextureCoordinate0.
MeshVertexAttribute textureCoordinate("kzTextureCoordinate0", VertexAttribute::SemanticTextureCoordinate, 0, gfx::Format::RG32_Float, ~0u);
createInfo.vertexFormat.attributes.push_back(textureCoordinate);

// Add three-component normals to the vertex format description.
// Normals enable you to use lighting on a mesh.
// Use the standard Kanzi name kzNormal.
MeshVertexAttribute normal("kzNormal", VertexAttribute::SemanticNormal, 0, gfx::Format::RGB32_Float, ~0u);
createInfo.vertexFormat.attributes.push_back(normal);

// Add three-component tangents to the vertex format description.
// Tangents enable you to use normal maps on a mesh.
// Use the standard Kanzi name kzTangent.
MeshVertexAttribute tangent("kzTangent", VertexAttribute::SemanticTangent, 0, gfx::Format::RGB32_Float, ~0u);
createInfo.vertexFormat.attributes.push_back(tangent);

// Now that you added all components to the vertex format description, update the offsets,
// strides, and vertex size.
createInfo.vertexFormat.updateSizesAndOffsets();

// Create a cluster. Two triangles define a face. Since a cube has six faces, you must create
// 36 indices (2 * 3 * 6 = 36). In this example, the entire mesh uses a single material, which
// is why you need only one cluster.
createInfo.indexCount = 36;
createInfo.indexType = IndexBufferTypeUInt16;
Mesh::CreateInfo::Cluster cluster(GraphicsPrimitiveTypeTriangles, 36, material, materialUrl);
createInfo.clusters.push_back(cluster);
createInfo.indexData.resize(createInfo.indexCount * sizeof(uint16_t));

// Create the vertices. Four vertices define one face of a cube. Since a cube has six faces,
// you must create 24 vertices (4 * 6 = 24). Here you create vertex faces with normals that
// point to the same direction. This makes the faces of a cube appear flat. You cannot reuse
// vertex positions because the normals for each face are separate.
{
    createInfo.vertexCount = 24;
    // Define the positions of the cube corners.
    // This example first defines the back face, then the front face.
    const Vector3 cornerPositions[] = {
        Vector3(1.0f, 1.0f, 1.0f),
        Vector3(-1.0f, 1.0f, 1.0f),
        Vector3(-1.0f, -1.0f, 1.0f),
        Vector3(1.0f, -1.0f, 1.0f),
        Vector3(1.0f, -1.0f, -1.0f),
        Vector3(1.0f, 1.0f, -1.0f),
        Vector3(-1.0f, 1.0f, -1.0f),
        Vector3(-1.0f, -1.0f, -1.0f)
    };

    // Define texture UV coordinates for all faces.
    const Vector2 UVs[] = {
        Vector2(1.0f, 1.0f),
        Vector2(0.0f, 1.0f),
        Vector2(0.0f, 0.0f),
        Vector2(1.0f, 0.0f)
    };

    // Define vertex indices for all faces.
    const unsigned int faceIndices[][4] = {
        // Front.
        { 0, 1, 2, 3 },
        // Right.
        { 5, 0, 3, 4 },
        // Back.
        { 6, 5, 4, 7 },
        // Left.
        { 1, 6, 7, 2 },
        // Top.
        { 5, 6, 1, 0 },
        // Bottom.
        { 3, 2, 7, 4 }
    };

    // Define normals for each face.
    const Vector3 faceNormals[] = {
        Vector3(0.0f, 0.0f, 1.0f),
        Vector3(1.0f, 0.0f, 0.0f),
        Vector3(0.0f, 0.0f, -1.0f),
        Vector3(-1.0f, 0.0f, 0.0f),
        Vector3(0.0f, 1.0f, 0.0f),
        Vector3(0.0f, -1.0f, 0.0f)
    };

    // Define tangents for each face.
    const Vector3 faceTangent[] = {
        Vector3(1.0f, 0.0f, 0.0f),
        Vector3(0.0f, 0.0f, -1.0f),
        Vector3(-1.0f, 0.0f, 0.0f),
        Vector3(0.0f, 0.0f, 1.0f),
        Vector3(1.0f, 0.0f, 0.0f),
        Vector3(1.0f, 0.0f, 0.0f)
    };

    uint16_t vertexIndex = 0;

    // To generate the vertex data, loop the data arrays that you defined above.
    for (unsigned int face = 0; face < 6; ++face)
    {
        // Add two triangles.
        uint16_t* indexData = reinterpret_cast<uint16_t*>(&createInfo.indexData[0]);
        unsigned int faceBaseIndex = face * 6;

        // The first three vertices of a face define the first triangle...
        indexData[faceBaseIndex + 0] = vertexIndex + 0;
        indexData[faceBaseIndex + 1] = vertexIndex + 1;
        indexData[faceBaseIndex + 2] = vertexIndex + 2;

        // ...and the second triangle uses the two last vertices of the face with the first vertex.
        // These two triangles create a quad.
        indexData[faceBaseIndex + 3] = vertexIndex + 2;
        indexData[faceBaseIndex + 4] = vertexIndex + 3;
        indexData[faceBaseIndex + 5] = vertexIndex + 0;


        // Write vertices for the face.
        for (unsigned int faceCorner = 0; faceCorner < 4; ++faceCorner, ++vertexIndex)
        {
            unsigned int boxCorner = faceIndices[face][faceCorner];

            // Write the correct vertex for this corner of each face.
            writeVertexAttribute(createInfo, vertexIndex, 0, cornerPositions[boxCorner]);

            // UVs for each face are the same.
            writeVertexAttribute(createInfo, vertexIndex, 1, UVs[faceCorner]);

            // Normal is constant throughout the face.
            writeVertexAttribute(createInfo, vertexIndex, 2, faceNormals[face]);

            // Tangent is constant throughout the face.
            writeVertexAttribute(createInfo, vertexIndex, 3, faceTangent[face]);
        }
    }
}

// Create a Box and set it as the bounding volume of the mesh.
// Position the box in the center of the mesh. Set the dimensions of the box along each axis
// to 2.0f, that is, from point (-1, -1, -1) to point (1, 1, 1) in the local coordinate space
// of the mesh.
createInfo.boundingBox = Box::fromCenterAndSize(Vector3(0.0f, 0.0f, 0.0f), Vector3(2.0f, 2.0f, 2.0f));

// Create a mesh from the data that you defined in the CreateInfo.
MeshSharedPtr mesh = Mesh::create(domain, createInfo, "box");

```

## Creating a mesh from native handles


You can use the Kanzi Engine API to create a mesh from existing OpenGL buffer handles and query those handles from an existing mesh.

To create a cube mesh from native handles using the Kanzi Engine API:

```
// Define a CreateInfo structure.
Mesh::CreateInfo createInfo;

// Describe the format for each vertex. In this example, every vertex has a position in 3D space,
// texture coordinates pointing to 2D texture space, and normal and tangent data in 3D space.

// Add a three-component position to the vertex format description.
// Use the standard Kanzi name kzPosition.
MeshVertexAttribute position("kzPosition", VertexAttribute::SemanticPosition, 0, gfx::Format::RGB32_Float, ~0u);
createInfo.vertexFormat.attributes.push_back(position);

// Add a two-component texture coordinate to the vertex format description.
// Texture coordinates enable you to use textures on a mesh.
// Use the standard Kanzi name kzTextureCoordinate0.
MeshVertexAttribute textureCoordinate("kzTextureCoordinate0", VertexAttribute::SemanticTextureCoordinate, 0, gfx::Format::RG32_Float, ~0u);
createInfo.vertexFormat.attributes.push_back(textureCoordinate);

// Add three-component normals to the vertex format description.
// Normals enable you to use lighting on a mesh.
// Use the standard Kanzi name kzNormal.
MeshVertexAttribute normal("kzNormal", VertexAttribute::SemanticNormal, 0, gfx::Format::RGB32_Float, ~0u);
createInfo.vertexFormat.attributes.push_back(normal);

// Add three-component tangents to the vertex format description.
// Tangents enable you to use normal maps on a mesh.
// Use the standard Kanzi name kzTangent.
MeshVertexAttribute tangent("kzTangent", VertexAttribute::SemanticTangent, 0, gfx::Format::RGB32_Float, ~0u);
createInfo.vertexFormat.attributes.push_back(tangent);

// Now that you added all components to the vertex format description, update the offsets,
// strides, and vertex size.
createInfo.vertexFormat.updateSizesAndOffsets();

// Create the vertices. Four vertices define one face of a cube. Since cube has six faces,
// you must create 24 vertices (4 * 6 = 24). Here you create vertex faces with normals that
// point to the same direction. This makes the faces of a cube appear flat. You cannot reuse
// vertex positions because the normals for each face are separate.
{
    createInfo.vertexCount = 24;

    // Define the positions of the cube corners.
    // This example first defines the back face, then the front face.
    const Vector3 cornerPositions[] = {
        Vector3(1.0f, 1.0f, 1.0f),
        Vector3(-1.0f, 1.0f, 1.0f),
        Vector3(-1.0f, -1.0f, 1.0f),
        Vector3(1.0f, -1.0f, 1.0f),
        Vector3(1.0f, -1.0f, -1.0f),
        Vector3(1.0f, 1.0f, -1.0f),
        Vector3(-1.0f, 1.0f, -1.0f),
        Vector3(-1.0f, -1.0f, -1.0f)
    };

    // Define texture UV coordinates for all faces.
    const Vector2 UVs[] = {
        Vector2(1.0f, 1.0f),
        Vector2(0.0f, 1.0f),
        Vector2(0.0f, 0.0f),
        Vector2(1.0f, 0.0f)
    };

    // Define vertex indices for all faces.
    const unsigned int faceIndices[][4] = {
        // Front.
        { 0, 1, 2, 3 },
        // Right.
        { 5, 0, 3, 4 },
        // Back.
        { 6, 5, 4, 7 },
        // Left.
        { 1, 6, 7, 2 },
        // Top.
        { 5, 6, 1, 0 },
        // Bottom.
        { 3,
          2,
          7,
          4 }
    };

    // Define normals for all faces.
    const Vector3 faceNormals[] = {
        Vector3(0.0f, 0.0f, 1.0f),
        Vector3(1.0f, 0.0f, 0.0f),
        Vector3(0.0f, 0.0f, -1.0f),
        Vector3(-1.0f, 0.0f, 0.0f),
        Vector3(0.0f, 1.0f, 0.0f),
        Vector3(0.0f, -1.0f, 0.0f)
    };

    // Define tangents for all faces.
    const Vector3 faceTangent[] = {
        Vector3(1.0f, 0.0f, 0.0f),
        Vector3(0.0f, 0.0f, -1.0f),
        Vector3(-1.0f, 0.0f, 0.0f),
        Vector3(0.0f, 0.0f, 1.0f),
        Vector3(1.0f, 0.0f, 0.0f),
        Vector3(1.0f, 0.0f, 0.0f)
    };

    uint16_t vertexIndex = 0;

    vector<uint16_t> indexBuffer;
    indexBuffer.resize(36);

    // To generate the vertex data, loop the data arrays that you defined above.
    // Mesh::CreateInfo stores source bytes per attribute in attributes[i].initialData;
    // the writeVertexAttribute helper sizes each attribute's buffer on demand.
    for (unsigned int face = 0; face < 6; ++face)
    {
        // Add two triangles.
        uint16_t* indexData = indexBuffer.data();
        unsigned int faceBaseIndex = face * 6;

        // The first three vertices of a face define the first triangle...
        indexData[faceBaseIndex + 0] = vertexIndex + 0;
        indexData[faceBaseIndex + 1] = vertexIndex + 1;
        indexData[faceBaseIndex + 2] = vertexIndex + 2;

        // ...and the second triangle uses the two last vertices of the face with the first vertex.
        // These two triangles create a quad.
        indexData[faceBaseIndex + 3] = vertexIndex + 2;
        indexData[faceBaseIndex + 4] = vertexIndex + 3;
        indexData[faceBaseIndex + 5] = vertexIndex + 0;

        // Write per-corner values for all four attributes.
        for (unsigned int faceCorner = 0; faceCorner < 4; ++faceCorner, ++vertexIndex)
        {
            unsigned int boxCorner = faceIndices[face][faceCorner];
            writeVertexAttribute(createInfo, vertexIndex, 0u, cornerPositions[boxCorner]);
            writeVertexAttribute(createInfo, vertexIndex, 1u, UVs[faceCorner]);
            writeVertexAttribute(createInfo, vertexIndex, 2u, faceNormals[face]);
            writeVertexAttribute(createInfo, vertexIndex, 3u, faceTangent[face]);
        }
    }

    // Create Kanzi graphics index buffer.
    gfx::BufferCreateInfo indexBufferCreateInfo;
    indexBufferCreateInfo.name = "Custom Index Buffer";
    indexBufferCreateInfo.usageFlag = gfx::BufferUsageFlag::IndexBuffer;
    indexBufferCreateInfo.size = static_cast<uint32_t>(indexBuffer.size() * sizeof(uint16_t));
    indexBufferCreateInfo.initialData = as_bytes(toSpan(indexBuffer));
    auto indexBufferHandle = gfx::create(indexBufferCreateInfo);
    createInfo.indexBufferHandle = indexBufferHandle;
    createInfo.indexType = IndexBufferTypeUInt16;
    createInfo.indexCount = indexBuffer.size();

    // Create a cluster. Two triangles define a face. Since a cube has six faces, you must create
    // 36 indices (2 * 3 * 6 = 36). In this example, the entire mesh uses a single material, which
    // is why you need only one cluster.
    Mesh::CreateInfo::Cluster cluster(GraphicsPrimitiveTypeTriangles, indexBuffer.size(), material, materialUrl);
    createInfo.clusters.push_back(cluster);
}

// Create a Box and set it as the bounding volume of the mesh.
// Position the box in the center of the mesh. Set the dimensions of the box along each axis
// to 2.0f, that is, from point (-1, -1, -1) to point (1, 1, 1) in the local coordinate space
// of the mesh.
createInfo.boundingBox = Box::fromCenterAndSize(Vector3(0.0f, 0.0f, 0.0f), Vector3(2.0f, 2.0f, 2.0f));

// Create a mesh from the data that you defined in the CreateInfo.
MeshSharedPtr mesh = Mesh::create(domain, createInfo, "box");

```


For details, see the `Mesh` class.
## Creating meshes with instancing


When you render a large number of copies of the same mesh, performing a draw call for each copy consumes GPU time and decreases application performance. Instancing makes it possible to draw multiple copies of a mesh with different attributes, such as position, size, and color, with a single render call.

This example renders four instances of a cube mesh at different locations and with different colors.

To create a cube mesh with instancing using the Kanzi Engine API:

```
// Create a custom shader to use instanced attributes.
const char* vertexSource =
    "#version 310 es\n"
    "in vec3 kzPosition;\n"
    "in vec3 InstancePosition;\n"
    "in vec4 InstanceColor;\n"
    "uniform highp mat4 kzProjectionCameraWorldMatrix;\n"
    "out vec4 outColor;\n"
    "void main() {\n"
    "precision mediump float;\n"
    "vec3 position = kzPosition + InstancePosition;\n"
    "gl_Position = kzProjectionCameraWorldMatrix * vec4(position, 1.0);\n"
    "outColor = InstanceColor;\n"
    "}\n";

const char* fragmentSource =
    "#version 310 es\n"
    "in vec4 outColor;\n"
    "layout(location = 0) out vec4 fragColor;\n"
    "void main() {\n"
    "precision lowp float;\n"
    "fragColor = outColor;\n"
    "}\n";

ShaderProgram::CreateInfo shaderCreateInfo;
{
    auto compiler = kanzi::makeShaderCompiler();

    gfx::ShaderFormat shaderFormat = gfx::ShaderFormat::Glsl43;
    for (auto&& format : { gfx::ShaderFormat::VulkanSpirv13, gfx::ShaderFormat::GlslES30, gfx::ShaderFormat::Glsl33 })
    {
        if (gfx::isShaderFormatSupported(format))
        {
            shaderFormat = format;
            break;
        }
    }

    array<ShaderCompiler::ShaderSource, 2> sources;
    sources[0].stage = gfx::ShaderStage::Vertex;
    sources[0].source = vertexSource;

    sources[1].stage = gfx::ShaderStage::Fragment;
    sources[1].source = fragmentSource;

    constexpr auto options = ShaderCompiler::OptionFlags::Default;
    auto shaderResult = compiler->compile(sources, options, asSpan(shaderFormat), "");

    shaderCreateInfo.addSourceShader(ShaderTypeVertex, toSpan(shaderResult.shaders[shaderFormat][gfx::ShaderStage::Vertex].blob));
    shaderCreateInfo.addSourceShader(ShaderTypeFragment, toSpan(shaderResult.shaders[shaderFormat][gfx::ShaderStage::Fragment].blob));
    if (shaderResult.info)
    {
        shaderCreateInfo.reflectionInfo = kanzi::move(shaderResult.info.value());
    }
}


static const ShaderVertexAttribute kzPosition = ShaderVertexAttribute("kzPosition", VertexAttribute::SemanticPosition,
                                                                      0, GraphicsElementTypeFLOAT, 0, 3, 0, 0);
static const ShaderVertexAttribute InstancePosition = ShaderVertexAttribute("InstancePosition", VertexAttribute::SemanticPosition,
                                                                            1, GraphicsElementTypeFLOAT, 0, 3, 1, 0);
static const ShaderVertexAttribute InstanceColor = ShaderVertexAttribute("InstanceColor", VertexAttribute::SemanticColor,
                                                                         0, GraphicsElementTypeFLOAT, 0, 4, 2, 0);
shaderCreateInfo.vertexFormat.push_back(kzPosition);
shaderCreateInfo.vertexFormat.push_back(InstancePosition);
shaderCreateInfo.vertexFormat.push_back(InstanceColor);

shaderCreateInfo.addFixedUniform("kzProjectionCameraWorldMatrix");

auto shader = ShaderProgram::create(domain, shaderCreateInfo, "CustomShader");
auto material = Material::create(domain, "CustomMaterial", shader);

// Define a CreateInfo structure and set it to not keep the data after uploading it to the GPU.
Mesh::CreateInfo createInfo;
createInfo.memoryType = GPUResource::GpuOnly;

// Describe the format for each vertex. In this example, every vertex has a position in 3D space,
// and every instance has a position in 3D space and a color.

// Add a three-component position to the vertex format description.
// Use the standard Kanzi name kzPosition.
MeshVertexAttribute position("kzPosition", VertexAttribute::SemanticPosition, 0, gfx::Format::RGB32_Float, ~0u);
createInfo.vertexFormat.attributes.push_back(position);

// Add instance position.
MeshVertexAttribute instancePosition("InstancePosition", VertexAttribute::SemanticPosition, 1, gfx::Format::RGB32_Float, 0);
instancePosition.divisor = 1;
createInfo.vertexFormat.attributes.push_back(instancePosition);

// Add instance color.
MeshVertexAttribute instanceColor("InstanceColor", VertexAttribute::SemanticColor, 0, gfx::Format::RGBA8_UNorm, 3 * sizeof(float));
instanceColor.divisor = 1;
createInfo.vertexFormat.attributes.push_back(instanceColor);

// Now that you added all components to the vertex format description, update the offsets,
// strides, and sizes.
createInfo.vertexFormat.updateSizesAndOffsets();

// Initialize index data.
createInfo.indexType = IndexBufferTypeUInt16;
createInfo.indexCount = 36;
createInfo.indexData.resize(createInfo.indexCount * sizeof(uint16_t));

// Create a cluster. Two triangles define a face. Since a cube has six faces, you must create
// 36 indices (2 * 3 * 6 = 36). In this example, the entire mesh uses a single material, which
// is why you need only one cluster.
Mesh::CreateInfo::Cluster cluster(GraphicsPrimitiveTypeTriangles, 36, material, "");
createInfo.clusters.push_back(cluster);

// Create the vertices. In this example, faces share vertices, so you need only eight vertices.
{
    createInfo.vertexCount = 8;
    // Define the positions of the cube corners.
    // This example first defines the back face, then the front face.
    const Vector3 cornerPositions[] = {
        Vector3(1.0f, 1.0f, 1.0f),
        Vector3(-1.0f, 1.0f, 1.0f),
        Vector3(-1.0f, -1.0f, 1.0f),
        Vector3(1.0f, -1.0f, 1.0f),
        Vector3(1.0f, -1.0f, -1.0f),
        Vector3(1.0f, 1.0f, -1.0f),
        Vector3(-1.0f, 1.0f, -1.0f),
        Vector3(-1.0f, -1.0f, -1.0f)
    };

    // Define vertex indices for all faces.
    const uint16_t faceIndices[][4] = {
        // Front.
        { 0, 1, 2, 3 },
        // Right.
        { 5, 0, 3, 4 },
        // Back.
        { 6, 5, 4, 7 },
        // Left.
        { 1, 6, 7, 2 },
        // Top.
        { 5, 6, 1, 0 },
        // Bottom.
        { 3, 2, 7, 4 }
    };

    // To generate the vertex data, loop the data arrays that you defined above.
    for (unsigned int face = 0; face < 6; ++face)
    {
        // Add two triangles.
        uint16_t* indexData = reinterpret_cast<uint16_t*>(&createInfo.indexData[0]);
        unsigned int faceBaseIndex = face * 6;

        // The first three vertices of a face define the first triangle...
        indexData[faceBaseIndex + 0] = faceIndices[face][0];
        indexData[faceBaseIndex + 1] = faceIndices[face][1];
        indexData[faceBaseIndex + 2] = faceIndices[face][2];

        // ...and the second triangle uses the two last vertices of the face with the first vertex.
        // These two triangles create a quad.
        indexData[faceBaseIndex + 3] = faceIndices[face][2];
        indexData[faceBaseIndex + 4] = faceIndices[face][3];
        indexData[faceBaseIndex + 5] = faceIndices[face][0];
    }

    // Write vertices.
    for (unsigned int vertexIndex = 0; vertexIndex < 8; ++vertexIndex)
    {
        // Write the correct vertex for this corner of each face.
        writeVertexAttribute(createInfo, vertexIndex, 0, cornerPositions[vertexIndex]);
    }
}

// Create the instance data: float position vector with three components and packed
// 32-bit color per instance.
{
    // Create four instances of the cube.
    createInfo.instanceCount = 4;
    createInfo.instanceData.resize(createInfo.instanceCount * createInfo.vertexFormat.instanceSize);

    // Define the positions.
    const Vector3 instancePositions[] = {
        Vector3(-1.0f, -1.0f, 0.0f),
        Vector3(-1.0f, 1.0f, 0.0f),
        Vector3(1.0f, 1.0f, 0.0f),
        Vector3(1.0f, -1.0f, 0.0f)
    };

    // Define the colors: white, red, green, blue.
    const uint32_t instanceColors[] = {
        0xffffffff,
        0xffff0000,
        0xff00ff00,
        0xff0000ff
    };

    byte* instanceBuffer = createInfo.instanceData.data();
    for (unsigned instance = 0; instance < createInfo.instanceCount; ++instance)
    {
        // Copy the positions and colors to the instance data buffer.
        auto pos = reinterpret_cast<float*>(instanceBuffer + instance * createInfo.vertexFormat.instanceSize);
        *pos++ = instancePositions[instance].getX();
        *pos++ = instancePositions[instance].getY();
        *pos++ = instancePositions[instance].getZ();

        auto color = reinterpret_cast<uint32_t*>(pos);
        *color = instanceColors[instance];
    }
}
// Create a Box and set it as the bounding volume of the mesh.
// Position the box in the center of the mesh. Set the dimensions of the box along each axis
// to 4.0f, that is, from point (-2, -2, -1) to point (2, 2, 1) in the local coordinate space
// of the mesh. This includes all the instances.
createInfo.boundingBox = Box::fromCenterAndSize(Vector3(0.0f, 0.0f, 0.0f), Vector3(4.0f, 4.0f, 2.0f));

// Create a mesh from the data that you defined in the CreateInfo.
MeshSharedPtr mesh = Mesh::create(domain, createInfo, "instancedBox");

```
