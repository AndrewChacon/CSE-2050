#Task # 1. Read lab manual for details.
from cmath import rect


def sort_matrix_by_row(matrix):
    new_lst = []
    # Use selection sort to solve this problem,
    def selection_sort(list):
        for i in range(0, len(list) - 1):
            min_index = i
            for j in range(i+1, len(list)):
                if list[min_index] > list[j]: min_index = j
            list[i], list[min_index] = list[min_index], list[i]
        return list
    for i in range(len(matrix)):
        new_lst.append(selection_sort(matrix[i]))
    # return new_lst.
    return new_lst

#Task # 2. Read lab manual for details.
# We have the following rectangles records in a list of dictionaries.
rectangles = [{ "ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"  },
             { "ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue" },
             { "ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"},
             { "ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
             ]

'''
    switch statment
    - length
    - breadth
    - color
'''

def sort_rectangles(title):
    print(title)
    # Using insertion sort to solve this problem.
    for i in range(0, len(rectangles)):
        for j in range(i):
    # sort by title.
            if rectangles[i][title] < rectangles[j][title]:
                rectangles[i],rectangles[j] = rectangles[j],rectangles[i]
    # return rectangles.
    return rectangles


