import price_info as code

def test_total():
 tc = 0
 for x in code.price_list.keys():
  if x in code.quantity_list:
   tc =code.price_list[x]*code.quantity_list[x]+tc
 assert(code.total_cost_shopping()==tc)
 

def test_cof():
 flag = True
 for x in code.price_list.keys():
  if x in code.quantity_list:
   if code.cost_of_fruits(x, code.quantity_list[x]) != code.price_list[x]*code.quantity_list[x]:
    flag = False
  assert(flag)
   

