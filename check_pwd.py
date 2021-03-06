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

  minusSign = False
  for c in password:
    if c == "-":
      minusSign = True

  plusSign = False
  for c in password:
    if c == "+":
      plusSign = True

  underScore = False
  for c in password:
    if c == "_":
      underScore = True

  rightBrac = False
  for c in password:
    if c == ")":
      rightBrac = True

  leftBrac = False
  for c in password:
    if c == "(":
      leftBrac = True

  star = False
  for c in password:
    if c == "*":
      star = True

  ampersand = False
  for c in password:
    if c == "&":
      ampersand = True

  upArrow = False
  for c in password:
    if c == "^":
      upArrow = True

  remainder = False
  for c in password:
    if c == "%":
      remainder = True

  moneySign = False
  for c in password:
    if c == "$":
      moneySign = True

  hashtag = False
  for c in password:
    if c == "#":
      hashtag = True

  atSign = False
  for c in password:
    if c == "@":
      atSign = True

  exclaim = False
  for c in password:
    if c == "!":
      exclaim = True

  tilda = False
  for c in password:
    if c == "`":
      tilda = True

  negate = False
  for c in password:
    if c == "~":
      negate = True



  if equalSign == False and minusSign == False and plusSign == False and underScore == False and  \
          rightBrac == False and leftBrac == False and star == False and ampersand == False and \
          upArrow == False and remainder == False and moneySign == False and hashtag == False and \
          atSign == False and exclaim == False and tilda == False and negate == False:
    return False

  validChar = ['~','`','!','@','#','$','%','^','&','*','(',')','_','+','-','=']
  for c in password:
    if c.isnumeric() == False and c.islower() == False and c.isupper() == False and c not in validChar:
        return False



  return True
