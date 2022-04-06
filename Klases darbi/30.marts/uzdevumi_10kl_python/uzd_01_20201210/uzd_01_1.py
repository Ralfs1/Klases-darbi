# Uzdevums: 01-1: Izveidot programmu, kas prasa lietotâjam ievadît skaitli n, tad programma aprçíina n+nn+nnn. Rezultâts tiek parâdîts konsolç.

skaitlis = int(input("Ievadi skaitli: "))
n1 = int( "%s" % skaitlis )
n2 = int( "%s%s" % (skaitlis,skaitlis) )
n3 = int( "%s%s%s" % (skaitlis,skaitlis,skaitlis) )
print (n1+n2+n3)