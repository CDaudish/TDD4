def check_pwd(password):
  if len(password) < 8:
    return False
  if len(password) > 20:
    return False
  return True
