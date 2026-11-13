print('welcom to place of the rabit🐇 ')
place_a=['🌿','🌿','🌿']
place_b=['🌿','🌿','🌿']
place_c=['🌿','🌿','🌿']
print(place_a)
print(place_b)
print(place_c)
numero=input("where should the rabit go?\n pleas chos a row and a colum:    ")
if numero[0]=='1':
 if numero[1]=='1':
    place_a[0]='🐇'
 elif numero[1]=='2':
    place_a[1]='🐇'
 elif numero[1]=='3':
    place_a[2]='🐇'
 else:
    print('invaliable choice')
elif numero[0]=='2':
 if numero[1]=='1':
    place_b[0]='🐇'
 elif numero[1]=='2':
    place_b[1]='🐇'
 elif numero[1]=='3':
    place_b[2]='🐇'
 else:
    print('invaliable choice')
elif numero[0]=='3':
 if numero[1]=='1':
    place_c[0]='🐇'
 elif numero[1]=='2':
    place_c[1]='🐇'
 elif numero[1]=='3':
    place_c[2]='🐇'
 else:
    print('invaliable choice')
else:
    print('invaliable choice')
print(place_a)
print(place_b)
print(place_c)
