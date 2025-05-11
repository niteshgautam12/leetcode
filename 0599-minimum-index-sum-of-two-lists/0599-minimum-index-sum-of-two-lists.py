class Solution(object):
    def findRestaurant(self, list1, list2):
        index_map = {val: i for i, val in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for j, val in enumerate(list2):
            if val in index_map:
                i = index_map[val]
                total_index = i + j
                if total_index < min_sum:
                    min_sum = total_index
                    result = [val]
                elif total_index == min_sum:
                    result.append(val)

        return result
