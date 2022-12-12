def math_operation(částka_měsiční, daň):
    y = částka_měsiční
    for i in range(doba * 12):
        if i == 0:
            continue
        x = (částka_měsiční / 100 / 12) * urok
        x = x - (daň / 100 * x)
        částka_měsiční += x
        částka_měsiční += y
    result = částka_měsiční
    return result

def math_operation2(částka_jednorázová, daň):
    for _ in range(doba * 12):
        x = (částka_jednorázová / 100 / 12) * urok
        x = x - (daň / 100 * x)
        částka_jednorázová += x
    result = částka_jednorázová
    return result

def result():
    result = math_operation2(částka_jednorázová, daň) + math_operation(částka_měsiční, daň)
    x = round(result)
    return x

def convert_to_str():
    new_str = ""
    x = str(result())
    sum = -1
    for i in x[::-1]:
        sum += 1
        if sum % 3 == 0 and sum != 0:
            new_str += "."
        new_str += i
    new_str = new_str[::-1]
    return new_str

print("Spořící/Investiční kalkulačka")
částka_jednorázová = int(input("Kolik peněz chcete jednorázově investovat "))
částka_měsiční = int(input("Kolik peněz chcete měsíčně investovat "))
doba = int(input("Kolik let chcete investovat "))
urok = int(input("Roční zhodnocení % "))
print("Mějte prosím na paměti že investice mají různé zvýhodnění co se danění týče.\nProto jsou výsledky se započítáním daně nepřesné, pouze orientační.")
daň = int(input("Daň ze zisku % "))

print(f"Naspořená částka je: {convert_to_str()} Kč.")
