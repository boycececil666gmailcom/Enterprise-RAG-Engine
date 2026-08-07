---
title: Using version control systems with Kanzi
source: https://docs.kanzi.com/4.1.0/en/working-with/version-control/version-control.html
---

# Using version control systems with Kanzi

When you add your Kanzi projects to a version control system, do not add these files and directories:

- `.kzproj_N`
- `.proj.kzm_N`
- `.lock`
- `.autosave`
- `.user`
- `assets`
- `build_vs2022`
- `compressed`
- `cubemaps`
- `gen`
- `mipmaps`
- `output`
- `lib`
- `thumbnails`
**Note:** The `cubemaps` and `mipmaps` directories excluded above hold the generated faces and roughness mipmaps of image-based lighting cubemap textures. Kanzi Studio regenerates them from the source image when they are missing, such as after a fresh clone. Therefore, also add to version control the source hdr or exr image from which you created each image-based lighting cubemap texture. See Using image-based lighting cubemap textures.
## Merging projects using version control tools

After configuring your version control tool you can use the Kanzi merge tool for Kanzi project updating and merging. For the integration Kanzi requires a version control tool that provides the necessary parameters to the Kanzi merge tool.

Example of parameter types |

Description |

MINE |

The parameter for the source project. |

THEIRS |

The parameter for the target project. |

BASE |

The parameter for the base project. |

MERGED |

The parameter for the merged project. |
## Integrating the Kanzi merge tool with a version control tool

To integrate the Kanzi merge tool with a version control tool:

1.

Configure your version control tool to use the Kanzi merge tool (`<KanziInstallation>/Studio/Bin/KanziMergeTool.bat`) for .kzproj files.
2.

Pass to your version control tool the absolute path to the `KanziStudio.exe`. For example, `C:\Program Files\Rightware\Kanzi\Studio\Bin\KanziStudio.exe`.
3.

Set the version control tool parameters for the Kanzi merge tool. For example, these parameters can be called MINE, THEIRS, BASE, MERGED.

## Integrating the Kanzi merge tool with SVN version control software

To integrate the Kanzi merge tool with SVN version control software, add Kanzi merge tool as an external program for merging files with the .kzproj extension.

For example, if you are using Tortoise SVN, in TortoiseSVN select SVN > Settings > External Programs > Merge Tool > Advanced and set:

- Filename, extension or mime-type to .kzproj
- External program to

```
<KanziInstallation>/Studio/Bin/KanziMergeTool.bat "<KanziInstallation>/Studio/Bin/KanziStudio.exe"  %mine %theirs %base %merged

```

For example, if your installation of Kanzi is in `C:\Program Files\Rightware\Kanzi`, use

```
C:\Program Files\Rightware\Kanzi\Studio\Bin\KanziMergeTool.bat "C:\Program Files\Rightware\Kanzi\Studio\Bin\KanziStudio.exe" %mine %theirs %base %merged

```
