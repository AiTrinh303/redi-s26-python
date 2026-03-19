

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common_elements = []

for elem in a:
    if elem in b:
        common_elements.append(elem)
        
print(common_elements)
