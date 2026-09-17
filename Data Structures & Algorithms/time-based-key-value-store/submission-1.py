# want to be able to store multiple values for the same key with different times
# want to be able to get a key's value at a certain time

class TimeMap:


    def __init__(self):
        # create a dictionary to store time and value for each key
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # check if the key exists
        if key in self.store:
            values = self.store[key]
            print(values)
            left = 0
            right = len(values) - 1
            # binary search for the most recent time
            while left <= right:
                mid = (left + right) // 2
                if int(values[mid][1]) == timestamp:
                    return values[mid][0]
                elif int(values[mid][1]) < timestamp:
                    res = values[mid][0]
                    left = mid + 1
                else:
                    right = mid - 1
            return res
        else:
            return res
        
