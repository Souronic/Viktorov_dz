for num in range(1, 1001, 2):
    cub_numb = num ** 3
    cube_a = cub_numb
    sum_cub = 0
    while cub_numb > 0:
        digit = cub_numb % 10
        sum_cub += digit
        cub_numb = cub_numb // 10
    if sum_cub % 7 == 0:
        print(num, "^3=", cube_a, ";Сумма=", sum_cub)
    final_sum = 0
    cub_numb = (num + 17) ** 3
    Sum_cub_b = num + 17
    cube_b = cub_numb
    while cub_numb > 0:
        digit = cub_numb % 10
        final_sum += digit
        cub_numb = cub_numb // 10
    if final_sum % 7 == 0:
        print(num, "+17=", Sum_cub_b, ";Куб", cube_b, ";Сумма:", final_sum)

