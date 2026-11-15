# N = int(input())

# for i in range(N):
#     S = input()

#     res = ""
#     postive = 0 
#     negative = 0
#     string = ""
#     negativestring = ""



#     while i < len(S):
#         if S[i].islower():
#             i += 1 
#             continue 
#         elif S[i].isupper():
#             res += S[i]
#             i += 1
#         elif S[i] == "-":
#             j = i
#             while j+1 < len(S) and S[j+1].isdigit():
#                 negativestring += S[j + 1]
#                 j += 1
#             negative -= int(negativestring)
#             i += 1
#         else:
#             string += S[i]
#             if i+1 < len(S) and (S[i+1].lower() or S[i+1].isupper()) or i+1:
#                 postive += int(string)
#                 string = ""
#                 i+= 1
#             else:
#                 postive += int(string)
#                 string = ""
#                 i+=1 


N = int(input())
for _ in range(N):
    S = input()
    
    letters = ""
    total_sum = 0
    current_num = ""
    
    for char in S:
        if char.isupper():
            letters += char
            if current_num:
                total_sum += int(current_num)
                current_num = ""
                
        elif char.islower():
            if current_num:
                total_sum += int(current_num)
                current_num = ""
                
        elif char == '-':
            if current_num:
                total_sum += int(current_num)
            current_num = "-"
            
        elif char.isdigit():
            current_num += char

    if current_num:
        total_sum += int(current_num)
        
    print(letters + str(total_sum))