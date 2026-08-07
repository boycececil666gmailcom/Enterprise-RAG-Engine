---
title: Bindings expressions reference
source: https://docs.kanzi.com/4.1.0/en/working-with/bindings/reference-for-bindings-expressions.html
---

# Bindings expressions reference


Here you can find the reference for the bindings expressions that you can add to the bindings of your nodes, render passes, material types, styles, and state managers. See Rendering, Material types and materials, Using styles and State manager.

Blue type marks the properties that are controlled by a binding.

When you create a binding for a property, the value that comes from that binding overrides the value that you set for that property in the Properties.

> **Tip:** In the Kanzi Studio Properties window, properties with Bindings are marked in blue type, and has the Binding icon  next to it:
>
> Orange type marks properties with several override sources:
>
> If a property has multiple override sources, only the one with the highest precedence will take effect. See Property system.
>
> When creating bindings, keep in mind that:
>
> - Only bindings to similar data types are valid. For example, you can bind only color to color, vector2 to vector2, and so on. See Type casting.
> - Binding takes the value of the last expression, whether it is an assignment, unary or binary operation, or just a constant value or variable itself.
> - In bindings you can cast strings between the four fundamental types: integer, float, boolean, and string.
>
> Casts between integer, float, and boolean are implicit and depend on the type of the property that uses the value. Casts to and from string are explicit.


See Using bindings and Troubleshooting bindings.
## Syntax

### # (comments)


Use a hash at the beginning of every line that contains a comment. You can use any sequence of characters in comments.

```
# This is a comment, so you can describe your binding expressions
# Calculate the value of A
A = (2 + 4) / 3

```

### () (parentheses)


Use parentheses to group and contain expressions and parameters, and control the order of execution.

```
# Containing expressions: calculate the modulo of two values
mod(23, 27)

```


```
# Grouping expressions: first add 2 and 4, then divide the result by 3,
# and return 2
A = (2 + 4) / 3

```


```
# First add the FOV property to the Render Transformation Scale X property field,
# then divide the result of the multiplication by 2
({../Camera/Fov} + {../Box/RenderTransformation}.scaleX) / 2

```

## Operators

### = (assign)


Assigns a value to a variable.
|

**Syntax** |

`var = value` |
|

**Parameters** |
|

`var` |

any valid variable name |
|

`value` |

any supported variable value |      |
|

**Examples** |

```
# Assigns the value 2.0 to the variable A.
A = 2.0

```


```
# Assigns the value 4.0 to the variable B.
B = 4.0

```
   |
### ? (conditional)


The conditional operator takes three input parameters. If the first parameter (`condition`) evaluates to true, the operator evaluates the second parameter (`expression1`) and returns its value. If the first parameter evaluates to false, the operator evaluates the third parameter (`expression2`) and returns its value.
|

**Syntax** |

`condition ? expression1 : expression2` |
|

**Parameters** |
|

`condition` |

any expression that Kanzi can implicitly convert to boolean |
|

`expression1` |

any expression |
|

`expression2` |

any expression |      |
|

**Returns** |

the same type as parameters |
|

**Examples** |

```
# Returns the value of A.
A = 2.0
B = 4.0
(A < B) ? A : B

```
   |
### Arithmetic operators

#### + (addition)


Adds two or more values, or combines strings into one.
|

**Syntax** |

`value1 + value2` |
|

**Parameters** |
|

`value1` |

int, float, string, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, Srt2D, Srt3D, or boolean: augend |
|

`value2` |

int, float, string, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, Srt2D, Srt3D, or boolean: addend |

When you use the addition operator, keep in mind that:

- When one parameter is int, float, or boolean, the other parameter can be of any type, except string.
- When both parameters are color, vector, matrix, or SRT, their type must be the same, except in these cases:

  - You can add Srt2D and Matrix3.
  - You can add Srt3D and Matrix4.

- When either or both parameters are color, vector, matrix, or SRT, Kanzi adds the values component-wise. Kanzi converts SRT to matrix before the addition.
  |
|

**Returns** |

- If both parameters are of the same int, float, string, or boolean type, returns that type.
- If one parameter is float and the other parameter is int or boolean, returns float.
- If one parameter is int and the other parameter is boolean, returns int.
- If either parameter is color, vector, or matrix, returns that type.
- If either parameter is Srt2D, returns Matrix3.
- If either parameter is Srt3D, returns Matrix4.
  |
|

**Examples** |

```
A = 2.0
B = 4

# Returns 6.0
A + B

```


```
A = "Hello "
B = "Kanzi!"

# Returns "Hello Kanzi!"
A + B

```


```
A = 3
B = true

# Returns 4
A + B

```


```
A = Vector2(0.5, 0.5)
B = 0.1

# Returns Vector2(0.6, 0.6)
A + B

```
   |
#### - (subtraction)


Subtracts the value of the second parameter from the value of the first parameter. As a negation operator, it returns the result equivalent to multiplying the value by -1.
|

**Syntax** |

`value1 - value2` |
|

**Parameters** |
|

`value1` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, Srt2D, Srt3D, or boolean: minuend |
|

`value2` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, Srt2D, Srt3D, or boolean: subtrahend |

When you use the subtraction operator, keep in mind that:

- When one parameter is int, float, or boolean, the other parameter can be of any type.
- When both parameters are color, vector, matrix, or SRT, their type must be the same, except in these cases:

  - You can subtract Srt2D from Matrix3 and the other way around.
  - You can subtract Srt3D from Matrix4 and the other way around.

- When either or both parameters are color, vector, matrix, or SRT, Kanzi performs a component-wise subtraction. Kanzi converts SRT to matrix before the subtraction.
  |
|

**Returns** |

- If both parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameter is int or boolean, returns float.
- If one parameter is int and the other parameter is boolean, returns int.
- If either parameter is color, vector, or matrix, returns that type.
- If either parameter is Srt2D, returns Matrix3.
- If either parameter is Srt3D, returns Matrix4.
  |
|

**Examples** |

```
A = 2.0
B = 4

# Returns -2.0
A - B

```


```
A = Vector2(0.5, 0.5)
B = 0.1

# Returns Vector2(0.4, 0.4)
A - B

```
   |
#### * (multiplication)


Multiplies the values of parameters.
|

**Syntax** |

`value1 * value2` |
|

**Parameters** |
|

`value1` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, Srt2D, Srt3D, or boolean: multiplicand |
|

`value2` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, Srt2D, Srt3D, or boolean: multiplier |

When you use the multiplication operator, keep in mind that:

- When one parameter is int, float, or boolean, the other parameter can be of any type.
- When both parameters are color, vector, matrix, or SRT, their type must be the same, except in these cases:

  - You can multiply Srt2D by Matrix3.
  - You can multiply Srt3D by Matrix4.

- When both parameters are SRT or matrix, Kanzi performs a matrix multiplication.
- When either or both parameters are color, vector, matrix, or SRT, Kanzi multiplies the values component-wise. Kanzi converts SRT to matrix before the multiplication.
  |
|

**Returns** |

- If both parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameter is int or boolean, returns float.
- If one parameter is int and the other parameter is boolean, returns int.
- If either parameter is color, vector, or matrix, returns that type.
- If either parameter is Srt2D, returns Matrix3.
- If either parameter is Srt3D, returns Matrix4.
  |
|

**Examples** |

```
A = 2.0
B = 4

# Returns 8.0
A * B

```


```
A = 3
B = true

# Returns 3
A * B

```


```
A = Vector2(0.5, 0.5)
B = Vector2(0.2, 0.4)

# Returns Vector2(0.1, 0.2)
A * B

```
   |
#### / (division)


Divides the value of the first parameter by the value of the second parameter.
|

**Syntax** |

`value1 / value2` |
|

**Parameters** |
|

`value1` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, Srt2D, Srt3D, or boolean: dividend |
|

`value2` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, Srt2D, Srt3D, or boolean: divisor |

When you use the division operator, keep in mind that:

- When one parameter is int, float, or boolean, the other parameter can be of any type.
- When both parameters are color, vector, matrix, or SRT, their type must be the same, except in these cases:

  - You can divide Srt2D by Matrix3 and the other way around.
  - You can divide Srt3D by Matrix4 and the other way around.

- When either or both parameters are color, vector, matrix, or SRT, Kanzi performs a component-wise division. Kanzi converts SRT to matrix before the division.
  |
|

**Returns** |

- If both parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameter is int or boolean, returns float.
- If one parameter is int and the other parameter is boolean, returns int.
- If either parameter is color, vector, or matrix, returns that type.
- If either parameter is Srt2D, returns Matrix3.
- If either parameter is Srt3D, returns Matrix4.
  |
|

**Examples** |

```
A = 2.0
B = 4

# Returns 0.5
A / B

```


```
A = Vector2(0.5, 0.5)
B = Vector2(0.2, 0.4)

# Returns Vector2(2.5, 1.25)
A / B

```
   |
### Relational operators

#### == (equal)


Checks whether two values are equal.
|

**Syntax** |

`value1 == value2` |
|

**Parameters** |
|

`value1` |

int, float, boolean, string, Vector2, Vector3, Vector4, Matrix3, Matrix4, Srt2D, Srt3D |
|

`value2` |

the same type as `value1`, except if `value1` is int or float, int or float |      |
|

**Returns** |

boolean |
|

**Examples** |

```
A = 2.0
B = 4.0

# Returns false
A == B

```
   |
#### != (not equal)


Checks whether two values are not equal.
|

**Syntax** |

`value1 != value2` |
|

**Parameters** |
|

`value1` |

int, float, boolean, string, Vector2, Vector3, Vector4, Matrix3, Matrix4, Srt2D, Srt3D |
|

`value2` |

the same type as `value1`, except if `value1` is int or float, int or float |      |
|

**Returns** |

boolean |
|

**Examples** |

```
A = 2.0
B = 4.0

# Returns true
A != B

```
   |
#### > (greater than)


Checks whether the value of the first parameter is larger than the value of the second parameter. For two strings checks whether the first string comes after the second string in alphabetical order.
|

**Syntax** |

`value1 > value2` |
|

**Parameters** |
|

`value1` |

int, float, string |
|

`value2` |

- if `value2` is int or float: int or float
- if `value2` is string: string
  |      |
|

**Returns** |

boolean |
|

**Examples** |

```
A = 2.0
B = 4.0

# Returns false
A > B

```


```
# Returns true
"Rob Krar" > "Anna Frost"

```
   |
#### < (less than)


Checks whether the value of the first parameter is smaller than the value of the second parameter. For two strings checks whether the first string comes before the second string in alphabetical order.
|

**Syntax** |

`value1 < value2` |
|

**Parameters** |
|

`value1` |

int, float, string |
|

`value2` |

- if `value2` is int or float: int or float
- if `value2` is string: string
  |      |
|

**Returns** |

boolean |
|

**Examples** |

```
A = 2.0
B = 4.0

# Returns true
A < B

```


```
# Returns false
"Rob Krar" < "Anna Frost"

```
   |
#### >= (greater than or equal to)


Checks whether the value of the first parameter is larger than or equal to the value of the second parameter.
|

**Syntax** |

`value1 >= value2` |
|

**Parameters** |
|

`value1` |

int, float, string |
|

`value2` |

- if `value2` is int or float: int or float
- if `value2` is string: string
  |      |
|

**Returns** |

boolean |
|

**Examples** |

```
A = 2.0
B = 4.0

# Returns false
A >= B

```
   |
#### <= (less than or equal to)


Checks whether the value of the first parameter is smaller than or equal to the value of the second parameter.
|

**Syntax** |

`value1 <= value2` |
|

**Parameters** |
|

`value1` |

int, float, string |
|

`value2` |

- if `value2` is int or float: int or float
- if `value2` is string: string
  |      |
|

**Returns** |

boolean |
|

**Examples** |

```
A = 2.0
B = 4.0

# Returns true
A <= B

```
   |
### Logical operators

#### && (logical AND)


Compares two expressions:

- If both expressions evaluate to true, returns true.
- If one or both expressions evaluate to false, returns false.

|

**Syntax** |

`expression1 && expression2` |
|

**Parameters** |
|

`expression1` |

a statement that returns a boolean value |
|

`expression2` |

a statement that returns a boolean value |      |
|

**Returns** |

boolean |
|

**Examples** |

```
A = 2.0
B = 4.0

# Returns false
A < B && B < 1

```
   |
#### || (logical OR)


Compares two expressions:

- If one or both expressions evaluate to true, returns true.
- If both expressions evaluate to false, returns false.

|

**Syntax** |

`expression1 || expression2` |
|

**Parameters** |
|

`expression1` |

a statement that returns a boolean value |
|

`expression2` |

a statement that returns a boolean value |      |
|

**Returns** |

boolean |
|

**Examples** |

```
A = 2.0
B = 4.0

# Returns true
A < B || B < 1

```
   |
#### ! (logical NOT)


Inverts the boolean value of an expression:

- If expression evaluates to false, returns true.
- If expression evaluates to true, returns, false.

|

**Syntax** |

`!(expression)` |
|

**Parameters** |
|

`expression` |

a statement that returns a boolean value |      |
|

**Returns** |

boolean |
|

**Examples** |

```
A = 2.0
B = 4.0

# Returns true
!(A > B)

```
   |
### Bitwise operators

#### ~ (bitwise NOT)


Inverts the bits of the binary representation of an integer:

- Bits that are 0 become 1.
- Bits that are 1 become 0.


The bitwise NOT operation on integer \(x\) returns \(-(x + 1)\).

The operation uses complementary binaries to represent negative integers. The first bit of the binary number is the sign bit:

- If the first bit is 0, the number is positive.
- If the first bit is 1, the number is negative.

|

**Syntax** |

`~value` |
|

**Parameters** |
|

`value` |

int |      |
|

**Returns** |

int |
|

**Examples** |

```
# Binary: 01010
A = 10

# Returns -11 (binary signed two's complement: 10101)
~A

```


```
# Binary signed two's complement: 10110
A = -10

# Returns 9 (binary: 01001)
~A

```
   |
#### & (bitwise AND)


Performs the logical AND operation on each pair of the corresponding bits of the binary representations of two integers:

- If both bits are 1, the bit in the result binary representation is 1.
- If one or both bits are 0, the bit in the result binary representation is 0.

|

X |

Y |

X & Y |
|

0 |

0 |

0 |
|

0 |

1 |

0 |
|

1 |

0 |

0 |
|

1 |

1 |

1 |

The operation uses complementary binaries to represent negative integers. The first bit of the binary number is the sign bit:

- If the first bit is 0, the number is positive.
- If the first bit is 1, the number is negative.

|

**Syntax** |

`value1 & value2` |
|

**Parameters** |
|

`value1` |

int |
|

`value2` |

int |      |
|

**Returns** |

int |
|

**Examples** |

```
# Binary: 1010
A = 10
# Binary: 1100
B = 12

# Returns 8 (binary: 1000)
A & B

```


```
# Binary signed two's complement: 10110
A = -10
# Binary: 01100
B = 12

# Returns 4 (binary: 00100)
A & B

```
   |
#### | (bitwise OR)


Performs the logical OR operation on each pair of the corresponding bits of the binary representations of two integers:

- If one or both bits are 1, the bit in the result binary representation is 1.
- If both bits are 0, the bit in the result binary representation is 0.

|

X |

Y |

X | Y |
|

0 |

0 |

0 |
|

0 |

1 |

1 |
|

1 |

0 |

1 |
|

1 |

1 |

1 |

The operation uses complementary binaries to represent negative integers. The first bit of the binary number is the sign bit:

- If the first bit is 0, the number is positive.
- If the first bit is 1, the number is negative.

|

**Syntax** |

`value1 | value2` |
|

**Parameters** |
|

`value1` |

int |
|

`value2` |

int |      |
|

**Returns** |

int |
|

**Examples** |

```
# Binary: 1010
A = 10
# Binary: 1100
B = 12

# Returns 14 (binary: 1110)
A | B

```


```
# Binary signed two's complement: 10110
A = -10
# Binary: 01100
B = 12

# Returns -2 (binary signed two's complement: 11110)
A | B

```
   |
#### ^ (bitwise XOR)


Performs the logical exclusive or (XOR) operation on each pair of the corresponding bits of the binary representations of two integers:

- If the bits are different, the bit in the result binary representation is 1.
- If the bits are the same, the bit in the result binary representation is 0.

|

X |

Y |

X ^ Y |
|

0 |

0 |

0 |
|

0 |

1 |

1 |
|

1 |

0 |

1 |
|

1 |

1 |

0 |

The operation uses complementary binaries to represent negative integers. The first bit of the binary number is the sign bit:

- If the first bit is 0, the number is positive.
- If the first bit is 1, the number is negative.

|

**Syntax** |

`value1 ^ value2` |
|

**Parameters** |
|

`value1` |

int |
|

`value2` |

int |      |
|

**Returns** |

int |
|

**Examples** |

```
# Binary: 1010
A = 10
# Binary: 1100
B = 12

# Returns 6 (binary: 0110)
A ^ B

```


```
# Binary signed two's complement: 10110
A = -10
# Binary: 01100
B = 12

# Returns -6 (binary signed two's complement: 11010)
A ^ B

```
   |
#### << (bitwise left shift)


Performs a sign-extending shift of the binary representation of an integer to the left by a given number of bits.

Left shifting \(x\) by \(y\) bits:

- Adds \(y\) rightmost 0 bits to the binary representation of \(x\).
- Removes the leftmost \(y\) bits in the binary representation of \(x\).


This means that left shifting \(x\) by \(y\) bits multiplies \(x\) by 2 raised to the power of \(y\):   \[x << y \rightarrow x * 2 ^y\]

The operation uses complementary binaries to represent negative integers. The first bit of the binary number is the sign bit:

- If the first bit is 0, the number is positive.
- If the first bit is 1, the number is negative.

|

**Syntax** |

`value << shift` |
|

**Parameters** |
|

`value` |

int |
|

`shift` |

int |      |
|

**Returns** |

int |
|

**Examples** |

```
# Binary: 0011
value = 3
shift = 2

# Returns 12 (binary: 1100)
value << shift

```


```
# Binary signed two's complement: 11101
value = -3
shift = 2

# Returns -12 (binary signed two's complement: 10100)
value << shift

```
   |
#### >> (bitwise right shift)


Performs a sign-extending shift of the binary representation of an integer to the right by a given number of bits.

Right shifting \(x\) by \(y\) bits:

- Removes the rightmost \(y\) bits in the binary representation of \(x\).
- Adds to the left \(y\) copies of the leftmost bit in the binary representation of \(x\).


This means that right shifting \(x\) by \(y\) bits divides \(x\) by 2 raised to the power of \(y\):   \[x >> y \rightarrow x / 2 ^y\]

The operation rounds down the result.

The operation uses complementary binaries to represent negative integers. The first bit of the binary number is the sign bit:

- If the first bit is 0, the number is positive.
- If the first bit is 1, the number is negative.

|

**Syntax** |

`value >> shift` |
|

**Parameters** |
|

`value` |

int |
|

`shift` |

int |      |
|

**Returns** |

int |
|

**Examples** |

```
# Binary: 1100
value = 12
shift = 2

# Returns 3 (binary: 0011)
value >> shift

```


```
# Binary signed two's complement: 10100
value = -12
shift = 2

# Returns -3 (binary signed two's complement: 11101)
value >> shift

```
   |
## Constants

### Color4


Use the `Color4()` constant to create a color value.

You can convert a float or Vector 4D property to a color value. See color4.

To learn how to access the property fields in a color property, see Color property field bindings.

To learn how to convert color values between color spaces, see Color functions.

To learn how to set color values in binding expressions in the linear color workflow, see Color property bindings.
|

**Syntax** |

`Color4(r, g, b, a)` |
|

**Parameters** |
|

`r` |

0â¦1 range: red color channel value |
|

`g` |

0â¦1 range: green color channel value |
|

`b` |

0â¦1 range: blue color channel value |
|

`a` |

0â¦1 range: alpha channel value |      |
|

**Returns** |

Color |
|

**Examples** |

```
# Sets the color to white and opaque.
Color4(1, 1, 1, 1)

```


```
# Sets the color to white and opaque. Alternative syntax.
Color(1, 1, 1, 1)

```
  [](../../_images/color1.svg)

```
# Sets the color to red with 70% transparency.
Color4(1, 0, 0, 0.7)

```
  [](../../_images/color2.svg)

```
# Sets the color to red and opaque.
Color4(1, 0, 0, 1)

```
  [](../../_images/color3.svg)

```
# Invalid expression, one argument is missing.
Color4(0.1, 1, 0.4)

```
   |
### Matrix3


Use the `Matrix3()` constant to create a 3x3 matrix.

You can:

- Convert a 2D transformation to a 3x3 matrix. See matrix3x3.
- Convert a 3x3 matrix to a 2D transformation. See extractSRT2D.

|

**Syntax** |

`Matrix3(m0, m1, m2,  m3, m4, m5,  m6, m7, m8)` |
|

**Parameters** |
|

`m0..m8` |

float: elements of a Matrix 3x3 property in column-major order |      |
|

**Returns** |

Matrix 3x3 |
|

**Examples** |

```
# Creates a 3x3 identity matrix.
Matrix3(1, 0, 0,  0, 1, 0,  0, 0, 1)

```


```
# Returns a 2D transformation with the Translation X and
# Translation Y property fields set to 100:
# Srt2D(1, 1, 0, 100, 100).
extractSRT2D(Matrix3(1, 0, 0,  0, 1, 0,  100, 100, 1))

```
   |
### Matrix4


Use the `Matrix4()` constant to create a 4x4 matrix.

You can:

- Convert a 3D transformation to a 4x4 matrix. See matrix4x4.
- Convert a 4x4 matrix to a 3D transformation. See extractSRT3D.

|

**Syntax** |

`Matrix4(m0, m1, m2, m3,  m4, m5, m6, m7,  m8, m9, m10, m11,  m12, m13, m14, m15)` |
|

**Parameters** |
|

`m0..m15` |

float: elements of a Matrix 4x4 property in column-major order |      |
|

**Returns** |

Matrix 4x4 |
|

**Examples** |

```
# Creates a 4x4 identity matrix.
Matrix4(1, 0, 0, 0,  0, 1, 0, 0,  0, 0, 1, 0,  0, 0, 0, 1)

```


```
# Returns a 3D transformation with the Rotation X
# property field set to 90, and the Translation X and
# Translation Y property fields set to 2:
# Srt3D(1, 1, 1,  90, 0, 0,  2, 2, 0).
extractSRT3D(Matrix4(1, 0, 0, 0,  0, 0, 1, 0,  0, -1, 0, 0,  2, 2, 0, 1))

```
   |
### Srt2D


Use the `Srt2D()` constant to apply transformation to a 2D node with the Render Transformation or Layout Transformation properties. In the Binding Editor set the Property to Layout Transformation or Render Transformation.

You can:

- Convert a 3x3 matrix to a 2D transformation. See extractSRT2D.
- Convert a 2D transformation to a 3x3 matrix. See matrix3x3.


To learn how to access the property fields in a 2D transformation property, see Transformation property field bindings.
|

**Syntax** |

`Srt2D(scaleX, scaleY, rotation, translationX, translationY)` |
|

**Parameters** |
|

`scaleX` |

int, float: the scale of the node on the x axis in percent |
|

`scaleY` |

int, float: the scale of the node on the y axis in percent |
|

`rotation` |

int, float: the rotation of the node in degrees |
|

`translationX` |

int, float: the translation of the node on the x axis in pixels |
|

`translationY` |

int, float: the translation of the node on the y axis in pixels |      |
|

**Returns** |

SRT Transformation 2D, calculated transformation for the scale, rotation, and translation of the bound 2D node |
|

**Examples** |

```
# Applies the transformation to the bound 2D node using the Layout Transformation
# or Render Transformation property, depending on which of these properties you
# set in the Binding Editor:
# - Scales the node to 150% percent on both axes
# - Rotates the node clockwise 90 degrees
# - Translates the node 400 pixels on the x axis, and 60.5 pixels on the y axis.
Srt2D(1.5, 1.5, 90.0, 400.0, 60.5)

```
    |
### Srt3D


Use the `Srt3D()` constant to apply transformation to a 3D node with the Render Transformation or Layout Transformation properties. In the Binding Editor set the Property to Layout Transformation or Render Transformation.

You can:

- Convert a 4x4 matrix to a 3D transformation. See extractSRT3D.
- Convert a 3D transformation to a 4x4 matrix. See matrix4x4.


To learn how to access the property fields in a 3D transformation property, see Transformation property field bindings.
|

**Syntax** |

`Srt3D(scaleX, scaleY, scaleZ,  rotationX, rotationY, rotationZ,  translationX, translationY, translationZ)` |
|

**Parameters** |
|

`scaleX` |

int, float: the scale of the node on the x axis in percent |
|

`scaleY` |

int, float: the scale of the node on the y axis in percent |
|

`scaleZ` |

int, float: the scale of the node on the z axis in percent |
|

`rotationX` |

int, float: the rotation of the node on the x axis in degrees |
|

`rotationY` |

int, float: the rotation of the node on the y axis in degrees |
|

`rotationZ` |

int, float: the rotation of the node on the z axis in degrees |
|

`translationX` |

int, float: the translation of the node on the x axis in device independent units |
|

`translationY` |

int, float: the translation of the node on the y axis in device independent units |
|

`translationZ` |

int, float: the translation of the node on the z axis in device independent units |      |
|

**Returns** |

SRT Transformation 3D, calculated transformation for the scale, rotation, and translation of the bound 3D node |
|

**Examples** |

```
# Applies the transformation to the bound 3D node using the Layout Transformation
# or Render Transformation property, depending on which of these properties you
# set in the Binding Editor:
# - Scales the node to 70% on all axes
# - Rotates the node counter-clockwise 30 degrees on the x axis,
#   60 degrees on the y axis, and 30 degrees on the z axis
# - Translates the node by 2.5 device-independent units on all axes
Srt3D(0.7, 0.7, 0.7,  -30.0, -60.0, -30.0,  2.5, 2.5, 2.5)

```
    |
### Vector2


Use the `Vector2()` constant to bind a vector property that has two property fields.

You can convert a float property to a Vector 2D property. See vector2.

To learn how to access the property fields in a Vector 2D property, see Property field bindings.
|

**Syntax** |

`Vector2(x, y)` |
|

**Parameters** |
|

`x` |

float: value of the first property field of a Vector 2D property |
|

`y` |

float: value of the second property field of a Vector 2D property |      |
|

**Returns** |

Vector 2D |
|

**Examples** |

```
# In the Binding Editor set the Property to a property that uses the Vector 2D
# data type.
# For example, to set in the bound node the Horizontal Margin property:
# - Left property field to 100
# - Right property field to 50
Vector2(100, 50)

```
   |
### Vector3


Use the `Vector3()` constant to bind a vector property that has three property fields.

You can convert a float property to a Vector 3D property. See vector3.

To learn how to access the property fields in a Vector 3D property, see Property field bindings.
|

**Syntax** |

`Vector3(x, y, z)` |
|

**Parameters** |
|

`x` |

float: value of the first property field of a Vector 3D property |
|

`y` |

float: value of the second property field of a Vector 3D property |
|

`z` |

float: value of the third property field of a Vector 3D property |      |
|

**Returns** |

Vector 3D |
|

**Examples** |

```
# In the Binding Editor set the Property to a property that uses the Vector 3D
# data type.
# For example, to set in the bound Point Light node the Point Light Attenuation
# property:
# - Constant property field to 1.2
# - Linear property field to 0.01
# - Quadratic property field to 0.02
Vector3(1.2, 0.01, 0.02)

```
   |
### Vector4


Use the `Vector4()` constant to bind a vector property that has four property fields.

You can convert a float or color property to a Vector 4D property. See vector4.

To learn how to access the property fields in a Vector 4D property, see Property field bindings.
|

**Syntax** |

`Vector4(x, y, z, w)` |
|

**Parameters** |
|

`x` |

float: value of the first property field of a Vector 4D property |
|

`y` |

float: value of the second property field of a Vector 4D property |
|

`z` |

float: value of the third property field of a Vector 4D property |
|

`w` |

float: value of the fourth property field of a Vector 4D property |      |
|

**Returns** |

Vector 4D |
|

**Examples** |

```
# In the Binding Editor set the Property to a property that uses the Vector 4D
# data type.
# For example, to set in the bound Pipeline State render pass the Scissor Area
# property:
# - X to 0.2 to set the horizontal offset of the area to 20% of the width of the
#   Viewport 2D
# - Y to 0.1 to set the vertical offset of the area to 10% of the height of the
#   Viewport 2D
# - Width to 0.6 to make the area 60% of the width of the Viewport 2D
# - Height to 0.8 to make the area 80% of the height of the Viewport 2D
Vector4(0.2, 0.1, 0.6, 0.8)

```
   |
## Type casting

### bool


Converts a value to a boolean.

Casts between integer, float, and boolean are implicit and depend on the type of the property that uses the value. Casts to and from string are explicit.
|

**Syntax** |

`bool(value)` |
|

**Parameters** |
|

`value` |

int, float, string |      |
|

**Returns** |

boolean |
|

**Examples** |

```
# Converts the boolean value "True" to integer 1, adds it to the integer 41,
# and assigns the result to the variable A. Returns integer 42.
A = 41 + bool("True")

```
   |
### color4


Converts a value to a color. When converting from a float, sets the float value to the red, green, blue, and alpha channels of the color property.

To learn how to access the property fields in a color property, see Color property field bindings.

To learn how to convert color values between color spaces, see Color functions.

To learn how to set color values in binding expressions in the linear color workflow, see Color property bindings.
|

**Syntax** |

`color4(value)` |
|

**Parameters** |
|

`value` |

float, Vector4 |      |
|

**Returns** |

color |
|

**Examples** |

```
# Returns Color4(0.5, 0.5, 0.5, 0.5).
# This expression is equivalent to:
# color = Color4(0, 0, 0, 0)
# color.r = 0.5
# color.g = 0.5
# color.b = 0.5
# color.a = 0.5
# sRGBToLinear(color)
color4(0.5)

```


```
# Converts the value of the Text property in the Text Box 2D node to a float and
# returns a color where each channel is set to the value of that float.
color4(float({@../Text Box 2D/TextConcept.Text}))

```


```
# Converts the value of the MyVector4 property to a color.
color4({@../MyVector4})

```
   |
### float


Converts a value to a float.

Casts between integer, float, and boolean are implicit and depend on the type of the property that uses the value. Casts to and from string are explicit.
|

**Syntax** |

`float(value)` |
|

**Parameters** |
|

`value` |

int, boolean, string |      |
|

**Returns** |

float |
|

**Examples** |

```
# Converts the string "5" to a float, adds it to the integer 5,
# and assigns the result to the variable A. Returns float 10.000000.
A = 5 + float("5")

```


```
# Implicitly converts boolean value True to float, adds it to the float 5.1,
# and assigns the result to the variable B. Returns float 6.1.
B = 5.1 + True

```
   |
### int


Converts a value to an integer.

Casts between integer, float, and boolean are implicit and depend on the type of the property that uses the value. Casts to and from string are explicit.
|

**Syntax** |

`int(value)` |
|

**Parameters** |
|

`value` |

float, boolean, string |      |
|

**Returns** |

integer |
|

**Examples** |

```
# Explicitly converts the string "5" to an integer, adds it to the integer 5,
# and assigns the result to the variable A. Returns integer 10.
A = 5 + float("5")

```


```
# Implicitly converts boolean value True to integer, adds it to the integer 5,
# and assigns the result to the variable B. Returns integer 6.
B = 5 + True

```


```
# Explicitly converts float 5.5 to an integer, adds it to the integer and
# assigns the result to the variable C. Returns integer 7.
C = 2 + float(5.5)

```
   |
### matrix3x3


Converts a 2D transformation to a 3x3 matrix.
|

**Syntax** |

`matrix3x3(srt2d)` |
|

**Parameters** |
|

`srt2d` |

Srt2D |      |
|

**Returns** |

Matrix 3x3 |
|

**Examples** |

```
# Converts the Render Transformation property value of a 2D node to a 3x3 matrix.
matrix3x3({@./Node2D.RenderTransformation})

```


```
# Returns Matrix3(0, 1, 0,  -1, 0, 0,  200, 50, 1).
matrix3x3(Srt2D(1, 1, 90, 200, 50))

```
   |
### matrix4x4


Converts a 3D transformation to a 4x4 matrix.
|

**Syntax** |

`matrix4x4(srt3d)` |
|

**Parameters** |
|

`srt3d` |

Srt3D |      |
|

**Returns** |

Matrix 4x4 |
|

**Examples** |

```
# Converts the Render Transformation property value of a 3D node to a 4x4 matrix.
matrix4x4({@./Node3D.RenderTransformation})

```


```
# Returns Matrix4(1, 0, 0, 0,  0, 0, 1, 0,  0, -1, 0, 0,  1, 2, 0, 1).
matrix4x4(Srt3D(1, 1, 1,  90, 0, 0,  1, 2, 0))

```
   |
### string


Converts a value to a string.

Casts between integer, float, and boolean are implicit and depend on the type of the property that uses the value. Casts to and from string are explicit.
|

**Syntax** |

`string(value)` |
|

**Parameters** |
|

`value` |

int, float, boolean |      |
|

**Returns** |

string |
|

**Examples** |

```
# Converts the integer 5 to a string, concatenates it to the string
# "Five is written as ", and assigns the result to the variable A.
# Returns string "Five is written as 5".
A = "Five is written as " + string(5)

```


```
# Converts the value of the variable A to a string, concatenates it
# to the string "Number of fingers on two hands is ", and assigns the result
# to the variable B. Returns string "Number of fingers on two hands is 10".
A = 10
B = "Number of fingers on two hands is " + string(A)

```
   |
### vector2


Converts a float to a vector property that has two property fields. Sets the float value to both property fields of the vector property.
|

**Syntax** |

`vector2(float)` |
|

**Parameters** |
|

`float` |

float |      |
|

**Returns** |

Vector 2D |
|

**Examples** |

```
# Returns Vector2(0.5, 0.5).
vector2(0.5)

```


```
# In the Binding Editor set the Property to a property that uses the Vector 2D
# data type.
# For example, to set in the bound 2D node the Horizontal Margin property Left
# and Right property fields to the value of the MyFloat property:
vector2({@../MyFloat})

```
   |
### vector3


Converts a float to a vector property that has three property fields. Sets the float value to all property fields of the vector property.
|

**Syntax** |

`vector3(float)` |
|

**Parameters** |
|

`float` |

float |      |
|

**Returns** |

Vector 3D |
|

**Examples** |

```
# Returns Vector3(0.5, 0.5, 0.5).
vector3(0.5)

```


```
# In the Binding Editor set the Property to a property that uses the Vector 3D
# data type.
# For example, to set in the bound Point Light node the Point Light Attenuation
# property Constant, Linear, and Quadratic property fields to the value of the
# MyFloat property:
vector3({@../MyFloat})

```
   |
### vector4


Converts a value to a vector property that has four property fields. When converting from a float, sets the float value to all property fields of the vector property.
|

**Syntax** |

`vector4(value)` |
|

**Parameters** |
|

`value` |

float, Color |      |
|

**Returns** |

Vector 4D |
|

**Examples** |

```
# Returns Vector4(0.5, 0.5, 0.5, 0.5).
vector4(0.5)

```


```
# In the Binding Editor set the Property to a property that uses the Vector 4D
# data type. The binding sets all property fields of the bound property to the
# value of the MyFloat property.
vector4({@../MyFloat})

```


```
# In the Binding Editor set the Property to a property that uses the Vector 4D
# data type. The binding sets the bound property to the value of the Brush Color
# property in the same node.
vector4({@./ColorBrush.Color})

```
   |
## Functions

### acquire


Gets a resource by looking up the resource ID that you pass to the `acquire` function.

The resource ID must be in a resource dictionary of the node where you use the `acquire` function, or one of its ancestor nodes:

- If the resource is not yet loaded into application memory, the `acquire` function loads the resource.
- If the resource ID is not defined, the `acquire` function returns an empty value.


See Using resource dictionaries.

For example, you can create a binding that gets the resource ID of a text resource from a data source, loads the text resource, and sets a Text Block node to show the content of that text resource. If you localize that text resource, the Text Block automatically shows the value of the resource for the current locale of the application. If you change the data in your data source, the binding function gets the resource, to which the resource ID points, and updates the text.

See Using a binding to load resources.
|

**Syntax** |

`acquire(resourceID)` |
|

**Parameters** |
|

`resourceID` |

string: defines a resource ID |      |
|

**Returns** |

Resource |
|

**Examples** |

```
# Gets a text resource with a resource ID that you set in a custom property type
# MyCustomProperty whose data type is Text.
# For example, to show in a Text Block node the text to which the resource ID
# in MyCustomProperty points, bind the Text property of that Text Block node
# to this expression.
acquire({@./MyProject.MyCustomProperty})

```


```
# Gets a text resource with a resource ID that you set in a data object name
# whose data type is string.
# For example, to show in a Text Block node the text to which the resource ID
# in name points, bind the Text property of that Text Block node to this
# expression.
acquire({DataContext.item.name})

```


```
# If the node that has this binding has the key focus, returns a brush with the
# resource ID Focused Brush. Otherwise returns a brush with the resource ID
# Default Brush.
# For example, to visually indicate when a 2D node has focus, bind the Background
# Brush property of that node to this expression.
{@./Node.Focused} ? acquire("Focused Brush") : acquire("Default Brush")

```
   |
### animate


Binds a property value to a piecewise function that you define in an Animation Data item. See Using piecewise functions in bindings.

`animate` takes two arguments: the property to which you are binding the Animation Data item, and the resource ID or kzb URL of the Animation Data item where you define the piecewise function that you want to use to set the value of the bound property.

When you use a resource ID, you have to place the Animation Data item to a resource dictionary where the node that contains the binding can access it. See Using resource dictionaries.

For example, you can use the `Animate` function to set the needle in a gauge to move faster between values 0 and 100 than it does for values larger than 100.
|

**Syntax** |

`animate(property, "animationDataResource")` |
|

**Parameters** |
|

`property` |

path and name of the property you want to use to move along the animation curve instead of time |
|

`animationDataResource` |

resource ID or kzb URL of the Animation Data item the animation curve of which you want to use to set the value of the bound property |      |
|

**Examples** |

```
# Uses the Speed property to move along the animation curve
# of the Animation Data item with the resource ID Speed curve.
animate({@./Speed}, "Speed curve")

```


```
# Uses the Speed property to move along the animation curve
# of the Animation Data item with the kzb URL Speed curve.
animate({@./Speed}, "kzb://cluster/Animation Data/Speed curve")

```
   |
### continueIf


Determines whether to continue the execution of a binding:

- If the expression that you pass to the function evaluates to `false`, stops executing the binding and does not modify the value of the target property.
- If the expression that you pass to the function evaluates to `true`, continues to execute the binding.


For example, use this function to avoid updating the properties of a node when a binding receives invalid input from a data source.
|

**Syntax** |

`continueIf(condition)` |
|

**Parameters** |
|

`condition` |

Any expression that Kanzi can implicitly convert to boolean.

All nonzero int and float values evaluate to `true` and only zero evaluates to `false`.  |      |
|

**Examples** |

```
# If the value of the Text property in the Text Box 2D node represents a
# positive number, this binding writes that value to its target property.
# If the value of the Text property does not represent a positive number,
# this binding does not change the value of its target property.
textInput = {@../Text Box 2D/TextConcept.Text}
continueIf(int(textInput) > 0)
textInput

```


```
# If the value of the speed data object is a positive integer, this binding
# writes that value to its target property.
# If the value of the speed data object is negative, this binding does
# not change the value of its target property.
continueIf({DataContext.gauges.speed} >= 0)
{DataContext.gauges.speed}

```


```
# If the magnitude of the Layout Transformation Scale of the 3D node to which
# you add this binding is less than 5, returns a color value.
# For example, you can bind the Ambient Color property of a 3D node to this
# binding expression.
maxScale = 5

scaleX = {@./Node3D.LayoutTransformation}.scaleX
scaleY = {@./Node3D.LayoutTransformation}.scaleY
scaleZ = {@./Node3D.LayoutTransformation}.scaleZ

scale = sqrt(scaleX * scaleX + scaleY * scaleY + scaleZ * scaleZ)

continueIf(scale < maxScale)

color = linearTosRGB(Color4(0.0, 0.5, 0.8, 1))
color

```
   |
### format


Formats values to a string. For example, use this function to set how a Text Block node displays a property value. See Formatting display of property values.
|

**Syntax** |

`format(formatString, arguments...)` |
|

**Parameters** |
|

`formatString` |

A string expression that specifies the format of the output string. In the `formatString`, Kanzi replaces the placeholder values that you mark with `{}` with the values from the `arguments` parameter.

To learn about the available formatting rules for placeholders, see Log message argument format specification.  |
|

`arguments` |

A list of values with which to replace the placeholders in the `formatString`. |      |
|

**Returns** |

string |
|

**Examples** |

```
# Inserts the values of the 'Node.Width' and 'Node.Height'
# properties to the format string.
format("The size of this node is: {}x{}", {@./Node.Width}, {@./Node.Height})

```


```
# Formats a floating point value to two decimal places.
format("The width of this node is: {:.2}", {@./Node.Width})

```


```
# Sets the order of arguments in the format string.
speed = {DataContext.gauges.speed}
battery = {DataContext.gauges.battery}
format("Speed: {1}. Battery: {0}", battery, speed)

```
   |
### Accessor functions

#### getCurrentValue


Gets the current value of the property that you want to bind. Use this function to modify the value of the property that you bind.
|

**Syntax** |

`getCurrentValue()` |
|

**Returns** |

the current value of the target property |
|

**Examples** |

```
# Binds a property to half of the current value of that property.
getCurrentValue() * 0.5

```


```
# Binds a property field of the property, which you set as the target property
# in the Binding Editor, to the Translation X property field of the same
# property.
# For example, to bind the Render Transformation Translation Y property field
# of a node to the Render Transformation Translation X property field, in the
# Binding Editor set the Property to Render Transformation
# and Property Field to Translation Y.
getCurrentValue().translationX

```
   |
#### getField


Gets an element in a vector or matrix.
|

**Syntax** |

`getField(matrix, index)` |
|

**Parameters** |
|

`matrix` |

Vector2, Vector3, Vector4, Matrix3, or Matrix4 |
|

`index` |

int |      |
|

**Returns** |

float: the element in the vector or matrix |
|

**Examples** |

```
# Gets the value of the third element in the matrix: 2.0.
myMatrix = Matrix3(0, 1, 2,  3, 4, 5,  6, 7, 8)
getField(myMatrix, 2)

```


```
# Gets the value of the second element in the matrix: 1.0.
myVector = Vector4(0, 1, 2, 3)
getField(myVector, 1)

```
   |
#### setField


Sets the value of an element in a vector or matrix.
|

**Syntax** |

`setField(matrix, index, value)` |
|

**Parameters** |
|

`matrix` |

Vector2, Vector3, Vector4, Matrix3, or Matrix4 |
|

`index` |

int: the index of the element whose value to set |
|

`value` |

float: the value to which to set the element |      |
|

**Examples** |

```
# Sets the value of the sixth element in the matrix to 0.
# After the operation the value of the matrix is (0, 1, 2,  3, 4, 0,  6, 7, 8)
myMatrix = Matrix3(0, 1, 2,  3, 4, 5,  6, 7, 8)
setField(myMatrix, 5, 0)

```
   |
#### getRow


Gets a row vector in a matrix.
|

**Syntax** |

`getRow(matrix, index)` |
|

**Parameters** |
|

`matrix` |

Matrix3, or Matrix4 |
|

`index` |

int: the index of the row whose value to get |      |
|

**Returns** |

Vector3, Vector4: the row in the matrix |
|

**Examples** |

```
# Gets the value of the third row in the matrix: Vector3(2, 5, 8).
myMatrix = Matrix3(0, 1, 2,  3, 4, 5,  6, 7, 8)
getRow(myMatrix, 2)

```
   |
#### setRow


Sets a row vector in a matrix.
|

**Syntax** |

`setRow(matrix, index, vector)` |
|

**Parameters** |
|

`matrix` |

Matrix3, or Matrix4 |
|

`index` |

int: the index of the row whose value to set |
|

`vector` |

Vector3, or Vector4: the value to which to set the row |      |
|

**Examples** |

```
# Sets the value of the third row in the matrix to Vector3(9, 10, 11).
# After the operation the value of the matrix is
#    0,  3,  6,
#    1,  4,  7,
#    9, 10, 11
myMatrix = Matrix3(0, 1, 2,  3, 4, 5,  6, 7, 8)
setRow(myMatrix, 2, Vector3(9, 10, 11))

```
   |
#### getColumn


Gets a column vector in a matrix.
|

**Syntax** |

`getColumn(matrix, index)` |
|

**Parameters** |
|

`matrix` |

Matrix3, or Matrix4 |
|

`index` |

int: the index of the column whose value to get |      |
|

**Returns** |

Vector3, Vector4: the column in the vector or matrix |
|

**Examples** |

```
# Gets the value of the third column in the matrix: Vector3(6, 7, 8).
myMatrix = Matrix3(0, 1, 2,  3, 4, 5,  6, 7, 8)
getColumn(myMatrix, 2)

```
   |
#### setColumn


Sets a column vector in a matrix.
|

**Syntax** |

`setColumn(matrix, index, vector)` |
|

**Parameters** |
|

`matrix` |

Matrix3, or Matrix4 |
|

`index` |

int: the index of the column whose value to set |
|

`vector` |

Vector3, or Vector4: the value to which to set the column |      |
|

**Examples** |

```
# Sets the value of the third column in the matrix to Vector3(9, 10, 11).
# After the operation the value of the matrix is
#    0,  3,  9,
#    1,  4, 10,
#    2,  5, 11
myMatrix = Matrix3(0, 1, 2,  3, 4, 5,  6, 7, 8)
setColumn(myMatrix, 2, Vector3(9, 10, 11))

```
   |
### Math functions

#### abs (absolute value)


Calculates the absolute value of a number or a variable. The absolute value of a number is always positive.
|

**Syntax** |

`abs(value)` |
|

**Parameters** |
|

`value` |

int, float, Color4, Vector2, Vector3, Vector4: number to compute |      |
|

**Returns** |

the same type as parameter |
|

**Examples** |

```
# Returns 5.2
abs(-5.2)

```
   |
#### ceil (ceiling)


Calculates the closest integer value that is greater than or equal to the value of the parameter.
|

**Syntax** |

`ceil(value)` |
|

**Parameters** |
|

`value` |

int, float, Color4, Vector2, Vector3, Vector4: number to compute |      |
|

**Returns** |

the same type as parameter |
|

**Examples** |

```
# Returns 3.0
ceil(2.06)

```


```
# Returns 16.0
ceil(15.92)

```


```
# Returns -2
ceil(-2.06)

```
   |
#### clamp


Constrains a value to lie between two values. `clamp` returns the same value as `min(max(value, low), high)`.
|

**Syntax** |

`clamp(low, high, value)` |
|

**Parameters** |
|

`low` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4 or boolean: the lower end of the range to constrain the value |
|

`high` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4 or boolean: the higher end of the range to constrain the value |
|

`value` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4 or boolean: the value to constrain |

When you use the `clamp` function, keep in mind that:

- When two or more of the parameters are color, vector, or matrix, their type must be the same. The remaining parameter can be int, float, or boolean.
- When any of the parameters are color, vector, or matrix, Kanzi constrains the values component-wise.
  |
|

**Returns** |

- If all parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameters are int or boolean, returns float.
- If one parameter is int and the other parameters are boolean, returns int.
- If any of the parameters are color, vector, or matrix, returns that type.


Casts between integer, float, and boolean are implicit.  |
|

**Examples** |

```
# Returns 1.0
clamp(1, 4, 0.5)

```


```
# Returns 0.0
clamp(false, 1, -0.5)

```


```
# Returns Vector2(1.0, 4.0)
clamp(Vector2(1, 2), Vector2(3, 5), Vector2(0, 4))

```


```
# Returns Vector2(3.0, 2.0)
clamp(Vector2(1, 2), 3, Vector2(3, 2))

```
   |
#### floor


Calculates the closest integer value that is less than or equal to the value of the parameter.
|

**Syntax** |

`floor(value)` |
|

**Parameters** |
|

`value` |

int, float, Color4, Vector2, Vector3, Vector4: number to compute |      |
|

**Returns** |

the same type as parameter |
|

**Examples** |

```
# Returns 0.000000
floor(0.8)

```


```
# Returns 1.000000
floor(1.5)

```


```
# Returns 15.000000
floor(15.92)

```


```
# Returns -12.000000
floor(-11.9)

```
   |
#### max (maximum)


Determines the larger of the two values and returns the larger value.
|

**Syntax** |

`max(value1, value2)` |
|

**Parameters** |
|

`value1` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4 or boolean: the first number to compare |
|

`value2` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4 or boolean: the second number to compare |

When you use the `max` function, keep in mind that:

- When one parameter is int, float, or boolean, the other parameter can be of any type.
- When both parameters are color, vector, or matrix, their type must be the same.
- When one parameter is color, vector, or matrix, Kanzi calculates the maximum component-wise.
  |
|

**Returns** |

- If both parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameter is int or boolean, returns float.
- If one parameter is int and the other parameter is boolean, returns int.
- If either parameter is color, vector, or matrix, returns that type.
  |
|

**Examples** |

```
# Returns 5
max(2, 5)

```


```
# Returns -2.1
max(-10, -2.1)

```


```
# Returns Vector2(3.0, 2.0)
max(Vector2(3.0, 1.0), 2)

```
   |
#### min (minimum)


Determines the smaller of the two values and returns the smaller value.
|

**Syntax** |

`min(value1, value2)` |
|

**Parameters** |
|

`value1` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the first number to compare |
|

`value2` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the second number to compare |

When you use the `min` function, keep in mind that:

- When one parameter is int, float, or boolean, the other parameter can be of any type.
- When both parameters are color, vector, or matrix, their type must be the same.
- When one parameter is color, vector, or matrix, Kanzi calculates the minimum component-wise.
  |
|

**Returns** |

- If both parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameter is int or boolean, returns float.
- If one parameter is int and the other parameter is boolean, returns int.
- If either parameter is color, vector, or matrix, returns that type.
  |
|

**Examples** |

```
# Returns 2
min(2, 5)

```


```
# Returns -10.0
min(-10, -2.1)

```


```
# Returns Vector2(2.0, 1.0)
min(Vector2(3.0, 1.0), 2)

```
   |
#### mod (modulo)


Calculates the modulo that is the remainder when one number is divided by another using the mathematical modulo congruence function.

See rem (remainder).
|

**Syntax** |

`mod(value1, value2)` |
|

**Parameters** |
|

`value1` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4 or boolean: the first number to compare: dividend |
|

`value2` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4 or boolean: the first number to compare: divisor |

When you use the `mod` function, keep in mind that:

- When one parameter is int, float, or boolean, the other parameter can be of any type.
- When both parameters are color, vector, or matrix, their type must be the same.
- When one parameter is color, vector, or matrix, Kanzi calculates the modulo component-wise.
  |
|

**Returns** |

- If both parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameter is int or boolean, returns float.
- If one parameter is int and the other parameter is boolean, returns int.
- If either parameter is color, vector, or matrix, returns that type.
  |
|

**Examples** |

```
# Returns 3
mod(13, 5)

```


```
# Returns 2
mod(-13, 5)

```


```
# Returns Vector2(0.0, 1.0)
mod(Vector2(4.0, 1.0), 2)

```
   |
#### pow (power)


Calculates exponential expressions. It is an efficient way for multiplying numbers by themselves.
|

**Syntax** |

`pow(n, e)` |
|

**Parameters** |
|

`n` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: base of the exponential expression |
|

`e` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4 or boolean: power by which to raise the base |

When you use the `pow` function, keep in mind that:

- When one parameter is int, float, or boolean, the other parameter can be of any type.
- When both parameters are color, vector, or matrix, their type must be the same.
- When one parameter is color, vector, or matrix, Kanzi calculates the exponentiation component-wise.
  |
|

**Returns** |

- If both parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameter is int or boolean, returns float.
- If one parameter is int and the other parameter is boolean, returns int.
- If either parameter is color, vector, or matrix, returns that type.
  |
|

**Examples** |

```
# Is equivalent to 2*2*2*2*2 and returns 32
pow(2, 5)

```


```
# Returns Vector2(9.0, 4.0)
pow(Vector2(3.0, 2.0), 2)

```
   |
#### rem (remainder)


Calculates the remainder when one number is divided by another rounded towards zero.

See mod (modulo).
|

**Syntax** |

`rem(value1, value2)` |
|

**Parameters** |
|

`value1` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the first number to compare: dividend |
|

`value2` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the first number to compare: divisor |

When you use the `rem` function, keep in mind that:

- When one parameter is int, float, or boolean, the other parameter can be of any type.
- When both parameters are color, vector, or matrix, their type must be the same.
- When one parameter is color, vector, or matrix, Kanzi calculates the remainder component-wise.
  |
|

**Returns** |

- If both parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameter is int or boolean, returns float.
- If one parameter is int and the other parameter is boolean, returns int.
- If either parameter is color, vector, or matrix, returns that type.
  |
|

**Examples** |

```
# Returns 3
rem(13, 5)

```


```
# Returns -3
rem(-13, 5)

```


```
# Returns Vector2(2.0, 1.0)
rem(Vector2(5.0, 4.0), 3)

```
   |
#### round


Calculates the closest integer.
|

**Syntax** |

`round(value)` |
|

**Parameters** |
|

`value` |

int, float, Color4, Vector2, Vector3, Vector4: number to compute |      |
|

**Returns** |

the same type as parameter |
|

**Examples** |

```
# Returns 1.0
round(0.8)

```


```
# Returns 2.0
round(1.5)

```


```
# Returns 0.0
round(0.1)

```
   |
#### sign


Calculates the sign value of a number or a variable:

- If the number is negative, the result is -1.
- If the number is 0, the result is 0.
- If the number is positive, the result it 1.

|

**Syntax** |

`sign(value)` |
|

**Parameters** |
|

`value` |

int, float, Vector2, Vector3, Vector4: number to compute |      |
|

**Returns** |

the same type as parameter |
|

**Examples** |

```
# Returns -1
sign(-5.2)

```


```
# Returns 0
sign(0)

```


```
# Returns 1
sign(5.2)

```


```
# Returns Vector2(1, -1)
sign(Vector2(10,-10))

```
   |
#### sqrt (square root)


Calculates the square root of a number. The square root value of a number is always positive.
|

**Syntax** |

`sqrt(n)` |
|

**Parameters** |
|

`n` |

int, float, Color4, Vector2, Vector3, Vector4: number to compute |      |
|

**Returns** |

the same type as parameter, except for int it returns float |
|

**Examples** |

```
# Returns 5.0
sqrt(25)

```
   |
### Trigonometric functions

#### acos (inverse cosine)


Calculates the inverse cosine of a value.
|

**Syntax** |

`acos(value)` |
|

**Parameters** |
|

`value` |

int, float: number in the range -1 .. 1 to compute |      |
|

**Returns** |

float: angle in degrees |
|

**Examples** |

```
# Returns 60.0
acos(0.5)

```
   |
#### asin (inverse sine)


Calculates the inverse sine of a value.
|

**Syntax** |

`asin(value)` |
|

**Parameters** |
|

`value` |

int, float: number in the range -1 .. 1 to compute |      |
|

**Returns** |

float: angle in degrees |
|

**Examples** |

```
# Returns 30.0
asin(0.5)

```
   |
#### atan (inverse tangent)


Calculates the inverse tangent of a value.
|

**Syntax** |

`atan(value)` |
|

**Parameters** |
|

`value` |

int, float: number to compute |      |
|

**Returns** |

float: angle in degrees |
|

**Examples** |

```
# Returns 45.0
atan(1)

```
   |
#### atan2 (two-argument inverse tangent)


Calculates the inverse tangent of two numbers.
|

**Syntax** |

`atan2(value1, value2)` |
|

**Parameters** |
|

`value1` |

int, float: the first number to compute |
|

`value2` |

int, float: the second number to compute |      |
|

**Returns** |

float: angle in degrees |
|

**Examples** |

```
# Returns 26.565050
atan2(1, 2)

```
   |
#### cos (cosine)


Calculates the cosine of an angle.
|

**Syntax** |

`cos(value)` |
|

**Parameters** |
|

`value` |

int, float: angle in degrees |      |
|

**Returns** |

float in the range -1..1 |
|

**Examples** |

```
# Returns 0.866025
cos(30)

```
   |
#### sin (sine)


Calculates the sine of an angle.
|

**Syntax** |

`sin(value)` |
|

**Parameters** |
|

`value` |

int, float: angle in degrees |      |
|

**Returns** |

float in the range -1..1 |
|

**Examples** |

```
# Returns 0.5
sin(30)

```
   |
#### sinc (sine cardinal)


Calculates the unnormalized sine cardinal of an angle.
|

**Syntax** |

`sinc(value)` |
|

**Parameters** |
|

`value` |

int, float: angle in degrees |      |
|

**Returns** |

float:

- 1.0 if `value` equals 0
- Otherwise `sin(valueRad)/valueRad`, where `valueRad` is `value` converted to radians
  |
|

**Examples** |

```
# Returns 0.636620
sinc(90)

```
   |
#### tan (tangent)


Calculates the tangent of an angle.
|

**Syntax** |

`tan(value)` |
|

**Parameters** |
|

`value` |

int, float: angle in degrees |      |
|

**Returns** |

float |
|

**Examples** |

```
# Returns 0.577350
tan(30)

```
   |
### Interpolation functions

#### linearStep


Performs a linear interpolation between two values. `linearStep` returns the same value as `clamp(0, 1, (value - low) / (high - low))`.
|

**Syntax** |

`linearStep(low, high, value)` |
|

**Parameters** |
|

`low` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the lower end of the linear function |
|

`high` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the higher end of the linear function |
|

`value` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the value to constrain |

When you use the `linearStep` function, keep in mind that:

- When multiple parameters are color, vector, or matrix, those parameters must be of the same type.
- When any of the parameters are color, vector, or matrix, Kanzi performs the linear interpolation component-wise.
  |
|

**Returns** |

- If all parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameters are int or boolean, returns float.
- If one parameter is int and the other parameters are boolean, returns int.
- If any of the parameters are color, vector, or matrix, returns that type.
  |
|

**Examples** |

```
# Returns 0.0
linearStep(1, 4, 0.5)

```


```
# Returns 0.64 (7/11)
linearStep(-3, 8, 4.0)

```


```
# Returns Vector2(0.625, 0.75)
linearStep(Vector2(0.0, 0.2), Vector2(0.8, 0.6), 0.5)

```
   |
#### mix


Performs a linear interpolation between two values using a value to weight between them. Kanzi computes the result using this function: `value1 * (1 - weight) + value2 * weight`.
|

**Syntax** |

`mix(value1, value2, weight)` |
|

**Parameters** |
|

`value1` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the first of the two values between which to interpolate |
|

`value2` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the second of the two values between which to interpolate |
|

`weight` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the value used to interpolate between `value1` and `value2` |

When you use the `mix` function, keep in mind that:

- When multiple parameters are color, vector, or matrix, those parameters must be of the same type.
- When any of the parameters are color, vector, or matrix, Kanzi performs the linear interpolation component-wise.
  |
|

**Returns** |

- If all parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameters are int or boolean, returns float.
- If one parameter is int and the other parameters are boolean, returns int.
- If any of the parameters are color, vector, or matrix, returns that type.
  |
|

**Examples** |

```
# Returns 2.5
mix(1, 4, 0.5)

```


```
# Returns Vector2(0.4, 0.4)
mix(Vector2(0.0, 0.2), Vector2(0.8, 0.6), 0.5)

```


```
# Returns a color property value that is the result of the linear
# interpolation between the values of the Diffuse Color property
# of the Sphere and Box nodes. The expression uses the Value
# property of the Slider node to set the weight.
mix({#Sphere/Diffuse}, {#Box/Diffuse}, {#Slider/RangeConcept.Value})

```
   |
#### smoothStep


Performs a smooth Hermite interpolation between `low` and `high` values using the `value` to weight between them, when `low` < `value` < `high`.

`smoothStep` returns the same value as:

```
t = clamp((value - low) / (high - low), 0.0, 1.0)
t * t * (3.0 - 2.0 * t)

```


Use smoothstep interpolation when you want a threshold function with a smooth transition.

See smootherStep.
|

**Syntax** |

`smoothStep(low, high, value)` |
|

**Parameters** |
|

`low` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the lower end of the Hermite function |
|

`high` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the higher end of the Hermite function |
|

`value` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the value used to weight between `low` and `high` |

When you use the `smoothStep` function, keep in mind that:

- When multiple parameters are color, vector, or matrix, those parameters must be of the same type.
- When any of the parameters are color, vector, or matrix, Kanzi performs the interpolation component-wise.
  |
|

**Returns** |

- If all parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameters are int or boolean, returns float.
- If one parameter is int and the other parameters are boolean, returns int.
- If any of the parameters are color, vector, or matrix, returns that type.
  |
|

**Examples** |

```
# Returns 0.104
smoothStep(0, 1, 0.2)

```


```
# Returns Vector2(0.683594, 0.843750)
smoothStep(Vector2(0.0, 0.2), Vector2(0.8, 0.6), 0.5)

```
   |
#### smootherStep


Performs a sigmoidal Hermite interpolation between `low` and `high` values using the `value` to weight between them, when `low` < `value` < `high`.

`smootherStep` returns the same value as:

```
t = clamp((value - low) / (high - low), 0.0, 1.0)
t * t * t * (t * (t * 6.0 - 15.0) + 10.0)

```


Use smootherstep interpolation when you want a threshold function with a smooth transition.

See smoothStep.
|

**Syntax** |

`smootherStep(value)` |
|

**Parameters** |
|

`low` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the lower end of the smootherstep function |
|

`high` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the higher end of the smootherstep function |
|

`value` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4, or boolean: the value used to weight between `low` and `high` |

When you use the `smootherStep` function, keep in mind that:

- When multiple parameters are color, vector, or matrix, those parameters must be of the same type.
- When any of the parameters are color, vector, or matrix, Kanzi performs the interpolation component-wise.
  |
|

**Returns** |

- If all parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameters are int or boolean, returns float.
- If one parameter is int and the other parameters are boolean, returns int.
- If any of the parameters are color, vector, or matrix, returns that type.
  |
|

**Examples** |

```
# Returns 0.05792
smootherStep(0, 1, 0.2)

```


```
# Returns Vector2(0.724792, 0.896484)
smootherStep(Vector2(0.0, 0.2), Vector2(0.8, 0.6), 0.5)

```
   |
#### step


Compares a value to a threshold.
|

**Syntax** |

`step(threshold, value)` |
|

**Parameters** |
|

`threshold` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4 or boolean: threshold to compare against |
|

`value` |

int, float, Color4, Vector2, Vector3, Vector4, Matrix3, Matrix4 or boolean: the value to compare against the threshold |

When you use the `step` function, keep in mind that:

- When both parameters are color, vector, or matrix, their type must be the same.
- When any of the parameters are color, vector, or matrix, Kanzi calculates the step component-wise.
  |
|

**Returns** |

- If both parameters are of the same int, float, or boolean type, returns that type.
- If one parameter is float and the other parameter is int or boolean, returns float.
- If one parameter is int and the other parameter is boolean, returns int.
- If either parameter is color, vector, or matrix, returns that type.


For example, for float:

- 0.0 if the `value` is lower than the `threshold`
- 1.0 if the `value` equals or is greater than the `threshold`
  |
|

**Examples** |

```
# Returns 1.0
step(2, 5)

```


```
# Returns 0.0
step(0.0, -0.1)

```


```
# Returns 1.0
step(1.0, 1.0)

```
   |
### Vector functions

#### length (magnitude)


Calculates the length (or magnitude) of a vector.
|

**Syntax** |

`length(vector)` |
|

**Parameters** |
|

`vector` |

Vector2, Vector3, Vector4 |      |
|

**Returns** |

float |
|

**Examples** |

```
# Returns 1
length(Vector3(1, 0, 0))

```


```
# Returns 1.414214
length(Vector2(1, 1))

```
   |
#### normalize


Calculates the normalized, or unit vector, which has the same direction as the input vector, but has a length of 1.
|

**Syntax** |

`normalize(vector)` |
|

**Parameters** |
|

`vector` |

Vector2, Vector3, Vector4 |      |
|

**Returns** |

the same type as parameter |
|

**Examples** |

```
# Returns Vector3(1, 0, 0)
normalize(Vector3(5, 0, 0))

```
   |
#### cross (vector product)


Calculates the vector product of two Vector3 or Vector4 values.
|

**Syntax** |

`cross(vector1, vector2)` |
|

**Parameters** |
|

`vector1` |

Vector3, Vector4 |
|

`vector2` |

the same type as the `vector1` parameter |

For Vector4 the operation ignores the last, or `w`, component. The last component of the resulting Vector4 has a value of 0.  |
|

**Returns** |

the same type as parameters |
|

**Examples** |

```
# Returns Vector3(0, -3, 3)
cross(Vector3(1, 0, 0), Vector3(3, 3, 3))

```
   |
#### dot (scalar product)


Calculates the scalar product of two vectors of the same length.
|

**Syntax** |

`dot(vector1, vector2)` |
|

**Parameters** |
|

`vector1` |

Vector2, Vector3, Vector4 |
|

`vector2` |

the same type as `vector1` |      |
|

**Returns** |

float |
|

**Examples** |

```
# Returns 18.0
dot(Vector3(2, 2, 2), Vector3(3, 3, 3))

```
   |
### Matrix and transformation functions

#### createRotation


Creates rotation in either the Layout Transformation or the Render Transformation property using the quaternion data type. The quaternion data type is used for rotation property fields. See createRotationX, createRotationY, createRotationZ, rotate, rotateX, rotateY, rotateZ.
|

**Syntax** |

`createRotation(x, y, z)` |
|

**Parameters** |
|

`x` |

int or float: the rotation on the X axis in degrees |
|

`y` |

int or float: the rotation on the Y axis in degrees |
|

`z` |

int or float: the rotation on the Z axis in degrees |      |
|

**Returns** |

quaternion |
|

**Examples** |

```
# Rotates the bound node:
# - 45 degrees clockwise on the X axis
# - 35 degrees clockwise on the Y axis
# - 30 degrees clockwise on the Z axis
createRotation(-45, -35, -30)

```
  [](../../_images/createrotation.svg)  |
#### createRotationX


Creates rotation in the Layout Transformation or the Render Transformation property on the X axis using quaternion data type. The quaternion data type is used for rotation property fields. See createRotation, createRotationY, createRotationZ, rotate, rotateX, rotateY, rotateZ.
|

**Syntax** |

`createRotationX(x)` |
|

**Parameters** |
|

`x` |

int or float: the rotation on the X axis in degrees |      |
|

**Returns** |

quaternion |
|

**Examples** |

```
# Rotates the bound node 55 degrees clockwise on the X axis.
createRotationX(-55)

```
  [](../../_images/createrotationx.svg)  |
#### createRotationY


Creates rotation in the Layout Transformation or the Render Transformation property on the Y axis using quaternion data type. The quaternion data type is used only for rotation property fields. See createRotation, createRotationX, createRotationZ, rotate, rotateX, rotateY, rotateZ.
|

**Syntax** |

`createRotationY(y)` |
|

**Parameters** |
|

`y` |

int or float: the rotation on the Y axis in degrees |      |
|

**Returns** |

quaternion |
|

**Examples** |

```
# Rotates the bound node 55 degrees clockwise on the Y axis.
createRotationY(-55)

```
  [](../../_images/createrotationy.svg)  |
#### createRotationZ


Creates rotation in the Layout Transformation or the Render Transformation property on the Z axis using quaternion data type. The quaternion data type is used only for rotation property fields. See createRotation, createRotationX, createRotationY, rotate, rotateX, rotateY, rotateZ.
|

**Syntax** |

`createRotationZ(z)` |
|

**Parameters** |
|

`z` |

int or float: the rotation on the Z axis in degrees |      |
|

**Returns** |

quaternion |
|

**Examples** |

```
# Rotates the bound node 55 degrees counterclockwise on the Z axis.
createRotationZ(55)

```
  [](../../_images/createrotationz.svg)  |
#### extractEulerX


Extracts the X Euler angle from the Layout Transformation or the Render Transformation properties. You can use `extractEulerX` for rotation property fields. `extractEulerX` takes a quaternion data type value as a parameter and returns float data. When you set an angle in an SRT3D property, the angle is stored in quaternion data type. Because the `extractEulerX` function extracts the angle from the quaternion, the returned Euler angle is not the same as the angle originally set in the SRT3D property. Both angles define the same rotation. See extractEulerY, extractEulerZ, createRotation, createRotationX, createRotationY, rotate, rotateX, rotateY, rotateZ.
|

**Syntax** |

`extractEulerX(rotationField)` |
|

**Parameters** |
|

`rotationField` |

rotation property field of either the Layout Transformation or the Render Transformation property |      |
|

**Returns** |

float |
|

**Examples** |

```
# Extracts the X Euler angle from a rotation property field
# of the Layout Transformation property.
extractEulerX({@./Node3D.LayoutTransformation}.rotation)

```


```
# Extracts the X Euler angle from the rotation property field
# of the Layout Transformation property and binds the value
# of the X Euler angle to the Rotation Y property field.
a = extractEulerX({@./Node3D.LayoutTransformation}.rotation)
createRotation(0, a, 0)

```
   |
#### extractEulerY


Extracts the Y Euler angle from the Layout Transformation or the Render Transformation properties. You can use `extractEulerY` for rotation property fields. `extractEulerY` takes a quaternion data type value as a parameter and returns float data.

When you set an angle in an SRT3D property, the angle is stored in quaternion data type. Because the `extractEulerX` function extracts the angle from the quaternion, the returned Euler angle is not the same as the angle originally set in the SRT3D property. Both angles define the same rotation.

See extractEulerX, extractEulerZ, createRotation, createRotationX, createRotationY, rotate, rotateX, rotateY, rotateZ.
|

**Syntax** |

`extractEulerY(rotationField)` |
|

**Parameters** |
|

`rotationField` |

rotation property field of either the Layout Transformation or the Render Transformation property |      |
|

**Returns** |

float |
|

**Examples** |

```
# Extracts the Y Euler angle from a rotation property field
# of the Layout Transformation property.
extractEulerY({@./Node3D.LayoutTransformation}.rotation)

```
   |
#### extractEulerZ


Extracts the Z Euler angle from the Layout Transformation or the Render Transformation properties. You can use `extractEulerZ` for rotation property fields. `extractEulerZ` takes a quaternion data type value as a parameter and returns float data.

When you set an angle in an SRT3D property, the angle is stored in quaternion data type. Because the `extractEulerX` function extracts the angle from the quaternion, the returned Euler angle is not the same as the angle originally set in the SRT3D property. Both angles define the same rotation.

See extractEulerX, extractEulerY, createRotation, createRotationX, createRotationY, rotate, rotateX, rotateY, rotateZ.
|

**Syntax** |

`extractEulerZ(rotationField)` |
|

**Parameters** |
|

`rotationField` |

rotation property field of either the Layout Transformation or the Render Transformation property |      |
|

**Returns** |

float |
|

**Examples** |

```
# Extracts the Z Euler angle from a rotation property field
# of the Layout Transformation property.
extractEulerZ({@./Node3D.LayoutTransformation}.rotation)

```
   |
#### extractSRT2D


Extracts a 2D transformation from a 3x3 matrix.
|

**Syntax** |

`extractSRT2D(matrix3)` |
|

**Parameters** |
|

`matrix3` |

Matrix3 |      |
|

**Returns** |

Srt2D |
|

**Examples** |

```
# Returns a 2D transformation with the Translation X and
# Translation Y property fields set to 100:
# Srt2D(1, 1, 0, 100, 100).
extractSRT2D(Matrix3(1, 0, 0,  0, 1, 0,  100, 100, 1))

```
   |
#### extractSRT3D


Extracts a 3D transformation from a 4x4 matrix.
|

**Syntax** |

`extractSRT3D(matrix4)` |
|

**Parameters** |
|

`matrix4` |

Matrix4 |      |
|

**Returns** |

Srt3D |
|

**Examples** |

```
# Returns a 3D transformation with the Rotation X
# property field set to 90, and the Translation X and
# Translation Y property fields set to 2:
# Srt3D(1, 1, 1,  90, 0, 0,  2, 2, 0).
extractSRT3D(Matrix4(1, 0, 0, 0,  0, 0, 1, 0,  0, -1, 0, 0,  2, 2, 0, 1))

```
   |
#### inverse


Calculates the inverse matrix of a matrix or SRT, or the inverse of a quaternion. Kanzi uses the quaternion data type for the rotation property fields of the Layout Transformation and Render Transformation properties.
|

**Syntax** |

`inverse(value)` |
|

**Parameters** |
|

`value` |

Matrix3, Matrix4, quaternion, Srt2D, Srt3D |      |
|

**Returns** |

- for Matrix3 and Srt2D returns Matrix3
- for Matrix4 and Srt3D returns Matrix4
- for quaternion returns quaternion
  |
|

**Examples** |

```
# Returns Matrix3(0.5, 0.0, 0.0,  0.0, 0.5, 0.0,  0.0, 0.0, 1.0)
inverse(Srt2D(2, 2, 0, 0, 0))

```


```
# Returns the inverse matrix of the Render Transformation rotation of
# the Box node.
inverse({@../Box/Node3D.RenderTransformation}.rotation)

```
   |
#### rotate


Creates whole SRT3D rotation property fields. You can use the SRT3D data type with the Layout Transformation and the Render Transformation properties. See rotateX, rotateY, rotateZ, createRotation, createRotationX, createRotationY, createRotationZ, getCurrentValue.
|

**Syntax** |

`rotate(rotationField, value)` |
|

**Parameters** |
|

`rotationField` |

rotation property field of either the Layout Transformation or the Render Transformation property |
|

`value` |

Vector3 |      |
|

**Returns** |

quaternion |
|

**Examples** |

```
# Rotates the bound node:
# - 45 degrees counterclockwise on the X axis
# - 35 degrees clockwise on the Y axis
# - 30 degrees clockwise on the Z axis
rotate(getCurrentValue().rotation, Vector3(45, -35, -30))

```
  [](../../_images/rotate.svg)  |
#### rotateX


Creates whole SRT3D rotation property fields on the X axis. You can use the SRT3D data type with the Layout Transformation and the Render Transformation properties. See rotate, createRotation, createRotationX, createRotationY, createRotationZ, getCurrentValue.
|

**Syntax** |

`rotateX(rotationField, value)` |
|

**Parameters** |
|

`rotationField` |

rotation property field of either the Layout Transformation or the Render Transformation property |
|

`value` |

int, or float |      |
|

**Returns** |

quaternion |
|

**Examples** |

```
# Rotates the bound node 45 degrees clockwise on the X axis.
rotateX(getCurrentValue().rotation, -45)

```
  [](../../_images/rotatex.svg)  |
#### rotateY


Creates whole SRT3D rotation property fields on the Y axis. You can use the SRT3D data type with the Layout Transformation and the Render Transformation properties. See rotate, createRotation, createRotationX, createRotationY, createRotationZ, getCurrentValue.
|

**Syntax** |

`rotateY(rotationField, value)` |
|

**Parameters** |
|

`rotationField` |

rotation property field of either the Layout Transformation or the Render Transformation property |
|

`value` |

int, or float |      |
|

**Returns** |

quaternion |
|

**Examples** |

```
# Rotates the bound node 45 degrees clockwise on the Y axis.
rotateY(getCurrentValue().rotation, -45)

```
  [](../../_images/rotatey.svg)  |
#### rotateZ


Creates whole SRT3D rotation property fields on the Z axis. You can use the SRT3D data type with the Layout Transformation and the Render Transformation properties. See rotate, createRotation, createRotationX, createRotationY, createRotationZ, getCurrentValue.
|

**Syntax** |

`rotateZ(rotationField, value)` |
|

**Parameters** |
|

`rotationField` |

rotation property field of either the Layout Transformation or the Render Transformation property |
|

`value` |

int, or float |      |
|

**Returns** |

quaternion |
|

**Examples** |

```
# Rotates the bound node 45 degrees counterclockwise on the Z axis.
rotateZ(getCurrentValue().rotation, 45)

```
  [](../../_images/rotatez.svg)  |
#### transform


Uses matrix or SRT to transform a vector.
|

**Syntax** |

`transform(matrix, vector)` |
|

**Parameters** |
|

`matrix` |

Matrix3: transforms Vector2, Vector3

Matrix4: transforms Vector3, Vector4

Srt2D: transforms Vector2, Vector3

Srt3D: transforms Vector3, Vector4  |
|

`vector` |

Vector2, Vector3, Vector4: the vector to transform |      |
|

**Returns** |

the same type as the `vector` parameter |
|

**Examples** |

```
# Returns Vector3(3.0, -2.0, 2.0)
myMatrix = Matrix4(1, 0, 0, 0,  0, 0, 1, 0,  0, -1, 0, 0,  1, 0, 0, 1)
transform(myMatrix, Vector3(2, 2, 2))

```


```
# Returns the transformation of Vector2(2, 2) by the Render Transformation
# property of the node.
transform({@./Node2D.RenderTransformation}, Vector2(2, 2))

```


```
# You can bind the 3D transformation of a node to this binding expression.
value = getCurrentValue()
transform = transform(value, Vector3(2, 2, 2))
value.translationX = transform.vectorX
value.translationY = transform.vectorY
value.translationZ = transform.vectorZ
value

```


For example, the transform of Vector2 by Srt2D follows this equation where \(S\) is scale, \(R\) is rotation, and \(T\) is translation:   \[ \begin{align}\begin{aligned}transform(Srt2D(SX, SY, R, TX, TY), Vector2(X, Y))\\\begin{split}= \begin{pmatrix} SX * (cos(R) * X - sin(R) * Y) + TX\\ SY * (sin(R) * X + cos(R) * Y) + TY \end{pmatrix}\end{split}\end{aligned}\end{align} \]

This is the matrix representation of the equation:   \[\begin{split}\begin{bmatrix} SX * cos(R) & -SY * sin(R) & TX\\ SY * sin(R) & SY * cos(R) & TY \\ 0 & 0 & 1 \end{bmatrix} * \begin{bmatrix} X\\ Y\\ 1 \end{bmatrix}\end{split}\]   |
#### transpose


Calculates the transpose of a matrix.
|

**Syntax** |

`transpose(value)` |
|

**Parameters** |
|

`value` |

Matrix3, Matrix4 |      |
|

**Returns** |

the same type as the input parameter |
|

**Examples** |

```
# Returns Matrix3(1, 4, 7,  2, 5, 8,  3, 6, 9)
transpose(Matrix3(1, 2, 3,  4, 5, 6,  7, 8, 9)

```
   |
### Color functions

#### hslToSrgb


Converts a value from HSL color space to sRGB color space. This function does not convert the alpha channel of a color value.

For example, use this function to convert an HSL color value, which comes from a data source, to sRGB color space before you set the Brush Color property of a node to that color.
|

**Syntax** |

`hslToSrgb(value)` |
|

**Parameters** |
|

`value` |

Vector4, Vector3 |      |
|

**Returns** |

If the parameter is Vector4, returns Vector4. If the parameter is Vector3, returns Vector3. |
|

**Examples** |

```
# Returns Vector3(1, 0, 0))
sourceColor = Vector3(0, 1, 0.5)
rgbVector = hslToSrgb(sourceColor)
rgbVector

```


```
# Interprets the values of three sliders as hue, saturation, and lightness
# values and converts the resulting HSL color through sRGB color space to
# linear color space.
# For example, to fill an Empty Node 2D node with the color, bind the
# Brush Color property of that node to this binding expression.
#
hslVec = Vector4(0, 0, 0, 1)
# Get the hue from the value of a slider whose range is 0 .. 360.
hslVec.x = {@../Hue Slider/RangeConcept.Value} / 360
# Get the saturation from the value of a slider whose range is 0 .. 100.
hslVec.y = {@../Saturation Slider/RangeConcept.Value} / 100
# Get the lightness from the value of a slider whose range is 0 .. 100.
hslVec.z = {@../Lightness Slider/RangeConcept.Value} / 100
# Convert the color from HSL to sRGB color space.
srgbColor = Color4(hslToSrgb(hslVec))
# Convert the color from sRGB to linear color space.
sRGBToLinear(srgbColor)

```


```
# Interprets the translation of a 3D node as an HSL color and converts that
# color to sRGB.
# For example, when you bind the Ambient Color property of a 3D node to this
# binding expression, the color changes when you move the node along the 3D
# axes within the range 0 .. 10:
# - Hue changes along the x axis.
# - Saturation increases along the y axis.
# - Lightness increases along the z axis.

x = {@./Node3D.RenderTransformation}.translationX
y = {@./Node3D.RenderTransformation}.translationY
z = {@./Node3D.RenderTransformation}.translationZ

position = Vector3(0, 0, 0)
position.x = abs(x) / 10
position.y = abs(y) / 10
position.z = abs(z) / 10

rgbVector = hslToSrgb(position)

output = Color4(0, 0, 0, 1)
output.r = rgbVector.x
output.g = rgbVector.y
output.b = rgbVector.z

sRGBToLinear(output)

```
   |
#### linearTosRGB


Converts a value from linear color space to sRGB color space. This function does not convert the alpha channel of a color value.

For example, use this function in a uniform binding in a material type whose shader expects sRGB color.
|

**Syntax** |

`linearTosRGB(value)` |
|

**Parameters** |
|

`value` |

Color4, float, Vector3 |      |
|

**Returns** |

the same type as the input parameter |
|

**Examples** |

```
# Converts the value of the Diffuse Color property from linear color space to
# sRGB color space.
# When you bind in a material type a color uniform to this binding expression,
# Kanzi writes the color value to the render state and uses it as the value of
# the color uniform when rendering the nodes that use the material type.
linearTosRGB({./Diffuse})

```
   |
#### premultiplyColor


Multiplies the values of the RGB channels in a color by the value of the alpha channel:

`Color4(color.r * color.a, color.g * color.a, color.b * color.a, color.a)`
|

**Syntax** |

`premultiplyColor(value)` |
|

**Parameters** |
|

`value` |

Color4, Vector4 |      |
|

**Returns** |

the same type as the input parameter |
|

**Examples** |

```
# Premultiplies the color that you bind to this binding expression.
premultiplyColor(getCurrentValue())

```
   |
#### srgbToHsl


Converts a value from sRGB color space to HSL color space. This function does not convert the alpha channel of a color value.

For example, use this function to show the saturation value of a color in a Text Block node.

To access the components of an HSL color value `hslVector`, use:

- `hslVector.x` for the hue
- `hslVector.y` for the saturation
- `hslVector.z` for the lightness

|

**Syntax** |

`srgbToHsl(value)` |
|

**Parameters** |
|

`value` |

Color4, Vector4, Vector3 |      |
|

**Returns** |

If the parameter is Vector4 or Color4, returns Vector4. If the parameter is Vector3, returns Vector3. |
|

**Examples** |

```
# Returns Vector4(0.25, 1, 0.5, 1) which represents the color
# hsla(90, 100%, 50%, 1).
sourceColor = Color4(0.5, 1, 0, 1)
sRGBColor = linearTosRGB(sourceColor)
hslVector = srgbToHsl(sRGBColor)
hslVector

```


```
# Converts the value of the Brush Color property in the parent node from linear
# color space to HSL color space and prints the saturation value of the color in
# percentage. For example, you can bind this expression to the Text property of
# a Text Block node.
srgbColor = linearTosRGB({@../ColorBrush.Color})
hslVector = srgbToHsl(srgbColor)
string(int(hslVector.y * 100)) + "%"

```
   |
#### sRGBToLinear


Converts a value from sRGB color space to linear color space. This function does not convert the alpha channel of a color value.

For example, use this function to convert a value to linear color space before assigning the value to the red, green, or blue channel of a color property.
|

**Syntax** |

`sRGBToLinear(value)` |
|

**Parameters** |
|

`value` |

Color4, float, Vector3 |      |
|

**Returns** |

the same type as the input parameter |
|

**Examples** |

```
# Returns the RGBA color (0, 192, 64, 255).
# This expression is equivalent to Color4(0, 0.75, 0.25, 1).
color = Color4(0, 0, 0, 1)
color.g = sRGBToLinear(0.75)
color.b = sRGBToLinear(0.25)
color

```


```
# Assigns the value of custom property MyFloatPropertyType to the
# red color channel of a color property.
#
# Get the current value of the target color property.
color = getCurrentValue()
# Convert the value of MyFloatPropertyType from sRGB color space to
# linear color space and assign it to the red color channel of the
# color property.
color.r = sRGBToLinear({@./MyFloatPropertyType})
# Return the color.
color

```


```
# Converts the value of the Ambient Color property from sRGB color space to
# linear color space.
# When you bind in a material type a color uniform to this binding expression,
# Kanzi writes the color value to the render state and uses it as the value of
# the color uniform when rendering the nodes that use the material type.
sRGBToLinear(getAmbient())

```
   |
### Range functions


A range property type stores a collection of values. Use ranges in bindings to:

- Read individual values from ranges.
- Manipulate multiple values at the same time.
- Write multiple values to array outputs.

#### createView


Creates a view over a range. The view refers to the values of the input range but its length is limited.

You can create multiple views for the same `range`. When you iterate the view, the iteration refers to locations in the input `range`.

See Light uniform bindings.
|

**Syntax** |

`createView<OutputSize>(range)`

`createView(range, length)`

`createView<constantLength>(range)`  |
|

**Parameters** |
|

`range` |

range: input range |
|

`length` |

int: variable or constant value that sets the maximum number of elements in the returned view |
|

`constantLength` |

int: constant value that sets the maximum number of elements in the returned view |      |
|

**Returns** |

a range that refers to the values of the input range, but whose length is limited to the minimum of the length of the input `range` and the `length` parameter. |
|

**Examples** |

```
# This is the default PointLightColor uniform binding in a material type that uses
# lights. The binding creates a view over the range of Point Light nodes in the
# scene and accesses the Point Light Color property of each Point Light node in that
# view. The length of the view is determined by the number of Point Light nodes
# supported by the material type.
pointLightsView = createView<OutputSize>({##RenderPass/DrawObjectsRenderPass.PointLights})
{pointLightsView ... PointLightColor}

```


```
# Modify the default PointLightColor uniform binding in a material type that uses
# lights. Set the length of the view over the range of Point Light nodes to the
# value of the MyLengthProperty set in a node that uses the material type that has
# this binding.
# This binding uses the createView(range, length) syntax where length can be
# a variable or constant value.
length = {./MyLengthProperty}
pointLightsView = createView({##RenderPass/DrawObjectsRenderPass.PointLights}, length)
{pointLightsView ... PointLightColor}

```


```
# Modify the default PointLightColor uniform binding in a material type that uses
# lights. Set the length of the view over the range of Point Light nodes to 2.
# This binding uses the createView<constantLength>(range) syntax where constantLength
# is a constant value.
pointLightsView = createView<2>({##RenderPass/DrawObjectsRenderPass.PointLights})
{pointLightsView ... PointLightColor}

```
   |
#### evaluate


Converts a range iterator to an evaluation of that range. Use this function to step through a collection of values stored in a range property.

The `evaluate` function advances the range iterator and returns the location in the range iterator before the advance.

For locations in the range iterator the `evaluate` function does not modify the iterator, but returns the next iteration location.

Use the splitString function to create a range iterator to evaluate.
|

**Syntax** |

`evaluate(range)` |
|

**Parameters** |
|

`range` |

range: input range |      |
|

**Returns** |

range: evaluation of the input range |
|

**Examples** |

```
# Returns "two".
myRange = splitString("one,two,three", ",")
evaluate(myRange)
string(evaluate(myRange))

```


```
# Sets the 2D Render Transformation property Translation property fields
# to the values that the user enters in the Text Box 2D node.
# For example, "100, 50" sets the Render Transformation property:
# - Translation X property field to 100
# - Translation Y property field to 50
renderTransformation = getCurrentValue()
stringRange = splitString({@../Text Box 2D/TextConcept.Text}, ",")
renderTransformation.translationX = float(stringRange)
evaluate(stringRange)
renderTransformation.translationY = float(stringRange)
renderTransformation

```


```
# This example is equivalent to the previous example.
renderTransformation = getCurrentValue()
stringRange = splitString({@../Text Box 2D/TextConcept.Text}, ",")
x = evaluate(stringRange)
y = evaluate(stringRange)
renderTransformation.translationX = float(x)
renderTransformation.translationY = float(y)
renderTransformation

```
   |
#### splitString


Splits a text string into a collection of substrings and returns that collection as a range iterator that you can use to step through the collection of substrings. Use the evaluate function to return the substrings one at a time.

See Using bindings to split text into parts.
|

**Syntax** |

`splitString(string, delimiter)` |
|

**Parameters** |
|

`string` |

string: input string |
|

`delimiter` |

string: separator to use to split the string |      |
|

**Returns** |

Range |
|

**Examples** |

```
# Returns "two".
myRange = splitString("one,two,three", ",")
evaluate(myRange)
string(evaluate(myRange))

```


```
# Returns "three".
myRange = splitString("one, two, three", ", ")
evaluate(myRange)
evaluate(myRange)
string(myRange)

```
   |
### Mesh functions


Meshes are resources that store vertex and index data. Use the mesh functions to access the GPU buffers and dimensions of a mesh, for example, when you want to bind a vertex buffer of a mesh as a storage buffer to a Compute Render Pass or use the vertex or index count to drive draw arguments.

The buffer accessors return the GPU buffer resource that backs a vertex attribute or the index buffer of the mesh. They return a null buffer resource if the input does not hold a mesh resource or if the requested attribute is not present.
#### meshGetIndexBuffer


Gets the index buffer of a mesh as a GPU buffer resource. For example, use this function to bind the index buffer of a mesh to a Compute Render Pass so that compute shaders can read or process the indices.
|

**Syntax** |

`meshGetIndexBuffer(mesh)` |
|

**Parameters** |
|

`mesh` |

Mesh resource |      |
|

**Returns** |

GPU buffer resource

If the input parameter does not hold a mesh resource, or the mesh does not have an index buffer, returns a null buffer resource.  |
|

**Examples** |

```
# Gets the index buffer of a mesh resource that you set in the
# custom property type MyMeshPropertyType.
meshGetIndexBuffer({./MyMeshPropertyType})

```


```
# Gets the index buffer of the mesh used by a sibling Model3D node.
meshGetIndexBuffer({@../Model/Model3D.Mesh})

```
   |
#### meshGetIndexCount


Gets the number of indices in the index buffer of a mesh. For example, use this function to drive the dispatch size of a Compute Render Pass that processes the indices of a mesh, or to set the draw count of an indirect draw.
|

**Syntax** |

`meshGetIndexCount(mesh)` |
|

**Parameters** |
|

`mesh` |

Mesh resource |      |
|

**Returns** |

integer

If the input parameter does not hold a mesh resource, or the mesh does not have an index buffer, returns 0.  |
|

**Examples** |

```
# Gets the number of indices in a mesh resource that you set in the
# custom property type MyMeshPropertyType.
meshGetIndexCount({./MyMeshPropertyType})

```
   |
#### meshGetNormalBuffer


Gets the GPU buffer that holds the vertex normals of a mesh. For example, use this function to bind the normal buffer of a mesh as input to a Compute Render Pass that processes per-vertex lighting or surface analysis.
|

**Syntax** |

`meshGetNormalBuffer(mesh)` |
|

**Parameters** |
|

`mesh` |

Mesh resource |      |
|

**Returns** |

GPU buffer resource

If the input parameter does not hold a mesh resource, or the mesh does not have a normal vertex attribute, returns a null buffer resource.  |
|

**Examples** |

```
# Gets the normal buffer of a mesh resource that you set in the
# custom property type MyMeshPropertyType.
meshGetNormalBuffer({./MyMeshPropertyType})

```
   |
#### meshGetPositionBuffer


Gets the GPU buffer that holds the vertex positions of a mesh. For example, use this function to bind the position buffer of a mesh as input to a Compute Render Pass that performs vertex transformations, culling, or geometry analysis.
|

**Syntax** |

`meshGetPositionBuffer(mesh)` |
|

**Parameters** |
|

`mesh` |

Mesh resource |      |
|

**Returns** |

GPU buffer resource

If the input parameter does not hold a mesh resource, or the mesh does not have a position vertex attribute, returns a null buffer resource.  |
|

**Examples** |

```
# Gets the position buffer of a mesh resource that you set in the
# custom property type MyMeshPropertyType.
meshGetPositionBuffer({./MyMeshPropertyType})

```


```
# Gets the position buffer of the mesh used by a sibling Model3D node.
meshGetPositionBuffer({@../Model/Model3D.Mesh})

```
   |
#### meshGetTangentBuffer


Gets the GPU buffer that holds the vertex tangents of a mesh. For example, use this function to bind the tangent buffer of a mesh as input to a Compute Render Pass that performs normal mapping or other tangent-space operations.
|

**Syntax** |

`meshGetTangentBuffer(mesh)` |
|

**Parameters** |
|

`mesh` |

Mesh resource |      |
|

**Returns** |

GPU buffer resource

If the input parameter does not hold a mesh resource, or the mesh does not have a tangent vertex attribute, returns a null buffer resource.  |
|

**Examples** |

```
# Gets the tangent buffer of a mesh resource that you set in the
# custom property type MyMeshPropertyType.
meshGetTangentBuffer({./MyMeshPropertyType})

```
   |
#### meshGetUVBuffer


Gets the GPU buffer that holds the vertex texture coordinates of a mesh for the specified UV channel. For example, use this function to bind a UV buffer of a mesh as input to a Compute Render Pass that processes texture-space data.
|

**Syntax** |

`meshGetUVBuffer(mesh, channel)` |
|

**Parameters** |
|

`mesh` |

Mesh resource |
|

`channel` |

integer

The 0-based UV channel index. `0` selects the first UV set, `1` the second, and so on.  |      |
|

**Returns** |

GPU buffer resource

If the input parameter does not hold a mesh resource, the channel index is negative, or the mesh does not have a UV vertex attribute at the specified channel, returns a null buffer resource.  |
|

**Examples** |

```
# Gets the first UV buffer of a mesh resource that you set in the
# custom property type MyMeshPropertyType.
meshGetUVBuffer({./MyMeshPropertyType}, 0)

```


```
# Gets the second UV buffer of the mesh used by a sibling Model3D node.
meshGetUVBuffer({@../Model/Model3D.Mesh}, 1)

```
   |
#### meshGetVertexCount


Gets the number of vertices in a mesh. For example, use this function to drive the dispatch size of a Compute Render Pass that processes per-vertex data, or to set the draw count of a non-indexed draw.
|

**Syntax** |

`meshGetVertexCount(mesh)` |
|

**Parameters** |
|

`mesh` |

Mesh resource |      |
|

**Returns** |

integer

If the input parameter does not hold a mesh resource, returns 0.  |
|

**Examples** |

```
# Gets the number of vertices in a mesh resource that you set in the
# custom property type MyMeshPropertyType.
meshGetVertexCount({./MyMeshPropertyType})

```
   |
### Texture functions


Textures are resources that you can use in rendering to represent an image. Use the texture functions to access the properties of textures.
#### textureGetAddressingMode


Gets the addressing mode of a texture that you can set using either:

- Wrap Mode property in a texture resource.
- Addressing Mode property in a Composition Target render pass.


For example, use this function to get the addressing mode of a texture when you want to use that addressing mode as input for decision making in other bindings.
|

**Syntax** |

`textureGetAddressingMode(texture)` |
|

**Parameters** |
|

`texture` |

Texture resource |      |
|

**Returns** |

integer:

- 0 if the addressing mode is Repeat
- 1 if the addressing mode is Mirror
- 2 if the addressing mode is Clamp
- 3 if the addressing mode is Mirror Once
- -1 if the input parameter does not hold a texture resource
  |
|

**Examples** |

```
# Gets the addressing mode of a texture resource that you set
# in the custom property type MyTexturePropertyType.
textureGetAddressingMode({./MyTexturePropertyType})

```


```
# Gets the addressing mode of the first Result Texture of sibling
# Composition Target render pass named Compose.
textureGetAddressingMode({@../Compose/CompositionTargetRenderPass.ResultTexture0})

```
   |
#### textureGetAnisotropyLevel


Gets the anisotropy level of a texture, which you set using the Anisotropy property in a texture resource. For example, use this function to get the anisotropy level of a texture resource when you want to use that anisotropy level as input for decision making in other bindings.
|

**Syntax** |

`textureGetAnisotropyLevel(texture)` |
|

**Parameters** |
|

`texture` |

Texture resource |      |
|

**Returns** |

integer:

- anisotropy level: 2, 4, 8, or 16
- 0 if anisotropic filtering is disabled
- -1 if the input parameter does not hold a texture resource
  |
|

**Examples** |

```
# Gets the anisotropy level of a texture resource that you set in
# the custom property type MyTexturePropertyType.
textureGetAnisotropyLevel({./MyTexturePropertyType})

```
   |
#### textureGetDepthCompareFunction


Gets the depth compare function of a Render Target Texture resource to which you render a result texture of a Composition Target render pass. For example, use this function to get the depth compare function of a texture resource when you want to use that function as input for decision making in other bindings.
|

**Syntax** |

`textureGetDepthCompareFunction(texture)` |
|

**Parameters** |
|

`texture` |

Texture resource |      |
|

**Returns** |

integer:

- 0 if the function is Never
- 1 if the function is Always
- 2 if the function is Less
- 3 if the function is Less or equal
- 4 if the function is Greater
- 5 if the function is Greater or equal
- 6 if the function is Equal
- 7 if the function is Not equal
- 8 if the function is Disabled
- -1 if the input parameter does not hold a texture resource
  |
|

**Examples** |

```
# Gets the depth compare function of a Render Target Texture resource that you set
# in the custom property type MyRenderTargetTexturePropertyType.
textureGetDepthCompareFunction({./MyRenderTargetTexturePropertyType})

```


```
# Gets the depth compare function of the Result Depth Texture of sibling
# Composition Target render pass named Compose.
textureGetDepthCompareFunction({@../Compose/CompositionTargetRenderPass.ResultDepthTexture})

```
   |
#### textureGetFilterMode


Gets the filter mode of a texture that you can set using either:

- Minification Filter property in a texture resource.
- Filter Mode property in a Composition Target render pass.


For example, use this function to get the filter mode of a texture resource when you want to use that filter mode as input for decision making in other bindings.
|

**Syntax** |

`textureGetFilterMode(texture)` |
|

**Parameters** |
|

`texture` |

Texture resource |      |
|

**Returns** |

integer:

- 0 if the mode is Nearest
- 1 if the mode is Linear
- -1 if the input parameter does not hold a texture resource
  |
|

**Examples** |

```
# Gets the value of the Minification Filter property of a texture resource that
# you set in the custom property type MyTexturePropertyType.
textureGetFilterMode({./MyTexturePropertyType})

```


```
# Gets the filter mode of the first Result Texture of sibling
# Composition Target render pass named Compose.
textureGetFilterMode({@../Compose/CompositionTargetRenderPass.ResultTexture0})

```
   |
#### textureGetHeight


Gets the height of a texture. For example, use this function when you want to use the height of a texture resource to set the height of a node.
|

**Syntax** |

`textureGetHeight(texture)` |
|

**Parameters** |
|

`texture` |

Texture resource |      |
|

**Returns** |

integer

If the input parameter does not hold a texture resource, returns -1.  |
|

**Examples** |

```
# Gets the height of a texture resource that you set in the custom property type
# MyTexturePropertyType.
textureGetHeight({./MyTexturePropertyType})

```


```
# Gets the height of the texture shown in the Image node which is a sibling of
# the node to which you add the binding.
textureGetHeight({@../Image/Image2D.Image})

```
   |
#### textureGetMipmapMode


Gets the mipmap mode of a texture, which you set using the Mipmap Mode property in a texture resource or Composition Target render pass. For example, use this function to get the mipmap mode of a texture resource when you want to use that mipmap mode as input for decision making in other bindings.
|

**Syntax** |

`textureGetMipmapMode(texture)` |
|

**Parameters** |
|

`texture` |

Texture resource |      |
|

**Returns** |

integer:

- 0 if the mipmap mode is Base
- 1 if the mipmap mode is Nearest
- 2 if the mipmap mode is Linear
- -1 if the input parameter does not hold a texture resource
  |
|

**Examples** |

```
# Gets the mipmap mode of a texture resource that you set in
# the custom property type MyTexturePropertyType.
textureGetMipmapMode({./MyTexturePropertyType})

```


```
# Gets the mipmap mode of the first Result Texture of sibling
# Composition Target render pass named Compose.
textureGetMipmapMode({@../Compose/CompositionTargetRenderPass.ResultTexture0})

```
   |
#### textureGetMultisampleLevel


Gets the multisample level of a Render Target Texture resource. For example, use this function to get the multisample level of a render target texture when you want to use that multisample level as input for decision making in other bindings.

The multisample level is meaningful only if the target platform supports implicit multisampling. The renderbuffer multisampling used by the Composition Target render pass resolves the samples as part of a blit operation to a Single Texture resource, which is why the result texture is not multisampled. See Using multisampling.
|

**Syntax** |

`textureGetMultisampleLevel(texture)` |
|

**Parameters** |
|

`texture` |

Texture resource |      |
|

**Returns** |

integer:

- number of anti-aliasing samples
- 0 if multisampling is disabled
- -1 if the input parameter does not hold a texture resource
  |
|

**Examples** |

```
# Gets the multisample level of a Render Target Texture resource that you set in
# the custom property type MyRenderTargetTexturePropertyType.
textureGetMultisampleLevel({./MyRenderTargetTexturePropertyType})

```
   |
#### textureGetPixelFormat


Gets the pixel format of a texture. For example, use this function to get the pixel format of a texture resource when you want to use that pixel format as input for decision making in other bindings.
|

**Syntax** |

`textureGetPixelFormat(texture)` |
|

**Parameters** |
|

`texture` |

Texture resource |      |
|

**Returns** |

integer

The return value corresponds to a value of the `GraphicsFormat` enumeration.

If the input parameter does not hold a texture resource, returns -1.  |
|

**Examples** |

```
# Gets the pixel format of a texture resource that you set in
# the custom property type MyTexturePropertyType.
textureGetPixelFormat({./MyTexturePropertyType})

```


```
# Gets the pixel format of the first Result Texture of sibling
# Composition Target render pass named Compose.
textureGetPixelFormat({@../Compose/CompositionTargetRenderPass.ResultTexture0})

```
   |
#### textureGetSize


Gets the size of a texture. For example, use this function when you want to use the size of a texture resource to set the size of a node.
|

**Syntax** |

`textureGetSize(texture)` |
|

**Parameters** |
|

`texture` |

Texture resource |      |
|

**Returns** |

Vector2

If the input parameter does not hold a texture resource, returns Vector2(-1.0f, -1.0f).  |
|

**Examples** |

```
# Gets the size of a texture resource that you set in the custom property type
# MyTexturePropertyType.
textureGetSize({./MyTexturePropertyType})

```
   |
#### textureGetWidth


Gets the width of a texture. For example, use this function when you want to use the width of a texture resource to set the width of a node.
|

**Syntax** |

`textureGetWidth(texture)` |
|

**Parameters** |
|

`texture` |

Texture resource |      |
|

**Returns** |

integer

If the input parameter does not hold a texture resource, returns -1.  |
|

**Examples** |

```
# Gets the width of a texture resource that you set in the custom property type
# MyTexturePropertyType.
textureGetWidth({./MyTexturePropertyType})

```


```
# Gets the width of the texture shown in the Image node which is a sibling of
# the node to which you add the binding.
textureGetWidth({@../Image/Image2D.Image})

```
   |
## Common binding expressions

### Variables


In binding expressions you can use variables.

```
# Assigns the value 1 to the variable 'A', and binds the value of
# the variable to the selected property.
A = 1

```


```
# Same as above, but using an alternative syntax.
A = (1)

```

### Property bindings


To bind a property to another property, enter in curly braces:

1.

The relative path to the node which contains the property to which you want to bind.
2.

A forward slash.
3.

The name of the source property.


> **Tip:** When you use the @ sign in a binding expression before the path to a node, Kanzi Studio:
>
> - Checks whether the path is valid and shows an error message in the Binding Editor if the path is not valid.
> - Updates the path in the binding expression whenever the location between the source and the target nodes in the node tree changes.


With the @ sign you can create bindings only within the same prefab, not between prefabs.

You can drag property names from the Properties to the Binding Editor.

You can use the operators and parentheses with property values and property field values.
|

**Syntax** |

`{[path]/[property]}` |
|

**Parameters** |
|

`[path]` |

relative path to node |
|

`[property]` |

name of the property |      |
|

**Examples** |

```
# Binds to the Layout Width property of the current node.
{@./Node.Width}

```


```
# Binds to the FOV property of the Camera node.
{@../Camera/Fov}

```


```
# Same as above, but Kanzi Studio does not track the location of the target node.
{../Camera/Fov}

```


```
# Binds to the Vertical Margin property of the Box node.
{@../Box/LayoutVerticalMargin}

```


```
# Multiplies the FOV property with the Layout Transformation Scale x
# property field.
{@../Camera/Fov} * {../Box/LayoutTransformation}.scaleX

```


```
# Binds each vector of a property to the Render Transformation property
# Translation X and Translation Y property fields of the current node.
# In the Binding Editor set the Target Property to a property that uses the
# Vector2D data type. For example, use the Horizontal Margin property.
x = {@./Node3D.RenderTransformation}.translationX
y = {@./Node3D.RenderTransformation}.translationY

myVector = Vector2(0.0, 0.0)

myVector.vectorX = x
myVector.vectorY = y

myVector

```
   |
### Property field bindings


To bind a property to a property field of a property, enter:

1.

In curly braces: the relative path to the node, forward slash, and property name.
2.

A period.
3.

The name of the property field.


Color and transformation properties have special property field names. See Color property field bindings and Transformation property field bindings.

For the property fields of other properties, use `N` or `VectorN`, where `N` is `X`, `Y`, `Z`, or `W` denoting the order in which the property is listed in the Kanzi Studio Properties window:
|

Description |

Property field label |

Property field |
|

The first property field |

X |

x, vectorX |
|

The second property field |

Y |

y, vectorY |
|

The third property field |

Z |

z, vectorZ |
|

The fourth property field |

W |

w, vectorW |

You can use the operators and parentheses with property values and property field values.

To bind a property field of a property to another property field of that property in the same node, use the getCurrentValue function to get the value of that property.
|

**Syntax** |

`{[path]/[property]}.[propertyField]` |
|

**Parameters** |
|

`[path]` |

relative path to node |
|

`[property]` |

name of the property |
|

`[propertyField]` |

name of the property field |      |
|

**Examples** |

```
# Point Light and Spot Light nodes have an attenuation property that
# has three property fields: Constant, Linear, and Quadratic.
# For example, for the Point Light Attenuation:
# To bind to the first property field (Constant)
{@../Light/PointLightAttenuation}.x

# To bind to the second property field (Linear)
{@../Light/PointLightAttenuation}.y

# To bind to the third property field (Quadratic)
{@../Light/PointLightAttenuation}.z

```


```
# Binds to the Horizontal Padding property Left property field of the Text node.
{@../Text/TextConcept.HorizontalPadding}.x

```


```
# Binds to the Vertical Margin property Bottom property field of the Image node.
{@../Image/Node.VerticalMargin}.vectorX

```


```
# Binds to the Vertical Margin property Top property field of the Image node.
{@../Image/Node.VerticalMargin}.vectorY

```


```
# Binds to the MyProject.MyProperty property Y property field of the parent node.
{@../MyProject.MyProperty}.y

```
   |
#### Color property field bindings


To bind a property to a color property field, use these names:
|

Description |

Property field label |

Property field |
|

Red color channel value |

R |

r, colorR |
|

Green color channel value |

G |

g, colorG |
|

Blue color channel value |

B |

b, colorB |
|

Alpha channel value |

A |

a, colorA |
|

**Syntax** |

`{[path]/[property]}.[propertyField]` |
|

**Parameters** |
|

`[path]` |

relative path to node |
|

`[property]` |

name of the color property |
|

`[propertyField]` |

name of the property field |      |
|

**Examples** |

```
# Binds to the Point Light Color property R property field
# (value of the red color channel) of the Point Light node.
{@../Point Light/PointLightColor}.r

```


```
# Binds to the Brush Color property G property field
# (value of the green color channel) of the parent node.
{@../ColorBrush.Color}.colorG

```


```
# Assigns the value of custom property MyFloatPropertyType to the
# red color channel of a color property.
#
# Get the current value of the target color property.
color = getCurrentValue()
# Convert the value of MyFloatPropertyType from sRGB color space to
# linear color space and assign it to the red color channel of the
# color property.
color.r = sRGBToLinear({@./MyFloatPropertyType})
# Return the color.
color

```
   |
#### Transformation property field bindings


To bind a property to a transformation property field, use these names:
|

Description |

Property field label |

Property field |
|

Value of the 3D node rotation around the X, Y, and Z axes which you set using rotation functions. See createRotation, createRotationX, createRotationY, createRotationZ, rotate, rotateX, rotateY, and rotateZ. |

Rotation |

rotation |
|

Value of the 2D node rotation around the Z axis |

Rotation R |

rotationZ |
|

Value of the node scale along the X axis |

Scale X |

scaleX |
|

Value of the node scale along the Y axis |

Scale Y |

scaleY |
|

Value of the node scale along the Z axis |

Scale Z |

scaleZ |
|

Value of the node location along the X axis |

Translation X |

x, translationX |
|

Value of the node location along the Y axis |

Translation Y |

y, translationY |
|

Value of the node location along the Z axis |

Translation Z |

z, translationZ |
|

**Syntax** |

`{[path]/[property]}.[propertyField]` |
|

**Parameters** |
|

`[path]` |

relative path to node |
|

`[property]` |

name of the transformation property |
|

`[propertyField]` |

name of the property field |      |
|

**Examples** |

```
# Binds to the Render Transformation property Translation X property field
# of the Image node.
{@../Image/Node2D.RenderTransformation}.x

```


```
# Binds to the Layout Transformation property Scale Y property field
# of the Box node.
{../Box/LayoutTransformation}.scaleY

```


```
# Multiplies the FOV property of the Camera node with the Render
# Render Transformation property Scale X property field of the
# Box node.
{../Camera/Fov} * {../Box/RenderTransformation}.scaleX

```


```
# Binds each vector of a property to the Render Transformation property
# Translation X and Translation Y property fields of the current node.
# In the Binding Editor set the Target Property to a property that uses the
# Vector2D data type. For example, use the Horizontal Margin property.
x = {@./Node3D.RenderTransformation}.translationX
y = {@./Node3D.RenderTransformation}.translationY

myVector = Vector2(0.0, 0.0)

myVector.vectorX = x
myVector.vectorY = y

myVector

```


```
# Gets the value of the Translation X property field of the
# transformation property that you bind to this expression.
getCurrentValue().translationX

```
   |
### Prefab root bindings


A node prefab or a render pass prefab can contain a tree of nodes or render passes, each with their own properties. When you edit the nodes or render passes in a prefab or any of its instances, you change those nodes or render passes in all instances of that prefab. However, you can customize individual instances of the prefab to have individual values by overriding the values in the default prefab. For example, when you create a prefab for a contact list entry, you want to show a different name, number, and photo for each contact list entry.

To bind a property of any node or render pass in a prefab to a property in the root of an instance of that prefab, in the binding expression enter in curly braces `##Template`, followed by a forward slash and the name of the property in the root of the prefab instance to which you want to bind.

For example, use the `##Template` binding syntax when you have a Text Block node in a Button prefab and you want to show different text in different instances of that prefab.

> **Tip:** You can let Kanzi Studio create a prefab root binding for you. When you select any node in a prefab or any render pass in a render pass prefab, and in the Properties click  next to a property, Kanzi Studio:
>
> 1.
>
> Creates from that property a custom property.
> 2.
>
> Adds the custom property to the prefab and shows the custom property as a frequently used property in each instance of the prefab.
> 3.
>
> Creates in the node or render pass the `##Template` binding to the custom property in the prefab root.


See Customizing instances of prefabs.
|

**Syntax** |

`{##Template/[property]}` |
|

**Parameters** |
|

`[property]` |

name of the property in the root of the prefab instance to which you want to bind |      |
|

**Examples** |

```
# Binds to the MyProject.ContactNameText property in the root of the prefab
# instance.
{##Template/MyProject.ContactNameText}

```
   |
### Alias bindings


To bind a property to an alias, enter in curly braces the `#` sign followed by the alias name, followed by a forward slash and property name of the item to which the alias points. See Using aliases.
|

**Syntax** |

`{#[aliasName]/[property]}` |
|

**Parameters** |
|

`[aliasName]` |

name of the alias |
|

`[property]` |

name of the property |      |
|

**Examples** |

```
# Binds to the Layout Width property of the target node of the alias named Grid.
{#Grid/Node.Width}

```


```
# Multiplies the FOV property of the target node of the alias named MainCamera
# with the Render Transformation property Scale X property field.
{#MainCamera/Fov} * {../Box/RenderTransformation}.scaleX

```
   |
### Data source bindings


To bind a data object to a property or a property field, enter in curly braces `DataContext` followed by a period, followed by the data object to which you want to bind the property or property field. Use a period to access child data objects.
|

**Syntax** |

`{DataContext.DataObject}` |
|

**Parameters** |
|

`DataObject` |

The data object to which you want to bind. |      |
|

**Examples** |

```
# Binds the property value of the item to the speed data object
# which is a child data object of the gauges data object
# in the data context of the item.
{DataContext.gauges.speed}

```


```
# Binds the data context itself. For example, use this if you want to
# use the current data context as the property value.
{DataContext}

```
   |
### Grid Layout bindings


To set the size of columns and rows in a Grid Layout node using bindings, enter in quotation marks each value followed by a semicolon:

- Use a floating point number to specify that the size of a row or a column is fixed. This is the same as when you set the value of the Columns or Rows property in the Properties to Fixed and define the size of this column or row.
- Add an asterisk prefix to specify that the size of a row or a column is proportional. This is the same as when you set the value of the Columns or Rows property in the Properties to Proportional and define the proportion of the Grid Layout this column or row takes.
- Leave the definition empty to specify that the Grid Layout node automatically sets the size of a row or a column. This is the same as when you set the value of the Columns or Rows property in the Properties to Automatic.

|

**Syntax** |

`"value0;value1; ... valueN;"` |
|

**Parameters** |
|

`value` |

float |      |
|

**Examples** |

```
# This binding to the Columns property sets the width of each of the three columns
# to a fixed size:
# - The width of the first column is 2.0.
# - The width of the second column is 3.0.
# - The width of the third column is 4.0.
"2.0;3.0;4.0;"

```


```
# This binding to the Rows property sets the height of each of the three rows
# to the fixed size 5.0.
"5.0;5.0;5.0;"

```


```
# This binding to the Rows property sets the height of the two rows to the height
# of their content.
";;"

```


```
# This binding to the Columns property sets the width of the columns in relation
# to the total width of the Grid Layout node:
# - The width of the first column is 1/6 of the width of the Grid Layout node.
# - The width of the second column is 2/6 of the width of the Grid Layout node.
# - The width of the third column is 3/6 of the width of the Grid Layout node.
"*1.0;*2.0;*3.0;"

```
   |
## Material type binding expressions


Bindings in material types enable you to:

- Modify the values of shader uniforms without editing shader code. See Uniform bindings.
- Store the results of bindings into temporary variables to which you can refer in other bindings. See Temporary variable bindings.

### Uniform binding functions


In a material type, vertex and fragment shaders define the uniforms and property types that you can use in that material. When rendering 3D nodes with a specific material type, uniform bindings allow Kanzi to write values to the render state and use those values for uniforms and property types.

See Shader uniforms and Uniform bindings.

To reduce memory consumption and improve performance, Kanzi provides binding functions for the most common shader uniforms. Kanzi executes every frame all bindings that use these functions.
#### getAmbient


In a uniform binding expression, gets the value of the Ambient Color property.

`getAmbient()` is the default binding of the `Ambient` shader uniform.
|

**Syntax** |

`getAmbient()` |
|

**Returns** |

Color: the value of the Ambient Color property. |
#### getCameraPosition


In a uniform binding expression, gets the camera location in world space.

`getCameraPosition()` is the default binding of the `kzCameraPosition` shader uniform.
|

**Syntax** |

`getCameraPosition()` |
|

**Returns** |

Vector 3D: the camera location in world space. |
#### getCameraWorldMatrix


In a uniform binding expression, gets the matrix to transform a point or matrix from local space to view (camera) space.

`getCameraWorldMatrix()` is the default binding of the `kzCameraWorldMatrix` shader uniform.

The `kzCameraWorldMatrix` uniform is the premultiplied matrix `kzCameraMatrix * kzWorldMatrix`, where:

- `kzCameraMatrix` transforms from world space to view (camera) space.
- `kzWorldMatrix` transforms from local space to world space. See getWorldMatrix.

|

**Syntax** |

`getCameraWorldMatrix()` |
|

**Returns** |

Matrix 4x4: the matrix that transforms a point or matrix from local space to view (camera) space. |
#### getNormalMatrix


In a uniform binding expression, gets the matrix to transform object normals from local space to world space.

`getNormalMatrix()` is the default binding of the `kzNormalMatrix` shader uniform.
|

**Syntax** |

`getNormalMatrix()` |
|

**Returns** |

Matrix 4x4: the matrix that transforms object normals from local space to world space. |
#### getCameraNormalMatrix


In a uniform binding expression, gets the matrix to transform object normals from local space to view (camera) space.

`getCameraNormalMatrix()` is the default binding of the `kzCameraNormalMatrix` shader uniform.

The `kzCameraNormalMatrix` uniform is the premultiplied matrix `kzCameraMatrix * kzNormalMatrix`, where:

- `kzCameraMatrix` transforms from world space to view (camera) space.
- `kzNormalMatrix` transforms from local space to world space. See getNormalMatrix.

|

**Syntax** |

`getCameraNormalMatrix()` |
|

**Returns** |

Matrix 4x4: the matrix that transforms object normals from local space to view (camera) space. |
#### getProjectionCameraWorldMatrix


In a uniform binding expression, gets the matrix to transform a point or matrix from local space to screen space.

`getProjectionCameraWorldMatrix()` is the default binding of the `kzProjectionCameraWorldMatrix` shader uniform.

The `kzProjectionCameraWorldMatrix` uniform is the premultiplied matrix `kzProjectionMatrix * kzCameraMatrix * kzWorldMatrix`, where:

- `kzProjectionMatrix` transforms from view space to screen space.
- `kzCameraMatrix` transforms from world space to view (camera) space.
- `kzWorldMatrix` transforms from local space to world space. See getWorldMatrix.

|

**Syntax** |

`getProjectionCameraWorldMatrix()` |
|

**Returns** |

Matrix 4x4: the matrix that transforms a point or matrix from local space to screen space. |
#### getViewPosition


In a uniform binding expression, gets the vector that you can use to calculate the view direction.

`getViewPosition()` is the default binding of the `kzViewPosition` shader uniform.

The `kzViewPosition` uniform is a homogeneous position vector that you can use to calculate the view direction as `kzWorldMatrix * vec4(kzPosition.xyz, 1.0) * kzViewPosition.w - kzViewPosition.xyz`, where:

- `kzWorldMatrix` transforms a point from local space to world space. See getWorldMatrix.
- `kzViewPosition.w` determines whether the vector is a position in space (w==1) or a direction (w==0).

|

**Syntax** |

`getViewPosition()` |
|

**Returns** |

Vector 4D: the homogeneous position vector that you can use to calculate the view direction. |
#### getWorldMatrix


In a uniform binding expression, gets the matrix to transform a point or matrix from local space to world space.

`getWorldMatrix()` is the default binding of the `kzWorldMatrix` shader uniform.
|

**Syntax** |

`getWorldMatrix()` |
|

**Returns** |

Matrix 4x4: the matrix that transforms a point or matrix from local space to world space. |
### Render pass properties in material type bindings


In a material type binding expression, to refer to a property in a render pass that draws nodes using the material type, enter in curly braces:

1.

`##RenderPass`
2.

A forward slash
3.

The name of the property in the render pass to which you want to bind


See Material type bindings.
|

**Syntax** |

`{##RenderPass/[property]}` |
|

**Parameters** |
|

`[property]` |

name of the property in a render pass to which you want to bind |      |
|

**Examples** |

```
# Binds to the MyProperty property in a render pass that draws nodes using the
# material type that has this binding.
{##RenderPass/MyProperty}

```


```
# This binding to a Matrix 4x4 property returns the inverse matrix of the product
# of the Calculated Projection Matrix and Calculated Camera Matrix properties in
# the Draw Objects render pass that draws nodes using the material type that has
# this binding.
projection = {##RenderPass/DrawObjectsRenderPass.ProjectionMatrix}
camera = {##RenderPass/DrawObjectsRenderPass.CameraMatrix}
inverse(projection * camera)

```


```
# This binding to a temporary variable property uses the evaluate binding function
# to step through a collection of values stored in the MyColorRange range property
# in the Draw Objects render pass that draws nodes using the material type that
# has this binding. The binding modifies the state of the range iterator in the
# render pass.
evaluate({##RenderPass/MyColorRange})

```
   |
### Light uniform bindings


In a material type, vertex and fragment shaders define the uniforms and property types that you can use in that material. When rendering 3D nodes with a specific material type, uniform bindings allow Kanzi to write values to the render state and use those values for uniforms and property types.

See Using material types and Rendering.

Light property types, such as `DirectionalLightColor`, `SpotLightPosition`, and `PointLightAttenuation`, support uniform arrays. This enables you to use multiple lights of the same type. See Uniform arrays for light property types.

A uniform binding for a light property type sets the uniform values in a render state based on the values extracted from lights that use that property type. For example, a uniform binding for the `PointLightColor` property type sets the render value based on the individual values of the Point Light Color property in all Point Light nodes in the scene that light those 3D nodes that use the material type which has the binding.

To get the range that contains the value of a property in each light node of a specific type, in the binding expression enter in curly braces `##RenderPass/DrawObjectsRenderPass.[lightType]`, followed by ellipsis and the name of the property in the light nodes.

To perform accumulation operations on a range of lights, use the `...` operator followed by an arithmetic operator.

See createView.
|

**Syntax** |

`{##RenderPass/[lightType] ... property}` |
|

**Parameters** |
|

`lightType` |

light node type: `DirectionalLights`, `PointLights`, or `SpotLights` |
|

`property` |

name of the property |      |
|

**Examples** |

```
# This binding adds in each Point Light node the value 0.5 to the value of
# the Point Light Attenuation property Constant property field.
pointLightsView = createView<OutputSize>({##RenderPass/DrawObjectsRenderPass.PointLights})
{pointLightsView ... PointLightAttenuation} + Vector3(0.5, 0.0, 0.0)

```


```
# This binding to a light color uniform halves the value of the Directional
# Light Color property in each Directional Light node.
directionalLightsView = createView<OutputSize>({##RenderPass/DrawObjectsRenderPass.DirectionalLights})
{directionalLightsView ... DirectionalLightColor} * 0.5

```


```
# This binding to a light color uniform multiplies in each Directional Light node
# the value of the Directional Light Color property by the value of the Opacity
# property and returns the result range.
rangeA = {##RenderPass/DrawObjectsRenderPass.DirectionalLights ... DirectionalLightColor}
rangeB = {##RenderPass/DrawObjectsRenderPass.DirectionalLights ... Node.Opacity}
rangeA * rangeB

```


```
# Get the range that contains the value of the Point Light Color property in each
# Point Light node.
rangeA = {##RenderPass/DrawObjectsRenderPass.PointLights ... PointLightColor}
# Get the range that contains the value of the Opacity property in each
# Point Light node.
rangeB = {##RenderPass/DrawObjectsRenderPass.PointLights ... Node.Opacity}
# Multiply the value of the Opacity property in each Point Light node.
totalOpacity = ...* rangeB
# For each Point Light node multiply the value of the Point Light Color property
# by the multiplied opacity.
rangeA * totalOpacity

```
   |
### Temporary variables in material type bindings


In a material type, a temporary variable binding enables you to store the result of a binding into a temporary variable. You can refer to this variable in other bindings in the same material type.

See Temporary variable bindings.

In a material type binding expression, to refer to the result of a temporary variable binding in the same material type, enter in curly braces:

1.

`##Self`
2.

A forward slash
3.

The name of the target property of the temporary variable binding


The `##Self` syntax refers to the render value of the property used by the render passes that draw nodes using the material type.
|

**Syntax** |

`{##Self/[temporaryVariableProperty]}` |
|

**Parameters** |
|

`[temporaryVariableProperty]` |

name of the temporary variable property to which you want to bind |      |
|

**Examples** |

```
# Binds to the MyProject.MyProperty property that is the target property
# of a temporary variable binding in the same material type.
{##Self/MyProject.MyProperty}

```


```
# This binding to a color property returns the color value obtained from the
# result of a temporary variable binding that targets the MyColorRange range
# property.
colors = splitString(string({##Self/MyColorRange}), " ")
color = Color4(0,0,0,1)
color.r = float(string(evaluate(colors)))
color.g = float(string(evaluate(colors)))
color.b = float(string(evaluate(colors)))
color

```
   |
