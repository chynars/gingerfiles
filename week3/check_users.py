def check_users(current_users, new_users):
 pass
#beginning of my code
 current_users = ['chirs', 'haritha', 'sally', 'darnell', 'superman']
 new_users = ['george', 'ringo', 'SUpERmAN', 'hannibal'] #using 'SUpERmAN' instead of 'superman' to check case insensitivity

 current_users = [name.lower() for name in current_users] #copy of current_users list to include all letter variations of existing users

 for new_user in new_users:
     if new_user.lower() in current_users:
         print("Username {} is taken, please enter a new username.".format(new_user))
     else:
        print("Username {} is available.".format(new_user))
#end of my code

if __name__ == "__main__":
 current_us = ['chris','haritha', 'sally', 'darnell', 'superman']
 new_us = ['george', 'ringo', 'superman', 'hannibal']
 check_users(current_us, new_us)
