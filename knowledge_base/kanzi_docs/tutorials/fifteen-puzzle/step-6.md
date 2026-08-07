---
title: Step 6 - Send messages
source: https://docs.kanzi.com/4.1.0/en/tutorials/fifteen-puzzle/step-6.html
---

# Step 6 - Send messages

In this step, you learn how to send messages from a Lua script.

You first create a function that checks whether the puzzle is solved and then add the functionality to show a message when the puzzle is solved.
## Detect a solved puzzle

To detect a solved puzzle:

1.

Define a function that checks whether the puzzle is solved before you define the `movePieceMessageHandler`.

```
-- Declare a function that checks for the victory condition.
local function checkForVictory()
    -- Count the number of pieces in a wrong position.
    local misplacedCount = 0
    for i = 0,PieceCount-1 do
        local piece = grid:getChild(i)
        local row = piece:getProperty(GridLayout2D.RowProperty)
        local column = piece:getProperty(GridLayout2D.ColumnProperty)
        local expectedRow = i // ColumnCount
        local expectedColumn = i % ColumnCount
        if row ~= expectedRow or column ~= expectedColumn then
            misplacedCount = misplacedCount + 1
        end
    end

    if misplacedCount == 0 then
        print("Victory!")
    end
end

```

2.

Call the function at the end of the `movePieceMessageHandler` message handler.

```
local function movePieceMessageHandler(args)

    ...

    checkForVictory()
end

```

Now when you solve the puzzle, the script prints `Victory!` to the **Log**. Send a message âââââ

To send a message:

1.

Use the **VictoryMessage** message type that is defined in the Kanzi Studio project.

In the script, initialize the variable next to other variables.

```
-- Find the "fifteen_puzzle.VictoryMessage" custom message type.
local VictoryMessage = MessageType:find("fifteen_puzzle.VictoryMessage")

```

2.

Modify the `checkForVictory` function so that after it prints a message to the **Log**, the function sends the `VictoryMessage` to the **Grid** node.

The **Grid** node uses a `VictoryMessage` trigger to set the **Victory Overlay State Manager** to the **Visible** state that shows the victory message.

Create the message arguments with `VictoryMessage:newMessageArguments()` and send the message to a node with the `dispatchMessage` member function.

```
local function checkForVictory()

...

    if misplacedCount == 0 then
        print("Victory!")

        -- Send a VictoryMessage to the grid node.
        local args = VictoryMessage:newMessageArguments()
        grid:dispatchMessage(VictoryMessage, args)
    end
end

```

Now the Lua script contains the complete game logic that:

- Fills the grid with pieces in random order.
- Reacts to input messages by moving the pieces according to the puzzle logic.
- Detects when the puzzle is solved and reacts by sending a message that displays the victory message in the application.

Previous step
## Whatâs next?

In this tutorial, you learned the basics of programming application logic in Kanzi with Lua.

To learn more about:

- Using Kanzi Engine Lua API in Kanzi Studio, see Using Lua.
- Kanzi functions that you can use in a Kanzi Lua script, see Kanzi Lua API reference.
- The Lua programming language, see https://www.lua.org/manual/5.4/.
