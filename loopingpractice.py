for hour in range(1,13):

  for min in range(0,60):
    if min < 10:
      print(f"{hour}:0{min}")
    else:
      print(f"{hour}:{min}")
