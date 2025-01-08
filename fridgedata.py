class Refrigerator:
    def __init__(self, brand, model, dimensions, color, price):  # all arguements are expected as strings, except the prices
        self.brand = brand
        self.model = model
        self.dimensions = dimensions  
        self.color = color
        self.price = price

    def volume(self):
        dimensions = [float(d) for d in self.dimensions.split('*')]   # Calculate the volume of the refrigerator in cubic centimeters.
        return dimensions[0] * dimensions[1] * dimensions[2]

    def __str__(self):
        return f"{self.brand} {self.model} ({self.color}) - ${self.price:.2f}"

# Instantiating the refrigerators
indesit = Refrigerator("Indesit", "CA140G.016", "200*66.5*60", "White", 1100.00)
atlant = Refrigerator("Atlant", "MXM1843-20", "205*64*60", "Beige", 1299.99)
beko = Refrigerator("Beko", "CSK-30000", "164*60*60", "White", 1200.00)
daewoo = Refrigerator("Daewoo", "FR-3501", "167.7*62.5*66.7", "Maple", 799.99)
electrolux = Refrigerator("Electrolux", "EJ-1800-ADW", "120.9*60.6*49.6", "Pink", 700.00)
whirlpool = Refrigerator("Whirlpool", "WBR-3012-W", "170.4*60*59.5", "White", 499.99)
pozis = Refrigerator("Pozis", "RS-405", "130*55*54", "Pink", 800.00)
hotpointAriston = Refrigerator("HPAriston", "RMBA-1200", "200*66*60", "StarDust", 599.99)
samsung = Refrigerator("Samsung", "RL-17-MBPS", "154.4*54.2*45.1", "White", 600.00)
stinol = Refrigerator("Stinol", "107.016", "167*60*60", "Laminated", 650.00)
nord = Refrigerator("Nord", "241-6-020", "148*61*57.4", "Pink", 350.00)
liebherr = Refrigerator("Liebherr", "CN-4003", "201.1*63*60", "White", 450.00)

# Storing the refrigerators in a list for easy manipulation
refrigerators = [
    indesit, atlant, beko, daewoo, electrolux, whirlpool, pozis,
    hotpointAriston, samsung, stinol, nord, liebherr
]

# Displaying data in a tabular format
def displayTabulated(data, title):   # Displaying data in a tabular format function.
    print(f"\n{title}")
    print(f"{'Brand':<15}{'Model':<20}{'Dimensions (cm)':<18}{'Color':<15}{'Price (USD)':<12}{'Volume (cm³)':<15}")
    print("=" * 95)

    for fridge in data:
        print(f"{fridge.brand:<15}{fridge.model:<20}{fridge.dimensions:<18}{fridge.color:<15}"
              f"${fridge.price:<11.2f}{fridge.volume():<15,.2f}")
        

def filterByPrice(maxPrice):    # Filtering refrigerators by price.
    return [fridge for fridge in refrigerators if fridge.price <= maxPrice]

def listByColor(color):     # Listing refrigerators of a specific color.
    return [fridge for fridge in refrigerators if fridge.color.lower() == color.lower()]

# Displaying all the refrigerators.
displayTabulated(refrigerators, "All Refrigerators")

# Displaying refrigerators under $850.
filtered = filterByPrice(850)
displayTabulated(filtered, "Refrigerators Under $850")

# Displaying all the white refrigerators.
whiteRefrigerators = listByColor("White")
displayTabulated(whiteRefrigerators, "White Refrigerators")
