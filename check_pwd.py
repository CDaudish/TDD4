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
  return True
