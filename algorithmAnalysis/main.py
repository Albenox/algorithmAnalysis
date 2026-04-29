# main.py
# Part 1: Implementation and basic testing

# Import the three search functions from the provided file
from search_algorithms import recursive_binary_search
from search_algorithms import iterative_binary_search
from search_algorithms import sequential_search


# Helper function to cleanly print results
# This avoids repeating the same if/else logic over and over
def print_result(search_name, target, index):
    # If index is not -1, the target was found
    if index != -1:
        print(f"{search_name}: {target} found at index {index}")
    else:
        # If index is -1, the target was not found
        print(f"{search_name}: {target} not found")


def main():
    # Create a small test list (given in the assignment)
    arr = [3, 5, 8, 12, 14, 18, 21]

    # Sort the list (important for binary search to work correctly)
    arr.sort()

    # Two test targets:
    # One that exists in the list
    target1 = 12

    # One that does NOT exist in the list
    target2 = 9

    # ---- TEST CASE 1: Target IS in the list ----
    print("Testing with target that is in the list:")

    # Recursive Binary Search requires low and high bounds
    index = recursive_binary_search(arr, target1, 0, len(arr) - 1)
    print_result("Recursive Binary Search", target1, index)

    # Iterative Binary Search only needs the array and target
    index = iterative_binary_search(arr, target1)
    print_result("Iterative Binary Search", target1, index)

    # Sequential Search checks each element one by one
    index = sequential_search(arr, target1)
    print_result("Sequential Search", target1, index)

    print()

    # ---- TEST CASE 2: Target is NOT in the list ----
    print("Testing with target that is not in the list:")

    # Repeat the same tests but with a value not in the list
    index = recursive_binary_search(arr, target2, 0, len(arr) - 1)
    print_result("Recursive Binary Search", target2, index)

    index = iterative_binary_search(arr, target2)
    print_result("Iterative Binary Search", target2, index)

    index = sequential_search(arr, target2)
    print_result("Sequential Search", target2, index)


# Standard Python entry point
# Ensures main() only runs when this file is executed directly
if __name__ == "__main__":
    main()