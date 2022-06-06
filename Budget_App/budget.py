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
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        space = int((30 - len(self.category)) / 2)
        exit_string = '*' * space + self.category + '*' * space
        while len(exit_string) < 30:
            exit_string += '*'

        for operation in self.ledger:
            exit_string += raw(operation)

        # exit_string += f'\nTotal: {self.get_balance()} '
        exit_string += '\nTotal: ' + str(self.get_balance()) + ' '
        return exit_string

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
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


def create_spend_chart(categories):
    categories_data = []
    total_spent = 0
    max_len = 0
    categories_len = len(categories)
    exit_rows = ['Percentage spent by category']

    for category in categories:

        if len(category.category) > max_len:
            max_len = len(category.category)

        spent = 0
        for operation in category.ledger:
            if operation['amount'] < 0:
                spent -= operation['amount']

        total_spent += spent

        categories_data.append({'category': category.category, 'spent': spent})

    for category in categories_data:
        category['percentage'] = round(category['spent'] * 100 / total_spent)

        splited = category['category'].split()
        while len(splited) < max_len:
            splited.append(' ')

        category['splited'] = ''.join(splited)

    # categories_data = sorted(categories_data, key=lambda x: x['percentage'], reverse=True)

    for i in range(100, -1, -10):
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
        exit_rows.append('     ' + ''.join([f"{cat['splited'][i]}  " for cat in categories_data]))

    return '\n'.join(exit_rows)
