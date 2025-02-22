# Online Shopping Cart
# Class : ShoppingCart
# Attributes : user, product, user_id, in_cart
# Method : add_to_cart(), remove_from_cart(), show_cart()


class ShoppingCart:
    def __init__(self, user, product, user_id, in_cart=True):
        self.user = user
        self.product = product
        self.user_id = user_id
        self.in_cart = in_cart

    def add_to_cart(self):
        if not self.in_cart:
            self.in_cart = True
            print(f"Add {self.product} to cart is successful")
        else:
            print(f"Add {self.product} to cart is failed")

    def remove_from_cart(self, cart):
        if self in cart:
            cart.remove(self)
            print(f"Remove {self.product} from cart is successful")
            return True
        else:
            print(f"Remove {self.product} from cart is failed")
            return False

    def __str__(self):
        return f"{self.user} has {self.product} in cart, User ID: {self.user_id}, In Cart: {self.in_cart}"


def calculate_total(cart):
    for item in cart:
        print(item)


# List of cart items
all_cart = [
    ShoppingCart("Jamal", "RTX 4090", 1),
    ShoppingCart("Charles", "RTX 3080", 2),
    ShoppingCart("Naufal", "RX 6600 XT", 3),
]

# Add to cart
all_cart[1].add_to_cart()

# Remove an item from cart
all_cart[2].remove_from_cart(all_cart)

# Calculate total
calculate_total(all_cart)
