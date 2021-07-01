import string


with open('DAY 1\password\password@1651-13.txt','r') as f:
    password = f.read()
#'7%SgY1^mj~qz'


list_pass = list(password)
alpha_lower = string.ascii_lowercase

alpha_upper = string.ascii_uppercase

numeric= string.digits

punch = string.punctuation

#Creating Blank list & embeding all charaters generated till now
var_list = []
var_list.extend(list(alpha_lower))
var_list.extend(list(alpha_upper))
var_list.extend(list(numeric))
var_list.extend(list(punch))



def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]




cracked_password = ''
for i in range(0,(len(list_pass))):
    for r in range(0,(len(var_list))):
        if list_pass[i] == var_list[r]:
            cracked_password = var_list[r] + cracked_password

print(reverse(cracked_password))