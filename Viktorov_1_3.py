numb = 0
while numb < 100:
    numb += 1
    if numb <= 20:
        if numb >= 5:
            print(numb, "процентов")
        elif numb % 2 == 0 or numb % 3 == 0:
            print(numb, "процента")
        else:
            print(numb, "процент")
    elif numb >20:
        if (numb % 10) >= 5 or numb % 10 == 0:
            print(numb, "процентов")
        elif (numb % 10) == 1:
            print(numb, "процент")
        else:
            print(numb, "процента")
