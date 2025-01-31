import os
import pyaes

def decrypt_file(file_name, key):
    """
    Desencripta um arquivo usando a chave fornecida.

    Args:
        file_name (str): Nome do arquivo a ser desencriptado.
        key (bytes): Chave de desencriptação.

    Returns:
        None
    """
    try:
        # Abrir o arquivo encriptado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Criar um objeto AES
        aes = pyaes.AESModeOfOperationCTR(key)

        # Desencriptar o arquivo
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo encriptado
        os.remove(file_name)

        # Salvar o arquivo desencriptado
        new_file = file_name.replace(".ransomwaretroll", "")
        with open(new_file, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo {file_name} desencriptado com sucesso!")

    except FileNotFoundError:
        print(f"Arquivo {file_name} não encontrado.")
    except Exception as e:
        print(f"Erro ao desencriptar arquivo: {e}")

if __name__ == "__main__":
    file_name = "teste.txt.ransomwaretroll"
    key = b"testeransomwares"
    decrypt_file(file_name, key)