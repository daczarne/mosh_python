# Absolut import statement
from ecommerce.customer import contact

# Relative import statement
from ..customer import contact

contact.contact_customer()


def calc_tax():
    print("Calculate the tax value.")


def calc_shipping():
    print("Calculate the shipping cost.")
