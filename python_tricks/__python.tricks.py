
######## STRING MANIPULATION ########
# replace string
s = "abcde"
new_s = s.replace("c","A")

# reverse string
new_s = s[::-1] # reverse 
new_s = s[0:4] # 0 - 3 index
first_element = s[0]
last_element = s[-1] # last character

# palindrome checking 
s = "abcdcba"
print(all(s[i] == s[len(s)-i-1] for i in range(len(s))) )
s == s[::-1]

# sentence to list 
test_string1 = "hello my name is June"
print(test_string1.split(" "))

# replace in string 
string.replace(",", " ")

# for i in s 
s = "abcdefg"
for i in s:
    print("haha", i)

#########################################
######## LIST/ARRAY MANIPULATION ########

# pop in list 
s_array = [ 1, 2, 3, 4, 5, 6,7]
s_array.pop(2) # index 
s_array.pop() # last element pop 
s_array.remove(6)
print(s_array)

# sorting arrays 
sorted(list) # this is only temporary when showing / actual result is same 
list.sort() # changes the actual list / and returns nothing 


#########################################
######## DICTIONARY ########
# dictionary basic usage 
sampledict = { "key1": "value1", "key2": "value2"}
print(sampledict["key1"])
print(len(sampledict))

#########################################




