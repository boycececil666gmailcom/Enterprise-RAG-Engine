---
title: Developing Kanzi applications for Android
source: https://docs.kanzi.com/4.1.0/en/working-with/android/android.html
---

# Developing Kanzi applications for Android


You can use these frameworks to develop Kanzi applications for the Android platform:
|

Kanzi Android framework (droidfw) |

Kanzi application framework (appfw) |

Kanzi Android Service |
|

A framework dedicated for developing Kanzi applications for Android. |

A framework for developing cross-platform applications. |

A framework that hosts Kanzi Android framework (droidfw) in an Android service and enables using its functionality across process-separated client applications. |
|

Exposes the Kanzi Java API, which allows you to write application and plugin code entirely in Java or Kotlin. You do not need to write any C++ or JNI code, but you can still use native Kanzi plugins. |

You write application and plugin code in C++ and extending Android-specific functionality requires writing JNI glue code. |

As with directly using Kanzi Android framework (droidfw), you can use Kanzi Java API from within the service application. Or you can communicate from your client applications using Kanzi Client API. |
|

Provides strong integration with the Android UI, including support for multiple simultaneous Kanzi-based Views and flexible composition of Kanzi and Android UI elements. |

Kanzi is rendered to only one View at a time. |

Multiplexes Kanzi Android framework (droidfw) abilities across applications, supporting multiple simultaneous views from multiple simultaneous applications. |
|

Kanzi integrates with the Android Choreographer which runs the Kanzi main loop tasks in the Android UI thread. You can directly use the Kanzi Java API from your application code without the need for dispatcher mechanisms. |

Kanzi runs in its own thread that is separate from the Android UI thread. To invoke the Kanzi Engine C++ API from your application code through JNI, post your code as a runnable to the Kanzi `TaskDispatcher`. |

A single Kanzi Android framework (droidfw) instance runs in the service application. Clients communicate with Kanzi Client API. |
|

If you want to create an application for the Android platform, and you intend to use Android APIs and services extensively, use the Kanzi Android framework (droidfw). |

If you want to create an application for multiple platforms and you intend to share non-trivial application code between the platforms, use the Kanzi application framework (appfw). |

If you want multiple android applications to share the same Kanzi libraries and runtime, use the Kanzi Android Service. |
|

See Developing with the Kanzi Android framework (droidfw). |

See Developing for Android with the Kanzi application framework (appfw). |

See Developing with the Kanzi Android Service. |
