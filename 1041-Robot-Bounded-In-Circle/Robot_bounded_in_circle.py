class Solution(object):
    def isRobotBounded(self, instructions):
        # Initial direction is "up" (0,1)
        dirX, dirY = 0, 1  
        # Initial position at origin
        x, y = 0, 0  

        # Iterate through each instruction
        for d in instructions:
            if d == "G":  
                # Move forward in the current direction
                x, y = x + dirX, y + dirY
            elif d == "L":  
                # Turn left: update direction (rotate 90° counterclockwise)
                dirX, dirY = -1 * dirY, dirX
            else:  
                # Turn right: update direction (rotate 90° clockwise)
                dirX, dirY = dirY, -1 * dirX

        # After executing all instructions once:
        # Robot is bounded if it's back at origin OR
        # if it's not facing "up" (meaning it will loop in a circle)
        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: "GGLLGG" - should return True (robot returns to origin)
    test1 = "GGLLGG"
    result1 = solution.isRobotBounded(test1)
    print(f"Test 1: '{test1}' -> {result1}")
    
    # Test case 2: "GG" - should return False (robot moves away indefinitely)
    test2 = "GG"
    result2 = solution.isRobotBounded(test2)
    print(f"Test 2: '{test2}' -> {result2}")
    
    # Test case 3: "GL" - should return True (robot will loop in a circle)
    test3 = "GL"
    result3 = solution.isRobotBounded(test3)
    print(f"Test 3: '{test3}' -> {result3}")
    
    # Test case 4: "GLRGLR" - should return True (robot returns to origin)
    test4 = "GLRGLR"
    result4 = solution.isRobotBounded(test4)
    print(f"Test 4: '{test4}' -> {result4}")
