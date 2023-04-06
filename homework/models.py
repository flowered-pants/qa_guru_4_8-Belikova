from dateclasses import dateclass
# Тестируем классы интернет-магазина
# Вам нужно реализовать и протестировать классы интернет-магазина.
# Все места, которые нужно дописать как в тестах, так и классах, отмечены `# TODO`.
#
# При реализации обращайте внимание на типизацию аргументов методов и возвращаемых значений.
# Так же обратите внимание на организацию тестов в файле с тестами:
# - Тесты сгруппированы по классу, который они тестируют.
# - Каждый тест называется именем соответствующего ему метода.
#
# Вы можете начать как с реализации классов, так и с тестов.


# Дополнительные вопросы:
# 1. С чего проще начать выполнение домашнего задания: с тестов или с реализации классов?
# 2. Почему для хранения товаров в корзине используется словарь, а не список?
# 3. Зачем нужен __hash__ в классе Product? Изучите этот метод и объясните, почему он нужен.

@dataclass
class Product:
    """
    Класс продукта без реализации методов
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        if self.quantity >= quantity:
            return True
        else:
            print('Недостаточное количество товара на складе')
            return False
        """
        Верните True если количество продукта больше или равно запрашиваемому
        и False в обратном случае
        """

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
            return (f'Вы купили {quantity} товара {self.name}')
        else:
            raise ValueError('К сожалению, покупка не удалась')
        raise NotImplementedError

    def __hash__(self):
        return hash(self.name + self.description)


    class Cart:
        """
        Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
        TODO реализуйте все методы класса
        """

        # Словарь продуктов и их количество в корзине
        products: dict[Product, int]

        def __init__(self):
            # По-умолчанию корзина пустая
            self.products = {}

        def add_product(self, product: Product, quantity=1):
            """
            Метод добавления продукта в корзину.
            Если продукт уже есть в корзине, то увеличиваем количество
            """
            if product in self.products:
                self.products[product] += quantity
            else:
                self.products[product] = quantity
            return None

        def remove_product(self, product: Product, quantity=None):
            """
            Метод удаления продукта из корзины.
            Если quantity не передан, то удаляется вся позиция
            Если quantity больше, чем количество продуктов в позиции, то удаляется вся позиция
            """
            if quantity=None:


        def clear(self):

            raise NotImplementedError

        def get_total_price(self) -> float:
            raise NotImplementedError

        def buy(self):
            """
            Метод покупки.
            Учтите, что товаров может не хватать на складе.
            В этом случае нужно выбросить исключение ValueError
            """
            raise NotImplementedError