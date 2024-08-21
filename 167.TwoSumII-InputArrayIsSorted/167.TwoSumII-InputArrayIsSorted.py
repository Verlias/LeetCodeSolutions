class Solution(object):
    def twoSum(self, numbers, target):
        first_pointer = 0
        second_pointer =  len(numbers) - 1

        while first_pointer <= second_pointer:
            sum = numbers[first_pointer] + numbers[second_pointer]
            if sum == target:
                return [first_pointer + 1, second_pointer + 1]
            elif sum < target:
                first_pointer += 1
            elif sum > target:
                second_pointer -= 1
