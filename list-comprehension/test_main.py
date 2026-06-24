from incomplete_main import filter_shop_inventory

run_cases = [
    (
        [("Dirty Rag", 5), ("Chainmail", 25), ("Leather Vest", 20)], 24, ["Dirty Rag", "Leather Vest"]
    ),
    (
         [("Chainmail", 25), ("Leather Vest", 20)], 20, ["Leather Vest"]
    ),
    (
        [("Chainmail", 25), ("Beautiful Boots", 15), ("Dirty Rag", 5), ("Leather Vest", 20)], 15, ["Beautiful Boots", "Dirty Rag"]
    ),
]

submit_cases = run_cases + [
    (
        [], 50, []
    ),
    (
        [("Leather Vest", 20), ("Chainmail", 25)], 30, ["Leather Vest", "Chainmail"]
    ),
]

def test(input1, input2, expected_output):
    print("---------------------------------")
    print("Inputs:")
    print(f" - shop inventory: {input1}")
    print(f" - player balance: {input2}")
    result = filter_shop_inventory(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False

def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

x = [("Rag", 10), ("Vest", 20)]
y = filter_shop_inventory(x, 15)
print(y)