def format_seconds(seconds):
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    return f'{days} days {hours} hours {minutes} minutes {seconds} seconds'

begin = int(input("введите начало диапазона --> "))
endF = int(input("введите конец диапазона --> "))

for i in range(begin, endF + 1):
    if i % 2 == 0:
        print(i, end=", ")


a = format_seconds(123456)
print(" ")
print(a)