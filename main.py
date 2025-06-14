# Kodni bu yerga yozing

from random import randint

print("""===== Loop Lab: Interaktiv Topshiriqlar =====
1. 🎯 Maxfiy sonni toping (Random son o‘yini)
2. 🔄 So‘zni teskari yozish
3. 🔢 Sonlar orasidagi eng kichigini topish
4. 🧮 FizzBuzz o‘yini (1 dan N gacha)
0. ❌ Dasturdan chiqish
=============================================
 """
)

tanlov = int(input("Tanlang:"))
count = 0

if tanlov == 1:
    number = randint(1,20)
    print(number) #sinov uchun
    print("1. 🎯 Maxfiy sonni toping (Random son o'yini")
    while count<5:
        
        taxmin = int(input("random sonni toping = "))
        count+=1
        if number == taxmin:
                print(f"Tabriklaymiz siz {count}-urinishda to'g'ri topdingiz")
                break
        elif taxmin > number:
                print("Siz tanlagan son Katta")    
        elif taxmin < number:
                print("Siz o'ylagan son kichik:")
        elif count == 5 and number == taxmin:
                print("Tabriklaymiz siz to'g'ri topdingiz")
                break
        elif count == 5 and number != taxmin:  
            print(f"Urinishlar soni tugadi to'g'ri javob {number}")      
    else:
        print(f"Urinishlar soni tugadi to'gri javob {number}")
        
elif tanlov == 2:
    
    print("🔄 So'zni teskari yozish")
    
    teskari = ''
    
    text = input("Matnni kiriting:")
    
    for i in range(len(text)-1,-1,-1):
        teskari += text[i]
        
    print(teskari)
    
elif tanlov == 3:
    print(" 🔢 Eng kichik sonni topish")
    for i in range(1,6):
        son = int(input(f"A[{i}] = "))
        if i == 1:
            min = son
        elif son < min:
            min = son
    print(min)

elif tanlov == 4:
    N = int(input("N = "))
    for i in range(1,N+1):
        if i % 3 == 0 and i % 5 == 0 :
            print("FizzBuzz")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
  
elif tanlov == 0 :
    print("Dastur yakunlandi. Xayr!")          