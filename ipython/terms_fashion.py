#写入匹配集里的每个物品的搜索关键词
import csv
fh = open ( '/home/ch/ipython/terms_matchsets.txt', 'w' ) 
f = open('/home/ch/ipython/outofid_matchsets.txt')
rate1 = open('/home/ch/taobao/dim_items.txt')
#dic里面保存了所有物品里面的数据id,cat_id,items
dic = dict()
for line in rate1:
    line = line.strip().split(' ')
    dic[line[0]] = [line[1],line[2]]

data = csv.reader(f,delimiter=';')
i = 0
for l in data:
    fh.write(str(i)+' ')
    i = i+1
    for li in l:
        stt = ''
        if(dic.has_key(li)):
            stt =stt + dic[li][1]+','
    fh.write(stt.strip(',')+'\n')
print 'write OK\n'
