import np as np
import pandas as pd

# vocabulary
char_names = [["Зеле", "Seele"], ["Серебряный волк","Silver Wolf"], ["Блейд", "Blade"], ["Кафка", "Kafka"],
             ["Фу Сюань", "Fu Xuan"], ["Цзин Лю", "Jingliu"]]

# function that translates russian date into english
def translate(Jumps):
    Jumps["warp type"] = Jumps["тип баннера"]
    Jumps["warp"] = Jumps["баннер"]
    Jumps["entity type"] = Jumps["тип"]
    Jumps["entity"] = Jumps["сущность"]
    Jumps["rarity"] = Jumps["редкость"]
    Jumps["warp time"] = Jumps["время"]
    Jumps = Jumps.drop(columns=["тип баннера", "баннер","тип","сущность","редкость","время"])
    Jumps["warp type"] = Jumps["warp type"].replace("Персонаж", "Character Event Warp")
    Jumps["entity type"] = Jumps["entity type"].replace("Конус", "Light Cone")
    Jumps["entity type"] = Jumps["entity type"].replace("Персонаж", "Character")
    Jumps["entity type"] = Jumps["entity type"].replace(np.nan, "Light Cone")
    for name in char_names:
        Jumps["warp"] = Jumps["warp"].replace(name[0], name[1])
        Jumps["entity"] = Jumps["entity"].replace(name[0], name[1])
    Jumps['warp time'] = pd.to_datetime(Jumps['warp time'], format='%d/%m/%y %H:%M:%S')
    Jumps.to_csv("Data/warps.csv", index=False, sep=";")