class Target: # Target
    def addition_v2(self):
        pass
class Old_Version: # Adaptee
    def addition(self, a, b):
        return a + b
class New_Version(Target): # Adapter
    def __init__(self, adaptee):
        self.adaptee = adaptee
    def addition_v2(self):
        return self.adaptee.addition(5, 5)
    def mean(self):
        return self.addition_v2() // 2
    def tax(self):
        return self.addition_v2() * .05
    def service_fee(self):
        return self.addition_v2() - 1
def client(target): # client
    print(target.addition_v2())
    print(target.mean())
    print(target.tax())
    print(target.service_fee())
def main():    
    instance = New_Version(Old_Version())
    client(instance)
main()