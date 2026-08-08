---
title: Using the Kanzi Command Prompt
source: https://docs.kanzi.com/4.1.0/en/best-practices/using-kanzi-command-prompt.html
---

# Using the Kanzi Command Prompt

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.
## Running the Kanzi Command Prompt

To run the Kanzi Command Prompt:

- In the Kanzi Studio main menu, select File > Open Kanzi Command Prompt.
- In the Windows Start Menu in the Rightware directory, select the Kanzi Command Prompt of the Kanzi version that you want to use.

## Setting the Kanzi Command Prompt environment variables

When you run the Kanzi Command Prompt, it sets these environment variables:

Environment variable |

Definition |

`KANZI_HOME` |

Sets the path to the Kanzi workspace. |

`ANDROID_HOME` |

Sets the path to the Android SDK. |

`JAVA_HOME` |

Sets the path to the 64-bit JDK. |

`ANDROID_STUDIO` |

Sets the path to the Android Studio executable.

For example, `C:\Program Files\Android\Android Studio\bin\studio64.exe`.  |

To set the Kanzi Command Prompt environment variables:

1.

In the Kanzi Studio main menu, select Edit > User Preferences. In the User Preferences window, in the Advanced tab, click Open Build Environment Configuration.
2.

Use one of these approaches to set the Kanzi Command Prompt environment variables:

  - Set the environment variables directly in the Build Environment Configuration window.

Kanzi Studio stores the environment variables in the `%ProgramData%\Rightware\<KanziVersion>\kanzi_environment_variables.bat` file. The Kanzi Command Prompt uses the environment variables set in this file.
  - Click kanzi_environment_variables.bat. Kanzi Studio opens in File Explorer the location of the file. In a text editor, edit the environment variables, and save the file. In the Build Environment Configuration window, click Refresh to see the updated values of the environment variables.
