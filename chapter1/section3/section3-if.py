# index          0        1         2       3
fruit_box = ['apple', 'orange', 'lemon', 'apple']
fruit = fruit_box[0] # fruit_boxの0番目なのでappleがfruitに入る
print(fruit) # apple
 
if(fruit == 'apple'):
    # fruitにはappleが入っているのでif文の中身が実行されて「eat」が表示される
    print('eat') # eat


# index          0        1         2       3
fruit_box = ['apple', 'orange', 'lemon', 'apple']
fruit = fruit_box[1] # fruit_boxの1番目なのでappleがorangeに入る
print(fruit) # orange

if(fruit == 'apple'):
    # fruitにはorangeが入っているのでappleとは一致しないのでif文の中身は実行されない
    print('eat') # 実行されない
