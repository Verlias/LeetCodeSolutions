# Thought Process
The fastest way to answer this question would be through a hashtable.
With the Hashtable I would count the frequencies of the elements in the array. If the element frequency is less than 2 that means there could be two arrays with distinct elements.
So I could use the hashtable to count the frequencies then iterate through every key value and check if it has a value less than two.
If it does return true. If not return false