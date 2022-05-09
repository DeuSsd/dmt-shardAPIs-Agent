import DBinterface as DBi

BLOCK_SIZE = 16
DES_KEY_FILE = 'U:\ВКР\ARappServer\Key.txt'
TEST_LOGIN = "TEST"
TEST_PASSWORD = "TEST0912375981237059812730"

# Обработка ошибки отсутствия файла с DES KEY
class FileEmpty(Exception):
    def __init__(self, arg):
        self.message = f"There is not DSA-encryption key in the file '{arg}'"

    def __str__(self):
        if self.message:
            return 'FileEmpty, {0} '.format(self.message)
        else:
            return 'FileEmpty has been raised'


# Обработка ошибки неправильного ключа DES KEY
class WrongDES_Key(Exception):
    def __init__(self, arg):
        self.message = f"There is changed DSA-encryption key in the file '{arg}'" \
                       "\nChange DSA-encryption key or rewrite all users (including the base user) in database."

    def __str__(self):
        if self.message:
            return 'WrongDES_Key, {0} '.format(self.message)
        else:
            return 'WrongDES_Key has been raised'


try:
    file = open(DES_KEY_FILE, "rb")
    if not open(DES_KEY_FILE, "rb").read():
        raise FileEmpty(DES_KEY_FILE)
    key = (file.read())
    file.close()
except FileNotFoundError:
    file = open(DES_KEY_FILE, "wb")
    print(f"No such file: '{DES_KEY_FILE}'")
    raise FileEmpty(DES_KEY_FILE)

##########################################################
def checkDES_Key():
    '''
    Проверка на наличие ключа DES KEY
    :return:
    '''
    if "Incorrect login or password" == DBi.User_DB.getNamefromlogin(TEST_LOGIN, TEST_PASSWORD):
        raise WrongDES_Key(DES_KEY_FILE)


# # дешифровка
# def decoding(password):
#     '''
#     Дештифрование пароля
#     :param name: password
#     :return:
#     '''
#     des = DES.new(key, DES.MODE_ECB)
#     data = des.decrypt(password)
#     data = data.decode('utf-8')
#     print("data", data)
#     return data