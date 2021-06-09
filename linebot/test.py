def join():
        startType=chooseleadtype()##line的請選擇發車類別(1or2)
'''def hi():
    return aaa
        continue
    else:'''

def joinn():
    pub_end=chooselocation()##line的請選擇目的地編號(12345)
    
    
def ww():
    if pub_end != '其他':
        print('請輸入你的乘車地址')
    elif pub_end != '各個地址' and pub_end != '各個地址' and pub_end != '各個地址'and pub_end != '各個地址':
        continue
    else:
        break
    return print('ok')

def getinfo():
    f = open('info.txt','w')
    all = f.readlines()
    for i in all:
        detail=i.split(',')
        if "1" in detail[0]:
            return detail[1],detail[2],detail[3],detail[4]
    return '未知','未知','未知','未知'
