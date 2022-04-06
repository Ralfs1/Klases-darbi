# Izveidot programmu, kura prasa lietotâjam sekunþu skaitu. 
# Sekundes tiek pârveidotas par “x hours y minutes z seconds” tipa tekstu. Rezultâts tiek parâdîts konsolç.

sec=float(input('Ievadi skaitli:'))

x=sec//3600
y=x//60
z=y//1
print('Stundas:',x,'Minūtes',y,'Sekundes',z)
