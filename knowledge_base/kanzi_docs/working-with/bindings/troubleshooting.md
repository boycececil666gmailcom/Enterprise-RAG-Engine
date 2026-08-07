---
title: Troubleshooting bindings
source: https://docs.kanzi.com/4.1.0/en/working-with/bindings/troubleshooting.html
---

# Troubleshooting bindings

Here you can find the error messages that the Binding Editor displays when there is an error in a binding. See Bindings expressions reference.
|

Error |

Problem |

Solution |
|

Cannot parse the binding expression because of a syntax error |

Kanzi cannot parse the binding expression because it contains a syntax error.

For example, in the above binding expression, the parameters of a function are not separated by a comma.  |

The `max()` function parameters must be separated by a comma. See max (maximum).  |
|

Assign a value to the identifier before you use it |

The binding expression contains a variable which does not have an assigned value.

For example, in the above binding expression, the variable `k` is not defined.  |

Assign a value for the variable `k`.  |
|

Invalid argument |

A function in the binding expression has too many parameters.

For example, in the above binding expression, the `pow()` function has three parameters.  |

The `pow()` function takes two parameters. See pow (power).  |
|

Invalid argument data type for the operation |

A function parameter in the binding expression has an unsupported data type.

For example, in the above binding expression, the `rotateX()` function parameters are both integers.  |

The `rotateX()` function takes the property field of a property as the first parameter, and an integer as the second parameter. See rotateX.  |
|

The attribute is not a valid property field of the property |

A property in the binding expression is using an invalid property field.

For example, in the above binding expression, Translation is not a defined property field of the Layout Transformation property.  |

Use the Translation X, Translation Y, or Translation Z property field of the Layout Transformation property. See Transformation property field bindings.  |
|

Invalid result data type |

The function in the binding expression returns a data type which does not match the data type of the target property.

For example, in the above binding expression, the `createRotationX()` function returns a quaternion data type while the target property supports the string, integer, float, and boolean data types. See createRotationX.  |

In the Binding Editor set:

- Property to a target property with a property field that supports the data type which the function in the binding expression returns.
- Property Field to a property field of the target property that supports the data type which the function in the binding expression returns.

For example, set it to ROTATION to use the quaternion data type.  |
|

Operation is not a valid binding operation |

The function in the binding expression does not exist.

For example, there is no function `mx()`.  |

Use an existing function. See Functions.  |
|

Set the target property type |

The target property type for the binding is not defined.

For example, in the above binding, the target property is not set.  |

In the Binding Editor set the Property to the property to which you want to bind.  |
|

Cannot find item |

The binding tries to refer to a node or property type in the project but cannot find that node or property type.

For example, in the above binding expression, the relative path to the Slider 3D node is not correct.  |

Make sure that the relative path to the node or property type points to the correct place.
**Tip:** When you use the @ sign in a binding expression before the path to a node, Kanzi Studio:
- Checks whether the path is valid and shows an error message in the Binding Editor if the path is not valid.
- Updates the path in the binding expression whenever the location between the source and the target nodes in the node tree changes.

With the @ sign you can create bindings only within the same prefab, not between prefabs.   |
|

Cannot use target property in the binding expression |

A binding expression, which tries to modify the current value of a property, uses the target property.

For example, the above binding expressions try to modify the values of the Layout Width and Render Transformation properties of the node.  |

In a binding expression that modifies the current value of a target property, use the `getCurrentValue()` function to get the value. See getCurrentValue.  |
