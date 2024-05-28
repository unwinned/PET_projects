import random


class CryptoUser:
    def __init__(self, name: str, wallet: str, lucky: int, balance: int) -> None:
        self.name = name
        self.wallet = wallet
        self.lucky = lucky
        self.balance = balance

    def print_user(self):
        print(f"name: {self.name}; wallet: {self.wallet}; lucky: {self.lucky}")

    def ludka(self):
        if self.balance > 0:
            if random.randint(0, 100) > self.lucky:
                self.balance *= 2
            else:
                self.balance /= 2
        else:
            print("Ебанько, иди баланс пополни, или больше играй, а то маме позвоню")
        print(f"{self.name}: current_balance: {self.balance},")


a = CryptoUser("Pasha Durov", "0xdf0sdfdsdfsdf00sdf", 90, 100000000000)
a.print_user()

print("----------------------------------------")

# b = CryptoUser("Tony Stark", "0xfghgfhfghfggfhftcvbnvbnvbnmbhm", 70, 10000000)
# b.print_user()

a.ludka()

