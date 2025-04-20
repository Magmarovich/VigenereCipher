import unittest
from vigenere import encrypt_vigenere, decrypt_vigenere

class TestVigenereCipher(unittest.TestCase):
    def test_encrypt_simple(self):
        """Тест простого шифрования без пробелов и специальных символов."""
        plaintext = "ATTACKATDAWN"
        key = "LEMON"
        print(f"Тестируем шифрование: текст = '{plaintext}', ключ = '{key}'")
        encrypted = encrypt_vigenere(plaintext, key)
        print(f"Результат шифрования: {encrypted}")
        self.assertEqual(encrypted, "LXFOPVEFRNHR")

    def test_decrypt_simple(self):
        """Тест простого дешифрования без пробелов и специальных символов."""
        ciphertext = "LXFOPVEFRNHR"
        key = "LEMON"
        print(f"Тестируем дешифрование: шифротекст = '{ciphertext}', ключ = '{key}'")
        decrypted = decrypt_vigenere(ciphertext, key)
        print(f"Результат дешифрования: {decrypted}")
        self.assertEqual(decrypted, "ATTACKATDAWN")

    def test_encrypt_with_spaces(self):
        """Тест шифрования текста с пробелами."""
        plaintext = "HELLO WORLD"
        key = "KEY"
        print(f"Тестируем шифрование: текст = '{plaintext}', ключ = '{key}'")
        encrypted = encrypt_vigenere(plaintext, key)
        print(f"Результат шифрования: {encrypted}")
        self.assertEqual(encrypted, "RIJVS UYVJN")

    def test_decrypt_with_spaces(self):
        """Тест дешифрования текста с пробелами."""
        ciphertext = "RIJVS UYVJN"
        key = "KEY"
        print(f"Тестируем дешифрование: шифротекст = '{ciphertext}', ключ = '{key}'")
        decrypted = decrypt_vigenere(ciphertext, key)
        print(f"Результат дешифрования: {decrypted}")
        self.assertEqual(decrypted, "HELLO WORLD")

    def test_encrypt_mixed_case(self):
        """Тест шифрования текста с разным регистром."""
        plaintext = "HeLLo"
        key = "KEY"
        print(f"Тестируем шифрование: текст = '{plaintext}', ключ = '{key}'")
        encrypted = encrypt_vigenere(plaintext, key)
        print(f"Результат шифрования: {encrypted}")
        self.assertEqual(encrypted, "RIJVS")

    def test_decrypt_mixed_case(self):
        """Тест дешифрования текста с разным регистром."""
        ciphertext = "RIJVS"
        key = "KEY"
        print(f"Тестируем дешифрование: шифротекст = '{ciphertext}', ключ = '{key}'")
        decrypted = decrypt_vigenere(ciphertext, key)
        print(f"Результат дешифрования: {decrypted}")
        self.assertEqual(decrypted, "HELLO")

if __name__ == "__main__":
    print("Запуск модульных тестов для шифра Виженера...")
    unittest.main(verbosity=2)