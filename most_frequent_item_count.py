# Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0

# Example
# input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
# ouptut: 5
# The most frequent number in the array is -1 and it occurs 5 times.

def most_frequent_item_count(collection):
    if not collection:
        return 0
    
    count_dict = {}
    for item in collection:
        count_dict[item] = count_dict.get(item, 0) + 1
    
    return max(count_dict.values())

def most_frequent_item_count1(collection):
    if not collection:
        return 0
    
    count_dict = {}
    for item in collection:
        count_dict[item] = count_dict.get(item, 0) + 1
    
    max_count = 0
    for count in count_dict.values():
        if count > max_count:
            max_count = count
            
    return max_count

def most_frequent_item_count2(collection):
    if not collection:
        return 0
    
    count_dict = {}
    for item in collection:
        count_dict[item] = count_dict.get(item, 0) + 1
    
    return max(count_dict.values()) if count_dict else 0