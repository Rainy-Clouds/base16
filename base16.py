hexadecimal = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

conversion  = input("Convert from or to base 16? (type from or to): ")

if conversion == "to":
  number = int(input("Enter a number: "))

  i = 0
  digits = []
  while True:
    if number / 16 ** i < 1:
      break
    digits.append(i)
    i += 1

  digits.reverse()
  decimal_list = []
  for digit in digits:
    decimal_list.append(number // (16 ** digit))
    number -= decimal_list[len(decimal_list) - 1] * 16 ** digit

  final_list = []
  for num in decimal_list:
    final_list.append(hexadecimal[num])

  final = "".join(final_list)
  print(final)

elif conversion == "from":
  number = input("Enter a hexadecimal value: ")

  number_list = list(number)
  number_list.reverse()

  final = 0
  for x in range(len(number_list)):
    final += hexadecimal.index(number_list[x]) * 16 ** x

  print(final)