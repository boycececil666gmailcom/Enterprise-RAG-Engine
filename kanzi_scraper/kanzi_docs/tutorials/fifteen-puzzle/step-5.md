---
title: Step 5 - React to input messages
source: https://docs.kanzi.com/4.1.0/en/tutorials/fifteen-puzzle/step-5.html
---

# Step 5 - React to input messages


In this step, you learn how to use message handlers in a Lua script.

You first declare a message handler and then add the functionality to the message handler to move the pieces.
## Declare a message handler


To declare a message handler:

1.

Use the **MovePieceMessage** message type that is defined in the Kanzi Studio project.

In the script, initialize the variable next to other variables.

In the **Preview**, when you click a **Piece** prefab, the **Button 2D** node sends this message to itself.

```
-- Find the "fifteen_puzzle.MovePieceMessage" custom message type.
local MovePieceMessage = MessageType:find("fifteen_puzzle.MovePieceMessage")

```

2.

Define the message handler function for the `MovePieceMessage` before you define the `createArray` function.

```
-- Declare a message handler function for the "MovePieceMessage".
local function movePieceMessageHandler(args)
    -- Read the message argument that contains the index of the clicked piece.
    local index = args:getArgument(PieceIndexProperty)

    -- Find the clicked node.
    local piece = grid:getChild(index - 1)

    -- Read the property values of the clicked node.
    local row = piece:getProperty(GridLayout2D.RowProperty)
    local column = piece:getProperty(GridLayout2D.ColumnProperty)

    print(string.format("Clicked node %d at (%d,%d)", index, row, column))
end

```

3.

For the `movePieceMessageHandler` function to do something, you must add it to a node. Do this with the `addMessageHandler` function when you create each piece, but before you add it to the grid.

```
-- Create the grid child nodes.
for i = 1,PieceCount do

    ...

    -- Add a message handler for the MovePieceMessage.
    piece:addMessageHandler(MovePieceMessage, movePieceMessageHandler)

    -- Add the new node to the grid.
    grid:addChild(piece)
end

```


When you save the script and in the **Preview** click , and then click any piece, the script prints to the **Log** the index of the clicked piece and its coordinates in the **Grid** node.
## Move puzzle pieces on click


Note that the message handlers persist after the script exits, even if you edit the script further. This script always removes all the created nodes with the `grid:removeAllChildren()`, which also removes the message handlers.

To move puzzle pieces on click:

1.

Declare variables to keep track of the empty slot in the grid.

In the script, initialize the variable next to other variables.

```
-- Keep track of the empty slot in the grid.
-- Initially the empty slot is at the bottom right of the grid.
local freeSlotRow = RowCount - 1
local freeSlotColumn = ColumnCount - 1

```

2.

Modify the `movePieceMessageHandler` message handler so that instead of just printing to the **Log**, it moves the clicked piece and records the move to the **Log**.

```
-- Declare a message handler function for the "MovePiece" message.
local function movePieceMessageHandler(args)
    -- Read the message argument that contains the index of the clicked piece.
    local index = args:getArgument(PieceIndexProperty)

    -- Find the node that was clicked.
    local piece = grid:getChild(index - 1)

    -- Read the property values of the clicked node.
    local row = piece:getProperty(GridLayout2D.RowProperty)
    local column = piece:getProperty(GridLayout2D.ColumnProperty)

    -- Check whether the piece can be moved.
    local dy = math.abs(row - freeSlotRow)
    local dx = math.abs(column - freeSlotColumn)
    if dx + dy == 1 then
       print(string.format("Moved piece %d from (%d,%d) to (%d,%d)", index, row, column, freeSlotRow, freeSlotColumn))

       -- Move the piece.
       piece:setProperty(GridLayout2D.RowProperty, freeSlotRow)
       piece:setProperty(GridLayout2D.ColumnProperty, freeSlotColumn)
       freeSlotRow = row
       freeSlotColumn = column
    end
end

```


When you save the script and in the **Preview** click , and then click any piece next to the empty slot, the script:

1.

Moves the piece.
2.

Prints to the **Log** the index of the clicked piece, and coordinates of its previous and current location in the grid.


Previous step Next step
