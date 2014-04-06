from bottle import route, run, template, request
import bottle
import ordrin
import random
from pprint import pprint
ORDIN_KEY = 'wv5pA16bxmYnIjGw06yvcV14fD6qYt5RxLZU28jkga4'

# return flaterned menu list, id stored in flat_id as ['l1_id','child_id', ...]
def flat_item(menulist):
    this_level=[]
    for menu in menulist:
        # pprint(menu)
        # pprint(menu.keys())
        this_id = menu['id']
        this_name = menu['name']
        if 'children' in menu:
            for item in flat_item(menu['children']):
                item['flat_id'].insert(0, this_id)
                item['flat_name'] = '/'.join([this_name, item['name']])
                this_level.append(item)
        else: # last level
            item = menu
            item['flat_id'] = [item['id']]
            item['flat_name'] = item['name']
            this_level.append(item)
    return this_level

@route('/', method=['GET', 'POST'])
def index():
    return open('index.html').read()

@route('/gen_order', method=['GET', 'POST'])
def gen_order():
    ordrin_api = ordrin.APIs(ORDIN_KEY, ordrin.TEST)

    # required
    addr = request.forms.get('addr', '21 college dr, stony brook')
    city = request.forms.get('city', 'newyork')
    azip = request.forms.get('zip', '11790')

    # opt
    item_number = int(request.forms.get('item_number', 4))
    item_multiply = int(request.forms.get('item_multiply', 1))
    #item_number *= item_multiply

    price_limit = int(request.forms.get('price_limit', 25))
    price_multiply = int(request.forms.get('price_multiply', 1))
    #price_limit *= price_multiply

    dlist = ordrin_api.delivery_list('ASAP', addr, city, azip)
    #pprint( dlist)
    #dlist = [entry for entry in dlist if entry['is_delivering']]
    dlist = [entry for entry in dlist]

    random.shuffle(dlist)
    #pprint(dlist[0])
    # random choose one restaurant

    rentry = dlist[0]
    rid = rentry['id']
    print rid 

    details = ordrin_api.restaurant_details(str(rid))
    #pprint(details)
    menu = flat_item(details['menu'])
    random.shuffle(menu)
    order = []
    amount = 0
    trays = []
    for o in menu:
        if amount > rentry['services']['deliver']['mino']:
            break
        if float(o['price'])<0.5:
            continue
        o['item_multiply'] = item_multiply
        o['tray'] = '%s/%d'%(o['flat_id'][0], item_multiply)
        if o['flat_id'][:1]:
             o['tray'] += ','
             o['tray'] += ','.join(o['flat_id'][:1])
        trays.append(o['tray'])
        amount += float(o['price'])*item_multiply
        order.append(o)
    #order = menu[:2]
    return {'restaurant':rentry, 'menu':'menu', 'order':order, 'amount': '%0.2f'%amount, 'trays':'+'.join(trays)}
    #return ordrin.delivery_check('ASAP', )

@route('/post_order', method=['GET', 'POST'])
def post_order():
    ordrin_api = ordrin.APIs(ORDIN_KEY, ordrin.TEST)
    for field in [
        'rid', 'em', 'tray',

        'tip',
        'first_name',
        'last_name',
        'phone',
        
        'zip',
        'addr',
        'city',
        'state']:
        if field not in request.forms:
            return {'error':'missing parameter %s'%fe}
    try:
        ret = ordrin_api.order_guest(
            rid = request.forms.get('rid'),
            em = request.forms.get('em'), 
            tray = request.forms.get('tray'), 
            tip = request.forms.get('tip'), 
            first_name = request.forms.get('first_name'), 
            last_name = request.forms.get('last_name'), 
            phone = request.forms.get('phone'), 
            zip = request.forms.get('zip'), 
            addr = request.forms.get('addr'), 
            city = request.forms.get('city'), 
            state = request.forms.get('state'), 
            card_number='4111111111111111', 
            card_cvc='123', 
            card_expiry='02/2016', 
            card_bill_addr='College Station', 
            card_bill_city='TX', 
            card_bill_state='TX', 
            card_bill_zip='77840', 
            card_bill_phone='2345678901', 
            addr2=None, 
            card_name=None, 
            card_bill_addr2=None, 
            delivery_date='ASAP')
        return ret
    except Exception, e:
        print 'fixme!', e
        return {"error":'success'}

@route('/src/<path:path>')
def callback(path):
    return bottle.static_file(path, root='/home/mayli/lucky/src/')

run(host='0.0.0.0', port=8888, debug=True, reloader=True, autojson=True)
