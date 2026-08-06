---
title: Step 1 - Run a Lua script
source: https://docs.kanzi.com/4.1.0/en/tutorials/fifteen-puzzle/step-1.html
---

# Step 1 - Run a Lua script


In this step, you learn how to run a Lua script and use Lua variables.
## Get the tutorial


To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Fifteen puzzle tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find:

- The tutorial starting point project in the `<KanziWorkspace>/Tutorials/Fifteen puzzle/Start` directory.
- The completed tutorial in the `<KanziWorkspace>/Tutorials/Fifteen puzzle/Completed` directory.

## Content of the starting point project


The starting point project contains the content that you need to complete this tutorial:

- **Grid** node defines the structure of the puzzle and, together with the **Background** node, its appearance. The **Grid** node contains a **VictoryMessage** trigger with a **State Manager: Go To State** Action that sets the **Victory Overlay State Manager** to the **Visible** state and shows the victory message when the user solves the puzzle.
- **Restart** node defines the appearance of the button that starts a new game. The **Restart** node contains a **Button: Click** trigger with a **State Manager: Go To State** Action that sets the **Victory Overlay State Manager** to the **Invisible** state and removes the victory message when the user clicks the button after solving the puzzle.
- **Victory Overlay** node defines the appearance of the message that the application shows when the user solves the puzzle. The **Victory Overlay State Manager** sets the visibility of **Victory Overlay** through the triggers and actions in the **Grid** and **Restart** nodes.
- The **Piece** prefab defines the appearance of the puzzle pieces. The **Piece** prefab contains an **Animation Player** that plays the **Reveal** keyframe animation clip when the user restarts the puzzle.
- In the **Piece** prefab, the **Button** node contains a **Button: Click** trigger with a **MovePieceMessage** action that the script uses to move pieces on the grid.
- The application uses the **PieceIndex** property type to show the numbers on puzzle pieces.
- The **Screen** node resource dictionary contains aliases to key nodes.

## Run a Lua script


To run a Lua script:

1.

In the **Node Tree**, select the **Root** > **Stack** > **Restart** node. In the **Node Components**, in the **Button: Click** trigger, press Alt and right-click **Actions** and select **Run Lua Script**.
2.

In the **Run Lua Script** Action, in the **Lua Script** property, select **+ Script File** and name the script **new_game**.
3.

In the **Library** > **Resource Files** > **Scripts**, open the script file and add:

```
-- Write output to the Log window.
print("Hello world!")

```

4.

In the **Script Editor**, click **Save**.


In the **Preview**, when you click , Kanzi sets off the trigger in the **Restart** node that executes the Lua script, and the script writes **Hello world!** to the **Log** window.

> **Tip:** To open the Log window, in the main menu select Window > Log.
## Use Lua variables


In Lua, you can declare:

- Local variables, which are accessible only in the scope of the script where you declare a variable

Kanzi destroys local variables at the end of the scope.
- Global variables, which are accessible in all scripts and are persistent across multiple script executions


To use Lua variables:

1.

In the **Script Editor**, replace the content of the **new_game.lua** script with:

```
print("Entering new_game.lua")
-- Initialize a local temporary variable x.
-- Variables that you declare locally are accessible only in the scope of this script.
-- Kanzi destroys local variables at the end of the scope.
local x = 0

-- Check whether the global persistent variable y is initialized in an earlier script execution.
if y == nil then
      -- Initialize a persistent global variable y on the first run of this script.
      -- Global variables are shared and accessible in all scripts.
      -- Global variables are persistent across multiple script executions.
      y = 0
end

-- Loop variable i across the values 1, 2, 3, 4, and 5.
-- Variables declared in a for loop are always local.
for i = 1,5 do

   -- Modify the local variable x.
   x = x + 1

   -- Modify the persistent global variable y.
   y = y + 1

   -- Write the variables to the Log window.
   print(string.format("%d: x = %d, y = %d", i, x, y))
end
print("Exiting new_game.lua")

```

2.

Save the script.


In the **Preview**, when you click , the script writes the output to the **Log** window. When you click  the second time, notice that the value of the local variable `x` is reset, while the value of the global variable `y` persists between executions.

Introduction Next step
