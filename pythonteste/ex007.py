a=input('Digite algo:')
print('o tipo primitivo dessa variável é :',type(a))
#Método acima serve para definir o tipo da variável declarada.
print('Só tem espaços?',a.isspace())
#Método usado para identificar se existe espaços ''
print('É um numero?',a.isnumeric())
# Método que identifica numeros.
print('É um alfabético?',a.isalpha())
# Metodo que identifica a tipo alfabético ex:a,B,c W...etc.
print('É um alfanumérico?',a.isalpha())
# Método utilizado para identificar se é letra ou numeros.
print('Está em maiúsculo?',a.isupper())
# Metodo para identificar se está escrito tudo em maiusculo.
print('Está em minúsculo?',a.islower())
# Método utilizado para identificar se está tudo em minusculo.
print('Está capítalizada',a.istitle())
#capitalizada significa  que a primeira letra e maiuscula e as demais minusculas.
