# Packages also use to edit files such as modules.

'''Women's, men's, and children's sections = packages
   T-shirts, jackets, and shoes = modules'''

# I opened new folder called 'ecommerce' and added __init__.py and shipping.py files.
# We can import entire module or one of one function/class.

####### 1. IMPORT ENTIRE MODULE #######

import ecommerce.shipping
ecommerce.shipping.calc_shipping()

#Code is too long so we need to change ⬇️

from ecommerce.shipping import calc_shipping
calc_shipping()

####### OR ########

from ecommerce import shipping
shipping.calc_shipping()





 