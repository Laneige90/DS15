def calculSales(ns):
    if len(ns) == 1:
        return

    if ns[0] < ns[1]:
        bank = ns[1] - ns[0]
        print(f'sales: {ns}')
        print(f'매출 증감액: +{bank}')
        del ns[0]
        return calculSales(ns)

    elif ns[0] > ns[1]:
        bank = ns[0] - ns[1]
        print(f'sales: {ns}')
        print(f'매출 증감액: -{bank}')
        del ns[0]
        return calculSales(ns)


sales = [12000, 13000, 12500, 11000, 10500, 98000, 91000, 91500, 10500, 11500, 12000, 12500]

calculSales(sales)
