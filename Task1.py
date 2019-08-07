dict = ['x座標', 'y座標', '幅', '高さ']
info = ['x', 'y', 'width', 'height']
enemys = {}
i = 0
# 自分の座標
me = {}
test = {}

print('自分の位置を決める')
for key in info:
    print(dict[i])
    value = int(input(dict))
    me[key] = value
    i += 1

print(me)
# 敵の座標 二次元配列

i = 0
for j in range(3):
    print('敵', j + 1, '座標を設定')
    for key in info:
        print(dict[i])
        value = int(input())
        test[key] = value
        i += 1

    enemys['enemy' + str(j + 1)] = test
    i = 0
print(enemys)



# 敵に当たっているか
if(me['x'] - enemys['enemy1']['x'] < me['width']/2 + enemy1['width']/2 # 横の判定
    and
    me['y'] - enemy1['y'] < me['height']/2 + enemy1['height']/2): # 縦の判定
    print('敵１に当たった')
    enemy = enemy - 1

if(me['x'] - enemy2['x'] < me['width']/2 + enemy2['width']/2 # 横の判定
    and
    me['y'] - enemy2['y'] < me['height']/2 + enemy2['height']/2): # 縦の判定
    print('敵２に当たった')
    enemy = enemy - 1

if(me['x'] - enemy3['x'] < me['width']/2 + enemy3['width']/2 # 横の判定
    and
    me['y'] - enemy3['y'] < me['height']/2 + enemy3['height']/2): # 縦の判定
    print('敵３に当たった')
    enemy = enemy - 1

if enemy == 0:
    print('congratulation')
