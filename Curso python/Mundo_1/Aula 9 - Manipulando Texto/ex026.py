frase = str(input('Digite uma frase: ')).lower().strip()

print(f'''A letra A aparece {frase.count('a')} vezes
Ela apareceu pela primera vez na {frase.find('a')+1}° posição  
E ultima posição que ala pareceu  oi na {frase.rfind('a')+1}°''')
