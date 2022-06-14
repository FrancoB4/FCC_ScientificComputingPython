def raw(operation):
    amount = str(float(operation['amount']))
    description = operation['description']

    if len(description) > 23:
        description = description[:23]
    elif len(description) < 23:
        description += ' ' * (23 - len(description))

    if len(amount.split('.')[1]) < 2:
        amount += '0'

    aligned_amount = ' ' * (7 - len(amount)) + amount if len(amount) <= 7 else amount[::-1][:7][::-1]

    return f'\n{description}{aligned_amount}'


class Category:
    """Budget Category to manage expenses and transactions

    Attributes:
        category (str): Name of the category
    """

    def __init__(self, category: str):
        self.category = category
        self.ledger = []

    def __str__(self):
        space = int((30 - len(self.category)) / 2)
        exit_string = '*' * space + self.category + '*' * space
        while len(exit_string) < 30:
            exit_string += '*'

        for operation in self.ledger:
            exit_string += raw(operation)

        exit_string += '\nTotal: ' + str(self.get_balance()) + ' '
        return exit_string

    def deposit(self, amount: (float | int), description: str = ''):
        """Add an amount of money to the category."""
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount: (float | int), description: str = '') -> bool:
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        funds = 0
        for operation in self.ledger:
            funds += operation['amount']
        return funds

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            other_category.ledger.append({'amount': amount, 'description': f'Transfer from {self.category}'})
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {other_category.category}'})
            return True
        return False

    def check_funds(self, amount):
        funds = self.get_balance()

        if funds >= amount:
            return True
        return False


def create_spend_chart(categories: list[Category], sort: bool = False) -> str:
    """Shows a graphic with the different percentages spent by categories

    Args:
        categories (list): A list with Category instances which will be showed in the graph.
        sort (bool): True if you want the chart to display categories in descending order.
    """
    categories_data = []
    total_spent = 0
    max_len = 0
    categories_len = len(categories)
    exit_rows = ['Percentage spent by category']

    for category in categories:

        if len(category.category) > max_len:
            max_len = len(category.category)  # Set the length of the longest category name

        spent = 0
        for operation in category.ledger:
            if operation['amount'] < 0:
                spent -= operation['amount']

        total_spent += spent  # Add each withdraw from each category to the total.

        # Save the spend data for each category.
        categories_data.append({'category': category.category, 'spent': spent})

    for category in categories_data:
        # Save the percentage that represents the category about the total spent.
        category['percentage'] = round(category['spent'] * 100 / total_spent)

        splitted = category['category'].split()  # Category name character by character to show them at the end.

        while len(splitted) < max_len:
            splitted.append(' ')  # Match the length of name strings to be able to display them.

        category['splitted'] = ''.join(splitted)

    if sort:
        categories_data = sorted(categories_data, key=lambda x: x['percentage'], reverse=True)

    for i in range(100, -1, -10):
        # Build the graphic
        index = str(i)
        while len(index) != 3:
            index = f' {index}'

        row = []
        for cat in categories_data:
            if cat['percentage'] >= i:
                row.append('o  ')
            else:
                row.append('   ')

        end_row = f"{index}| {''.join(row)}"

        exit_rows.append(end_row)

    exit_rows.append('    ' + '-' * (categories_len * 3 + 1))

    for i in range(max_len):
        # Add the names of the categories
        exit_rows.append('     ' + ''.join([f"{cat['splitted'][i]}  " for cat in categories_data]))

    return '\n'.join(exit_rows)


if __name__ == '__main__':
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(food)
    print(clothing)

    print(create_spend_chart([clothing, food, auto]))
    print(create_spend_chart([clothing, food, auto], sort=True))
