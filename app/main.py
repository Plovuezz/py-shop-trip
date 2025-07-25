from app.customer import process_data, get_data_from_json


def shop_trip() -> None:

    data = get_data_from_json("app/config.json")
    fuel_price, customers_list, shops_list = process_data(data)

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")

        min_cost = None
        shop_to_go = None

        for shop in shops_list:
            cost = customer.calculate_trip_price(shop, fuel_price)
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs{cost: 0.2f}")
            if min_cost is None or cost < min_cost:
                min_cost = cost
                shop_to_go = shop

        if customer.money < min_cost:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        print(f"{customer.name} rides to {shop_to_go.name}", end="\n\n")
        customer.buy_products(shop_to_go)

        print(f"{customer.name} rides home")
        amount_left = round(customer.money - min_cost, 2)
        print(f"{customer.name} now has {amount_left} dollars", end="\n\n")


if __name__ == "__main__":
    shop_trip()
