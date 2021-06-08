class Data():
    def __init__(self, values):
        self.names = values[::3]

        del values[::3]

        self.buy = values[::2]
        self.sell = values[1::2]

        self.best_buy_value = max(self.buy)
        self.best_sell_value = min(self.sell)

    def get_all_list(self):
        message = ''
        i = 0
        while i < len(self.names):
            message += f'{self.names[i]}: \nПродажа: {self.buy[i]} \nПокупка: {self.sell[i]} \n\n'
            i += 1

        message = message.rstrip()
        return message

    def __get_best_values(self, values, best_value):
        message = ''
        i = 0

        while i < len(values):
            if values[i] == best_value:
                message += f'{self.names[i]} - {best_value}\n'
            i += 1

        message = message.rstrip()
        return message

    def get_best_buy_value(self):
        return self.__get_best_values(self.buy, self.best_buy_value)

    def get_best_sell_value(self):
        return self.__get_best_values(self.sell, self.best_sell_value)