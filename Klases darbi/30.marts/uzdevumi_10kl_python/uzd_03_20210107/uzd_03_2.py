
# Atrast cik skaitļi norādītajā intervālā dalās ar lietotāja norādīto dalītāju.

sakt=int(input("Sākuma vērtība:"))
end=int(input("Beigu vērtība:"))
dala=int(input("Dalītāja vērtība:"))

cik=0

for i in range(sakt,end+1):
    if i%dala==0:
        cik+=1
#print(cik)
print(f"{cik} skatiļi ir starp {sakt} un {end}, kas dalās ar {dala}")