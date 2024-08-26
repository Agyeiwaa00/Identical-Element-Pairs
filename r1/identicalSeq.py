
# Print the frequency of each element
def check_integer(nums):
    # Check if every item in the list is an integer
    for num in nums:
        if not isinstance(num, int):
            print(f"Invalid input detected: '{num}' is not an integer.")
            return False
    return True

def countIdenticalPairs(nums):

    P_count = 0
    fSet = {}

    # Check for  empty array
    if not nums:
        print ("The array is empty. No pairs can be formed.")
        return 0
    
    # check string input
    if not check_integer(nums):
        print("The list contains non-integer values. Please enter a valid list of integers.")
        return 0

    # Count the frequency of each number
    for num in nums:
      if num in fSet:
        fSet[num] += 1
      else:
            fSet[num] = 1 

    # Calculate the number of pairs   
    for count in fSet.values():
        if count > 1:
            P_count+= (count * (count - 1)) // 2
    for element, count in fSet.items():
        print(f"Element {element} appears {count} times")
    return P_count


nums = [1, 2, 2, 3, 1, 1]
result = countIdenticalPairs(nums)
print(f"Number of identical pairs: {result}")

# ====================== CODE DOCUMENTATION ================================ 
# In this code , the P_count is variable which is used to store the total numbers of identical pair found in the num array; It is initial to zero 

    
# A variable named fSet is used to initialise dictionary and it used used to keep track of how many times each number appears in the nums array 

    
# The for loop iterates over each number (num) in the nums array

    
# Line checks if the current number num is already a key in the fSet dictionary.If the number num is already in the dictionary, this line increments its value by 1 and if num is not already a key in the num_count dictionary, it is set to 1 indicating that this is the first time this number has been encountered.

    
# A new loop iterates over each frequency count in the dictionary fSet and checks if the frequency count is greater than 1

    
# If the frequency is greater than 1, line 54 calculates the number of pairs that can be formed from count occurrences of the same number. The formula (count * (count - 1)) // 2 is the combination formula for choosing 2 items from count items. The result is then added to P_count

    
# Finally, the function returns the total count of such pairs P_count.

    
# At line the number of identical pairs will be 0

    
# Line 6 6Convert the input string to a list of integers

    
# Line 57 calculates the number of pairs that can be formed from count occurrences of the same number . The use of this approach is a well-established mathematical approach to count pairs, making it both intuitive and reliable

    
# The second loop iterates over the values in the dictionary fSet. Each count represents how many times a particular number appears in the original list nums.

    
# if a number appears more than one, the new count is added and store in the P_count and the value is return

    
# For values that do not appear more than once in the list, the program effectively ignores them when counting pairs

    
# Line 58 ensures only the relevant condition should be considered i.e if a number apears more than one

    
# if every number appears only once, the fuction will return 0

    
# In the case the input is empty, the functions return 0

    
# I will create a function called countIdenticalPairs that accepts input called nums and write the rest of the code. After that I will test with different scenerio

    
# The code identifies identical pairs correctly by first counting the frequency of each number in the list and then using these frequencies to determine how many pairs of indices (i, j) can be formed where nums[i] == nums[j] and i < j

    
# Input with only one element will return 0

    
# Empty input scenerio will also return zero indicating that there were no identical pairs. Check line 69

    
# No, it will not affect the logic of the entire function. Returning zero for empty array only indicate that there were no identical pairs found

    
# The second loop is found at line 66 and it is use to count the frequency of the values in the dictionary 'fSet'

    
# one it detects non integer input, the it will return 0 and treat it as invalid input. Space are use to seperate the input element

    
# Line 77 guides tthe user to input a list of intergers

    
# num must be in the dictionary and if the code detects num for the first time, it value is stored as 1. Check line 86

    
# Line 83 to 87 uses the time complexity O(1) and space complexity O(n) to operate on the Array. Hence This efficiency makes the code block well-suited for handling large arrays, as both the time and space complexities grow linearly with the size of the input

    
# The alternative approcah is to use the Counter method from collections where you replace line 84 - 88 to fSet = Counter(nums)

    
# Line 76 prompt the user not to enter empty array

    
# On line 85, the for loop iterates over the elements in the array and start counting  if it encounters already existed element by adding its value to one but if the element appears once, one is assign to its value

    
# nums has been described in the check_integer function as an instance of integer, so when a string or symbol enter the input, the code describe such input as invalid

    
# Zero input returns 0

    
# Invalid input such as strings, or symbols will only return zero with messsage "The list contains non-integer values. Please enter a valid list of integers."

    
# The logic  behind the counting frequency is that it loop through each element in the list. For each element, it checks whether it has been encountered before.

    
# if num already a key in the dictionary fSet, increment its count. This help the second loop to calculate the number of identical pairs detected. Else if num is not in the dictionary, add it with an initial count of 1. 

    
# Invalid input such as strings, or symbols will only return 0 with messsage "The list contains non-integer values. Please enter a valid list of integers."
