print('welcom to place of the rabit🐇 ')
filed=[['🌿','🌿','🌿'],['🌿','🌿','🌿'],['🌿','🌿','🌿']]
print(f' {filed[0]} \n {filed[1]} \n {filed[2]}')
numero=input("where should the rabit go?\n pleas chos a row and a colum:    ")
row=int(numero[0])
colum=int(numero[1])
filed[row-1][colum-1]="🐇"
print(f' {filed[0]} \n {filed[1]} \n {filed[2]}')