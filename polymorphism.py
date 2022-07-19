
class France():
    def capital(self):
        print("The capital city of France is Paris")

    def language(self):
        print("The official language of France is French")

    def population(self):
        print("The population of France is about 67 million.")

class Spain():
    def capital(self):
        print("The capital city of Spain is Madrid.")

    def language(self):
        print("The official language of Spain is Spanish")

    def population(self):
        print("The population of Spain is about 47 million.")


obj_fr = France()
obj_sp = Spain()

for country in (obj_fr, obj_sp):
    country.capital()
    country.language()
    country.population()
        
