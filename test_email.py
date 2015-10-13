import re
mystring = 'From: abd@163.com (aha)'
result = re.search('(\w.-+)@(\w.-+)',mystring)
if result:
    print (result.group(0))
    print (result.group(1))
    print (result.group(2))

    
