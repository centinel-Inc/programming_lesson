# index          0        1         2       3
fruit_box = ['apple', 'orange', 'lemon', 'apple']

# fruit_boxのindex0番目から順番にfruitに中身を取り出す
# 1回目 fruit = 'apple'
# 2回目 fruit = 'orange'
# 3回目 fruit = 'lemon'
# 4回目 fruit = 'apple'
for fruit in fruit_box:
    print(fruit) # apple orange lemon appleが順番に表示される


for fruit in fruit_box:
    print(fruit) # apple 
    # breakを実行するとfor文の処理を中断して終了するので2回目の処理が実行されない
    break
# 2回目の処理で止まるので、出力結果は「apple」


fruit_box = ['apple', 'orange', 'lemon', 'apple']
# fruit_boxからorangeだけ食べたい
for fruit in fruit_box:
    if fruit != 'orange':
        print('pass')
        # continueより下にある処理を実行せずに次のループに移行する
        # breakとの違いはその時点でfor文の処理を止めるか、次のループにいくか
        continue
    print('eat')
# 出力結果は「pass eat pass passが順番に表示される

# continueがない場合
fruit_box = ['apple', 'orange', 'lemon', 'apple']
for fruit in fruit_box:
    if fruit != 'orange':
        print('pass')
    print('eat')
# continueで処理が止まらないので
# 出力結果は
# 1回目 pass eat 
# 2回目 eat 
# 3回目 pass eat 
# 4回目 pass eat