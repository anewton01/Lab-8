#the authors' names are Abby Newton and Allison Macrowski
def remove_substring(string,removed):
    output=[]#creates an empty list
    index=0
    while index<len(string):#moves across string
        if string[index:index+len(removed)]==removed:#checks for string to remove
            index +=len(removed)#moves over string removed
        else:
            output.append(string[index]) #appends onto list
            index+=1 #moves index
    print("".join(output))#prints new, full list


remove_substring("SPAM!HelloSPAM! worldSPAM!!","SPAM!")
