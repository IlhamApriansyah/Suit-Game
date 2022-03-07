import random


print("Pemenang dari suit game berdasarkan peraturan ini : \n"
								+"Batu vs Kertas -> Kertas menang \n"
								+ "Batu vs Gunting -> Batu menang \n"
								+"Kertas vs Gunting -> Gunting menang \n")

while True:
	print("Masukan pilihan \n 1 untuk batu, \n 2 untuk kertas, dan \n 3 untuk gunting \n")
	

	choice = int(input("Giliranmu : "))

	while choice > 3 or choice < 1:
		choice = int(input("Masukan pilihanmu : "))
		

	if choice == 1:
		choice_name = 'Batu'
	elif choice == 2:
		choice_name = 'Kertas'
	else:
		choice_name = 'Gunting'
		
	
	print("Pilihanmu adalah : " + choice_name)
	print("\nsekarang giliran AI.......")

	
	comp_choice = random.randint(1, 3)
	
	
	while comp_choice == choice:
		comp_choice = random.randint(1, 3)


	if comp_choice == 1:
		comp_choice_name = 'Batu'
	elif comp_choice == 2:
		comp_choice_name = 'Kertas'
	else:
		comp_choice_name = 'Gunting'
		
	print("yang dipilih AI adalah: " + comp_choice_name)

	print(choice_name + " vs " + comp_choice_name)


	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )):
		print("\nkertas menang ", end = "")
		result = "kertas"
		
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)):
		print("\nbatu menang", end = "")
		result = "batu"
	else:
		print("\ngunting menang", end = "")
		result = "gunting"

	if result == choice_name:
		print("\n<== Kamu menang ==>")
	else:
		print("\n<== AI menang ==>")
		
	print("Mau main lagi? (Y/T)")
	ans = input()


	if ans == 't' or ans == 'T':
		break
	
print("\nTerimakasih sudah mau bermain!!")
