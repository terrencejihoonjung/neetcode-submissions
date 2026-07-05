class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by position and speed 
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        sorted_cars = sorted(cars, key=lambda item:item[0])

        # calculate num_turns for each car 
        turns = [0] * len(sorted_cars)
        for i, (pos, spd) in enumerate(sorted_cars):
            distance_remaining = target - pos 
            rate = distance_remaining / spd
            turns[i] = rate

        # iterate through car and num_turns
        print(turns)
        stack = []
        for turn in turns:
            if len(stack) == 0 or stack[-1] > turn: 
                stack.append(turn)
        
            while len(stack) > 0 and stack[-1] <= turn: stack.pop()
            stack.append(turn)
        return len(stack)
    
    # what enables a car to catch up to the car in front of it? 
    #   - if the car's position is less than the car in front of it 
    #   - if the car's speed is greater than the car in front of it
    
    # at what speed does the car have to be to catch up to the car in front of it? 
    # [1, 7] and [4, 2] and target = 8
    # car 1 -> 1 -> 5 -> 9(8)
    # car 2 -> 4 -> 6 -> 8

    # car 1 -> 7 -> 1 turns 
    # car 2 -> 4 -> 2 turns 

    # num_turns = (distance remaining) // (speed) + 1

    # sort cars by position + speed 
    # calculate the # of turns for each car 
    # iterate through the turns
        # add turn to stack 
        # at curr turn, if top of stack is <= curr_turn, then pop stack and add curr_stack 

    # answer is the length of stack 

    