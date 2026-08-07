---
title: Deploying Kanzi applications
source: https://docs.kanzi.com/4.1.0/en/working-with/deploying-applications/deploying-kanzi-applications.html
---

# Deploying Kanzi applications


While you develop Kanzi applications using Kanzi Studio and Visual Studio on Windows, you can compile your Kanzi applications for and execute on any mobile or embedded platform that supports OpenGL ES 3.0 or Vulkan 1.1.

Kanzi platform packages come with build configuration files and scripts that you can modify to adjust them to your build environment.
## Supported platforms


To deploy your Kanzi application to a target platform, you have to build it for the target platform. The output of building activity is an executable or an installer package that you can run or install on a target device. Kanzi supports building using Visual Studio 2022 on Windows and CMake for non-Windows platforms.

When you create your Kanzi application with a C++ application in Kanzi Studio, Kanzi creates a set of platform configurations. Kanzi creates platform configurations in `<ProjectName>/Application/configs/platforms`.

These platform packages are available with a Kanzi installation:

- Android (ARM, Aarch64, x86, x86_64). See Deploying Kanzi applications to Android.
- 64-bit Windows (Visual Studio 2022). See Deploying Kanzi applications to Windows.


You can receive these platform packages on request:

- QNX (aarch64, x86_64). See Deploying Kanzi applications to QNX.
- Linux (X11 GLX, Vivante fbdev, WSEGL, Wayland, DRM GBM). See Deploying Kanzi applications to Linux.
- Nucleus (Vivante fbdev, AXSB)
- iOS (aarch64). See Deploying Kanzi applications to iOS.


Contact Rightware sales at [sales@rightware.com](mailto:sales%40rightware.com) to find out more.

This table provides a summary of platforms that Kanzi supports.
|

Platform |

Windowing system |

Graphics backend |

CPU architecture |

Environment |
|

Windows |

Windows |

- WGL and OpenGL ES
- WGL and OpenGL
- Vulkan
  |

- x86
- x86_64
  |

Windows |
|

Linux |

- Vivante fbdev
- WSEGL
- X11
- Wayland
- DRM GBM
  |

- EGL and OpenGL ES
- GLX and OpenGL
- Vulkan
  |

- armhf
- x86
- aarch64
- x86_64
  |

POSIX |
|

Android |

Android |

- EGL and OpenGL ES
- Vulkan
  |

- armv7
- x86
- aarch64
- x86_64
  |

POSIX |
|

iOS |

UIKit |

Vulkan (MoltenVK) |

aarch64 |

POSIX |
|

QNX |

QNX Screen |

- EGL and OpenGL ES
- Vulkan
  |

- armv7
- x86
- aarch64
- x86_64
  |

POSIX |
|

Integrity |

- Vivante fbdev
- WSEGL
- Renesas WM
- GHS FB
- GHS GBM
  |

EGL and OpenGL ES |

- arm
- x86
- aarch64
- x86_64
  |

POSIX |
|

Nucleus |

- Vivante fbdev
- AXSB
  |

EGL and OpenGL ES |

arm |

POSIX |

If your target platform is currently not supported, we can create and add support for it.

Contact Rightware sales at [sales@rightware.com](mailto:sales%40rightware.com) to find out more.
