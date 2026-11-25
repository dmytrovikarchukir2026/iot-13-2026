class BankAccount:
    def __init__(self, account_id, owner_name, balance=0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
    
        self.__account_id = account_id
        self.__owner_name = owner_name
        self.__balance = balance

    def get_account_id(self):
        return self.__account_id

    def get_owner_name(self):
        return self.__owner_name

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Рахунок поповнено на {amount} грн.")
        else:
            print("Сума поповнення повинна бути додатною.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сума зняття повинна бути додатною.")
        elif amount > self.__balance:
            print("Недостатньо коштів на рахунку.")
        else:
            self.__balance -= amount
            print(f"Знято {amount} грн.")

    def show_account(self):
        print(f"ID рахунку: {self.__account_id}")
        print(f"Власник: {self.__owner_name}")
        print(f"Баланс: {self.__balance:.2f} грн.")

    def __str__(self):
        return (
            f"ID: {self.__account_id}, "
            f"Власник: {self.__owner_name}, "
            f"Баланс: {self.__balance:.2f} грн."
        )

    def __del__(self):
        print(f"Рахунок {self.__account_id} видалено.")


class Bank:
    def __init__(self, name):
        self.__name = name
        self.__accounts = []

    def add_account(self, account):
        for existing_account in self.__accounts:
            if existing_account.get_account_id() == account.get_account_id():
                print(f"Рахунок з ID {account.get_account_id()} вже існує.")
                return

        self.__accounts.append(account)
        print(f"Рахунок {account.get_account_id()} додано до банку.")

    def remove_account(self, account_id):
        for account in self.__accounts:
            if account.get_account_id() == account_id:
                self.__accounts.remove(account)
                print(f"Рахунок {account_id} видалено з банку.")
                return

        print(f"Рахунок {account_id} не знайдено.")

    def sort_accounts(self):
        self.__accounts.sort(key=lambda account: account.get_balance())

        print("\nРахунки, відсортовані за балансом:")
        for account in self.__accounts:
            print(account)

    def show_all_accounts(self):
        print(f"\nБанк: {self.__name}")
        print("Список усіх рахунків:")

        for account in self.__accounts:
            print(account)


def main():
    bank = Bank("Python Bank")

    account1 = BankAccount(101, "Dmytro", 1500.50)
    account2 = BankAccount(102, "Andriy", 2500.00)
    account3 = BankAccount(103, "Roman", 800.75)

    bank.add_account(account1)
    bank.add_account(account2)
    bank.add_account(account3)

    for account in bank._Bank__accounts:
        print(f"ID: {account.get_account_id()}, Ім'я: {account.get_owner_name()}")

    print("\nІнформація про перший рахунок:")
    account1.show_account()

    print("\nПоповнення першого рахунку:")
    account1.deposit(500.25)

    print("\nЗняття коштів з другого рахунку:")
    account2.withdraw(300.50)

    bank.show_all_accounts()

    bank.sort_accounts()

    print("\nВидалення рахунку:")
    bank.remove_account(102)

    bank.show_all_accounts()


if __name__ == "__main__":
    main()
