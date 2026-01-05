def duplikaty(retazec:str) -> str:
    vystup = retazec[0]
    for i in range(1, len(retazec)):
        if retazec[i] != vystup[-1]:
            vystup += retazec[i]
    return (vystup)
print(duplikaty("jaaaaaaannnnnnnnoooooooo"))