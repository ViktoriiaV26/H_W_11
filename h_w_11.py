#2
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
s4 = set.intersection(set1, set2, set3)
print("2. s4:", s4)

#3
print("="*100)
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
s4 = set.difference(set1, set2, set3)
print("3. s4:", s4)

#4
print("="*100)
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
set4 = set.union(set1, set2, set3)
print("4. set4:", set4)
#5
print("="*100)   #add element
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
my_set = set(sampleList)
my_set.update(sampleSet)
print("5.my_set:", my_set)

#6
print("="*100)
# return a set of identical items from the given two
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
new_set = set1.intersection(set2)
print("6.new_set:", new_set)

#7
print("="*100)
# return a new set with all elements from both one, removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set_3 = set1.union(set2)
print("7. set_3:", set_3)

#8
print("="*100)
# Учитывая два набора Python, обновите первый набор элементами, которые существуют только в первом наборе,
# но не во втором наборе.
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set3 = set1.difference(set2)
print("8.", set3)



#9
print("="*100)
# Remove elements 10, 20, 30
set1 = {10, 20, 30, 40, 50}
set1.discard(10)
set1.discard(20)
set1.discard(30)
print("9. set1:", set1)


#11
print("="*100)
# Check if two sets have common elements
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set_ = set1.intersection(set2)
print("11. set_:", set_)



#12
print("="*100)
# update set 1 by adding elements from set 2
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set1.update(set2)
print("12. set1:", set1)


#13
print("="*100)
# Delete elements from set1, which aren't common to set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
n_set = set1.difference(set2)
print("13. n_set:", n_set)
n_set.clear()
print(n_set)

#14
my_list = [[1, None, 2, 3, 4+5j, 6],
           [1.0, 2.5, None, 3,9, 4.0+5.2j, 6.1],
           ['1', '2', '3.6', None, '4+5.7j', '6']]
list_int = []
list_float = []
list_str = []
for item in my_list:
    types = [type(elem).__name__ for elem in item if type(elem).__name__]
    single_types = []
    single_types = [i_type for i_type in types if i_type not in single_types]
    types_count = [types.count(element_type) for element_type in single_types]

    max_type_count = max(types_count)
    index_max = types_count.index(max(types_count))
    main_type = single_types[index_max]

    separated_list = [element for element in item if type(element).__name__ == main_type]
    list_int.extend(separated_list)
    list_float.extend(separated_list)
    list_str.extend(separated_list)
print("list_int:", list_int)
print("list_float:", list_float)
print("list_str:", list_str)

a_list_int = [i for i in list_int if type(i) == int]
print("a_list_int:", a_list_int)
a_list_float = [i for i in list_int if type(i) == float]
print("a_list_float:", a_list_float)
a_list_str = [i for i in list_int if type(i) == str]
print("a_list_str:", a_list_str)
