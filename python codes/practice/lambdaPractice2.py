# Using filter() + lambda, extract odd numbers from list

nums = [3,4,2,4,6,5,1,1,44,56,23,5443,65,34]
odds = list(filter(lambda x : x%2!=0 and x!=1 , nums))
print(odds)
