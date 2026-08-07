---
title: Using Java and Kotlin
source: https://docs.kanzi.com/4.1.0/en/working-with/java/using-java.html
---

# Using Java and Kotlin


Kanzi Java API implements platform-independent Java proxies for Kanzi classes, providing rich access to the Kanzi functionality in Java and Kotlin. This enables you to create applications that are tightly integrated with the Android APIs.

On Android, you can use the Kanzi Java API directly from the Android UI thread without the need for dispatcher mechanisms. See Developing with the Kanzi Android framework (droidfw).

This topic provides an overview of the fundamentals of Kanzi Java API. For complete API reference, see Kanzi Engine Java API reference.
## Requirements


Kanzi Java API requires Java 8 (1.8) or higher.
## Using properties


Kanzi Java API classes contain static members for built-in property types such as `metadata.NodeMetadata.OpacityProperty`. To read and write these properties:
