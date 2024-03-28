#the authors' names are Abby Newton and Allison Macrowski
def replace_substring(string,removed,replaced):
    output=[]#creates empty list
    index=0
    while index<len(string):#moves across the string
        if string[index:index+len(removed)]==removed:#checks for string to remove
            index+=len(removed)#moves over string length of removed string
            output.append(replaced)#appends new string in place of removed
        else:
            output.append(string[index])#appends onto list
            index+=1#moves index
    print("".join(output))#prints new, full list


replace_substring("SPAM!HelloSPAM! worldSPAM!!","SPAM!","?")
