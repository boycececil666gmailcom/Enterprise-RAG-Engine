---
title: Using resource dictionaries
source: https://docs.kanzi.com/4.1.0/en/working-with/resources/using-resource-dictionaries.html
---

# Using resource dictionaries

A resource dictionary is a collection of resource IDs pointing to resources. You can add a resource dictionary to any node.

By default, resource dictionaries are present in:

- Screen node
- Root nodes of all prefabs

A node can access all resource IDs in its own resource dictionary and in resource dictionaries defined in its ancestor nodes. You can assign resource IDs as values for resource properties and they are shown in Kanzi Studio with the syntax ResourceID â Resource.

You can make resources local to any node. By adding a resource to a scope of a node you add a resource ID entry to the resource dictionary of that node. A resource ID is an identifier that abstracts a resource from where it is used.
## Adding a resource dictionary to a node

To add a resource dictionary to a node, in the Node Tree press Alt and right-click a node and select Resource Dictionary.
## Viewing the content of a resource dictionary

To view the content of a resource dictionary:

1.

In the Node Tree select the node the content of whose resource dictionary you want to see in the Dictionaries. Resources listed in the Dictionaries are color-coded:

  - White type marks the effective resources from the selected resource dictionary.

For example, in the image below, all resources in the Screen node are effective.
  - Gray italics type marks the resources which are overridden by resources from another resource dictionary.

For example, in the image below, the value of the Body text resource in the resource dictionary of the Screen node is overridden by the Body text resource in the resource dictionary of the Warning message node.
  - Orange type marks aliases. See Using aliases.

For example, in the image below, the Media is an alias pointing to the Screen/RootPage/Media node.
  - White type on light gray background marks the resources in the selected locale or theme which use the default value set in a localization table or theme group. See Localization and Theming your applications.

For example, in the image below, the en-US locale in the Localization Table uses the default value for the Hello text resource ID defined in that localization table.

## Viewing and activating locales and themes

To view and activate locales and themes, in the Dictionaries click Locales and Themes to enable the viewing of localization tables and theme groups, and for each localization table and theme group select the locale and theme you want to see in the Preview.
## Adding a resource to a resource dictionary

To add a resource to a resource dictionary:

1.

Add a resource dictionary to a node. See Adding a resource dictionary to a node.
2.

In the Dictionaries click + Add Resource and select:

  - Create and select the type of resource you want to create.
  - Add Existing and select a resource that already exists in your project.

## Using a kzb URL for a resource in a resource dictionary

You can use a kzb URL to point to resources in another Kanzi Studio project.

To use a kzb URL for a resource in a resource dictionary:

1.

In the Dictionaries double-click the cell for the resource for which you want to use a kzb URL and in the dropdown menu select < URL >.
2.

In the cell enter the kzb URL of the resource you want to use.

For example, to use a font from another Kanzi Studio project, enter the kzb URL pointing to that font.

## Using resource dictionaries in the API

To create a resource dictionary:

```
// Create a resource dictionary.
ResourceDictionarySharedPtr dictionary = ResourceDictionary::create(domain, "Dictionary");

```

To add content to a resource dictionary:

```
// Add resources to a resource dictionary.
dictionary->add(ResourceID("red icon"), texture);
dictionary->add(ResourceID("blue icon"), "kzb://my_project/Textures/Blue Icon");

```

To get resources from a resource dictionary:

```
// Acquire resources from a resource dictionary.
ResourceSharedPtr redIcon = dictionary->acquire(ResourceID("red icon"));
ResourceSharedPtr blueIcon = dictionary->acquire(ResourceID("blue icon"));

```

To change the resource dictionary of a node:

```
// Change the resource dictionary of a node.
node->setResourceDictionary(dictionary);

```

To extend the existing resource dictionary of a node:

```
// Extend the existing resource dictionary of a node with a nested resource dictionary.
node->addResourceDictionary(dictionary);

```

For details, see the `ResourceDictionary` class.
