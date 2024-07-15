class ExpenseCategory:
    def __init__(self, name):
        self.name = name
        self.amount = 0.0

    def add_expense(self, amount):
        self.amount += amount


class ExpenseTracker:
    def __init__(self):
        self.categories = {}

    def add_category(self, name):
        self.categories[name] = ExpenseCategory(name)

    def get_category(self, name):
        return self.categories.get(name)

    def get_all_categories(self):
        return list(self.categories.values())
