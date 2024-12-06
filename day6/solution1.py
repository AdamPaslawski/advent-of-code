def main():
    matrix = []

    with open("input6.txt", "r") as f:
        for line in f.readlines():
            matrix.append(line.rstrip("\n"))

    num_rows = len(matrix)
    num_columns = len(matrix[0])

    print(f"Dimensions of grid: {num_rows,num_columns}")

    # Find where the guard be at
    DIRECTIONS = {
        "<": (0, -1),
        ">": (0,1),
        "^": (-1,0),
        "v": (1,0),
    }

    # Wth does 90 degrees mean
    turn = { 
        (0, -1):(-1,0),
        (-1,0):(0,1),
        (0,1):(1,0),
        (1,0):(0, -1)
    }
    for row in range(num_rows):
        for col in range(num_columns):
            if matrix[row][col] in DIRECTIONS:
                start_location = row,col
                start_direction = DIRECTIONS[matrix[row][col]]
                break

    visited = set()
    visited.add(start_location)

    direction_map = {}
    direction_map[(row,col)] = [start_direction]

    print(f"guard is at : {start_location} in direction {start_direction}")

    locaysh = start_location
    direction = start_direction

    def navigate(locaysh, matrix, direction):
        # At most we can try all directions
        next_locaysh = (locaysh[0] + direction[0],locaysh[1] + direction[1])

        if next_locaysh[0] < 0 or next_locaysh[0] > num_rows-1 or next_locaysh[1] <0 or next_locaysh[1] > num_columns - 1:
            return -1,-1

        next_locaysh_content = matrix[next_locaysh[0]][next_locaysh[1]]

        if next_locaysh_content == "#":
            print(f"Bro, we colided we gotta rip a 90 degree turn fam")
            # gotta turn
            direction = turn[direction] 

            if next_locaysh[0] < 0 or next_locaysh[0] > num_rows-1 or next_locaysh[1] <0 or next_locaysh[1] > num_columns - 1:
                return -1,-1

            next_locaysh = (locaysh[0] + direction[0],locaysh[1] + direction[1])
        return next_locaysh, direction



    while True:
        locaysh, direction = navigate(locaysh, matrix, direction)
    
        # We walked off the earth! we are DONE
        if (locaysh, direction) == (-1,-1):
            break

        directions_for_locaysh = direction_map.get(locaysh, [])

        if locaysh in visited and direction in directions_for_locaysh:
            # We have been here before and were headed in the same direction.
            # Let's go ahead and conclude this cruise
            raise Exception("Cycle detected")
    
        #New locaysh cruised, right on
        visited.add(locaysh)
        if locaysh in direction_map:
            direction_map[locaysh].append(direction)
        else:
            direction_map[locaysh] = [direction]



    print(len([locaysh for locaysh in visited]))
    return [locaysh for locaysh in visited], matrix, start_location, start_direction


visited, matrix, start_location, start_direction, DIRECTIONS, TURN = main()