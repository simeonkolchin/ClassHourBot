from enum import Enum

T = '1986917537:AAH210iKRrnipe9DH_nUoQt1P9_7usMxAW8'

db_file = "database.vdb"

class States(Enum):
    S_START = '3333'  # Начало нового диалога
    S_ENTER_NAME = '3331'

    Q_1 = '1'
    Q_2 = '2'
    Q_3 = '3'
    Q_4 = '4'
    Q_5 = '5'
    Q_6 = '6'
    Q_7 = '7'
    Q_8 = '8'
    Q_9 = '9'
    Q_10 = '10'