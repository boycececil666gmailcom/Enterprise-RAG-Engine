---
title: Using Package Manager to create and deploy an asset package
source: https://docs.kanzi.com/4.1.0/en/working-with/package-manager/kpm-to-create-deploy-assets.html
---

# Using Package Manager to create and deploy an asset package

## Creating an asset package project


To create an asset package in Kanzi Studio using the Package Manager:

1.

In the New Project window, create your project using a template of your choice from the Template dropdown.
2.

After building the content of your project, enable the Export in Asset Package property for the assets you want to include in the package.
3.

Enable the Is Asset Package in your project properties.
4.

Save your project.
5.

Navigate to the root of your project directory in the file explorer, which contains three new files that assist in creating and deploying the package:

  - `conanfile.py` governs the asset packaging.
  - `create_and_deploy.bat` is a convenience script that runs the Conan command to create the asset package and deploy it to a specified Conan repository.
  - `README.md` is a quick reference on how to create your asset package as a Conan package and deploy it to a remote.

6.

Edit `create_and_deploy.bat`:

This script contains helper variables you can modify as needed. You can update the package name, version, and the Kanzi version for which this package is intended.

## Creating the asset package as a local Conan package


To create an asset package that you can test locally:

1.

Run `create_and_deploy.bat`:

Deploys the package to the local Conan cache. It does not upload the package to any remote.

> **Note:** This script creates a Conan package identified by a reference of the form `my_asset/1.0.0@kanzi-4.1.0-assets/stable`. The `kanzi-4.1.0-assets` user segment is built from the `KANZI_VERSION` variable in `create_and_deploy.bat`; the `stable` channel is the script default.
> 2.
>
> Open the Package Manager in Kanzi Studio:
>
> - Select the Local tab.
> - Refresh the local packages list by clicking the refresh icon.


  - Your new asset package appears under the local assets.


> **Note:** On non-Windows platforms, use the `create_and_deploy.sh` script instead.
## Creating and deploying the asset package to a remote repository


To create an asset package and publish it to a remote repository:

1.

Run `create_and_deploy.bat <remote>`:

Deploys the package to the local Conan cache and uploads it to remote `<remote>`.

> **Note:** This script creates a Conan package identified by a reference of the form `my_asset/1.0.0@kanzi-4.1.0-assets/stable`. The `kanzi-4.1.0-assets` user segment is built from the `KANZI_VERSION` variable in `create_and_deploy.bat`; the `stable` channel is the script default.
> 2.
>
> Open the Package Manager in Kanzi Studio:
>
> - Select the Remote tab.
> - From the Repository dropdown list, select the repository to where you deployed the asset package.


  - Refresh the repository list by pressing the refresh icon.


  - Your new asset package appears under the repository assets.


> **Note:** On non-Windows platforms, use the `create_and_deploy.sh` script instead.
