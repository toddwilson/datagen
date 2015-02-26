from random import uniform
from datagen.types import register_type, type_arg
from datagen import main


@type_arg("price")  # Use the same name as the type defined in reg_type()
def price_argument(arg):  # This method is passed the contents of what's in price[]
    return int(arg)  # This will get passed to price() when iterating


@register_type("price")  # the decorator sets the name of the type
def price(max_price):  # the method must accept one argument (even if not used)
    return round(uniform(0, max_price), 2)


if __name__ == '__main__':
    main()
