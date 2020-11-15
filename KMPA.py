# Knuth–Morris–Pratt Algorithm
# Ethan Trott
# COS 350 - Assignment 6

# creates our failure function by finding longest prefix of P that is a suffix of P for each substring
def createFailureTable(P):
    table = [0] * len(P)

    #for each substring, find the longest prefix that is also a suffix
    for i in range(len(P)):
        sub = P[:i+1]

        length = len(sub)-1
        # for each possible prefix length (biggest to smallest):
        while (length > 0):
            # if the prefix is a suffix, store it as the biggest and break the loop
            if sub[:length] == sub[len(sub)-length:]:
                table[i] = length
                break
            length -= 1

    return table

#returns the position of the first occurence of P inside of T, or -1 if there isn't one
def match(T,P):
    failureTable = createFailureTable(P)
    curPos = 0

    # while there is more room to search, and we haven't found the substring, continue searching
    while (curPos + len(P) <= len(T) and T[curPos:curPos+len(P)] != P):

        # find the index of the first mismatch, and skip forward by the correct amount according to the failure function
        for i in range(len(P)-1):
            if (P[i] != T[curPos + i]):
                curPos += failureTable[i] + 1
                break


    #if we searched the entire thing with no match, return -1
    if (curPos + len(P) > len(T)):
        return -1
    #else return the match position
    else:
        return curPos