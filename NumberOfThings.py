def how_many(the_list):
  verb = 'are'
  if the_list[0] == 1 :
    verb = 'is'
  return f"There {verb} {the_list[0]} {the_list[1]}."
  
print(how_many([5, "trinket"]))
print(how_many([1, "king"]))