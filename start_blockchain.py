import hashlib

class FexoCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_has = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Anna sends 2 FexoCoin to Mike"
t2 = "Bob sends 11 FexoCoin to Mike"
t3 = "Mike sends 4.1 FexoCoin to Bob" 
t4 = "Daniel sends 3.2 FexoCoin to Anna"
t5 = "Mike sends 0.2 FexoCoin to Charlie"
t6 = "Eric sends 5.2 FexoCoin to Daniel"

initial_block = FexoCoinBlock("AAA",[t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = FexoCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = FexoCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)

fourth_block = FexoCoinBlock(third_block.block_hash, [t4, t2])

print(fourth_block.block_data)
print(fourth_block.block_hash)

fifth_block = FexoCoinBlock(fourth_block.block_hash, [t1, t6])

print(fifth_block.block_data)
print(fifth_block.block_hash)