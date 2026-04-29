# First non-repeating character

s = input("Enter the String: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in s:
    if freq[ch] == 1:
        print("First non-repeating: ",ch)
        break