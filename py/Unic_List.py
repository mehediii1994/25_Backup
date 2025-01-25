
def unique_list(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
print(unique_list([10, 15, 100, 5, 20, 25, 200, 10,30, 35, 300, 15, 40, 45, 400, 20, 50, 50, 55, 500, 25]))
    
