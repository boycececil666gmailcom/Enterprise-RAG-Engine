---
title: Using the Kanzi views and view adapters
source: https://docs.kanzi.com/4.1.0/en/working-with/android/droidfw/views.html
---

# Using the Kanzi views and view adapters

## Adding a Kanzi view

Kanzi exposes the `KanziSurfaceView` and `KanziTextureView` view types derived from the Android `SurfaceView` and `TextureView` respectively. [](../../../_images/classes.svg)

- `KanziSurfaceView` renders directly to a surface obtained from hardware composer, which makes its performance better. But it comes with the restriction that an application can render it only behind or on the top of the rest of the views in an Activity.
- `KanziTextureView` renders to a texture like a regular view. This allows an application to mix its content freely with Android content and you can move, transform, animate, and even make it translucent.

See [Android SurfaceView vs TextureView](https://source.android.com/devices/graphics/arch-tv#surface_or_texture) or Creating a transparent view.

You can declare a Kanzi view in the Android layout and inflate that view anywhere in the same way as a regular Android view.

```
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
   xmlns:app="http://schemas.android.com/apk/res-auto">

   <com.rightware.kanzi.KanziSurfaceView
      android:id="@+id/view1"
      app:name="View1"
      app:kzbPathList="project1.kzb"
      app:startupPrefabUrl="kzb://project1/Prefabs/View1" />

```

### Creating multiple views

You can activate multiple Kanzi-based views simultaneously within an app and access them across different Activities or Fragments.
## Configuring a Kanzi view

These view types expose various configurations that you can assign directly from a layout.
|

Attribute |

Use |

Format |

Default value |
|

`name` |

Name of the view. |

string |

`Kanzi View` |
|

`kzbPathList` |

Comma-separated list of kzb files. When set, Kanzi automatically loads these files when the view is attached. You can also pass a cfg file that contains a list of kzb files that you want to load. |

string |

`null` |
|

`startupPrefabUrl` |

URL of the startup prefab. When set, Kanzi asynchronously loads and instantiates this prefab as a child of the view. |

string |

`null` |
|

`clearColor` |

Color used to clear the surface. |

color |

`0xff000000` |
|

`clearEnabled` |

Flag to enable the clearing of the surface. |

boolean |

`True` |

Alternatively, you can assign these configuration options with setters after inflation.
