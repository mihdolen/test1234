class Dict1:
    def __init__(self, d): 
        self.d = d
        pass

    def concat(self) -> str:
        conc = ""
        for value in self.d.values():
            conc += str(value)
        return conc
    
    def sum(self, keys_list):
        sum = 0
        for element in keys_list:
            if element in self.d.keys():
                sum += self.d[element]
        return sum





d1 = {"a": 22, "b": 44, "c": 66}
print(d1.values())
print(d1.keys())

m1 = Dict1({"a": 22, "b": 44, "c": 66})
print(m1.concat())
print(m1.sum((["a", "c"])))

