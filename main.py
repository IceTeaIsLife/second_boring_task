def f21(x):
    if x[1] == 1957:
        return 11
    elif x[1] == 1981:
        return 12
    elif x[1] == 2009:
        if x[3] == 2006:
            if x[2] == 'yacc':
                return 6
            elif x[2] == 'ocaml':
                if x[0] == 'cuda':
                    return 7
                elif x[0] == 'hy':
                    return 8
            elif x[2] == 'mql4':
                if x[4] == 1983:
                    return 9
                elif x[4] == 1970:
                    return 10
        elif x[3] == 1999:
            if x[4] == 1970:
                if x[2] == 'yacc':
                    return 3
                elif x[2] == 'ocaml':
                    return 4
                elif x[2] == 'mql4':
                    return 5
            elif x[4] == 1983:
                if x[2] == 'yacc':
                    return 0
                elif x[2] == 'ocaml':
                    return 1
                elif x[2] == 'mql4':
                    return 2


# print(f21(['cuda', 1981, 'mql4', 2006, 1970]))
# print(f21(['cuda', 1957, 'yacc', 2006, 1970]))


def f22(code):
    # binary = bin(code)
    # binary = binary[2:]
    # if len(binary) < 32:
    #     binary = '0' * (32 - len(binary)) + binary
    # binary = binary[::-1]
    # a = binary[0:9]
    # b = binary[9:13]
    # c = binary[13:18]
    # d = binary[18:27]
    # e = binary[27]
    # f = binary[28:32]
    # new_binary = e + c[::-1] + d[::-1] + a[::-1] + f[::-1] + b[::-1]
    # return int(new_binary, 2)
    f = (code & ((2 ** 32 - 1) & ~(2 ** 28 - 1))) >> 24
    e = (code & ((2 ** 28 - 1) & ~(2 ** 27 - 1))) << 4
    d = (code & ((2 ** 27 - 1) & ~(2 ** 18 - 1))) >> 1
    c = (code & ((2 ** 18 - 1) & ~(2 ** 13 - 1))) << 13
    b = (code & ((2 ** 13 - 1) & ~(2 ** 9 - 1))) >> 9
    a = (code & (2 ** 9 - 1)) << 8
    return a | b | c | d | e | f


# print(f22(0xbfe4ef52))
# print((f22(0xbfe4ef52)))
print(f22(0xeb7da79a))


def f23(table):
    unique_row = []
    new_table = []
    for row in table:
        for column in row:
            if column not in unique_row:
                unique_row.append(column)
        for column in unique_row:
            if unique_row[unique_row.index(column)] == 'Выполнено':
                unique_row[unique_row.index(column)] = 'Y'
            elif unique_row[unique_row.index(column)] == 'Не выполнено':
                unique_row[unique_row.index(column)] = 'N'
            elif unique_row[unique_row.index(column)].count('-') == 2:
                phone_number = unique_row[unique_row.index(column)]
                phone_number = phone_number.split('-')
                unique_row[unique_row.index(column)] = f'({phone_number[0]}) {phone_number[1]}-{phone_number[2]}'
            elif unique_row[unique_row.index(column)].count('.') == 2:
                date = unique_row[unique_row.index(column)].split('.')
                unique_row[unique_row.index(column)] = f'{date[0]}/{date[1]}/{date[2]}'
            elif unique_row[unique_row.index(column)].count('.') == 1:
                number = round(float(unique_row[unique_row.index(column)]), 1)
                unique_row[unique_row.index(column)] = str(number)
        new_table.append(unique_row)
        unique_row = []
    return new_table

# table = f23([['Выполнено', '465-214-2435', '0.61', '21.05.99', '21.05.99'],
#              ['Выполнено', '047-823-2854', '0.64', '26.11.04', '26.11.04'],
#              ['Выполнено', '321-193-3098', '0.08', '10.12.99', '10.12.99'],
#              ['Не выполнено', '294-301-3239', '0.08', '24.11.00', '24.11.00']])
# print(table)
