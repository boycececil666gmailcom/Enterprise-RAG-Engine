---
title: Reference for showing Kanzi Engine plugin custom types in Kanzi Studio
source: https://docs.kanzi.com/4.1.0/en/working-with/plugins/reference-for-showing-kanzi-engine-plugin-custom-types.html
---

# Reference for showing Kanzi Engine plugin custom types in Kanzi Studio

You can use Kanzi Engine plugins to create custom property types and messages using the Kanzi Engine API, and use them in Kanzi Studio.

To pass to Kanzi Studio information about the custom property types and messages you create in a Kanzi Engine plugin, you declare metadata that describe these property types and messages.

The metadata enable Kanzi Engine plugin users to interact with the plugin content in Kanzi Studio.

For example, metadata defines the type of Kanzi Studio property editor for setting a value for a property, and the set of values to select from.

Declare only the metadata you need. Kanzi Studio assigns the default values to the attributes that you do not set.

This table lists the metadata attributes you can use.
|

Attribute |

Description |

Use for property types |

Use for message types |
|

displayName |

Name of the property or message the way it is shown in Kanzi Studio |

x |

x |
|

tooltip |

Tooltip for the property or message |

x |

x |
|

category |

Property category name the way it is shown in Kanzi Studio |

x |

x |
|

valueProvider |

Source of the possible values for the property that Kanzi Studio lets the user select from |

x |   |
|

host |

Node types for which Kanzi Studio suggests the property, and whether Kanzi Studio adds the property automatically or lets the user add it |

x |   |
|

editor |

Type of Kanzi Studio editor used to set the value for the property |

x |   |
|

defaultValue |

The initial value that the property gets when it is added to a node or resource in Kanzi Studio |

x |   |
|

lowerBound |

Lowest value the property can have |

x |   |
|

upperBound |

Highest value the property can have |

x |   |
|

step |

Amount by which the property value changes when a Kanzi Studio user edits it |

x |   |
|

sendable |

Whether Kanzi Studio shows the message as an action |

x |   |
|

listenable |

Whether Kanzi Studio shows the message as a trigger |

x |   |
|

sortingIndex |

Position of the property within its property category in Kanzi Studio |

x |   |
|

studioVisibility |

Whether the property or message is available in Kanzi Studio |

x |

x |
|

legacyName |

Name of the property or message in the earlier versions of the plugin |

x |

x |
## displayName

Sets the name of the property or message the way it is shown in Kanzi Studio.
|

**Syntax** |

`metadata.displayName = "name";` |
|

**Values** |
|

`name` |

Name of the property or message the way you want to see it in Kanzi Studio |      |
|

**Examples** |
