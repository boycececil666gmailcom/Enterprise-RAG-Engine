---
title: Deploying Kanzi applications to iOS
source: https://docs.kanzi.com/4.1.0/en/working-with/deploying-applications/deploying-kanzi-applications-for-ios.html
---

# Deploying Kanzi applications to iOS


Kanzi Studio provides tools to generate an Xcode project from your Kanzi application and deploy it to an iOS device.
## Requirements


To develop iOS applications with Kanzi, you need:

- macOS
- Xcode 26.3 or newer
- iOS SDK 26 or newer
- Vulkan SDK with MoltenVK
- CMake 3.25 or newer
- An Apple Developer account for deploying to physical iOS devices


For more information about setting up the environment for iOS development, see [https://developer.apple.com](https://developer.apple.com/).

To deploy to a physical iOS device, you need an Apple Developer certificate to sign the application. See https://developer.apple.com/support/code-signing/.
## Generating the Xcode project


To generate the Xcode project for your Kanzi application:

1.

In Kanzi Studio, export the kzb file of your project. Select File > Export > Export KZB.
2.

Copy the `Application` folder to your Mac development machine.
3.

On your Mac development machine, set the `KANZI_HOME` environment variable to the location of your Kanzi iOS platform package.
4.

From the root of the `Application` folder, run `generate_cmake_xcode_ios_project.sh` to generate the Xcode project:

```
./generate_cmake_xcode_ios_project.sh --platform device

```


> **Note:** If the script is not executable, run `chmod +x generate_cmake_xcode_ios_project.sh` first.
>
## Building and deploying from Xcode


To build and deploy a Kanzi application to an iOS device from Xcode:

1.

Connect your iOS device to your Mac development machine with a USB cable.
2.

Open the generated Xcode project from the `build_ios` folder.
3.

In Xcode, set up code signing for your Apple Developer certificate. See [Apple code signing](https://developer.apple.com/support/code-signing/).
4.

Click Run to build and deploy the application.

## Building and deploying from the command line


To build and deploy a Kanzi application to an iOS device from the command line:

1.

Connect your iOS device to your Mac development machine with a USB cable.
2.

From the `Application` folder, build and install the application to the `output` folder:

```
xcodebuild -project build_ios/<ApplicationName>_ios.xcodeproj \
    -scheme <ApplicationName> -configuration Release \
    -destination 'generic/platform=iOS' \
    DEVELOPMENT_TEAM=<YourTeamID> \
    'DSTROOT=$(PROJECT_DIR)' \
    install

```


Replace `<YourTeamID>` with your Apple Developer Team ID. You can find your Team ID in your [Apple Developer account](https://developer.apple.com/account) under Membership details.

`xcodebuild` places the built application in `output/<ApplicationName>.app`.

> **Tip:** If you do not have an existing provisioning profile, add `-allowProvisioningUpdates` to the `xcodebuild` command to allow it to automatically create one.
> 3.
>
> Find the identifier of your connected device:
>
> ```
> xcrun devicectl list devices
>
> ```
>
> 4.
>
> Install the application on the device:
>
> ```
> xcrun devicectl device install app \
> --device <DeviceIdentifier> \
> output/<ApplicationName>.app
>
> ```
>
> 5.
>
> Launch the application on the device:
>
> ```
> xcrun devicectl device process launch \
> --console \
> --device <DeviceIdentifier> \
> <BundleIdentifier>
>
> ```


> **Note:** The `--console` option prints logs from the iOS application to the macOS terminal.
>
> `<BundleIdentifier>` is the bundle ID of your application, typically in the format `com.company-name.app-name`. For example, `com.rightware.kanzi.basicapplication`.
>
