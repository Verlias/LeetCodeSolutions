# Thought Process
I have to find the the integer value that occurs only once in the array, and I have to find it quickly among all the numbers in the array

Considering that I have to find it really fast I could use a hashtable to my advantage.

The hashtable will store each unique value and if it occurs more than once it would increment the key's value.

Then I would look at all the keys and check which one has a value one then return it.