# Sequence Description Function
# Given an integer input denoting the N-th sequence where N > 0 and the base case of 2 at N[0], the function returns
# the string sequence that counts the occurences of each number of the N-1th sequence
# ie.
# N[0] = 2
# N[1] = 12
# N[2] = 1112
# ...
# Where N[2] = 1112 can be read as 1 count of "1" and 1 count of "2" in the previous sequence on N[1]

def seq_des(num):
    # Base Case - return 2 if input is 0 or below
    if num <= 0:
        return "2"
    # Perform recursive call for previous sequence
    prev = seq_des(num-1)
    num_rec = []
    # Expand the counter list (num_rec) if the integer value of the previous sequence's entry
    # is higher than the length of the list. Then increment the value of the corresponding list index - 1
    # eg. "1" entry increments value at num_rec[0], "2" entry at num_rec[1]
    for i in prev:
        if len(num_rec) < int(i):
            for k in range(int(i) - len(num_rec)):
                num_rec.append(0)
        num_rec[int(i)-1] += 1
    str_list = ""
    # Set the sequence string based on values in num_rec, in ascending order
    # 0 values in num_rec are not printed
    for j in range(len(num_rec)):
        if num_rec[j] > 0:
            str_list = str_list + str(num_rec[j]) + str(j+1)
    # Return finalized sequence string to caller
    return str_list
    
print(seq_des(15))