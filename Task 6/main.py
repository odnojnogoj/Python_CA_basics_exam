# Sukurkite terminalo programą, kuri bankui leis apdoroti gaunamas užklausas. Bankas gali gauti trijų tipų užklausas:

# - transfer i j sum: prašymas pervesti pinigų sumą iš i-osios sąskaitos į j-ąją;
# - deposit i sum: prašymas įnešti pinigų sumą į i-ąją sąskaitą;
# - withdraw i sum: prašymas išsiimti pinigų sumą iš i-osios sąskaitos.

# Jūsų programa taip pat turėtų galėti apdoroti netinkamas užklausas. Yra dviejų tipų negaliojančios užklausos:
# - neteisingas sąskaitos numeris prašymuose;
# - didesnės pinigų sumos, nei yra šiuo metu, išėmimas/pervedimas.

# Po kiekvienos operacijos išveskite ar ji pavyko, ar ne ir parodykite sąskaitų balansus ekrane.

######################

# Pvz. Kai duoti pradiniai sąskaitų balansai yra:
# ACCOUNTS = [10, 100, 20, 50, 30]

# Įvestos užklausos į terminalą:
# - "withdraw 2 10"
# - "transfer 5 1 20"
# - "deposit 5 20"
# - "transfer 3 4 15"

# Atitinkamai išvedami rezultatai, po kiekvienos užklausos:
# - Operation was successful; New account balances: [10, 90, 20, 50, 30]
# - Operation was successful; New account balances: [30, 90, 20, 50, 10]
# - Operation was successful; New account balances: [30, 90, 20, 50, 30]
# - Operation was successful; New account balances: [10, 90, 20, 50, 30]
# - Operation was successful; New account balances: [30, 90, 5, 65, 30]

######################

# Pvz. Kai duoti pradiniai sąskaitų balansai yra:
# ACCOUNTS = [20, 1000, 500, 40, 90]

# Įvestos užklausos į terminalą:
# - "deposit 3 400"
# - "transfer 1 10 10"
# - "withdraw 4 50"

# Atitinkamai išvedami rezultatai, po kiekvienos užklausos:
# - Operation was successful; New account balances: [20, 1000, 900, 40, 90]
# - Operation is invalid, such account does not exist; New account balances: [20, 1000, 900, 40, 90]
# - Operation is invalid, not enough balance; New account balances: [20, 1000, 900, 40, 90]

# !!! Pastaba: Papildomas taškas, jeigu panaudosite klases. !!!

class Account:
    def __init__(self, balance):
        self.balance = balance
        self.message_done = "Operation was successful; New account balances:" 
        self.message_error_account = "Operation is invalid, such account does not exist; New account balances:"
        self.message_error_balace = "Operation is invalid, not enough balance; New account balances: "

    def transfer(self, i, j, summ):
        if i >= len(self.balance) or j >= len(self.balance):
            return (print(self.message_error_account, self.balance))
        elif summ > self.balance[i]:
            print(self.message_error_balace, self.balance)
        else:
            self.balance[i] = self.balance[i] - summ
            self.balance[j] = self.balance[j] + summ
            print(self.message_done, self.balance)

    def deposit(self, i, summ):
        if i >= len(self.balance):
            print(self.message_error_account, self.balance)
        else:
            self.balance[i] = self.balance[i] + summ
            print(self.message_done, self.balance)

    def withdraw(self, i, summ):
        if i >= len(self.balance):
            print(self.message_error_account, self.balance)
        elif summ > self.balance[i]:
            print(self.message_error_balace, self.balance)
        else:
            self.balance[i] = self.balance[i] - summ
            print(self.message_done, self.balance)

ACCOUNTS = Account([10, 100, 20, 50, 30])

while True:
    print("Input command options: ")
    print("transfer i j sum - to transfer SUM from I to J account")
    print("deposit i sum - to deposit SUM to I account")
    print("withdraw i sum - to withdraw SUM from I account")

    input_terminal = input().split(" ")
    if input_terminal[0] == "transfer":
        i = int(input_terminal[1])
        j = int(input_terminal[2])
        summ = int(input_terminal[3])
        ACCOUNTS.transfer(i, j, summ)

    if input_terminal[0] == "deposit":
        i = int(input_terminal[1])
        summ = int(input_terminal[2])
        ACCOUNTS.deposit(i, summ)

    if input_terminal[0] == "withdraw":
        i = int(input_terminal[1])
        summ = int(input_terminal[2])
        ACCOUNTS.withdraw(i, summ)
