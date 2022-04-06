# Izveidot programmu, kura prasa lietotâjam ievadît cilindra râdiusu un tâ augstumu,
# tiek aprçíinâts cilindra laukums un tilpums. Rezultâts tiek parâdîts konsolç.
# tilpums = 3.14 * râdiuss * râdiuss * augstums
# laukums = 2 * (3.14 * râdiuss * râdiuss) + augstums * (2 * 3.14 * râdiuss)

pi = 3.14
augstums = float(input('ievadi cilindra augstumu: '))
radiuss = float(input('ievadi cilindra rādiusu: '))
tilpums = pi * radiuss * radiuss * augstums
laukums = 2*(pi*radiuss*radiuss) + augstums * (2*pi*radiuss)
print("tilpums ir: ", tilpums)
print("laukums ir: ", laukums)
