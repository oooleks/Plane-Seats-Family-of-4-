def put_family_in(n ,s):
  if n>=1 and n<=50:
    r = 0
    seats = s.split()
    print("Reserved seats: ", seats)
    col = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K"]
    Paterns = ["BCDE", "DEFG", "FGHJ"]
    thisdict = {}

    for i in range(1, n+1):
      thisdict.update({i:''})
      for x in col:
        if str(i)+str(x) not in seats:
          thisdict[i] = thisdict[i] + x
    print("Available row/seat: ", thisdict)
         
    for y in thisdict.values():
      if Paterns[0] in y and Paterns[1] in y:
        r += 2
        continue
      elif Paterns[0] in y or Paterns[1] in y or Paterns[2] in y:
        r += 1
    
    print(r, "families of 4 can be seated")  
  else:
    print("Please, correct number of rows (n)!")

put_family_in(2, "1A 2F 1C")
