---
title: Requirements for iOS application development with Kanzi
source: https://docs.kanzi.com/4.1.0/en/working-with/ios/requirements.html
---

# Requirements for iOS application development with Kanzi


To develop iOS applications with Kanzi, you need:

- macOS
- Xcode 26.3 or newer
- iOS SDK 26 or newer
- Vulkan SDK with MoltenVK
- CMake 3.25 or newer
- An Apple Developer account for deploying to physical iOS devices


For more information about setting up the environment for iOS development, see [https://developer.apple.com](https://developer.apple.com/).
## Setting up the development environment

### Installing Xcode and the iOS SDK


To install Xcode and the iOS SDK:

1.

Download and install Xcode from the Mac App Store or from https://developer.apple.com/xcode/.
2.

In Xcode, add the iOS platform. Select Xcode > Settings, then look for the iOS platform under the Components or Platforms tab, depending on your version of Xcode.

### Installing the Vulkan SDK with MoltenVK


Kanzi uses Vulkan for rendering on iOS through MoltenVK. Kanzi requires Vulkan 1.1 as the minimum version. For best compatibility, use the latest available Vulkan SDK. To install the Vulkan SDK:

1.

Download and install the Vulkan SDK from https://vulkan.lunarg.com/sdk/home.
2.

Make sure that the MoltenVK component is included in the installation.


> **Note:** If you install the Vulkan SDK to a custom location instead of the default `/Users/*user*/VulkanSDK`, set the `VULKAN_SDK` environment variable to the installation path of your Vulkan SDK.
>
