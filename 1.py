import eel,os,math
def long(A,B):
    A=list(map(float,A[:2]))
    B=list(map(float,B[:2]))
    AD = abs(A[1] - B[1]) * 111.3 * math.cos(B[0])
    BC = abs(A[1] - B[1]) * 111.3 * math.cos(A[0])
    AB = abs(A[0] - B[0]) * 111.1
    AH = abs(AD - BC) / 2
    BH = math.sqrt(abs(AB ** 2 - AH ** 2))
    HD = abs(AD-AH)
    BD = math.sqrt(BH ** 2 + HD ** 2)
    return round(BD,3)
def analyze(cars_list: list[list[str]]):
    text = '\n'
    for car in cars_list:
        if car != [''] and car != '"'and car != 'Ш':
            print(car)
            print(car[3])
            text += f"Авто {car[3]} по адресу {round(float(car[0]),5)},{round(float(car[1]),5)}"\
            f" Сигнал -- {"✔" if car[2]== '' else car[2]+'❌'}\n\r"
    text+= "\n\n\n\n\n\n\n"

    for num,car in enumerate(cars_list):
        for scar in cars_list[num+1:]:
            if car != [''] and scar != [''] and car != '"':
                print(car," ",scar)
                print(car[3])
                text += f"Между {car[3]} и {scar[3]} -- {long(car,scar)} КМ\n\r"
    text += "\n\r\n\r"
    with open(f"{os.path.dirname(os.path.abspath(__file__))}\web\last_file.txt", 'r+',encoding='UTF-8') as f:
        f.write(str(text))
        f.close()
    return text


@eel.expose
def on_load_load_last():
    with open(f"{os.path.dirname(os.path.abspath(__file__))}\web\last_file.txt", 'r+',encoding='UTF-8') as f:
        l_text=f.read()
        print(l_text)
        f.close()
        return l_text
@eel.expose
def get_file_test():
    file = "'Широта';'Долгота';'Описание';'Подпись';'Номер метки'\n\r59.93128814510101;30.31787559790033;'База';'A429HO78';\n\r59.93458338770518;30.332295153564367;;'P768AB78';\n\r59.9354017630424;30.311953280395446;;'X623OB78';\n\r59.93822284904074;30.34825966162103;'ДТП';'M976XB78';\n\r59.94506997982365;30.302640650695693;;'Y104KA78';\n\r59.924869017077754;30.327660296386558;;'T555XX78';\n\r59.946383260924485;30.329891894286888;'Заправка';'C643BE78';"
    car_list = file.split('\n')[1:]
    for num, car in enumerate(car_list):
        car_list[num] =car.split(';')
    print("passed")
    return analyze(car_list) 

@eel.expose
def get_file(file: str):
    car_list = file.split('\n')[1:]
    for num, car in enumerate(car_list):
        car_list[num] =car.split(';')
    return analyze(car_list)


if __name__ == "__main__":
        
    eel.init('web', allowed_extensions=["js","html"])
    eel.start("main.html", size=(550,750),mode="chrome")
#Расчёт дальности
