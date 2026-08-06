---
title: Step 3 - Instantiate prefabs
source: https://docs.kanzi.com/4.1.0/en/tutorials/fifteen-puzzle/step-3.html
---

# Step 3 - Instantiate prefabs


In this step, you learn how to instantiate prefabs from a Lua script.

To instantiate a prefab to the node tree:

1.

Find a prefab with `tryAcquireResource`.
2.

Create a node from the prefab with `instantiate`.
3.

Add the node to the node tree with `addChild`.


```
-- Find the node with the alias "Grid".
local grid = contextNode:lookupNode("#Grid")
assert(grid)

-- Find the "Piece" prefab.
local piecePrefab = contextNode:tryAcquireResource("kzb://fifteen_puzzle/Prefabs/Piece")

-- Use the piecePrefab to create a node named "New piece".
local node = piecePrefab:instantiate("New piece")

-- Add the node to the grid.
grid:addChild(node)

```

## Add pieces to the puzzle grid


Instantiate **Piece** prefabs to populate the puzzle grid with 15 pieces in order from 1 to 15. You leave the last grid slot empty so that you can play the game.

To add pieces to the puzzle grid, in the **Script Editor**, replace the content of the **new_game.lua** script with:

```
print("Entering new_game.lua")

-- Find the "Grid" node using its alias.
local grid = contextNode:lookupNode("#Grid")
assert(grid)

-- Find the "fifteen_puzzle.PieceIndex" custom property type.
local PieceIndexProperty = PropertyType:find("fifteen_puzzle.PieceIndex")

-- Find the "Piece" prefab.
local piecePrefab = contextNode:tryAcquireResource("kzb://fifteen_puzzle/Prefabs/Piece")

-- Declare the constants for the grid size and number of pieces.
-- The number of pieces is one less than the number of grid slots
-- because you need an empty slot to play the game.
local RowCount = 4
local ColumnCount = 4
local PieceCount = RowCount * ColumnCount - 1

-- Remove all grid items that were created in the project or by the earlier
-- executions of the script.
grid:removeAllChildren()

-- Create the grid child nodes.
for i = 1,PieceCount do
    -- Create a grid item.
    local piece = piecePrefab:instantiate("piece_" .. i)

    -- Assign the number to the piece.
    piece:setProperty(PieceIndexProperty, i)

    -- Set the grid coordinates of the node.
    -- Use integer division to get the row index and modulo to get the column index.
    local row = (i-1) // ColumnCount
    local column = (i-1) % ColumnCount
    piece:setProperty(GridLayout2D.RowProperty, row)
    piece:setProperty(GridLayout2D.ColumnProperty, column)

    -- Add the node to the grid.
    grid:addChild(piece)
end

print("Exiting new_game.lua")

```


When you save the script and in the **Preview** click , the script populates the grid with 15 pieces in order from 1 to 15 and leaves the last slot in the grid empty.

Previous step Next step
