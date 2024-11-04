from random import choices



def vodici_pole(n):   # tato funkce mi tvoří string 1234567890 s opakovanim tak abych mel stejne mnozstvi znaku jako je pocet poli v clovicku n
    """
    vytvori radu cisel v podobe 1234567890123.... tak aby celkove mnozstvi cislic bylo ¨n¨
    :param n: int - pocet poli
    :return: str
    """
    return ("1234567890" * ((n // 10) + 1))[:n]

def throw_dice(roll_bias: float):
    """
    hod kostkou
    :param roll_bias: pravdepodobnost hodu cisla ¨6¨
    :return: vrati nahodny int 1-6
    """
    rest_chance = ((1 - roll_bias) / 5)
    roll = choices(roll_tuple, weights=(rest_chance, rest_chance, rest_chance, rest_chance, rest_chance, roll_bias), k=1)[0]
    return roll

def how_many_tiles(roll_bias: float):
    """
    kolik je celkovy hod?
    :param roll_bias: pravdepodobnost hodu ¨6¨
    :return: celkovy hod v podobe seznamu cislic (napr. [6, 6, 4] nebo [3] atd...)
    """
    total_throw = []
    throw = throw_dice(roll_bias)
    total_throw.append(throw)
    while throw == 6:
        total_throw.append(throw_dice(roll_bias))
    return total_throw

def move_figure(figure_pos: int, total_throw: list):
    """

    :param figure_pos: vstupni pozice figurky
    :param total_throw: celkovy hod
    :return: figure_pos -
    """


#print(vodici_pole(42))