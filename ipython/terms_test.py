#写入测试文件里面的每个物品的terms
import csv
fh = open ( '/home/ch/ipython/terms_test.txt', 'w' ) 
f = open('/home/ch/taobao/test_items.txt')
rate1 = open('/home/ch/taobao/dim_items.txt')
#dic里面保存了所有物品里面的数据id,cat_id,items
dic = dict()
for line in rate1:
    line = line.strip().split(' ')
    dic[line[0]] = [line[1],line[2]]

for l in f:
    stt = ''
    l=l.strip()
    if(dic.has_key(l)):
        stt =stt + dic[l][0] + ',' + dic[l][1]
    fh.write(stt + '\n')
print 'write OK\n'
