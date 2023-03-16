bop = int(input("what size do you want?"))
for i in range(bop + 1, 0, -1):
  for j in range(0, i -1):
        print('  ', end='    #')
  print("#")