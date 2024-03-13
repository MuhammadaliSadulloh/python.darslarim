#6-dars(sonlar)
r=float(input('radiusni kiriting r='))
PI=3.1465658
l=(2*PI*r)
s=(PI*(r**2))
print('Aylana uzunligi=',l)
print('Aylana yuzi=',s)
print('PI=',PI)



#7-dars(1)
q=['','bexi','nok']
q[1]=('banan')
q[0]=('xurmo')
q[-2]=('shaftoli')
q.append('tarvuz')
q.insert(2,'anjir')
q.insert(5,'o`rik')
print(q)



#7-dars(2)
cars=[]
cars.append('malibu')
cars.append('captiva')
cars.append('nexia')
cars.append('gentra')
cars.append('cobalt')
#del cars[-2]
cars.remove('captiva')
print(cars)



#7-dars(ro'yxatlar)  (umumiy)
cars=['bmw E39 M5','malibu','captiva','nexia','gentra','cobalt']
cars.append('audi')
#append bu lug`atning oxiriga o`zgaruvchi qo`shadi
cars[-4]='bmw F90 M5'
print(cars)
cars.insert(2,'mersedez benz')
cars.insert(5,'ferrari')
#insert bu kiritilgan index o`rnida yangi o`zgaruvchi qo`shadi
print(cars)
print(cars[6].title())
#title o`zgaruvchining bosh harfini katta harflar bilan yozib beradi
cars.remove('mersedez benz')
#remove bu aytilgan o`zgaruvchini lug`atdan chiqarib tashlaydi
print(cars[7].title())
cars[1]='bmw e30 M5'
#sort bu o`zgaruvchilarni alifbo tartibida tartiblayi
cars.sort()
print(cars)



# 8-dars(ro'yxatlar bilan ishlash)
davlatlar = ['uzb', 'aqsh', 'vetnam', 'yaponiya', 'koreya', 'germaniya']
print(davlatlar)
print('davlatlar soni:', len(davlatlar))
# len>>>elementlar sonini
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
# reverse ro'yxat elemntlarini teskari tartiblaydi
print(davlatlar)
sonlar = [10, 15, 76, 9843, 27, 13, 766, 3, 422, 86359, 299, 37, 32920, 5, 9, 7, 3, 2, 1]
print(sonlar)
sonlar.sort()
print(sonlar)
print(sorted(sonlar, reverse=True))
print('120<1200gacha juft sonlar', list(range(120, 1201, 2)))
print('sonlar yig`indisi:', sum(sonlar))
print('eng kattasidan eng kichigini ayirmasi:', (max(sonlar) - min(sonlar)))
print('ro`yxat elementlar soni:', len(sonlar))
print(sonlar[0:5])
taomlar = ['osh', 'sho`rvo', 'kavob', 'tuxum', 'sut']
nonushta = taomlar[3:5]
nonushta.append('shirinliklar')
nonushta.append('choy')
print('taomlar:', taomlar)
print('nonushtaga:', nonushta)
nonushta[0] = 'qaymoq va non'
nonushta = tuple(nonushta)
#tuple ro'yxatni o'zgarmas royxatga aylantiradi
print(nonushta)



#9-dars(for takrorlash operatori)
dustlar=['Behruz','Adiz','Bekzod','Suxrob','Shoxjahon']
for sukin in dustlar:
    print(f"ko`tingda tursiging yo`g`u isming {sukin}")
    print('e chichqoq')
print(f'kod {len(dustlar) } marta takrorlandi')
sonlar=list(range(11,101,2))
#range harakatni ma'lum bir necha marta takrorlaydi
print(sonlar)
for daraja in sonlar:
#for takrorlash operatori
    print(f"{daraja} ning kubi {daraja**3} ga teng")
print('')
print(' ')
kinolar=[]
a=int(input('yoqtirgan kinolaringiz nechta?:'))
for kino in range(a):
    kinolar.append(input(f"yoqtirgan {kino+1}-kinoyingizni kiriting:"))
print(kinolar)
odamlar=[]
a=int(input('bugun nechta odam bilan ko`rishdiz?:'))
for odam in range(a):
    odamlar.append(input(f" {odam+1}-sining ismi:"))
print(odamlar)



# 10-dars (if-else)
cars=['toyota','mazda','hyundai','gm','bmw']
for a in cars:
    if a=="gm" or a=='bmw':
        print(a.upper())
    else:
        print(a.title())
a=input('ismingiz nima?:')
if a.lower()=='behruz':
    print('assalomaleykuum bratimm qandayssiiz')
else:print('hormang aka')
b=int(input(f'{a} aka xoxlamagan sonizni kiriting:'))
if b<=0:
    c=int(input('ex musbat son kiritishingiz kerak edi. Musbat son kiriting akam:'))
    if c<=0:
        print("idinaxuy!")
    else:
        print(f'{c}ning ildizi',(c**(1/2)),'ga teng aka')
else:
    print(f'{b}ning ildizi',(b**(1/2)),'ga teng aka')
a=int(input("yoshiz nechchida?:"))
if a>=18:



#11-dars(if-elif-else ketma-ketligi)
a=int(input('juft son kiriting'))
if a%2==0:print('rahamat aka!')
else:print('bu juft son emas aka! ')
b=int(input('yoshiz nechchida'))
if b<=4 or b>=60:
    narx='tekin 0'
elif b<=18:
    narx=10000
else:
    narx=20000
print(f"sizga chipta {narx} so'm")
print('ikkita son o`ylang!')
a=int(input('birinchi a sonni kiriting!:'))
b=int(input('ikkinchi b sonni kiriting!:'))
if a==b:
    print("a=b")
elif a>b:
    print("a>b")
else:
    print("a<b")


mahsulot=['qalam','ruchka','daftar','sir','non','ketchup','olma','nok','apelsin','saqich']
savat=[]
for m in range(5):
    savat.append(input('mahsulotlarni kiriting!:'))
print(savat)
for narsa in savat:
    if narsa in mahsulot:
        print(f'bizda {narsa} bor')
    else:
        print(f'kechirasiz bizda {narsa} yo`q')


foydalanuvchilar=['muhammadali','abror','sarvar','dilshod','bekzod']
login=input('yangi login kiriting!:')
if login in foydalanuvchilar:
    print('login band yangi login kiriting!')
else:
    print(f'xush kelibsiz {login}')


b=int(input('biror butun son kiriting!:'))
for a in range(2,11):
    if not b%a:
        print(f'{b} {a}ga bo`linadi!')