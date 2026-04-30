# main.py
# Part 3: Measure and compare runtime growth

# Import random so we can generate random lists and random targets
import random

# Import time so we can measure how long each search takes
import time

# Import the three search functions from the provided file
from search_algorithms import recursive_binary_search
from search_algorithms import iterative_binary_search
from search_algorithms import sequential_search


def main():
    # These are the different list sizes required by the assignment
    dataSize = [5000, 50000, 100000, 150000, 1000000]

    # Print a basic title for the results
    print("Search Algorithm Runtime Results")
    print("--------------------------------")

    # Outer loop: goes through each data size
    for N in dataSize:

        # These variables will keep track of the total time across 10 runs
        SumRBS = 0
        SumIBS = 0
        SumSeqS = 0

        # Inner loop: runs the experiment 10 times for the current data size
        for _ in range(10):

            # Create a sorted list of N random numbers
            # Binary search requires the list to be sorted
            arr = sorted([random.randint(1, 1000000) for _ in range(N)])

            # Choose a random target to search for
            target = random.randint(1, 1000000)

            # Time recursive binary search
            start = time.perf_counter()
            recursive_binary_search(arr, target, 0, len(arr) - 1)
            SumRBS += (time.perf_counter() - start) * 1_000_000

            # Time iterative binary search
            start = time.perf_counter()
            iterative_binary_search(arr, target)
            SumIBS += (time.perf_counter() - start) * 1_000_000

            # Time sequential search
            start = time.perf_counter()
            sequential_search(arr, target)
            SumSeqS += (time.perf_counter() - start) * 1_000_000

        # After 10 runs, calculate and print the average time for each algorithm
        print(f"N = {N}")
        print(f"Average Recursive Binary Search time: {SumRBS / 10:.2f} µs")
        print(f"Average Iterative Binary Search time: {SumIBS / 10:.2f} µs")
        print(f"Average Sequential Search time: {SumSeqS / 10:.2f} µs")
        print()


# Standard Python entry point
if __name__ == "__main__":
    main()