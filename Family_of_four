def put_family_in(n ,s):
  if n>=1 and n<=50:
    r = 0
    seats = s.split()
    print("Reserved seats: ", seats)
    col = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K"]
    Paterns = ["BCDE", "DEFG", "FGHJ"]
    k = []
    
    for i in range(1, n+1):
      for x in col:
        k.append(str(i)+str(x))
        
    for i in k:
      if i in seats:
        k.pop(k.index(i))
       
    thisdict = {}
    for i in range(1, n+1):
      thisdict.update({i:''})
      for y in k:
        if y.strip("ABCDEFGHJK") == str(i):
          thisdict[i] = thisdict[i] + y.strip("0123456789")
    print("Available row/seat: ", thisdict)
         
    for y in thisdict.values():
      if Paterns[0] in y and Paterns[1] in y:
        r += 2
        continue
      elif Paterns[0] in y or Paterns[1] in y or Paterns[2] in y:
        r += 1
    
    print(r, "families of 4 can fit")  
  else:
    print("Please, correct number of rows (n)!")

put_family_in(6, "1A 2F 1C")