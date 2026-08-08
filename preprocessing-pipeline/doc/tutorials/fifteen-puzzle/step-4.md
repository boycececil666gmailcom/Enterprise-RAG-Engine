---
title: Step 4 - Randomize the grid
source: https://docs.kanzi.com/4.1.0/en/tutorials/fifteen-puzzle/step-4.html
---

# Step 4 - Randomize the grid

In this step, you learn how to define your own functions in a Lua script. First you define helper functions, then you use these functions to randomize the initial positions of the pieces in the grid.

To randomize the grid:

1.

Define a function that returns an array of integers.

In Lua, you declare functions with the `function` keyword.

Add the function to the script before the `grid:removeAllChildren()`.
**Note:** This function starts the array at index 1. This is customary in Lua, but is not required. Keep in mind that the Kanzi Engine functions, such as `getChild`, start indexing at 0.
```
-- Declare a function that returns a list of integers from 1 to length.
local function createArray(length)
-- Initialize a variable that contains an empty array.
local array = {}
-- Fill the array with integers.
for i = 1,length do
array[i] = i
end
return array
end
```
2.
Define a function that randomizes the given array of integers, and add it after the `createArray` function.
You can use the built-in Lua Math library.
```
-- Declare a function that randomizes the array argument with Fisher-Yates shuffle.
local function shuffleArray(array)
-- Loop backward from array length to 2.
for i = #array, 2, -1 do
-- Use the Lua Math library to create a random integer.
local j = math.random(i) -- j is in range [1,i]
-- Swap the array items at index i and j.
array[i], array[j] = array[j], array[i]
end
end
```
3.
Not all puzzle configurations are solvable 15 puzzles. Define a function that checks whether a given permutation represents a solvable puzzle. If the puzzle is not solvable, this function modifies the permutation. Add the function after the `shuffleArray` function.
```
-- Declare a function that modifies the given permutation to make it a solvable puzzle.
local function makeSolvable(permutation)
local n = #permutation
-- Count the number of inversions in the permutation.
local inversions = 0
for i = 1,n do
for j = i+1,n do
if permutation[i] > permutation[j] then
inversions = inversions + 1
end
end
end
-- If the puzzle is not solvable, swap two adjacent pieces to fix it.
if inversions % 2 == 1 then
permutation[1], permutation[2] = permutation[2], permutation[1]
end
end
```
4.
To get a randomized grid, use the helper functions in the grid creation.
```
...
-- Remove all grid items that were created in the project or by the earlier
-- executions of the script.
grid:removeAllChildren()
-- Create a random permutation.
local permutation = createArray(PieceCount)
shuffleArray(permutation)
-- Ensure that the permutation is a solvable puzzle.
makeSolvable(permutation)
...
```
5.
Modify the part of the script that populates the grid so that it applies the permutation.
```
...
-- Create the grid children.
for i = 1,PieceCount do
-- Create a grid item.
local piece = piecePrefab:instantiate("piece_" .. i)
-- Assign the number to the piece.
piece:setProperty(PieceIndexProperty, i)
-- Set the grid coordinates of the new node.
local p = permutation[i]
-- Use integer division to get the row index and modulo to get the column index.
local row = (p-1) // ColumnCount
local column = (p-1) % ColumnCount
...
```

When you save the script and in the **Preview** click , the script populates the grid with 15 pieces in random order.

Previous step Next step
