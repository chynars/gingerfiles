def check_users(current_users, new_users):
 pass
#beginning of my code
 current_users = ['chirs', 'haritha', 'sally', 'darnell', 'superman'] #list of current users (usernames not available)
 new_users = ['george', 'ringo', 'SUpERmAN', 'hannibal'] #list of usernames for users creating an account - using 'SUpERmAN' instead of 'superman' to check case insensitivity

 current_users = [name.lower() for name in current_users] #copy of current_users list to include all letter variations of existing users

 for new_user in new_users: #loop through new_users to check if the username is available
     if new_user.lower() in current_users: 
         print("Username {} is taken, please enter a new username.".format(new_user)) #in the current_user list
     else:
        print("Username {} is available.".format(new_user)) #not in the current_user list
#end of my code

if __name__ == "__main__":
 current_us = ['chris','haritha', 'sally', 'darnell', 'superman']
 new_us = ['george', 'ringo', 'superman', 'hannibal']
 check_users(current_us, new_us)
