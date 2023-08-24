import csv
import datetime

# with open("bank_records.csv", "w", encoding='utf-8', newline='') as initial_records:
#     opening_writer = csv.writer(initial_records, quoting=csv.QUOTE_NONNUMERIC)
#     column_headings = ['Name', 'Balance']
#     opening_writer.writerow(column_headings)
#
# with open("transaction_data.csv", "w", encoding='utf-8', newline='') as transaction_file:
#     opening_writer2 = csv.writer(transaction_file, quoting=csv.QUOTE_NONNUMERIC)
#     transaction_writer = csv.writer(transaction_file, quoting=csv.QUOTE_NONNUMERIC)
#     column_headings2 = ['Name', 'transaction type', 'transaction amount', 'transaction time']
#     opening_writer2.writerow(column_headings2)


class Bank:

    options = ['1 - View Balance',
               '2 - Withdraw',
               '3 - Deposit',
               '4 - View transaction history',
               '0 - quit']

    def __init__(self, initial_amount=0):
        self.name = str(input("Enter name: ")).lower()
        self.balance = initial_amount

    # def user_exists(self):
    #     pass

    def deposit(self, amount_to_be_deposited):
        self.balance = self.balance + amount_to_be_deposited
        with open("transaction_data.csv", "a+", encoding='utf-8', newline='') as transaction_file:
            transaction_writer = csv.writer(transaction_file, quoting=csv.QUOTE_NONNUMERIC)
            final_data = [self.name, 'deposit', amount_to_be_deposited, datetime.datetime.now()]
            transaction_writer.writerow(final_data)

    def withdrawal(self, amount_to_be_withdrawn):
        self.balance = self.balance - amount_to_be_withdrawn
        with open("transaction_data.csv", "a+", encoding='utf-8', newline='') as transaction_file:
            transaction_writer = csv.writer(transaction_file, quoting=csv.QUOTE_NONNUMERIC)
            final_data = [self.name, 'withdrawal', amount_to_be_withdrawn, datetime.datetime.now()]
            transaction_writer.writerow(final_data)

    def update_balance(self):
        with open("bank_records.csv", "r", encoding='utf-8', newline='') as records:
            reader = csv.reader(records, quoting=csv.QUOTE_NONNUMERIC)
            data = list(reader)
        with open("bank_records.csv", "w", encoding='utf-8', newline='') as records:
            writer = csv.writer(records, quoting=csv.QUOTE_NONNUMERIC)
            found = False
            for row in data:
                if row[0] == self.name:
                    found = True
                    row[1] = self.balance
                    writer.writerows(data)
                    print(data)
                else:
                    continue
            if not found:
                data.append([self.name, self.balance])
                writer.writerows(data)

    def menu(self):
        with open("bank_records.csv", "r", encoding='utf-8', newline='') as records:
            reader = csv.reader(records, quoting=csv.QUOTE_NONNUMERIC)

            # checking if person already exists in database
            for row in reader:
                if row[0] == self.name:
                    self.balance = row[1]
                    break

            chosen_option = 100
            while chosen_option != 0:
                for option in self.options:
                    print(option)
                try:
                    chosen_option = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid entry")

                if chosen_option == 1:
                    print("Balance is: ", self.balance)

                elif chosen_option == 2:
                    withdrawn_amount = float(input("Enter amount to be withdrawn: "))
                    self.withdrawal(withdrawn_amount)
                    self.update_balance()

                elif chosen_option == 3:
                    deposited_amount = float(input("Enter amount to be deposited: "))
                    self.deposit(deposited_amount)
                    self.update_balance()

                elif chosen_option == 4:
                    with open("transaction_data.csv", "r", encoding='utf-8') as transaction_file:
                        reader2 = csv.reader(transaction_file, quoting=csv.QUOTE_NONNUMERIC)
                        for row in reader2:
                            if row[0] == self.name:
                                print(row)
                            else:
                                continue

                elif chosen_option == 0:
                    break

                else:
                    print("Please enter a number between 0 and 5 only")


banker = Bank()
banker.menu()
