# TODO: Import the Counter class from counter.py
# Use format: from counter import Counter
from counter import Counter

# Comprehensive test case handler
test_case = input()

if test_case == "init_test":
    # TODO: Test the initialization with default value
    # Create a counter with no arguments and print it
    # Expected output: "Count: 0"
    Counter()
    print(Counter())

elif test_case == "init_with_value":
    # TODO: Test initialization with a specific value
    # Create a counter with initial value 10 and print it
    # Expected output: "Count: 10"
    Counter(10)
    print(Counter(10))

elif test_case == "string_representation":
    # TODO: Test the string representation
    # Create a counter with value 5 and print it directly
    # Expected output: "Count: 5"
    print(Counter(5))

elif test_case == "addition":
    # TODO: Test the addition operation
    # Create a counter with value 3, add 7 to it, and print the result
    # Expected output: "Count: 10"
    Counter(3) + 7
    print(Counter(3) + 7)

elif test_case == "chained_addition":
    # TODO: Test chained addition operations
    # Create a counter with value 1, add 2, then add 3 to the result, and print
    # Expected output: "Count: 6"
    result =Counter(1) + 2 
    print(result + 3)

elif test_case == "negative_values":
    # TODO: Test with negative values
    # Create a counter with value -5 and print it
    # Then add -3 to it and print the result
    # Expected outputs: "Count: -5" and "Count: -8"
    Counter(-5)
    print(Counter(-5))
    print(Counter(-5) + -3)

elif test_case == "zero_value":
    # TODO: Test with zero values
    # Create a counter with value 0, add 0, and print
    # Expected output: "Count: 0"
    print(Counter(0) + 0)

elif test_case == "large_values":
    # TODO: Test with large values
    # Create a counter with value 1000000 and add 9000000
    # Expected output: "Count: 10000000"
    print(Counter(1000000) + 9000000)

elif test_case == "multiple_counters":
    # TODO: Test interaction between multiple counters
    # Create counter1 with value 5 and counter2 with value 10
    # Print both counters
    # Expected outputs: "Count: 5" and "Count: 10"
    counter1 = Counter(5)
    counter2 = Counter(10)
    print(counter1)
    print(counter2)

elif test_case == "type_validation":
    # TODO: Test adding different types
    # Try adding a float (2.5) to a counter with value 5
    # Expected output: "Count: 7.5"
    print(Counter(5) + 2.5)