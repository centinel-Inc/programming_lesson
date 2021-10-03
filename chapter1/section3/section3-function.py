fruit_box1 = ['apple', 'orange', 'lemon', 'orange', 'orange']
# appleの数を数えたい
apple_count = 0
for fruit in fruit_box1:
    if(fruit == 'apple'):
        apple_count += 1
print(apple_count) # 1が表示される



# 3つあるfruit_boxからりんごが一番多いものが知りたい
fruit_box1 = ['apple', 'orange', 'lemon', 'orange', 'orange']
fruit_box2 = ['apple', 'apple', 'apple', 'orange', 'orange']
fruit_box3 = ['orange', 'orange', 'orange', 'lemon', 'lemon']

apple_count = 0
for fruit in fruit_box1:
    if(fruit == 'apple'):
        apple_count += 1
print(apple_count) # 1が表示される

apple_count = 0
for fruit in fruit_box2:
    if(fruit == 'apple'):
        apple_count += 1
print(apple_count) # 3が表示される

apple_count = 0
for fruit in fruit_box3:
    if(fruit == 'apple'):
        apple_count += 1
print(apple_count) # 0が表示される



# appleがいくつfruit_boxに入っているか数える関数
# def 関数名(引数)
def count_apple(fruit_box):
    apple_count = 0
    for fruit in fruit_box:
        if fruit == 'apple':
            apple_count += 1

    return apple_count

apple_count = count_apple(fruit_box1)
print(apple_count) # 1

print(count_apple(fruit_box2)) # 3
print(count_apple(fruit_box3)) # 0
# fruit_box2が一番多い