class ExpenseTracker:
  def __init__(self, income):
      self.income = income
      self.categories = {
          1: {"name": "Housing", "budget": 0, "expenses": 0},
          2: {"name": "Transportation", "budget": 0, "expenses": 0},
          3: {"name": "Utilities", "budget": 0, "expenses": 0},
          4: {"name": "Entertainment", "budget": 0, "expenses": 0},
          5: {"name": "Food", "budget": 0, "expenses": 0}
      }

  def add_expense(self, category_number, amount):
      category = self.categories.get(category_number)
      if category:
          category["expenses"] += amount
          print(f"Added ${amount} to {category['name']} expenses.")
          if category["expenses"] > category["budget"]:
              print("WARNING: You've exceeded the budget for this category!")
              increase_budget = input("Do you want to increase the budget for this category? (yes/no): ")
              if increase_budget.lower() == "yes":
                  new_budget = float(input("Enter the new budget amount: $"))
                  self.set_budget(category_number, new_budget)
      else:
          print("Invalid category number.")

  def view_expenses(self):
      print("\nMonthly Expenses:")
      for category_number, details in self.categories.items():
          print(f"{details['name']}: ${details['expenses']}")

  def set_budget(self, category_number, budget_amount):
      category = self.categories.get(category_number)
      if category:
          category["budget"] = budget_amount
          print(f"Set ${budget_amount} as the budget for {category['name']} category.")
      else:
          print("Invalid category number.")

  def view_budget(self):
      print("\nMonthly Budget:")
      for category_number, details in self.categories.items():
          print(f"{details['name']} Budget: ${details['budget']}")

  def remaining_income(self):
      total_expenses = sum(details['expenses'] for details in self.categories.values())
      return self.income - total_expenses


def print_categories():
  print("\nExpense Categories:")
  for category_number, details in ExpenseTracker(0).categories.items():
      print(f"{category_number}. {details['name']}")


def main():
  income = float(input("Enter your monthly income: $"))
  tracker = ExpenseTracker(income)

  print("\nSet Budget for Each Category:")
  for category_number, details in tracker.categories.items():
      budget_amount = float(input(f"Enter budget amount for {details['name']}: $"))
      tracker.set_budget(category_number, budget_amount)

  while True:
      print("\n1. Add Expense\n2. View Expenses\n3. Set Budget\n4. View Budget\n5. Remaining Income\n6. Exit")
      choice = input("Enter your choice: ")

      if choice == "1":
          print_categories()
          category_number = int(input("Enter category number: "))
          amount = float(input("Enter expense amount: $"))
          tracker.add_expense(category_number, amount)
      elif choice == "2":
          tracker.view_expenses()
      elif choice == "3":
          print_categories()
          category_number = int(input("Enter category number: "))
          budget_amount = float(input("Enter budget amount: $"))
          tracker.set_budget(category_number, budget_amount)
      elif choice == "4":
          tracker.view_budget()
      elif choice == "5":
          print(f"\nRemaining Income: ${tracker.remaining_income()}")
      elif choice == "6":
          print("Exiting the expense tracker.")
          break
      else:
          print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()
