from vigenere import encrypt_vigenere, decrypt_vigenere

def interactive_mode():
    print("Добро пожаловать в интерактивный режим проверки шифра Виженера!")
    while True:
        print("\nВыберите действие:")
        print("1. Зашифровать текст")
        print("2. Расшифровать текст")
        print("3. Выйти")
        choice = input("Ваш выбор (1/2/3): ").strip()

        if choice == "1":
            plaintext = input("Введите текст для шифрования: ").strip()
            key = input("Введите ключ: ").strip()
            encrypted = encrypt_vigenere(plaintext, key)
            print(f"Зашифрованный текст: {encrypted}")
        elif choice == "2":
            ciphertext = input("Введите текст для дешифрования: ").strip()
            key = input("Введите ключ: ").strip()
            decrypted = decrypt_vigenere(ciphertext, key)
            print(f"Расшифрованный текст: {decrypted}")
        elif choice == "3":
            print("Выход из интерактивного режима. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    interactive_mode()