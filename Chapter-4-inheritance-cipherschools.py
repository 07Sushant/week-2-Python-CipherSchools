class smartphone:
    def info(self,brand,price,camera):
        self.brand = brand
        self.price = price
        self.camera = camera
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    def make_a_call(self,number):
        return f"calling{number}...."

smartphone = smartphone('nokia','1100',1000)
print(smartphone.fullname)