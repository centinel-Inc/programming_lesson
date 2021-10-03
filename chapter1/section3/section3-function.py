# appleがいくつfruit_boxに入っているか数える関数
def count_apple(fruit_box):
    apple_num = 0
    for fruit in fruit_box:
        if(fruit == 'apple'):
            apple_num += 1

    return apple_num


# 3つあるfruit_boxからりんごが一番多いものが知りたい
fruit_box1 = ['apple', 'orange', 'lemon', 'orange', 'orange']
fruit_box2 = ['apple', 'apple', 'apple', 'orange', 'orange']
fruit_box3 = ['orange', 'orange', 'orange', 'lemon', 'lemon']
print(count_apple(fruit_box1)) # 1
print(count_apple(fruit_box2)) # 3
print(count_apple(fruit_box3)) # 0
# fruit_box2が一番多い


# 関数がない世界
apple_num = 0
for fruit in fruit_box1:
    if(fruit == 'apple'):
        apple_num += 1
print(apple_num)

apple_num = 0
for fruit in fruit_box2:
    if(fruit == 'apple'):
        apple_num += 1
print(apple_num)

apple_num = 0
for fruit in fruit_box3:
    if(fruit == 'apple'):
        apple_num += 1
print(apple_num)
