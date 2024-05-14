class Solution:
    """
    This took a *long* time to get working, mostly stemming from me being
    stubborn in wanting a solution that didn't rely on editing `grid` in-
    place. On the whole this isn't the most efficient, it could definitely
    be smarter in utilising paths it has explored before, but it works.
    """

    def depth_first_max(self,
        i: int,                     # current cell x-index
        j: int,                     # current cell y-index
        viable: dict,               # indices of viable cells
        visited: List[tuple[int]],  # indicies of visited cells
        total: int = 0              # maximum path found so far
    ):
        cell = (i, j)
        # path ends if cell already visited or isn't viable
        if cell in visited or cell not in viable: return total

        # add cell value to running total
        total += viable[cell]
        # don't return here this path
        path = visited + [cell]

        # consider best adjacent direction to extend the path
        return max(
            self.depth_first_max(i-1, j, viable, path, total),  # left
            self.depth_first_max(i+1, j, viable, path, total),  # right
            self.depth_first_max(i, j-1, viable, path, total),  # up
            self.depth_first_max(i, j+1, viable, path, total)   # down
        )


    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # create a dictionary of cells in the grid with non-zero value,
        # i.e. those cells which are conidered viable to visit. using this
        # lets us avoid also passing grid for an in-place solution
        viable_cells = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: continue
                # key is indexes, value is gold
                viable_cells[(i, j)] = grid[i][j]

        max_path = 0
        for start_i, start_j in viable_cells:
            max_path = max(
                max_path,
                # `visited=[]` resets the path for each new start point
                # if set as a default argument (as with total) then we
                # see some funky behaviour with the first cell missed
                self.depth_first_max(start_i, start_j, viable_cells, [])
            )

        return max_path
