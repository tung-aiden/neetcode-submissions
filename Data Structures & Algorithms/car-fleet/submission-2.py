class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # initializing car dict to store position and speed
        car_dict = {}

        # adding position and speed for each car to dict
        for i in range(len(position)):
            car_dict[position[i]] = speed[i]

        # sort the dict by position in decreasing order
        sorted_by_pos = sorted(car_dict.items(), key=lambda item:item[0], reverse = True)
        print(sorted_by_pos)

        stack = []
        for i in range(len(sorted_by_pos)):
            time_to_target = (target - sorted_by_pos[i][0]) / sorted_by_pos[i][1]
            print(time_to_target)
            if stack and stack[-1] >= time_to_target:
                print("here")
                continue
            else:
                stack.append(time_to_target)
        num_fleets = len(stack)
        return num_fleets


        