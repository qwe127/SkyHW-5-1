from request import Request
from courier import Courier
from exception import BaseError


from shop import Shop
from store import Store

shop = Shop(
    items={
        'печеньки': 3,
        'собачки': 2,
        'коробки': 5,
    },
)

store = Store(
    items={
        'печеньки': 3,
        'собачки': 2,
        'коробки': 5,
    },
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    while True:
        for storage_name in storages:
            print(f'В {storage_name} хранится: {storages[storage_name].get_items()}')
        user_input = input("input: Доставить 3 печеньки из склад в магазин\n")

        if user_input in 'stop':
            break
        try:
            request = Request(request_str=user_input, storages=storages)
        except BaseError as error:
            print(error.message)
            continue
        courier = Courier(request=request, storages=storages)
        try:
            courier.move()
        except BaseError as error:
            courier.cancel()
            print(error.message)


if __name__ == '__main__':
    main()
