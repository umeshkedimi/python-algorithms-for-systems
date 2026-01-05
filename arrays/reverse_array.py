def reverse_array(nums: list[int]) -> None:
    """Reverse the input array in plcae using two pointers"""
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]

        left += 1
        right -= 1


# --- Test Cases ---
# Test 1: Odd lenght
nums_odd = [1,2,3,4,5]
reverse_array(nums_odd)
print(f"Odd length: {nums_odd}")

# Test 2: Even length
nums_even = [10, 20, 30, 40]
reverse_array(nums_even)
print(f"Even length:{nums_even}")


