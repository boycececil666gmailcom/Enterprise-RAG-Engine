---
title: OpenGL extensions used in Kanzi
source: https://docs.kanzi.com/4.1.0/en/working-with/rendering/opengl-extensions.html
---

# OpenGL extensions used in Kanzi

This table lists the OpenGL extensions that Kanzi uses.

Feature: OpenGL extensions |

Requirement |

Debugging:

- `GL_KHR_debug`

If you call `Renderer::logOpenGLInformation` and this extension is available, Kanzi uses it. |

Shader compatibility:

- `GL_ARB_ES3_compatibility`
- `GL_ARB_ES3_1_compatibility`
- `GL_ARB_ES3_2_compatibility`

If you use OpenGL ES shaders with desktop OpenGL, one of these extensions must be available. |

Vertex formats:

- `GL_ARB_half_float_vertex`
- `GL_EXT_vertex_half_float`

If you use half-float vertex formats, one of these extensions must be available, unless your platform supports OpenGL ES 3.0+ or OpenGL 4.2+. See Optimizing meshes. |

Texture and render target formats:

- `GL_EXT_texture_norm16`

If in a texture or render target you select any 16-bit signed or unsigned format, Kanzi uses this extension, if it is available. |

Texture and render target formats:

- `GL_EXT_color_buffer_half_float`

If in a texture or render target you select any 16-bit float format, Kanzi uses this extension, if it is available. |

Texture and render target formats:

- `GL_EXT_color_buffer_float`

If in a texture or render target you select any 32-bit float format, Kanzi uses this extension, if it is available. |

Texture and render target formats:

- `GL_EXT_texture_compression_s3tc`
- `GL_EXT_texture_compression_rgtc`
- `GL_ARB_texture_compression_rgtc`
- `GL_ARB_texture_compression_bptc`
- `GL_EXT_texture_compression_bptc`

If you use BCn texture formats, the corresponding format out of these must be available. |

Texture and render target formats:

- `GL_KHR_texture_compression_astc_ldr`
- `GL_KHR_texture_compression_astc_hdr`

If you use ASTC texture formats, the corresponding format out of these must be available. See Using the ASTC algorithm. |

Texture and render target formats:

- `GL_EXT_texture_filter_anisotropic`
- `GL_ARB_texture_filter_anisotropic`

If you set anisotropic filtering in any of your textures, this extension must be available. |

Advanced color blending:

- `GL_KHR_blend_equation_advanced`
- `GL_KHR_blend_equation_advanced_coherent`

If you set any node or material to use an advanced color blending mode, these extensions must be available. See Advanced color blending modes. |
