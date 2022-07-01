from typing import Any, List


class Order:
    def __init__(self, id: str):
        self._id = id

    @property
    def id(self) -> str:
        return self._id


class AechList:
    def __init__(self):
        self._list = list()
        self._size = len(self._list)

    def values(self) -> list:
        return self._list

    def append(self, value) -> None:
        self._list.append(value)
        self._update_size()

    def pop(self) -> Any:
        value = self._list.pop()
        self._update_size()
        return value

    def _update_size(self):
        self._size = len(self._list)

    @property
    def size(self) -> int:
        return self._size


class Record:
    def __init__(self):
        self._orders: AechList[Order] = AechList()

    def record(self, order: Order) -> None:
        self._orders.append(order)

    def get_last(self, orders: int) -> list:
        ordered_orders = AechList()

        if orders <= self._orders.size:
            for _ in range(orders):
                ordered_orders.append(self._orders.pop())

        return ordered_orders.values()


def print_orders(orders: List[Order]) -> None:
    if len(orders) == 0:
        print("NULL")
        return

    for order in orders:
        print(order.id, end=" ")
    print("", end="\n")


if __name__ == "__main__":
    orders = Record()

    orders.record(Order("1"))
    orders.record(Order("2"))
    orders.record(Order("3"))
    orders.record(Order("4"))
    orders.record(Order("5"))
    orders.record(Order("6"))
    orders.record(Order("7"))
    orders.record(Order("8"))
    orders.record(Order("9"))

    ordered_orders = orders.get_last(10)
    print_orders(ordered_orders)
    ordered_orders = orders.get_last(9)
    print_orders(ordered_orders)
    ordered_orders = orders.get_last(1)
    print_orders(ordered_orders)
    ordered_orders = orders.get_last(0)
    print_orders(ordered_orders)

    exit(0)
