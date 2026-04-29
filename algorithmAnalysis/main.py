# main.py
# Part 2: Randomized testing

# Import random so we can generate random numbers and random targets
import random

# Import the three search functions from the provided file
from search_algorithms import recursive_binary_search
from search_algorithms import iterative_binary_search
from search_algorithms import sequential_search


# Helper function to cleanly print results
def print_result(search_name, target, index):
    # If index is not -1, the target was found
    if index != -1:
        print(f"{search_name}: {target} found at index {index}")
    else:
        # If index is -1, the target was not found
        print(f"{search_name}: {target} not found")


def main():
    # Create a random list of 20 numbers from 1 to 100
    arr = [random.randint(1, 100) for _ in range(20)]

    # Sort the list so binary search will work correctly
    arr.sort()

    # 50% chance to choose a target from the list
    # 50% chance to choose 999, which should not be in the list
    if random.random() < 0.5:
        target = random.choice(arr)
    else:
        target = 999

    # Print the list and target so we can see what is being searched
    print("Random sorted list:")
    print(arr)
    print()
    print(f"Target: {target}")
    print()

    # Run recursive binary search
    index = recursive_binary_search(arr, target, 0, len(arr) - 1)
    print_result("Recursive Binary Search", target, index)

    # Run iterative binary search
    index = iterative_binary_search(arr, target)
    print_result("Iterative Binary Search", target, index)

    # Run sequential search
    index = sequential_search(arr, target)
    print_result("Sequential Search", target, index)


# Standard Python entry point
if __name__ == "__main__":
    main()