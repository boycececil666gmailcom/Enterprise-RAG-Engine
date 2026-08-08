---
title: Creating backups of your projects
source: https://docs.kanzi.com/4.1.0/en/working-with/backups/backups.html
---

# Creating backups of your projects

In Kanzi Studio you can create:

- **Automatic backups**. Every time Kanzi Studio automatically saves your project it makes a copy of the project and stores it in a file with .autosave extension. Kanzi Studio stores only one copy of the .autosave file. See Setting automatic backups and Restoring your project from an automatic backup.
- **Manual backups**. Every time you save your project, Kanzi Studio makes a copy of the project and stores it in a file with extension _N, where N is the consecutive number of the backup. Kanzi Studio stores the ten latest project file backups. For example, if the name of your project is Orchard, project file is Orchard.proj.kzm, latest backup is Orchard.proj.kzm_1, second to latest backup is Orchard.proj.kzm_2, and so on. See Restoring your project from a manual backup.
- Restore Points. Use restore points to return to an earlier version of your project. When you create a restore point for a project, Kanzi Studio makes the complete copy of your project into a timestamped directory in the `<ProjectName>/Restore Points` directory. See Creating restore points and Restoring a project from a restore point.

## Setting automatic backups

Every time Kanzi Studio automatically saves your project it makes a copy of the project and stores it in a file with .autosave extension. Kanzi Studio stores only one copy of the .autosave file.

By default Kanzi Studio automatically saves your project every 15 minutes. Kanzi Studio automatically saves your project only if you make a change in the project.

To set the automatic backups, select Edit > User Preferences and in the Autosave:

- To take automatic backups into use, enable the Enabled setting.
- To set the time between automatic backups, enter the number of minutes in the Interval text box.

## Restoring your project from an automatic backup

To restore your project from an automatic backup, select File > Open Backup Save and select Autosave to open the automatic backup.
## Restoring your project from a manual backup

Every time you save your project, Kanzi Studio makes a copy of the project and stores it in a file with extension _N, where N is the consecutive number of the backup. Kanzi Studio stores the ten latest project file backups. For example, if the name of your project is Orchard, project file is Orchard.proj.kzm, latest backup is Orchard.proj.kzm_1, second to latest backup is Orchard.proj.kzm_2, and so on.

To restore your project from a manual backup, select File > Open Backup Save and select Backup and the version you want to open.
## Creating restore points

Use restore points to return to an earlier version of your project. When you create a restore point for a project, Kanzi Studio makes the complete copy of your project into a timestamped directory in the `<ProjectName>/Restore Points` directory.

Making restore points for your project is useful so that you can return to the state of your project before you made, for example, a significant change to your project.

To create a restore point, while you have your project open in Kanzi Studio and before you make a significant change, select File > Save Restore Point.

Kanzi Studio makes the complete copy of your project into a timestamped directory in the `<ProjectName>/Tool_project/Restore Points` directory.
## Restoring a project from a restore point

To restore a project from a restore point:

1.

Go to the project directory of the project you want to restore and open the `Tool_project/Restore Points` directory.
2.

Open the timestamped directory from which you want to restore your project and open the Kanzi Studio project file. The project from the restore point you selected opens in a new instance of Kanzi Studio.
