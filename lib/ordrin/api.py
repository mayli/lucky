"""This package is a python wrapper for the ordr.in API. The main developer
documentation for this API is located at http://ordr.in/developers"""
from api_helper import APIHelper, PRODUCTION, TEST

class APIs(object):

  urls = {}

  def __init__(self, api_key, servers=TEST):
    """Sets up this module to make API calls. The first argument is the developer's
    API key and the second specifies which servers should be used.

    Arguments:
    api_key -- The developer's API key
    servers -- How the server URLs should be set. Must be PRODUCTION or TEST.
    """
    self.helper = APIHelper(api_key, servers)

  
  #order endpoints
  
  
  def order_guest(self, rid, em, tray, tip, first_name, last_name, phone, zip, addr, city, state, card_number, card_cvc, card_expiry, card_bill_addr, card_bill_city, card_bill_state, card_bill_zip, card_bill_phone, addr2=None, card_name=None, card_bill_addr2=None, delivery_date=None, delivery_time=None):
    """Arguments:
    rid--Ordr.in's unique restaurant identifier for the restaurant.
    em--The customer's email address
    tray--Represents a tray of menu items in the format '[menu item id]/[qty],[option id],...,[option id]'
    tip--Tip amount in dollars and cents
    first_name--The customer's first name
    last_name--The customer's last name
    phone--The customer's phone number
    zip--The zip code part of the address
    addr--The street address
    city--The city part of the address
    state--The state part of the address
    card_number--Credit card number
    card_cvc--3 or 4 digit security code
    card_expiry--The credit card expiration date.
    card_bill_addr--The credit card's billing street address
    card_bill_city--The credit card's billing city
    card_bill_state--The credit card's billing state
    card_bill_zip--The credit card's billing zip code
    card_bill_phone--The credit card's billing phone number

    Keyword Arguments:
    addr2--The second part of the street address, if needed
    card_name--Full name as it appears on the credit card
    card_bill_addr2--The second part of the credit card's biling street address.


    Either
    delivery_date--Delivery date
    delivery_time--Delivery time
    OR
    delivery_date--Delivery date"""
    return self.helper._call_endpoint('order', 'order_guest', ["rid"], rid=rid, em=em, tray=tray, tip=tip, first_name=first_name, last_name=last_name, phone=phone, zip=zip, addr=addr, city=city, state=state, card_number=card_number, card_cvc=card_cvc, card_expiry=card_expiry, card_bill_addr=card_bill_addr, card_bill_city=card_bill_city, card_bill_state=card_bill_state, card_bill_zip=card_bill_zip, card_bill_phone=card_bill_phone, addr2=addr2, card_name=card_name, card_bill_addr2=card_bill_addr2, delivery_date=delivery_date, delivery_time=delivery_time)
  
  
  def order_user(self, rid, tray, tip, first_name, last_name, email, current_password, phone=None, zip=None, addr=None, addr2=None, city=None, state=None, nick=None, card_name=None, card_number=None, card_cvc=None, card_expiry=None, card_bill_addr=None, card_bill_addr2=None, card_bill_city=None, card_bill_state=None, card_bill_zip=None, card_bill_phone=None, card_nick=None, delivery_date=None, delivery_time=None):
    """Arguments:
    rid--Ordr.in's unique restaurant identifier for the restaurant.
    tray--Represents a tray of menu items in the format '[menu item id]/[qty],[option id],...,[option id]'
    tip--Tip amount in dollars and cents
    first_name--The customer's first name
    last_name--The customer's last name
    email -- The user's email
    current_password -- The user's current password

    Keyword Arguments:


    Either
    phone--The customer's phone number
    zip--The zip code part of the address
    addr--The street address
    addr2--The second part of the street address, if needed
    city--The city part of the address
    state--The state part of the address
    OR
    nick--The delivery location nickname. (From the user's addresses)
    Either
    card_name--Full name as it appears on the credit card
    card_number--Credit card number
    card_cvc--3 or 4 digit security code
    card_expiry--The credit card expiration date.
    card_bill_addr--The credit card's billing street address
    card_bill_addr2--The second part of the credit card's biling street address.
    card_bill_city--The credit card's billing city
    card_bill_state--The credit card's billing state
    card_bill_zip--The credit card's billing zip code
    card_bill_phone--The credit card's billing phone number
    OR
    card_nick--The credit card nickname. (From the user's credit cards)
    Either
    delivery_date--Delivery date
    delivery_time--Delivery time
    OR
    delivery_date--Delivery date"""
    return self.helper._call_endpoint('order', 'order_user', ["rid"], rid=rid, tray=tray, tip=tip, first_name=first_name, last_name=last_name, email=email, current_password=current_password, phone=phone, zip=zip, addr=addr, addr2=addr2, city=city, state=state, nick=nick, card_name=card_name, card_number=card_number, card_cvc=card_cvc, card_expiry=card_expiry, card_bill_addr=card_bill_addr, card_bill_addr2=card_bill_addr2, card_bill_city=card_bill_city, card_bill_state=card_bill_state, card_bill_zip=card_bill_zip, card_bill_phone=card_bill_phone, card_nick=card_nick, delivery_date=delivery_date, delivery_time=delivery_time)
  
  #restaurant endpoints
  
  
  def delivery_check(self, datetime, rid, addr, city, zip):
    """Arguments:
    datetime--Delivery date and time
    rid--Ordr.in's unique restaurant identifier for the restaurant.
    addr--Delivery location street address
    city--Delivery location city
    zip--The zip code part of the address

    Keyword Arguments:

"""
    return self.helper._call_endpoint('restaurant', 'delivery_check', ["rid", "datetime", "zip", "city", "addr"], datetime=datetime, rid=rid, addr=addr, city=city, zip=zip)
  
  
  def delivery_list(self, datetime, addr, city, zip):
    """Arguments:
    datetime--Delivery date and time
    addr--Delivery location street address
    city--Delivery location city
    zip--The zip code part of the address

    Keyword Arguments:

"""
    return self.helper._call_endpoint('restaurant', 'delivery_list', ["datetime", "zip", "city", "addr"], datetime=datetime, addr=addr, city=city, zip=zip)
  
  
  def fee(self, datetime, rid, subtotal, tip, addr, city, zip):
    """Arguments:
    datetime--Delivery date and time
    rid--Ordr.in's unique restaurant identifier for the restaurant.
    subtotal--The cost of all items in the tray in dollars and cents.
    tip--The tip in dollars and cents.
    addr--Delivery location street address
    city--Delivery location city
    zip--The zip code part of the address

    Keyword Arguments:

"""
    return self.helper._call_endpoint('restaurant', 'fee', ["rid", "subtotal", "tip", "datetime", "zip", "city", "addr"], datetime=datetime, rid=rid, subtotal=subtotal, tip=tip, addr=addr, city=city, zip=zip)
  
  
  def restaurant_details(self, rid):
    """Arguments:
    rid--Ordr.in's unique restaurant identifier for the restaurant.

    Keyword Arguments:

"""
    return self.helper._call_endpoint('restaurant', 'restaurant_details', ["rid"], rid=rid)
  
  #user endpoints
  
  
  def change_password(self, email, password, current_password):
    """Arguments:
    email--The user's email address
    password--The user's new password
    current_password -- The user's current password

    Keyword Arguments:

"""
    return self.helper._call_endpoint('user', 'change_password', ["email"], email=email, password=password, current_password=current_password)
  
  
  def create_account(self, email, pw, first_name, last_name):
    """Arguments:
    email--The user's email address
    pw--The user's password
    first_name--The user's first name
    last_name--The user's last name

    Keyword Arguments:

"""
    return self.helper._call_endpoint('user', 'create_account', ["email"], email=email, pw=pw, first_name=first_name, last_name=last_name)
  
  
  def create_addr(self, email, nick, phone, zip, addr, city, state, current_password, addr2=None):
    """Arguments:
    email--The user's email address
    nick--The nickname of this address
    phone--The customer's phone number
    zip--The zip code part of the address
    addr--The street address
    city--The city part of the address
    state--The state part of the address
    current_password -- The user's current password

    Keyword Arguments:
    addr2--The second part of the street address, if needed

"""
    return self.helper._call_endpoint('user', 'create_addr', ["email", "nick"], email=email, nick=nick, phone=phone, zip=zip, addr=addr, city=city, state=state, current_password=current_password, addr2=addr2)
  
  
  def create_cc(self, email, nick, card_number, card_cvc, card_expiry, bill_addr, bill_city, bill_state, bill_zip, bill_phone, current_password, bill_addr2=None):
    """Arguments:
    email--The user's email address
    nick--The nickname of this address
    card_number--Credit card number
    card_cvc--3 or 4 digit security code
    card_expiry--The credit card expiration date.
    bill_addr--The credit card's billing street address
    bill_city--The credit card's billing city
    bill_state--The credit card's billing state
    bill_zip--The credit card's billing zip code
    bill_phone--The credit card's billing phone number
    current_password -- The user's current password

    Keyword Arguments:
    bill_addr2--The second part of the credit card's biling street address.

"""
    return self.helper._call_endpoint('user', 'create_cc', ["email", "nick"], email=email, nick=nick, card_number=card_number, card_cvc=card_cvc, card_expiry=card_expiry, bill_addr=bill_addr, bill_city=bill_city, bill_state=bill_state, bill_zip=bill_zip, bill_phone=bill_phone, current_password=current_password, bill_addr2=bill_addr2)
  
  
  def delete_addr(self, email, nick, current_password):
    """Arguments:
    email--The user's email address
    nick--The nickname of this address
    current_password -- The user's current password

    Keyword Arguments:

"""
    return self.helper._call_endpoint('user', 'delete_addr', ["email", "nick"], email=email, nick=nick, current_password=current_password)
  
  
  def delete_cc(self, email, nick, current_password):
    """Arguments:
    email--The user's email address
    nick--The nickname of this address
    current_password -- The user's current password

    Keyword Arguments:

"""
    return self.helper._call_endpoint('user', 'delete_cc', ["email", "nick"], email=email, nick=nick, current_password=current_password)
  
  
  def get_account_info(self, email, current_password):
    """Arguments:
    email--The user's email address
    current_password -- The user's current password

    Keyword Arguments:

"""
    return self.helper._call_endpoint('user', 'get_account_info', ["email"], email=email, current_password=current_password)
  
  
  def get_all_saved_addrs(self, email, current_password):
    """Arguments:
    email--The user's email address
    current_password -- The user's current password

    Keyword Arguments:

"""
    return self.helper._call_endpoint('user', 'get_all_saved_addrs', ["email"], email=email, current_password=current_password)
  
  
  def get_all_saved_ccs(self, email, current_password):
    """Arguments:
    email--The user's email address
    current_password -- The user's current password

    Keyword Arguments:

"""
    return self.helper._call_endpoint('user', 'get_all_saved_ccs', ["email"], email=email, current_password=current_password)
  
  
  def get_order(self, email, oid, current_password):
    """Arguments:
    email--The user's email address
    oid--Ordr.in's unique order id number.
    current_password -- The user's current password

    Keyword Arguments:

"""
    return self.helper._call_endpoint('user', 'get_order', ["email", "oid"], email=email, oid=oid, current_password=current_password)
  
  
  def get_order_history(self, email, current_password):
    """Arguments:
    email--The user's email address
    current_password -- The user's current password

    Keyword Arguments:

"""
    return self.helper._call_endpoint('user', 'get_order_history', ["email"], email=email, current_password=current_password)
  
  
  def get_saved_addr(self, email, nick, current_password):
    """Arguments:
    email--The user's email address
    nick--The nickname of this address
    current_password -- The user's current password

    Keyword Arguments:

"""
    return self.helper._call_endpoint('user', 'get_saved_addr', ["email", "nick"], email=email, nick=nick, current_password=current_password)
  
  
  def get_saved_cc(self, email, nick, current_password):
    """Arguments:
    email--The user's email address
    nick--The nickname of this address
    current_password -- The user's current password

    Keyword Arguments:

"""
    return self.helper._call_endpoint('user', 'get_saved_cc', ["email", "nick"], email=email, nick=nick, current_password=current_password)
  