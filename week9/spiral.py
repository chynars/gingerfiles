import sys

# I went with a pattern approach for this problem
# I noticed a pattern on both sides of the diagonals, and decided to loop through the two sides and sum one side then the other,
# then sum those two sides together
# I also did not really do the problem solving steps, that's because I wasn't really sure to start
# and whenever i am doing coding assignments frankly, i google the heck out of everything i'm doing
# and try to take stuff from what I search and incorporate into what I'm doing. 
# These comments are a mess, sorry.

# Going from the left side of the diagnonal, the pattern is 1+3+7+13+21+31
# So, I googled a mathmatical equation for that sequence, so that I could loop through all of those numbers
#  in the sequence and sum them together, and what I figured out from that was this:
#   1 + (2) = 3
#   3 + (4) = 7
#   7 + (6) = 13
#   
# and so on... so the difference?? (idk the word for it) is 2. 
# so Step1: go through diagonal left and start from center of 1, then find the sum w a difference of 2
center = 1
sum_left = 0
difference = 2

for x in range(1,502):
    sum_left = sum_left + center
    center = center + difference
    difference = difference + 2
    

# Going from the right side of the diagonal, the pattern is 1, 5, 9, 17, 25, etc.
# This one was a little confusing, because I couldn't really find an equation for these numbers,
# so I did a solving for x type of thing, and the difference was 4, but it was doubled? this was hard
# to figure out.. and im not really sure what I was doing here to be honest, i also had a lot of help
# from the internet so yea...
# 1 + x = 5 , x = 4
# 5 + x = 9, x = 4
# 9 + x = 17, x = 8
# 17 + x = 25, x = 8
# so the difference for this one was 4, but it repeated so i was not sure what that meant.
# I tried just seeing if using even numbers only as x would work, still not sure why though
# step 2: go through diagonal right and find the sum
center_again = 1
sum_right = 0 
difference = 4

for x in range(1,502):
    sum_right = sum_right + center_again
    center_again = center_again + difference
    if (x % 2 == 0):
        difference = difference + 4
    
#step 3: print the sum
print(sum_left + sum_right)