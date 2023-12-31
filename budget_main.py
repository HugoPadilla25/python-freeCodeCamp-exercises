import budget
from budget import create_spend_chart

def main():
    food = budget.Category("Food")
    food.deposit(1000, "initial deposit")
    print(food.withdraw(10.15, "groceries"))
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = budget.Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    print(clothing.get_balance())
    print(food.get_balance())
    auto = budget.Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(food)
    print(clothing)
    print(auto)
    print(create_spend_chart([food, clothing, auto]))

if __name__ == '__main__':
    main()
