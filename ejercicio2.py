letra = input("Ingrese la letra:")
while letra not in('a','b','c','d','e'):
    if letra == '.':
        break
    letra = input("Ingrese otra vez su letra:")
print('Su letra o punto   es:{}'.format(letra))
