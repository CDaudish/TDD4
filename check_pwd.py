def check_pwd(password):
  if len(password) < 8:
    return False

  if len(password) > 20:
    return False

  isLowerCase = False
  for c in password:
    if c.islower() == True:
      isLowerCase = True
  if isLowerCase == False:
    return False

  isUpperCase = False
  for c in password:
    if c.isupper() == True:
      isUpperCase = True
  if isUpperCase == False:
    return False

  isNumber = False
  for c in password:
    if c.isnumeric() == True:
      isNumber = True
  if isNumber == False:
    return False

  equalSign = False
  for c in password:
    if c == "=":
      equalSign = True


  if equalSign == False:
    return False


  return True
