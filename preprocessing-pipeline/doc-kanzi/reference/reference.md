---
title: References
source: https://docs.kanzi.com/4.1.0/en/reference/reference.html
---

# References

Description |

Reference |

**Glossary** |

Glossary |

**Application configuration**

Use application configurations to configure your Kanzi application. See Application development.  |

Application configuration reference |

**Binding expressions**

Use bindings to set the value of a property or property field with the value from another property, property field, or a data source.

See Using bindings.  |

Bindings expressions reference |

**Triggers and actions**

Use triggers and actions to create interactions based on user input.

See Using triggers.  |

Triggers reference

Actions and messages reference  |

**Resource profiling**

Use resource profiling to measure during runtime how long it takes to load and deploy resources and prefabs in your Kanzi application.

See Measuring the loading and deployment time of resources.  |

Resource profiling reference |

**Kanzi Engine plugin custom types in Kanzi Studio**

See Extending the functionality of Kanzi Engine and Extending the functionality of Kanzi Engine with Java.  |

Reference for showing Kanzi Engine plugin custom types in Kanzi Studio |

**Kanzi Studio property editors**

Editors available in Kanzi Studio for property types that you declare in Kanzi Engine plugins.  |

Kanzi Studio property editors for property types declared in Kanzi Engine plugins |

**Keyboard input codes**

Use the keyboard input codes in your Kanzi Studio plugin to create interaction with the keyboard in your application.  |

Key input codes reference |

**Kanzi Studio commands**

You can automate Kanzi Studio tasks by running Kanzi Studio commands from a script. See Automating Kanzi Studio tasks.  |

Kanzi Studio command reference |

**Kanzi Studio default shortcut keys** |

Default shortcut keys |

**OpenGL extensions**

List of OpenGL extensions that Kanzi uses.  |

OpenGL extensions used in Kanzi |
## Kanzi property types references

Description |

Reference |

**Default and available property types for nodes and resources** |

Node and resource reference |

**Default property types** |

Property types reference |
## Kanzi API references

Description |

Reference |

**Kanzi Engine C++ API**

Use the Kanzi Engine C++ API to program Kanzi applications, develop Kanzi Engine plugins, and interface with devices and application execution environment.  |

Kanzi Engine C++ API reference |

**Kanzi Engine Java API**

Use this Kanzi Engine Java API to interact with Kanzi through a platform-agnostic API available in Java or Kotlin. See Using Java and Kotlin.  |

Kanzi Engine Java API reference |

**Kanzi Android framework API**

Use the Kanzi Android framework for full Android UI integration, including support for writing your application and plugin code entirely in Java or Kotlin.

When you use Kanzi Android framework, you do not need to write native code, but you can still use native Kanzi plugins.  |

Kanzi Android framework API reference |

**Kanzi Android application framework API**

Use the Kanzi application framework when you want to write one Kanzi application and use it on different platforms. Use the Kanzi Android application framework API to integrate a native Kanzi application into an Android application.

When you use the application framework, your application and plugin code are native.  |

Kanzi Android application framework API reference |

**Kanzi Studio plugin API**

Kanzi Studio plugins extend the functionality of Kanzi Studio and run in Kanzi Studio.

See Overview of Kanzi Studio plugin API.  |

Kanzi Studio plugin API reference |

**Kanzi Studio localization plugin API**

Kanzi uses the gettext PO file format to handle localized text resources and sets the text direction based on the first character in a string.

In PO files, you can use Unicode characters. With Unicode characters, you can also control text direction, such as the direction of left-to-right text in right-to-left locales. To learn how to control text direction with Unicode characters, see [How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls).

When you use Unicode characters, make sure you insert them correctly. On Windows and Linux, you can use the Character Map application.

To learn more about the gettext PO file format, see [The Format of PO Files](http://www.gnu.org/software/gettext/manual/gettext.html#PO-Files).

If you want to define your own import and export format for the localized text resources, use the Kanzi Studio localization plugin API to create a Kanzi Studio plugin. You can find an example of such plugin, which uses CSV to export and import text into localization tables, in the `<KanziWorkspace>/Examples/CsvPlugin` directory.
**Note:** When localized text contains a combination of simple and complex scripts, or left-to-right and right-to-left locales, in some cases the Kanzi Studio Localization Editor renders the text differently from the Kanzi Studio Preview. To fine-tune the text, use the Unicode control characters in the Localization Editor or in the PO files.
See CSV plugin example.  |
Kanzi Studio localization plugin API reference |
