import PySimpleGUI as sg  
from pyModbusTCP.client import ModbusClient
import time
import sys


stat = [0,0,0,0,0,0,0,0]
##stat1 = 1
##stat2 = 1
##stat3 = 1
##stat4 = 1
##stat5 = 1
##stat6 = 1
##stat7 = 1
##stat8 = 1

ishl = [0,0,0,0,0,0,0,0]
##ishl1 = 1
##ishl2 = 1
##ishl3 = 1
##ishl4 = 1
##ishl5 = 1
##ishl6 = 1
##ishl7 = 1
##ishl8 = 1

comm = [0,0,0,0,0,0,0,0]
##comm1 = 1
##comm2 = 1
##comm3 = 1
##comm4 = 1
##comm5 = 1
##comm6 = 1
##comm7 = 1
##comm8 = 1

strat = [0,0,0,0,0,0,0,0]
##strat1 = 1
##strat2 = 1
##strat3 = 1
##strat4 = 1
##strat5 = 1
##strat6 = 1
##strat7 = 1
##strat8 = 1

porog1 = [0,0,0,0,0,0,0,0]
##porog11 = 1
##porog12 = 1
##porog13 = 1
##porog14 = 1
##porog15 = 1
##porog16 = 1
##porog17 = 1
##porog18 = 1

porog2 = [0,0,0,0,0,0,0,0]
##porog21 = 1
##porog22 = 1
##porog23 = 1
##porog24 = 1
##porog25 = 1
##porog26 = 1
##porog27 = 1
##porog28 = 1

porog3 = [0,0,0,0,0,0,0,0]
##porog31 = 1
##porog32 = 1
##porog33 = 1
##porog34 = 1
##porog35 = 1
##porog36 = 1
##porog37 = 1
##porog38 = 1

porog4 = [0,0,0,0,0,0,0,0]
##porog41 = 1
##porog42 = 1
##porog43 = 1
##porog44 = 1
##porog45 = 1
##porog46 = 1
##porog47 = 1
##porog48 = 1

sg.Input(default_text='Введите заменяемый тег', key='TAG')
sg.theme('Default')             #Обьясление цветовой схемы интерфейса
data = [['Текущие состояние', stat[0], stat[1], stat[2], stat[3], stat[4], stat[5], stat[6], stat[7]],
['Ток шлейфа(мкА)', ishl[0], ishl[1], ishl[2], ishl[3], ishl[4], ishl[5], ishl[6], ishl[7]],
['Команда', comm[0], comm[1], comm[2], comm[3], comm[4], comm[5], comm[6], comm[7]],
['Стратегия', strat[0], strat[1], strat[2], strat[3], strat[4], strat[5], strat[6], strat[7]],
['Порог 1', porog1[0], porog1[1], porog1[2], porog1[3], porog1[4], porog1[5], porog1[6], porog1[7]],
['Порог 2', porog2[0], porog2[1], porog2[2], porog2[3], porog2[4], porog2[5], porog2[6], porog2[7]],
['Порог 3', porog3[0], porog3[1], porog3[2], porog3[3], porog3[4], porog3[5], porog3[6], porog3[7]],
['Порог 4', porog4[0], porog4[1], porog4[2], porog4[3], porog4[4], porog4[5], porog4[6], porog4[7]]]
#['Таймер 1', timer11, timer12, timer13, timer14, timer15, timer16, timer17, timer18],
#['Таймер 2', timer21, timer22, timer23, timer24, timer25, timer26, timer27, timer28],
#['Таймер 3', timer31, timer32, timer33, timer34, timer35, timer36, timer37, timer38],
#['Таймер 4', timer41, timer42, timer43, timer44, timer45, timer46, timer47, timer48]]

headings = ['', 'Шлейф 1', 'Шлейф 2', 'Шлейф 3', 'Шлейф 4', 'Шлейф 5', 'Шлейф 6', 'Шлейф 7', 'Шлейф8']

layout = [          #Интерфейс
    [sg.Text('IP адрес устройства'), sg.Input(default_text='192.9.200.99', key='IP')],   #Строчка для ввода IP
    [sg.Text('Порт устройства'), sg.Input(default_text='502', key='port')],   #Строчка для ввода IP
    [sg.Text('Status: ready', key='out')], #Вывод статуса программы
    [sg.Text('Таблица чтения'), sg.Button('Connect')], #Сообщение
    [sg.Table(values=data, headings=headings, max_col_width=30,
                    # background_color='light blue',
                    auto_size_columns=True,
                    #display_row_numbers=True,
                    justification='right',
                    num_rows=8,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    row_height=35,
                    tooltip='Таблица чтения')],
    [sg.Text('                           '), sg.Text('Шлейф 1 '), sg.Text('Шлейф 2 '), sg.Text('Шлейф 3 '), sg.Text('Шлейф 4 '), sg.Text('Шлейф 5 '), sg.Text('Шлейф 6 '), sg.Text('Шлейф 7 '), sg.Text('Шлейф 8' )],
    [sg.Text('Стратегия работы'), sg.Input(key='str1', size=(8,1)), sg.Input(key='str2', size=(8,1)), sg.Input(key='str3', size=(8,1)), sg.Input(key='str4', size=(8,1)), sg.Input(key='str5', size=(8,1)), sg.Input(key='str6', size=(8,1)), sg.Input(key='str7', size=(8,1)), sg.Input(key='str8', size=(8,1))],
    [sg.Text('Порог 1               '), sg.Input(key='p11', size=(8,1)), sg.Input(key='p12', size=(8,1)), sg.Input(key='p13', size=(8,1)), sg.Input(key='p14', size=(8,1)), sg.Input(key='p15', size=(8,1)), sg.Input(key='p16', size=(8,1)), sg.Input(key='p17', size=(8,1)), sg.Input(key='p18', size=(8,1))],
    [sg.Text('Порог 2               '), sg.Input(key='p21', size=(8,1)), sg.Input(key='p22', size=(8,1)), sg.Input(key='p23', size=(8,1)), sg.Input(key='p24', size=(8,1)), sg.Input(key='p25', size=(8,1)), sg.Input(key='p26', size=(8,1)), sg.Input(key='p27', size=(8,1)), sg.Input(key='p28', size=(8,1))],
    [sg.Text('Порог 3               '), sg.Input(key='p31', size=(8,1)), sg.Input(key='p32', size=(8,1)), sg.Input(key='p33', size=(8,1)), sg.Input(key='p34', size=(8,1)), sg.Input(key='p35', size=(8,1)), sg.Input(key='p36', size=(8,1)), sg.Input(key='p37', size=(8,1)), sg.Input(key='p38', size=(8,1))],
    [sg.Text('Порог 4               '), sg.Input(key='p41', size=(8,1)), sg.Input(key='p42', size=(8,1)), sg.Input(key='p43', size=(8,1)), sg.Input(key='p44', size=(8,1)), sg.Input(key='p45', size=(8,1)), sg.Input(key='p46', size=(8,1)), sg.Input(key='p47', size=(8,1)), sg.Input(key='p48', size=(8,1))],
    [sg.Button('Writh')]   #Кнопка
]
window = sg.Window('GoodBuyBMPull', layout, icon=r'C:/Users/rozze/OneDrive/Рабочий стол/Feels/Replicator.ico') #Обдьявление окна интерфейса

def Connect():
    ip_address = values['IP']
    ##ip_address = int(str_ip_address) 
    str_port = values['port']
    port = int(str_port) 
    MB = ModbusClient(host=ip_address, port=port)
    MB.open()
    while True:
        if MB.is_open():
            window['out'].update(f'Status: Connect is done!')
            rr = MB.read_holding_registers(3, 8)
            # [False, True]
            if not rr[0] and rr[1]:
                print ('work')
               ## sys.exit(0)
            # [True, True]
            elif rr[0] and rr[1]:
                print ('not work')
               ## sys.exit(1)
            print ('-')
           ## sys.exit(-1)
        else:
            window['out'].update(f'Status: Connect is fail!')
            
while True:
    event, values = window.read()
    if event is None or event == sg.WIN_CLOSED:
        break
    if event == 'Connect':
        Connect()
