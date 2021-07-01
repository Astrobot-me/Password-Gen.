import string, random,datetime
from cryptography.fernet import Fernet

save_file = datetime.datetime.now().strftime('%H%M-%d')


#for generating alphabets,numbers & punchuations
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

#print(var_list)

suffled = random.shuffle(var_list)

char = int(input('Enter the Length of your password:- \n'))

password = (''.join(var_list[0:char]))

#encrypting password
key = Fernet.generate_key()

fernet = Fernet(key)
encrypted_password = fernet.encrypt(password.encode())



#saving Encrypted 
with open(f"DAY 1\Encrypted Password\Encrypted_pass@{save_file}.txt",'w') as f:
    f.write(str(encrypted_password))

#saving password to
with open(f"DAY 1\password\password@{save_file}.txt",'w') as r:
    r.write(password)
