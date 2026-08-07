---
title: Logging
source: https://docs.kanzi.com/4.1.0/en/working-with/logging/logging.html
---

# Logging

Use the Kanzi logging system to print messages to the Log window, the Kanzi debug console, standard output, and the system log on your target device. For example, use logging to find problems in your Kanzi application, and to inform the user about the status of your application.

You can:

- Print log messages using the Kanzi logging macros. See Printing log messages.
- Use log levels to show log messages based on their severity. See Setting the log level.
- Use log categories to group log messages that contain information related to specific functionality. See Using log categories.
- Redirect all Kanzi log messages using a custom logger. See Creating a custom logger.

## Printing log messages

Use the Kanzi logging macros to print messages to the log. Most of the logging macros use a fixed log level to indicate the severity of the information in the message. See Setting the log level.
**Tip:** Do not use application critical code in the logging macro calls. If you place application critical code as an argument to the logging macro call, and during compilation you disable the log level or the log category assigned to the message in the call, the preprocessor removes the logging macro call together with the application critical code.
Kanzi has these logging macros:
|
Logging macro |
Description |
|
`log.hpp::kzLogError` |
Log error messages using the Default Logger (`DefaultLogger`), the `error` (`log_level.hpp::KZ_LOG_LEVEL_ERROR`) log level, and the log category that you provide as an input parameter. |
|
`log.hpp::kzLogWarning` |
Log warning messages using the Default Logger (`DefaultLogger`), the `warning` (`log_level.hpp::KZ_LOG_LEVEL_WARNING`) log level, and the log category that you provide as an input parameter. |
|
`log.hpp::kzLogInfo` |
Log info messages using the Default Logger (`DefaultLogger`), the `info` (`log_level.hpp::KZ_LOG_LEVEL_INFO`) log level, and the log category that you provide as an input parameter. |
|
`log.hpp::kzLogTrace` |
Log trace messages using the Default Logger (`DefaultLogger`), the `trace` (`log_level.hpp::KZ_LOG_LEVEL_TRACE`) log level, and the log category that you provide as an input parameter. |
|
`log.hpp::kzLogDebug` |
Log debug messages using the Default Logger (`DefaultLogger`), the `info` (`log_level.hpp::KZ_LOG_LEVEL_INFO`) log level, and the log category `LogCategories::KZ_LOG_CATEGORY_DEBUG`. |
|
`log.hpp::kzLog` |
Log messages using a custom logger, and the log level and category that you provide as input parameters. See Creating a custom logger. |
To print log messages:
1.
In your application code, use a logging macro where you want to print a log message. For example:
- Debug macro:
```
// Print "This is a debug message.".
kzLogDebug(("This is a debug message."));
```

Prints to the log:

```
info:debug> This is a debug message.

```

  - Error macro:

```
// Print "This is an error message." using the log category MY_LOG_CATEGORY.
// Use log categories to group your log messages based on the functionality to which they are related.
kzLogError(MY_LOG_CATEGORY, ("This is an error message."));

```

See Using log categories.

Prints to the log the path to the file, the line number where the error originated, and the error message:

```
error:My category:c:\kanziworkspace\projects\myproject\application\src\myproject.cpp:196> This is an error message.

```

  - Info macro:

```
// Print "1 plus 2 equals 3." using the log category MY_LOG_CATEGORY.
kzLogInfo(MY_LOG_CATEGORY, ("{} plus {} equals {}.", 1, 2, 1+2));
int length = 100;
// Print "The length is 100.".
kzLogInfo(MY_LOG_CATEGORY, ("The length is {}.", length));

```

See Using log categories.

Prints to the log:

```
info:My category> 1 plus 2 equals 3.
info:My category> The length is 100.

```

2.

Build and run your application. See Deploying Kanzi applications.

For example, on Windows build your application in Visual Studio using the Debug build configuration. When you run the application and reach in the code the point where you call the logging macro, Kanzi prints the message to the debug console.

## Formatting log messages in code

A log message is either a scalar value or a format specification string followed by the format arguments.

For example:

```
// Define a log category named "my category".
#define MY_LOG_CATEGORY KZ_LOG_CREATE_CATEGORY(KZ_LOG_ENABLED_CATEGORY, "my category")

        // The log message is an integer constant.
        kzLogInfo(MY_LOG_CATEGORY, (100));

        // Log integer variable.
        int length = 100;

        // Output: 100
        kzLogInfo(MY_LOG_CATEGORY, (length));

        // Log a string literal.
        // Output: Single log message.
        kzLogInfo(MY_LOG_CATEGORY, ("Single log message."));

        // Log a formatted message.
        // Format string: "{} plus {} equals {}.".
        // Format arguments: 1, 2, 1+2.
        // Output: 1 plus 2 equals 3.
        kzLogInfo(MY_LOG_CATEGORY, ("{} plus {} equals {}.", 1, 2, 1 + 2));

```

The format specification string is a literal text that can contain the format argument references in curly braces:

`"Text {...} text {...} ... {...} ..."`

When the logger writes the message, it replaces the argument references with a string representation of the values of the referred argument, and keeps the rest of the literal text unchanged. This is the structure of the format argument reference:

`{[argument index][:format specification]}`

The format argument index and format specification are optional.
**Note:** Place a colon ahead of the format specification part.
To prevent interpreting an opening brace â{â as the format argument reference, prefix it with two backslashes: `\\{`
Note that if it is followed by a closing brace â}â, it is not removed and remains in the log message output. The sole string literal is not considered a format string and is not parsed for format argument references.
For example:
```
// Log message consists of format string and one argument.
// Output: {} { some text }
kzLogInfo(MY_LOG_CATEGORY, ("\\{} \\{ {} } { this text is removed ", "some text"));
// Single string literals are not parsed as log message format string.
// Output: This text is string literal. Braces are kept {}, and { this text remains.
kzLogInfo(MY_LOG_CATEGORY, ("This text is string literal. Braces are kept {}, and { this text remains."));
```

The format argument index is a position of the format argument in the argument list. The first format argument has the index 0, followed by the argument with index 1, and so on. The last format argument has the index N-1, where N is the total number of the format arguments.

The format specification part of the format argument reference describes how to convert the referenced argument to the string when the reference is substituted with the string representation of the argument. See Log message argument format specification section for details.

When the log message is written, the format argument references found in the message format string are replaced with a string representation of the corresponding arguments.

In the simplest case the format arguments are referenced by empty braces **â{}â**:

```
// Format message arguments are referenced one by one using empty braces.
// Output: 1 2 3.
kzLogInfo(MY_LOG_CATEGORY, ("{} {} {}.", 1, 2, 3));

// Output: 1 plus 2 equals 3.
kzLogInfo(MY_LOG_CATEGORY, ("{} plus {} equals {}.", 1, 2, 1 + 2));

```

You can also reference the format arguments using the argument index explicitly:

```
// Log values in custom order.
// Output: 3 1 2 3 5.
kzLogInfo(MY_LOG_CATEGORY, ("{2} {0} {1} {2} {4}.", 1, 2, 3, 4, 5));

// Log values in custom order using implicit argument indexing.
// Note: The argument reference '{1}' followed by '{}'.
// Output: argument #4 = 5, argument #0 = 1, argument #2 = 3, argument #3 = 4, argument #4 = 5.
kzLogInfo(MY_LOG_CATEGORY, ("argument #4 = {4}, argument #0 = {0}, argument #2 = {2}, argument #3 = {}, argument #4 = {}.", 1, 2, 3, 4, 5));

```

In the last example you can see that the indexed argument reference **â{2}â** is followed by argument reference without index **â{}â**. In such a case the argument referenced without index is the one (#3 in this case) following the argument referenced with index (#2 in this case).
### Log message argument format specification

The log message format argument reference consists of argument index and format specification. The format specification describes how the log message format argument value is converted to a string and how it is positioned when the message is written to the log. The logging system takes the format argument value type into account when converting the value to the textual representation, making logging typesafe.

The format specification has this structure:

`[align][sign][#][0][width][.precision][specifier]`

The align format argument sets the positioning of the resulting text. The available values for align:
|

Align value |

Output |
|

`<` |

Text aligned to the left within the available space. |
|

`>` |

Text aligned to the right within the available space. This is the default setting. |

The sign is valid for numeric types only. The available values for sign:
|

Sign value |

Output |
|

`+` |

The sign of the number for both positive and negative numbers. |
|

`-` |

The sign of the number for negative numbers. This is the default setting. |
|

space |

Leading space for positive numbers, and a minus sign for negative numbers. |

The **#** format argument is valid for octal or hexadecimal specifier of integer types. If present, the output is prefixed by â0â for the **o** specifier or by â0xâ/â0Xâ for the **x/X** specifier.

The **0** format argument pads the number with zeroes to the left instead of spaces when the value converted to string consumes less characters than **width**.

The **width** format argument is an integer number describing the minimum width of the output text. If the text does not consume the whole width, the remaining space is padded with spaces or, if the **0** format argument is specified, with zeros.

The **precision** format argument is only valid for floating point types and describes how many digits to display after decimal point.

The **precision** format argument denotes the notation to use when converting the format argument value to a string. The available **specifier** values depend on the format argument type. This table lists the available values for **specifier**.
|

Specifier |

Output |
|

Character |   |
|

`c` |

Single character. This is the default for signed characters. |
|

`d` |

The number in base 10. |
|

`u` |

Unsigned number in base 10. This is the default for unsigned characters. |
|

`o` |

The number in base 8. |
|

`x` |

The number in base 16 using lowercase letters a - f. |
|

`X` |

The number in base 16 using uppercase letters A - F. |
|

Integer |   |
|

`d` |

The number in base 10. This is the default for signed integers. |
|

`u` |

Unsigned number in base 10. This is the default for unsigned integers. |
|

`o` |

The number in base 8. |
|

`x` |

The number in base 16 using lower case letters a - f. |
|

`X` |

The number in base 16 using upper case letters A - F. |
|

Floating point |   |
|

`e` |

The number in scientific notation. The letter âeâ denotes the exponent part. |
|

`E` |

The number in scientific notation. The letter âEâ denotes the exponent part. |
|

`f` |

The number in decimal floating point notation, lowercase. This is the default for floating point numbers. |
|

`F` |

The number in decimal floating point notation, upper case. |
|

`g` |

The number in the shortest possible representation : âeâ or âfâ. |
|

`G` |

The number in the shortest possible representation : âEâ or âFâ. |
|

`a` |

The number in hexadecimal floating point notation, lower case. |
|

`A` |

The number in hexadecimal floating point notation, upper case. |
|

`x` |

The same as âaâ. |
|

`X` |

The same as âAâ. |
|

Pointer |   |
|

`p` |

The pointer address. This is the default for pointers. |
**Note:** If the argument type does not match the specifier field, the default specifier for the argument type is used to convert the argument value to a string.
If the type of the format argument is a pointer, the Logging subsystem writes to the log the address stored in the pointer. If the type of the format argument is array `(T[])`, the Logging subsystem writes to the log the address of the first element of that array. Only string literals of type `const char[]` or `char[]` are written to the log as text.
To write to the log the string pointed to by the `const char*` or `char*` pointer, you can use the `string_view` object. You can initialize the `string_view` object with the pointer to the string that you want to log and then use that object as a log format argument. If you pass a pointer to the string as a format argument, only the address of that string is written to the log.
You can use objects of user-defined type as log format arguments. The Logging subsystem uses the `logArgumentToString` template function to convert objects of user-defined type to string. Only the **align** format argument is applicable for user-defined types. The Logging subsystem specializes `logArgumentToString` for several user-defined types.
#### Examples

To log a message using various argument specifiers:

```
// Log the value of 10 in different base systems.
// Output: decimal: 10, octal: 012, hexadecimal: 0xa.
kzLogInfo(MY_LOG_CATEGORY, ("decimal: {}, octal: {:#o}, hexadecimal: {:#x}.", 10, 10, 10));

// Using argument index could be shortened to:
// added in resulting text to octal or hexadecimal presentation.
// Output: decimal: 10, octal: 012, hexadecimal: 0xa.
kzLogInfo(MY_LOG_CATEGORY, ("decimal: {}, octal: {0:#o}, hexadecimal: {0:#x}.", 10));

// Field width is 4 characters.
// Output: decimal:  10.
kzLogInfo(MY_LOG_CATEGORY, ("decimal:{:4}.", 10));

// Field width is 4 characters, left aligned.
// Output: decimal:10  .
kzLogInfo(MY_LOG_CATEGORY, ("decimal:{:<4}.", 10));

// Field width is 4 characters, zero filled.
// Output: decimal:0010.
kzLogInfo(MY_LOG_CATEGORY, ("decimal:{:04}.", 10));

// Field width is 4 characters, with sign and left aligned.
// Output: decimal:+10 .
kzLogInfo(MY_LOG_CATEGORY, ("decimal:{:<+4}.", 10));

```

To use string format arguments:

```
const char* message = "Hello world!!!";

// Write message to the log:
// Output: Message: Hello World!!!
kzLogInfo(MY_LOG_CATEGORY, ("Message: {}", string_view(message)));

// Write string literal to the log:
// Output: Message: String literal message.
kzLogInfo(MY_LOG_CATEGORY, ("Message: {}", "String literal message."));

```

## Setting the log level

Use log levels to show log messages based on their severity. For example, to log critical issues during application execution, use the `error` log level (`log_level.hpp::KZ_LOG_LEVEL_ERROR`).

The Kanzi logging system has these log levels:
|

Log level |

Name |

Severity |

Description |
|

`log_level.hpp::KZ_LOG_LEVEL_ERROR` |

`error` |

1 |

Logs critical malfunction messages. Create detailed error messages so that you can receive enough information about an issue. |
|

`log_level.hpp::KZ_LOG_LEVEL_WARNING` |

`warning` |

2 |

Logs facts that require attention, which are not necessarily malfunctions. For example, use a warning message to notify the user about an outcome from which the application can recover, such as a missing parameter that has a default value, or an event that can lead to performance degradation, but is not a failure. |
|

`log_level.hpp::KZ_LOG_LEVEL_INFO` |

`info` |

3 |

Logs information that gives a brief overview of what is happening in the system, log states passed, static information about configuration, and so on. |
|

`log_level.hpp::KZ_LOG_LEVEL_TRACE` |

`trace` |

4 |

Logs the maximum amount of information about the system. This is the most verbose log level. Use this level to troubleshoot issues. |

These log levels are enabled by default:

- `log_level.hpp::KZ_LOG_LEVEL_ERROR`
- `log_level.hpp::KZ_LOG_LEVEL_WARNING`
- `log_level.hpp::KZ_LOG_LEVEL_INFO`

To set the log level, use the `log_level.hpp::KZ_LOG_LEVEL_ENABLED_THRESHOLD` macro.

For example, to set a log level that enables all log levels:

```
#define KZ_LOG_LEVEL_ENABLED_THRESHOLD KZ_LOG_LEVEL_TRACE

```

You can create you own log levels. See `LogLevelMacros::KZ_LOG_CREATE_LEVEL`.
## Using log categories

Use log categories to group log messages that contain information related to specific functionality.

The Kanzi logging system has these default log categories:
|

Log category |

Description |
|

`LogCategories::KZ_LOG_CATEGORY_DEBUG` |

Collects debug messages. |
|

`LogCategories::KZ_LOG_CATEGORY_GRAPHICS_MESH_EXTRA` |

Collects graphics mesh log messages. |
|

`LogCategories::KZ_LOG_CATEGORY_EGL_EXTRA` |

Collects EGL log messages. |
|

`LogCategories::KZ_LOG_CATEGORY_GENERIC` |

Collects log messages that you have not assigned to any other log category. It is recommended to always explicitly assign a log message to one of the log categories, or create a new log category. |

To create and use a log category:

1.

Create a log category with the `LogCategoryMacros::KZ_LOG_CREATE_CATEGORY` macro:

```
// Create a log category named "My category" and set the state of the category to enabled.
// The Kanzi logging system uses category state to filter log messages.
// To disable a log category, use the KZ_LOG_DISABLED_CATEGORY.
#define MY_LOG_CATEGORY    KZ_LOG_CREATE_CATEGORY(KZ_LOG_ENABLED_CATEGORY, "My category")

```

2.

Print a log message in the log category that you created:

```
// Print to the log "This is an info message." using the MY_LOG_CATEGORY log category.
kzLogInfo(MY_LOG_CATEGORY, ("This is an info message."));

```

3.

Build and run your application or interact with your application in the Kanzi Studio Preview. When your application reaches the code where you created the log message, Kanzi prints the message to the debug console or to the Kanzi Studio Log window:

```
info:My category> This is an info message.

```

## Creating a custom logger

To redirect log messages, you can implement a custom logger class, which inherits from `AbstractLogger`, and push the custom logger to the Kanzi logging system. Make your logger class override the `AbstractLogger::writeOverride` function.

To write log messages using your custom logger, use the `log.hpp::kzLog` macro.

If you want to use your custom logger to write all the application log messages, register the logger in the Default Logger (`DefaultLogger`). The Default Logger inherits from `AbstractLogger` and contains a chain of loggers through which every log message passes. These loggers are by default registered in the Default Logger:
|

Default logger |

Destination of log messages |
|

`CoutLogger` |

Standard output |
|

`AndroidLogger` |

Android system log |
|

`Win32DebugLogger` |

Kanzi debug console on Windows |

To implement a logger:

```
// Use this logger to store log messages in a container for later retrieval.
//
// This class inherits from kanzi::AbstractLogger and implements the writeOverride() function. It stores logs in the container.
// To retrieve the logs, use the get() function.
class SimpleLogger : public AbstractLogger
{
public:
    // Kanzi calls this function to write messages to the log.
    //
    // This function stores the log message in a container. To retrieve all log messages, use the get() function.
    // Each log message includes:
    // - The message text
    // - The log level
    // - The log category
    // - If the message is an error, the file name and the line number where the error occured
    //
    // \param level The log level of the message.
    // \param levelName The string representation of the log level.
    // \param categoryName The string representation of the log category.
    // \param fileName The name of the file in which the message originated.
    // \param lineNumber The number of the line on which the message originated.
    // \param message The message.
    void writeOverride(LogLevel level, string_view levelName, string_view categoryName,
                       string_view fileName, size_t lineNumber, string_view message) override
    {
        // Start the log with the level name.
        string logMessage(levelName);

        // Separate the log level and the log category with a colon.
        logMessage += ':';

        // Add the category name.
        logMessage.append(categoryName.data(), categoryName.length());

        if (level == LogLevelError)
        {
            // The error is reported.
            // To show where in the code the error was reported, add the file name and the line number to the message.
            logMessage.append(fileName.data(), fileName.length());

            // Separate the file name and the line number with a colon.
            logMessage += ':';
            logMessage += to_string(lineNumber);
        }

        // Add an angle bracket and the message text.
        logMessage += "> ";
        logMessage.append(message.data(), message.length());

        // Append the log message to the log vector.
        m_log.push_back(logMessage);
    }

    // Get log vector reference.
    vector<string>& getLog()
    {
        return m_log;
    }

private:
    // Log vector.
    vector<string> m_log;
};

```

To use a logger explicitly:

```
// SimpleLogger inherits from kanzi::AbstractLogger and implements writeOverride.
SimpleLogger simpleLogger;

// Write a log message using SimpleLogger.
kzLog(simpleLogger, KZ_LOG_LEVEL_INFO, KZ_LOG_CATEGORY_GENERIC, ("Lets log 1 + 2 = {}.", 1 + 2));

```

To use a logger in logger chain:

```
// SimpleLogger inherits from kanzi::AbstractLogger and implements writeOverride.
AbstractLoggerUniquePtr simpleLogger(new SimpleLogger());

// Before adding SimpleLogger to the logger chain, get the pointer to it.
// After you add SimpleLogger to the logger chain, the logger chain controls the lifetime of SimpleLogger.
SimpleLogger* simpleLoggerPtr = static_cast<SimpleLogger*>(simpleLogger.get());

// Push SimpleLogger to the logger chain. Now both SimpleLogger and the rest of the loggers handle every logged message.
DefaultLogger::pushLogger(kanzi::move(simpleLogger));

// Write a log message. SimpleLogger handles this message.
kzLogInfo(KZ_LOG_CATEGORY_GENERIC, ("Lets log 1 + 2 = {}.", 1 + 2));

```

To exclusively redirect log messages to a logger:

```
// SimpleLogger inherits from kanzi::AbstractLogger and implements writeOverride.
AbstractLoggerUniquePtr simpleLogger(new SimpleLogger());

// Before adding SimpleLogger to the logger chain, get the pointer to it.
// After you add SimpleLogger to the logger chain, the logger chain controls the lifetime of SimpleLogger.
SimpleLogger* simpleLoggerPtr = static_cast<SimpleLogger*>(simpleLogger.get());

// Remove all default loggers from the logger chain. This way you make only SimpleLogger, which you push to the chain later, handle the logged messages.
DefaultLogger::popAllLoggers();

// Push SimpleLogger to the logger chain. Now only SimpleLogger handles every logged message.
DefaultLogger::pushLogger(kanzi::move(simpleLogger));

// Write a log message. SimpleLogger handles this message.
kzLogInfo(KZ_LOG_CATEGORY_GENERIC, ("Lets log 1 + 2 = {}.", 1 + 2));

```

## QNX system logger (slogger2)

On QNX you can use the QNX system logger (slogger2) to write log messages. When you redirect log messages to slogger2, your Kanzi application continues writing the log messages to the default logger.

By default QNX writes the slogger2 logs to `/tmp/slogger2/<Kanzi-application-name>.<process-id>`.

Keep in mind that slogger2 initializes after Kanzi reads the configuration for your Kanzi application. For this reason the slogger2 logs do not contain the log messages before that time.

To learn how to configure slogger2 in a Kanzi application, see QNX system logger (slogger2).
### Viewing a slogger2 log file

To view a slogger2 log file on a QNX device, run:

```
slog2info -l <log-filename>

```

### Registering a custom slogger2 buffer

Kanzi enables you to register a custom slogger2 buffer and pass it to a Kanzi application. Your Kanzi application then uses the buffer to write logs. For example, you can register a custom slogger2 buffer when you want to give the buffer a custom name or if you want to set any of the properties from the `slog2_buffer_set_config_t` structure passed to `slog2_register`.

When you register a slogger2 buffer, slogger2 ignores all the other QNX logger configuration parameters that you set in an `application.cfg` or `Application::onConfigure`.

Keep in mind that -1 and null are not valid values for the slogger2 buffer name.

To register a custom slogger2 buffer, in `Application::onConfigure` set:

```
configuration.slog2Config.customSlog2Buffer = value

```

where `value` is a `slog2_buffer_t` type buffer. The default value is nullptr (disabled).

For example, you can register a custom slogger2 buffer like this:

```
// Register one slog2_buffer_t buffer.
vector<slog2_buffer_t> buffers = vector<slog2_buffer_t>(1);

slog2_buffer_set_config_t buffersetConfig{ 1, "MyBufferset", SLOG2_INFO, {{ "MyBuffer", 16 }}, UINT32_MAX };

if (slog2_register(&buffersetConfig, buffers.data(), 0) != 0)
{
    // Handle the error.
}

// Pass the registered buffer to the application.
configuration.slog2Config.enabled = true;
configuration.slog2Config.customSlog2Buffer = buffers[0];

```

### Cleaning up after slogger2

When your Kanzi application quits, slogger2 by default calls `slog2_reset`. This frees all the slogger2 buffers registered by a Kanzi process, not just the one registered by Kanzi. You can change this behavior by overriding `Application::uninitializePlatform`. For example, change this behavior when you want to call `slog2_reset` after a Kanzi application quits.

```
class MyApplication : public Application
{

   ...

public:

     ...

     // Override the uninitializePlatform method to prevent calling slog2_reset.
     void uninitializePlatform() final
     {

         ...

     }
 }

```
