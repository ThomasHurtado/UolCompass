import hashlib

while True:
    texto = input("Digite uma string ou '0' para sair : ")

    if texto.lower() == '0':
        break

    hash_sha1 = hashlib.sha1(texto.encode())
    print("Hash:", hash_sha1.hexdigest())
