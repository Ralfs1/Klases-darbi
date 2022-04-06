
# Atrast pozitīva skaitļa ciparu summu. Piemērs: 14214 => 12

skaitlis=input("ievadi pozitīvu skaitli:")
sum=0
if int(skaitlis)<0:
    print("Nav ievadīts pozitīvs skaitlis")
else:
    for i in skaitlis:
        sum+= int(i)
print(f"Ievadītā skaitļa ciparu summa ir {sum}.")
