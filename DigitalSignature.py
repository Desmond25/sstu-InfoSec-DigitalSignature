from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Генерация ключей DSA
key = DSA.generate(2048)

# Чтение файла
with open('message.txt', 'rb') as f:
    message = f.read() 

# Создание объекта для вычисления хеша
hash_object = SHA256.new(message)

# Создание объекта для вычисления ЭЦП
signer = DSS.new(key, 'fips-186-3')

# Подпись данных
signature = signer.sign(hash_object)

# Сохранение подписи в файл
with open('signature.pem', 'wb') as f:
    f.write(signature)

# Загрузка подписи из файла
with open('signature.pem', 'rb') as f:
    signature = f.read()

# Создание объекта для вычисления хеша
hash_object = SHA256.new(message)

# Создание объекта для проверки подписи
verifier = DSS.new(key, 'fips-186-3')

# Проверка подписи
try:
    verifier.verify(hash_object, signature)
    print('Signature is valid.')
except ValueError:
    print('Signature is not valid.')



# Изменение подписи
with open('signature.pem', 'a') as f:
    f.write('not valid')

# Загрузка подписи из файла
with open('signature.pem', 'rb') as f:
    signature = f.read()

# Создание объекта для вычисления хеша
hash_object = SHA256.new(message)

# Создание объекта для проверки подписи
verifier = DSS.new(key, 'fips-186-3')

# Проверка подписи
try:
    verifier.verify(hash_object, signature)
    print('Signature is valid.')
except ValueError:
    print('Signature is not valid.')
