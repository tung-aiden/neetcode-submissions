class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # we can calculate the time it takes for each car to get to the target
        # if a car ahead of another car takes a longer time, then they become a fleet

        car_dict = {}
        for i in range(len(position)):
            car_dict[position[i]] = speed[i]
        print(car_dict)
        sorted_cars = sorted(car_dict.items(), key = lambda x:x[0], reverse=True)
        print(sorted_cars)
        stack = []
        for i in range(len(sorted_cars)):
            time_to_target = float((target - sorted_cars[i][0]) / sorted_cars[i][1])
            print(time_to_target)
            if not stack:
                stack.append(time_to_target)
            elif time_to_target <= stack[-1]:
                continue
            else:
                stack.append(time_to_target)
        print(stack)
        return len(stack)


        