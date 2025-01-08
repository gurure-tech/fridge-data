class Refrigerator:
    def __init__(self, brand: str, model: str, size: float, colour: str, price: float) -> None:  #Dunder method
        self.brand = brand
        self.model = model
        self.size = size
        self.colour = colour
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f"Refrigerator ({self.brand}) is already turned on!!")
        else:
            self.turned_on = True
            print(f"Refrigerator ({self.brand}) is now turned on!!")

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f"Refrigerator ({self.brand}) is now turned off!!")
        else:
            print(f"Refrigerator ({self.brand}) is already turned off!!")

    def run(self, seconds:  int) -> None:
        if self.turned_on:
            print(f"Running ({self.brand}) for {seconds} seconds")
        else:
            print("The Mandalorian shouts: 'Turn on the damn Refrigerator already'")

    def __add__(self, other):
        return f"{self.brand} + {other.brand}"

    def __mul__(self, other):
        return f"{self.brand} * {other.brand}"

    def __str__(self) -> str:  # returns a readable not the memory location/address of the instance
        return f"{self.brand} (Model: {self.model})"

    def __repr__(self) -> str:
        return f"Refrigerator(brand = '{self.brand}' , Model = '{self.model}')"

indesit: Refrigerator = Refrigerator("Indesit", "CA140G.016", 200*66.5*60, "White", 1100.00)    # type annotation or type hint, just the same as beko = Refrigerator(), instantiate the first Refrigerator
atlant: Refrigerator = Refrigerator("Atlant", "MXM1843-20", 205*64*60, "Beige", 1299.99) 
beko: Refrigerator = Refrigerator("Beko", "CSK-30000", 164*60*60, "White", 1100.00) 
daewoo: Refrigerator = Refrigerator("Daewoo", "FR-3501", 167.7*62.5*66.7, "SandyWhite", 499.99) 
electrolux: Refrigerator = Refrigerator("Electrolux", "EJ-1800-ADW", 120.9*60.6*49.6, "CreamWhite", 700.00) 
whirlpool: Refrigerator = Refrigerator("Whirlpool", "WBR-3012-W", 170.4*60*59.5, "OffWhite", 499.99) 
pozis: Refrigerator = Refrigerator("Pozis", "RS-405", 130*55*54, "Pink", 800.00) 
hotpointAriston: Refrigerator = Refrigerator("HPAriston", "RMBA=1200", 200*66*60, "StarDust", 599.99) 
samsung: Refrigerator = Refrigerator("Samsung", "RL-17-MBPS", 154.4*54.2*45.1, "White", 600.00) 
stinol: Refrigerator = Refrigerator("Stinol", "107.016", 167*60*60, "SnowWhite", 650.00) 
nord: Refrigerator = Refrigerator("Nord", "241-6-020", 148*61*57.4, "SnowWhite", 350.00)
liebherr: Refrigerator = Refrigerator("Liebherr", "CN-4003", 201.1*63*60, "White", 450.00)

print(repr(indesit))
print(indesit)

print(beko)
beko.turn_on()
beko.run(40)
beko.turn_off()
beko.run(10)