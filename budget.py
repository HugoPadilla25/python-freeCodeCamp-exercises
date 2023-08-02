
class Category:
    def __init__(self, category = ''):
        self._category = category
        self._ledger = []
        self._retiros = []

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        self._category = value
    @category.deleter
    def category(self):
        del self._category

    @property
    def ledger(self):
        return self._ledger
    @ledger.setter
    def ledger(self, value):
        self._ledger = value
    @ledger.deleter
    def ledger(self):
        del self._ledger

    @property
    def retiros(self):
        return self._retiros
    @retiros.setter
    def retiros(self, value):
        self._retiros = value
    @retiros.deleter
    def retiros(self):
        del self._retiros

    def __str__(self):
        bal = 0
        bill = ''
        slices = len(self.ledger)
        i = 0
        while i < slices:
            bal += float(self.ledger[i]["amount"])
            bill += (str(self.ledger[i]["description"]).ljust(23, ' '))[:23] + str('{:.2f}'.format(self.ledger[i]["amount"])).rjust(7, ' ') + '\n'
            i += 1

        return f'''{self.category.center(30, '*').title()}
{bill}Total: {'{:.2f}'.format(bal)}'''

    def deposit(self, amount=None, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount=None, description=''):
        bal = 0
        slices = len(self.ledger)
        i = 0
        while i < slices:
            bal = float(self.ledger[i]["amount"])
            i += 1
        if bal >= amount:
            self.ledger.append({"amount": (amount)*-1, "description": description})
            self.retiros.append(amount)
            return True
        else:
            return False

    def get_balance(self):
        bal = 0
        slices = len(self.ledger)
        i = 0
        while i < slices:
            bal += float(self.ledger[i]["amount"])
            i += 1
        return bal

    def transfer(self, amount=None, destinity=None):
        bal = 0
        slices = len(self.ledger)
        i = 0
        while i < slices:
            bal += float(self.ledger[i]["amount"])
            i += 1
        if bal >= amount:
            self.ledger.append({"amount": (amount)*-1, "description": f'Transfer to {destinity.category}'})
            destinity.ledger.append({"amount": amount, "description": f'Transfer from {self.category}'})
            return True
        else:
            return False

    def check_funds(self, amount=None):
        bal = 0
        slices = len(self.ledger)
        i = 0
        while i < slices:
            bal += float(self.ledger[i]["amount"])
            i += 1
        if bal >= amount:
            return True
        else:
            return False


def create_spend_chart(categories):
    total = 0
    categories_subtotal = {}
    categories_percent = {}
    names = []
    spent_chart = ''

    for category in categories:
        for m in category.retiros:
            total += m
            cat_total = m
        categories_subtotal[category.category] = round(cat_total, 2)

    for i in categories_subtotal:
        categories_percent[i] = round((categories_subtotal[i] * 100) / total, 2)

    for i in range(100, -10, -10):
        spent_chart += (str(i).rjust(3)+'|'+'\n')

    for j in categories_percent:
        names.append(j)

    largest_word = 0

    for t in names:
        letters = len(t)
        if letters > largest_word:
            largest_word = letters

    counter = 0
    spent_names = ''

    while counter < largest_word:
        name_word = ''
        count_names = 0
        while count_names < len(names):
            try:
                name_word += ' ' + names[count_names][counter] + ' '
            except:
                name_word += '  '+' '
            count_names += 1
        spent_names += '\n' +'    '+ name_word + ' '
        counter += 1

    percent = []

    for r in categories_percent:
        rd = 0
        m = int(categories_percent[r])
        if m <= 10 and m > 0:
            rd = 0
        else:
            rd = int(m/10)
        percent.append(('o'*(rd+1)).rjust(11, ' '))

    counter = 0
    discounter = 10
    percent_chart = ''
    while counter <= 10:
        blanck_pos  = ''
        count_blanck = 0
        while count_blanck < len(percent):
            try:
                blanck_pos += ' ' + percent[count_blanck][counter] + ' '
            except:
                blanck_pos += '  '+' '
            count_blanck += 1
        percent_chart += '\n' + (str((discounter)*10).rjust(3)+'|') + blanck_pos +' '
        counter += 1
        discounter -= 1

    separator = '    ' + '---'*((len(names))) + '-'

    return f'''Percentage spent by category{percent_chart}
{separator}{spent_names}'''
