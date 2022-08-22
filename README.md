# Dinamyc Programming Five Elementals Land
Dinamyc programming approcah to finding the minimum cost path in a array.
Five Elementals Land is a minigame event in the mobile game Immortal Taoists. 
In this minigame there are five elements: gold, wood, earth, water and fire.
Each element is strong agains one element and is weak to another, similar to a game of rock, paper, scissors.
The cost to move to a cell with a weaker element is 0, to a cell with a stronger is 2 and the rest costs 1.
The objective is to reach the end of the map with the minimum cost.
The end of the map is in the diagonal of the start.

This program will print 2 arrays, the original array with the individual costs to move to each cell (the obstacle cells are left as open spaces), and the memo array with the minimum cost to reach each cell.