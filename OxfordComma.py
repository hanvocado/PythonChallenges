def commafy(items):
  if len(items) == 0 :
      return ''
  elif len(items) == 1 :
      return items[0]
  elif len(items) == 2 :
      return f"{items[0]} and {items[1]}"
  else :
      comma_seperated = ', '.join(items[:-1])
      return f"{comma_seperated}, and {items[-1]}"
  
print(commafy(["trinket", "learning", "fun"]))
print(commafy(["one", "two"]))
print(commafy([]))
print(commafy(["lions", "tigers", "bears"]))
