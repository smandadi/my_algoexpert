#!/usr/bin/env python3

# Write a function that takes in a "special" array and returns its product sum.

# A "special" array is a non-empty array that contains either integers or other "special" arrays.
# The product sum of a "special" array is the sum of its elements, where "special" arrays inside
# it are summed themselves and then multiplied by their level of depth.

# The depth of a "special" array is how far nested it is. For instance, the depth of | [] is 1; the depth of the inner array in [[]]] is 2 ;
# the depth of the innermost array in [[[]]] is 3.

# Therefore, the product sum of [x, y] is x + y; the product sum of [x, Ly, z]] is x + 2 * (y + z);
# the product sum of [x, Ly, [z]]] is x + 2 * (y + 3z).


# is a list or an integer.
# time: O(n) | Space O(d), d = all elemsnts in the list
def productSum(array):
    depth = 1
    flatten_list = [item for sublist in array for item in ([flatten_list_out(sublist, depth+1)] if isinstance(sublist, list) else [sublist])]
    return sum(flatten_list)    


def flatten_list_out(array, depth):
    
    item_count = 0
    for item in array:
        if isinstance(item, list):
            item_count += depth *(flatten_list_out(item, depth+1))
        else:
            item_count += depth * item
    return item_count


if __name__ == "__main__":
    assert productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]) == 12, "This works!!!"