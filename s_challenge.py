"""
    Stori project:
        A city’s skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed
        from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape
        photo (Input), write a program to output the skyline formed by these buildings collectively (Output)
        Input:
            [Li, Ri, Hi] = where Li and Ri are the x coordinates of the left and right edge of the ith building and Hi
            is the height. Assume that all the buildings are perfect rectangles grounded on an absolutely flat
            surface at height 0.
        Output:
            List of key points (red dots in the output figure) in the format of [ [x1,y1], [x2,y2] ] that uniquely
            defines a skyline. A key point is the left endpoint of a horizontal line segment.
        Keep in mind:
            The output list must be sorted by the X position and there must be no consecutive horizontal
            lines of equal height in the output skyline.

    Inputs:
        Building N = [left_edge, right_edge, height]
        Building 1 = [2, 9, 10]
        Building 2 = [3, 6, 15]
        Building 3 = [5, 12, 12]
        Building 4 = [13, 16, 10]
        Building 5 = [15, 17, 5]
        
    Functions: 
        create_building_object
        read_data
        sort_data_tuples
        get_intersections
        create_all_edges
        join_edges_with_same_x_value
        sort_heights
        get_skyline
        main
    Classes: 
        Building
        
"""


class Building:
    def __init__(self, left_edge, right_edge, height):
        self.left_edge = left_edge
        self.right_edge = right_edge
        self.height = height
# Create the building object, it's used to get track of the edges and height for each building.


def create_building_object(arr):
    """
      Get data array that was given from the user.
    :param arr:
    :return: array of objects of type building.
    """
    buildings = []
    for data in arr:
        buildings.append(Building(data[0], data[1], data[2]))
    return buildings
# Gets the array of data and return an array with all the objects.


def read_data():
    """
        Read data of the buildings.
    :return: array of arrays with the information.
    The array have arrays of len = 3.
    """
    buildings_data = []
    n = 1
    print('\n\nReading buildings: ')
    while True:
        temp = []
        option = ''
        print(f'\nBuilding #{n}')
        while True:
            try:
                left_edge = float(input('Left_edge: '))
                break
            except ValueError:
                print('That was no valid number! Try again.')
        while True:
            try:
                right_edge = float(input('Right_edge: '))
                break
            except ValueError:
                print('That was no valid number! Try again.')
        while True:
            try:
                height = float(input('Height: '))
                break
            except ValueError:
                print('That was no valid number! Try again.')
        temp.append(left_edge)
        temp.append(right_edge)
        temp.append(height)
        buildings_data.append(temp)
        while option.lower() != 'no' or option.lower() != 'yes':
            option = str(input('\nNew building? (yes/no): '))
            print(option.lower())
            if option.lower() != 'no' and option.lower() != 'yes':
                print('Just yes or no!... Try again.')
            else:
                break
        if option.lower() == 'no':
            break
        n += 1
    return buildings_data
# Read all the buildings data, its open to read the number of buildings the user wants.


def sort_data_tuples(arr):
    """
    Sort array with tuples by the first entry of the tuples.
    :param arr:
    :return sorted array:
    """
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i][0] > arr[j][0]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr
# Takes array with tuples and sort them by the first element on the tuple. Bubbling sort.


def get_intersections(arr):
    """
    Getting the sorted array creates the intersection points of the buildings. 
    :param arr: 
    :return returns the intersections dots array: 
    """
    intersection_dots = []
    for i in range(0, len(arr)):
        lower_bound = arr[i].left_edge
        upper_bound = arr[i].right_edge
        for j in range(0, len(arr)):
            if lower_bound < arr[j].left_edge < upper_bound:
                if arr[j].height > arr[i].height:
                    # print(lower_bound, arr[j].left_edge, arr[i].height, upper_bound, end="\n")
                    intersection_dots.append((arr[j].left_edge, arr[i].height))
            if lower_bound < arr[j].right_edge < upper_bound:
                if arr[j].height > arr[i].height:
                    # print(lower_bound, arr[j].right_edge, arr[i].height, upper_bound, end="\n")
                    intersection_dots.append((arr[j].right_edge, arr[i].height))
    return intersection_dots


def create_all_edges(arr):
    """
    Creates all the edges of the buildings.
    :param arr: 
    :return array with all the buildings edges. (4 for each building): 
    """
    building_edges = []
    for building in arr:
        building_edges.append((building.left_edge, 0))
        building_edges.append((building.left_edge, building.height))
        building_edges.append((building.right_edge, 0))
        building_edges.append((building.right_edge, building.height))
    return building_edges


def join_edges_with_same_x_value(arr):
    """
    With the sorted elements joins the ones that have the same x axis value.
    
    :param arr: 
    :return array with arrays inside.: 
    """
    initial = arr[0][0]
    temp = [arr[0]]
    all_points = []
    for i in range(1, len(arr)):
        if arr[i][0] == initial:
            temp.append(arr[i])
        else:
            initial = arr[i][0]
            all_points.append(temp)
            temp = [arr[i]]
    all_points.append(temp)
    return all_points


def sort_heights(arr):
    """
    Sort array with arrays inside where each one haves tuples, we use the second entry of the tuples.
    :param arr: 
    :return: 
    """
    for k in range(0, len(arr)):
        for i in range(0, len(arr[k])):
            for j in range(i, len(arr[k])):
                if arr[k][i][1] > arr[k][j][1]:
                    temp = arr[k][i]
                    arr[k][i] = arr[k][j]
                    arr[k][j] = temp
    return arr


def get_skyline(arr):
    """
    Create the final skyline. 
    :param arr: 
    :return array with tuples.: 
    """
    first_element = 0
    skyline = []
    for x_group in arr:
        if first_element == 0:
            skyline.append(x_group[len(x_group) - 1])
            first_element += 1
        else:
            # index = 0
            for i in range(0, len(x_group)):
                if x_group[i][1] == skyline[len(skyline) - 1][1]:
                    if len(x_group) - 1 > i:
                        skyline.append(x_group[i + 1])
                        break
                    elif len(x_group) - 1 == i:
                        skyline.append(x_group[i - 1])
                        break
    return skyline


def main():
    data = read_data()
    buildings = create_building_object(data)
    intersections = get_intersections(buildings)
    all_edges = create_all_edges(buildings)
    all_points = intersections + all_edges
    sorted_data = sort_data_tuples(all_points)
    joined_points = join_edges_with_same_x_value(sorted_data)
    sorted_heights = sort_heights(joined_points)
    skyline = get_skyline(sorted_heights)
    print('Skyline formed by these buildings:', end="\n")
    print(skyline)
# Main function of the project.


main()
