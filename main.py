import string

from colorama import Fore, Style, init

from intro import intros

# Inisialisasi colorama
init(autoreset=True)

# Mengubah warna judul menjadi biru neon
intros("CaesarEncrypt", 210, 1.0, 0.5, "=", True)


def CaesarEncrypt(message, key):
    shift = key % 26
    cipher = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift],
    )
    EncryptedMessage = message.lower().translate(cipher)
    return EncryptedMessage


def CaesarDecrypt(EncryptedMessage, key):
    shift = key % 26
    cipher = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[-shift:] + string.ascii_lowercase[:-shift],
    )
    message = EncryptedMessage.translate(cipher)
    return message


# Menu pemilihan
print(Fore.CYAN + "Pilih opsi:")
print(Fore.CYAN + "================\n")
print(Fore.LIGHTMAGENTA_EX + "1. Enkripsi")
print(Fore.LIGHTMAGENTA_EX + "2. Dekripsi")
option = input(Fore.YELLOW + "\nMasukkan pilihan (1/2):" + Style.RESET_ALL)

if option == "1":
    # Input untuk pesan dan kunci untuk enkripsi
    message = input(
        Fore.RED + "\nMasukkan pesan yang ingin dienkripsi: " + Style.RESET_ALL
    )
    key = int(input(Fore.RED + "Masukkan kunci (angka): " + Style.RESET_ALL))

    # Enkripsi pesan
    sample1 = CaesarEncrypt(message, key)
    print(Fore.GREEN + f"Encrypt Message : {sample1}" + Style.RESET_ALL)

elif option == "2":
    # Input untuk pesan dan kunci untuk dekripsi
    encrypted_message_input = input(
        Fore.RED + "\nMasukkan pesan yang ingin didekripsi: " + Style.RESET_ALL
    )
    key = int(input(Fore.RED + "Masukkan kunci (angka): " + Style.RESET_ALL))

    # Dekripsi pesan
    sample2 = CaesarDecrypt(encrypted_message_input, key)
    print(Fore.GREEN + f"Decrypt Message : {sample2}" + Style.RESET_ALL)

else:
    print(Fore.RED + "Pilihan tidak valid. Silakan pilih 1 atau 2." + Style.RESET_ALL)
