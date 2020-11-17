from hashlib import sha256

class Block:
    def __init__(self , index , timestamp , data , previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        # to be calculate
        self.hash = self.calculate_hash()

    #calculate hash
    def calculate_hash(self):
        everything = str(self.index) + str(self.timestamp) +str(self.data) +str(self.previous_hash) 
        step2 = everything.encode()
        step3 = sha256(step2)
        final_result = step3.hexdigest()
        return final_result

myblock1 = Block(1 ,"11/17/20:27" , "amount:1000usd" ,"")
myblock2 = Block(myblock1.index+1 ,"11/17/20:30" , "amount:500usd" , myblock1.hash )
print("-------")
print(myblock1.hash)
print(myblock2.previous_hash)



