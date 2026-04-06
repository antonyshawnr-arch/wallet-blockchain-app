import uuid

class Wallet:
    def __init__(self, name):
        self.name = name
        self.address = str(uuid.uuid4())
        self.balance = 100
        self.transactions = []

    def send(self, recipient, amount, blockchain):
        if self.balance >= amount:
            blockchain.new_transaction(self.address, recipient.address, amount)

            self.balance -= amount
            recipient.balance += amount

            tx = {
                'from': self.address,
                'to': recipient.address,
                'amount': amount
            }

            self.transactions.append(tx)
            recipient.transactions.append(tx)

            return "Transaction Successful"
        return "Insufficient Balance"

    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "balance": self.balance
        }
