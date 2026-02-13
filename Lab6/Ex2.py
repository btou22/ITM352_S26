def check_list_length(lst):
    if len(lst) < 5:
        print("Fewer than 5 elements")
    elif 5 <= len(lst) <= 10:
        print("Between 5 and 10 elements (inclusive)")
    else:
        print("More than 10 elements")

# Tests with different lengths
check_list_length([1, 2, 3])
check_list_length([1, 2, 3, 4, 5])
check_list_length(list(range(10)))
check_list_length(list(range(11)))

def check_list_length(lst):
    if len(lst) < 5:
        print("Fewer than 5 elements")
    elif 5 <= len(lst) <= 10:
        print("Between 5 and 10 elements (inclusive)")
    else:
        print("More than 10 elements")

# Tests with different lengths
check_list_length([1, 2, 3])
check_list_length([1, 2, 3, 4, 5])
check_list_length(list(range(10)))
check_list_length(list(range(11)))

test_cases = [
    [],                      # < 5
    [1, 2, 3, 4],            # < 5
    [1, 2, 3, 4, 5],         # 5..10
    list(range(10)),         # 5..10
    list(range(11)),         # > 10
]

for case in test_cases:
    print("Length:", len(case))
    check_list_length(case)

def describe_length(lst):
    n = len(lst)
    if n < 5:
        return "lt5"
    elif n <= 10:
        return "5to10"
    else:
        return "gt10"

tests = [
    ([], "lt5"),
    ([1, 2, 3, 4], "lt5"),
    ([1, 2, 3, 4, 5], "5to10"),
    (list(range(10)), "5to10"),
    (list(range(11)), "gt10"),
]

for lst, expected in tests:
    actual = describe_length(lst)
    assert actual == expected, f"len={len(lst)} expected {expected} got {actual}"

print("All tests passed!")

