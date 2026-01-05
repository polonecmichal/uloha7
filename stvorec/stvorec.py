def stvorec(n:int, znak:str) ->  str:
    vystup = ""
    for i in range(0,n):
        if i==0 or i==n-1:
            vystup += znak* n
            vystup += "\n"
        else:
            vystup += znak + " "*(n-2) + znak
            vystup += "\n"
    return vystup
print(stvorec(5,"$"))