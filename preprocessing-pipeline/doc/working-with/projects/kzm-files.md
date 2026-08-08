---
title: Kzm file format
source: https://docs.kanzi.com/4.1.0/en/working-with/projects/kzm-files.html
---

# Kzm file format

Kzm is the Kanzi Studio project file format that replaces the kzproj file format. Instead of a single kzproj project file, Kanzi Studio stores your project in multiple kzm files. Each kzm file contains data for one project item. For example, each material type, material, animation, render pass, and so on has its own kzm file.

The goal of the kzm file format is to improve change review, teamwork, and collaboration on Kanzi Studio projects by:

- Providing granular, human-readable files so you can clearly see and review exactly what changed
- Reducing merge conflicts and making any remaining ones easier to resolve
- Simplifying the sharing of project items between different projects
- Enabling scriptable modifications through diff-friendly files
**Note:** Your feedback is very important to us.
Submit your feedback on the kzm file format [here](https://docs.kanzi.com/feedback/v1/forms/feedback-feature.html?featureId=KzmFileFormat&featureTitle=the%20kzm%20file%20format&productArea=studio&productVersion=4.0.0).
Kanzi Studio can still open kzproj projects, but when you save such a project, Kanzi Studio automatically converts it to kzm and removes the kzproj file. This conversion is not reversible. Once you save a project in kzm format, you can no longer revert that project to the kzproj format.
Kanzi Studio shows a notification to inform you about the conversion before completing the save operation.
Kanzi Studio also lets you merge changes from disk when it detects that project files changed externally. See Responding to kzm file changes.
