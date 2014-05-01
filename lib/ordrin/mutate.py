import hashlib

def sha256(value):
  return hashlib.sha256(value).hexdigest()

def state(value):
  return value.upper()

def phone(value):
  phone_number = str(value)
  #strips out everything but digits from the phone number
  phone = ''.join(c for c in value if c in '0123456789')
  if len(phone)==10:
    return '{}{}{}-{}{}{}-{}{}{}{}'.format(*phone)
  else:
    raise ValueError("Phone number '{}' did not have exactly 10 digits".format(value))

def identity(value):
  return value

mutators = {'sha256' : sha256,
            'state' : state,
            'phone' : phone,
            'identity' : identity}
