dny_v_týdnu = ["PO", "ÚT", "ST", "ČT", "PÁ", "SO", "NE"]
leden = 31
únor = 28
březen = 31
duben = 30 
květen = 31 
červen = 30
červenec = 31
srpen = 31
září = 30
říjen = 31
listopad = 30
prosinec = 31

rok = leden + únor + březen + duben + květen + červen + červenec + srpen + září + říjen + listopad + prosinec
years = 40
years1 = years / 4


for j in range(1, years):
    if j % 4 == 0:
        print(rok + 1)

    else: 
        print(rok)
