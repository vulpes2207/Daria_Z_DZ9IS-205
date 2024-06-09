def find_minimum_cs(sd, cs, cn_invent):
    result = []
    for cn in sorted(cs, reverse=True):
        while sd >= cn and cn_invent[cn] > 0:
            sd -= cn
            cn_invent[cn] -= 1
            result.append(cn)
            if sd == 0:
                return result
    return None if change > 0 else result

prs = {
    "молоко": 20, "хлеб": 15, "яблоки": 10, "бананы": 30,
    "сыр": 40, "ветчина": 50, "мороженое": 25, "вода": 5,
    "сок": 35, "шоколадка": 45}


cs = [1, 5, 10, 15, 20]
cn_invent = {1: 10, 5: 5, 10: 2, 15: 3, 20: 0}

while True:
    prt_name = input("Введите продукт или 'выход': ")
    if prt_name == "выход":
        break
    if prt_name not in prs:
        print("Такого продукта нет.")
        continue

    try:
        v = int(input(f"Стоимость {prt_name} {prs[prt_name]} рублей. Введите сумму: "))
    except ValueError:
        print("Введите корректную сумму.")
        continue

    if v < prs[prt_name]:
        print("Недостаточно средств.")
        continue

    change = v - prs[prt_name]
    cs_needed = find_minimum_cs(change, cs, cn_invent)

    if cs_needed is None:
        print("Невозможно выдать сдачу.")
    else:
        print(f"Сдача: {change} руб. Монеты: {cs_needed}")
        print("Остаток монет в кассе:", cn_invent)

if __name__ == "__main__":
    main()