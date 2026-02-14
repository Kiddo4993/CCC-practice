Pressed = input()
Shown = input()

i = 0 
j = 0 

pressedkey = ""
sillykey = ""
quietkey = ""


while i <len(Pressed) and j < len(Shown):
    if Pressed[i] == Shown[j]:
        i += 1
        j += 1
    else: 
        if len(Pressed) == len(Shown):
            pressedkey = Pressed[i]
            sillykey = Shown[j]
            quietkey = "-"
            break
        elif quietkey != "" and Pressed[i] == quietkey:
          i += 1
        elif i + 1 < len(Pressed) and Pressed[i+1] == Shown[j]:
            quietkey = Pressed[i]
            i +=1
        else:
            pressedkey = Pressed[i]
            sillykey = Shown[j]
            i += 1
            j += 1
                
if quietkey == "" and i < len(Pressed):
    quietkey = Pressed[i]





print(pressedkey + " " + sillykey)
print(quietkey)
