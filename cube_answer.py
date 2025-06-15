#題目一:邊長為n且邊以*表示的正三角形

def triangle(n):
    
    if n < 2:
        return None
    
    for i in range(n):
        if i == 0:
            print(" " * (n-1) + "*")  #第一行   
        elif i == n - 1:
            print("* " * n) #最後一行
        else:
            print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")  #中間行



#題目二:奇數升冪往前偶數降冪在後

def sort_odd_even_number(n):

    number_string = str(n)
    odd_numbers = []
    even_numbers = []

    for number in number_string:
        if int(number) % 2 == 0:
            even_numbers.append(int(number))
        else:
            odd_numbers.append(int(number))
    
    odd_numbers.sort(reverse=True)  # 奇數降冪
    even_numbers.sort()  # 偶數升冪

    result = odd_numbers + even_numbers 
    result = int(''.join(map(str, result)))

    print(result)
