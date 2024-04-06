"""Computes immediate cost given order."""

TAQUERIA_MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
DEFAULT_VALUE = 0.0


def customer_order() -> None:
    """Provides an updated customer order."""
    total_cost = 0

    while True:
        try:
            order = input("Item: ").title()
            total_cost += TAQUERIA_MENU.get(order, DEFAULT_VALUE)

            print(f"Total: ${total_cost:.2f}")

        except EOFError:
            print(total_cost)
            break


if __name__ == "__main__":
    customer_order()
