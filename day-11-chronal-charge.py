from aoc_helpers import *
serial_number = int(get_input(11)[0])

print(serial_number)


def power_level(x, y, serial_number = serial_number):
    rack_id = x + 10
    power = (rack_id * y + serial_number) * rack_id
    power = power //100 % 10
    power -= 5
    return power

#print(power_level(3,5,8))
#print(power_level(122,79,57))
#print(power_level(217,196,39))
#print(power_level(101,153,71))

def grid_print(grid, max_x = 5, max_y = 5):
    to_x = min(len(grid), max_x)
    to_y = min(len(grid), max_y)

    grid_str = ""
    for y in range(to_y):
        for x in range(to_x):
            val = grid[x][y]
            if val >= 0:
                grid_str += " "
            grid_str += " " + str(grid[x][y])
        grid_str += "\n"
    print(grid_str)


def find_best(serial_number):
    #grid[x][y]
    grid = [[power_level(x, y, serial_number) for y in range(1,301)] for x in range(1,301)]
    grid_print(grid)

    cur_max = -5*99
    cur_cell = None

    cum_grid = grid
    for x, col in enumerate(grid):
        col_sum = 0
        for y, val in enumerate(col):
            col_sum += val
            cum_grid[x][y] = col_sum

    for y in range(len(grid)):
        row = [cum_grid[x][y] for x in range(300)]
        row_sum = 0
        for x, val in enumerate(row):
            row_sum += val
            cum_grid[x][y] = row_sum

    grid_print(cum_grid)

    for sq_size in range(1,300):
        for x in range(300-sq_size):
            for y in range(300-sq_size):
                left, right = x-1, x+sq_size-1
                top, bottom = y-1, y+sq_size-1

                cell_sum = cum_grid[right][bottom]

                #print((x, y, cell_sum))
                if x > 0 and y > 0:
                    cell_sum += cum_grid[left][top]
                #print((x, y, cell_sum))
                if x > 0:
                    cell_sum -= cum_grid[left][bottom]
                #print((x, y, cell_sum))
                if y > 0:
                    cell_sum -= cum_grid[right][top]
                #print((x, y, cell_sum))


                if cell_sum > cur_max:
                    #print("New max %s (was %s) at %s" % (cell_sum, cur_max, (x+1, y+1, sq_size)))
                    cur_max = cell_sum
                    cur_cell = (x+1, y+1, sq_size)
                #print()

    print(cur_max)
    return cur_cell

#print(find_best(18)) # 90,269,16
#print(find_best(42)) # 232,251,12
print(find_best(serial_number))


