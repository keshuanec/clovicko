from random import choices


# class Figurka:
#     def __init__(self, barva: str, pozice: int, podoba = "&"):
#         self.barva = barva
#         self.pozice = pozice
#         self.podoba = podoba
#     def vypis_info(self):
#         print(f"moje barva je {self.barva}, aktualni pozice je {self.pozice} a moje podoba je {self.podoba}")
#
# figurka_1 = Figurka("bila", 1,)


def play_game(n: int, roll_bias: float, output: bool):           #n = počet herních polí, roll bias = pravděpodobnost hodu šestky (1/6 je spravedlivá kostka), output = True/False zda chceme zobrazit průběh hry graficky nebo jenom zapsat do souboru
    if output == True:
        print(f"pocet poli = {n}, pravdepodobnost hodu 6 = {round((roll_bias * 100),1)}%")
    figure_pos = 1
    figure = "&"
    start = "S"
    cursed = "X"
    finish = "C"
    field = ""
    empty = "_"
    counter = 0
    numbers = ""
    i = 1
    num = 1
    hod = 0
    print_roll = ""
    roll_tuple = (1,2,3,4,5,6)
    rest_chance = ((1 - roll_bias) / 5)




    while i <= n:                           # tato smyčka mi tvoří string 1234567890 s opakovanim tak abych mel stejne mnozstvi znaku jako je pocet poli v clovicku n
        if num < 10:
            numbers += str(num)
            num += 1
            i += 1
        else:
            num = 0
            numbers += str(num)
            num += 1
            i+=1


    while figure_pos != n:                                                       # smyčka jede dokud pozice figurky neni na hodnote posledniho pole
        #roll = randint(1, 6)                                                    # hod kostkou
        roll = choices(roll_tuple, weights=(rest_chance, rest_chance, rest_chance, rest_chance, rest_chance, roll_bias), k=1)[0] #ruzna pravdepodobnost jednotlivych hozenych hodnot. Rovnoměrně se rozpočítá pravděpodobnost u ostatních po zadání šance na šestku
        print_roll += str(roll) + " "                                            # hodnota hodu ktera se bude tisknout do vystupu
        hod += roll                                                              # celková hodnota hodu v připade hozenych šestek
        while roll == 6:                                                         # dokud házím šestky, tak se hody opakují
            # roll = randint(1, 6)                                               # viz výše jen znovu při hodu šestky
            roll = choices(roll_tuple, weights=(rest_chance, rest_chance, rest_chance, rest_chance, rest_chance, roll_bias), k=1)[0]
            print_roll += str(roll) + " "                                        # viz výše jen znovu při hodu šestky
            hod += roll                                                          # viz výše jen znovu při hodu šestky
        if figure_pos + hod <= n:                                                # kontrola toho jestli hodem nepřeskočíme cíl
            figure_pos += hod
        counter += 1                                                             # počítadlo hodů
        if counter == 10000:
            break
        pos = 1                                                                  # reset vykreslované pozice na 1
        while pos <= n:                                                          # vykreslování jednotlivých herních polí
            if pos == figure_pos:                                                # pokud je je vykreslovaná pozice stejná jako pozice figurky, tak nakreslíme figurku
                field += figure
                if figure_pos % 13 == 0 and figure_pos < n:                                         # kontrola jestli figurka nestojí na otrávené pozici
                    figure_pos = 1
            elif pos == 1 and pos != figure_pos:                                 # na první pozici vykreslíme start
                field += start
            elif pos % 13 == 0:                                                  # na každé 13 pozici vykreslíme otrávené pole
                field += cursed
            elif pos == n:                                                       # na poslední pozici vykreslíme cíl
                field += finish
            else:
                field += empty                                                   # na všech ostatních máme prázná pole
            pos += 1


        if output == True:
            print(f"Stage: {counter}, roll = {print_roll}\n{field}\n{numbers}")     # tisk výstupu jednotlivých kol
        hod = 0                                                                 # vynulování výsledného hodu
        field = ""                                                              # vynulování vykrelování kola
        print_roll = ""                                                         # vynulování tisknutého hodu

    if output == True:
        print(f"Game finished in turn {counter}")                                   # tisk finální zprávy
    return counter

def analyze_game(n, num, roll_bias):                    # n počet polí, num počet simulací, roll_bias pravděpodobnost šestky
    counter_list = []
    for i in range(num):
        counter_list.append(play_game(n,roll_bias, False))
    return (sum(counter_list))/(len(counter_list))

def print_average_lengths(x, y):                            # funkce, ktera vypíše průměrnou délku hry na velikosti polí od x do y
    for field_count in range(x, y+1):
        print(f"polí: {field_count}, průměrná délka: {analyze_game(field_count, 50, 1 / 6)} kol")

def find_optimal_bias(n, num):
    roll_bias = 0
    min_bias = roll_bias
    min_bias_count = analyze_game(n, num, round(roll_bias,2))
    roll_bias += 0.05
    while roll_bias < 1:
        analysed = analyze_game(n, num, round(roll_bias,2))
        if analysed < min_bias_count:
            min_bias = roll_bias
            min_bias_count = analysed
        roll_bias += 0.05
    return min_bias

def print_optimal_biases():             #nejlepší bias pro plány o velikosti 5, 10, 100 a 500, po 100 simulacích
    print(f"optimální šance na šestku pro 5 polí je: {(find_optimal_bias(5, 100)*100)}%")
    print(f"optimální šance na šestku pro 10 polí je: {(find_optimal_bias(10, 100)*100)}%")
    print(f"optimální šance na šestku pro 100 polí je: {(find_optimal_bias(100, 100)*100)}%")
    print(f"optimální šance na šestku pro 500 polí je: {round((find_optimal_bias(500, 100)*100),2)}%")





#print_optimal_biases()
#find_optimal_bias(40, 100)
#print_average_lengths(2, 100)
#print(analyze_game(42, 100, 0))
print(play_game(100, 1/6, True))
print("tohle je pokusnej vklad, tak snad to bude fachat")
print("toto je druha zmena provedena na velkem pocitaci")