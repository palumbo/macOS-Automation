import sys
import os

# for f in sys.argv[1:]:
# 	print f

# print sys.argv[-2]  << output is  /Users/palumbo/Desktop/Untitled 3 as STR

path = sys.argv[-2]
folder_str = path.split('/')
ig_user = folder_str[-1]
# print folder 

# url = "https://www.instagram.com/" + folder

#print url 
#print type(url) 
# print url

# export PATH=/usr/local/bin:$PATH

print ig_user
os.system("export PATH=/usr/local/bin:$PATH")
os.system("open https://instagram.com/" + ig_user)
#subprocess.call('open https://instagram.com/' + ig_user)


