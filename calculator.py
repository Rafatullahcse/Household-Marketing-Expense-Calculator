def calculate_total_expenses(expenses):
    total = 0.0
    for category in expenses.get_all_categories():
        total += category.amount
    return total


def calculate_category_total(expenses, category_name):
    category = expenses.get_category(category_name)
    if category:
        return category.amount
    return 0.0


def generate_summary(expenses):
    summary = "Marketing Expense Summary:\n"
    for category in expenses.get_all_categories():
        summary += f"{category.name}: ${category.amount:.2f}\n"
    summary += f"Total: ${calculate_total_expenses(expenses):.2f}"
    return summary
