#Uzraksti programmu, kas pieprasa no lietotaja ievadit tris lenkus (kas varetu piederet vienam tristurim) un ar funkcijas palidzibu parbauda, vai sie lenki ir derigi tristura veidosanai.
def lenkuParbaude(len1,len2,len3):
  rezultats = False
  if len1+len2+len3==180:
    rezultats = True
  return rezultats

len1 = int(input("Ievadiet 1.lenki: "))
len2 = int(input("Ievadiet 2.lenki: "))
len3 = int(input("Ievadiet 3.lenki: "))
rez = lenkuParbaude(len1,len2,len3)
if rez:
  print("Tristuris eksiste!")
else:
  print("Tristuris neeksiste!")
  