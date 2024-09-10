def count_letter_a(s):
    count = s.lower().count('a')
    return count

string = input("Informe uma string para verificar a ocorrência de 'a': ")
count = count_letter_a(string)
print(f"A letra 'a' ocorre {count} vezes na string.")
