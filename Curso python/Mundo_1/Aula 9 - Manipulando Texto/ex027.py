nome = str(input('digite seu nome completo: ')).title().split()


primero_nome = nome[0]
ultimo_nome = nome[-1] #-1 mostra o ultimo

print(f'''Seu primero nome é: {primero_nome}
Seu ultimo nome é: {ultimo_nome}
''')
