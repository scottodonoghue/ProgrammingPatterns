import xml.etree.ElementTree as ET
tree = ET.parse('ihop.xml')
root = tree.getroot()


class IHOPParser:
    def __init__(self, xmlfile) -> None:
        self.xmlfile = xmlfile

    def parse(self):
        tree = ET.parse(self.xmlfile)
        root = tree.getroot()
        names = [element.text for element in root.findall("./food/name")]
        prices = [element.text for element in root.findall("./food/price")]
        descriptions = [element.text for element in root.findall("./food/description")]
        calories = [element.text for element in root.findall("./food/calories")]

        print(f"Caloris: {calories}")
        self.data = {
            "item_name": names,
            "item_price": prices,
            "item_description": descriptions,
            "item_calories" : calories 
        }


class McDonaldsParser:
    def __init__(self, xmlfile) -> None:
        self.xmlfile = xmlfile

    def parse(self):
        tree = ET.parse(self.xmlfile)
        root = tree.getroot()
        names = [element.text for element in root.findall("./item/food_name")]
        prices = [element.text for element in root.findall("./item/price")]
        descriptions = [element.text for element in root.findall("./item/description")]
        calories = [element.text for element in root.findall("./item/num_calories")]

        print(f"Caloris: {calories}")
        self.data = {
            "item_name": names,
            "item_price": prices,
            "item_description": descriptions,
            "item_calories" : calories 
        }



if __name__ == "__main__":
    file = "ihop.xml"
    # file = "mcdonalds.xml"

    if "ihop" in file:
        parser = IHOPParser(file)
    elif "mcdonalds" in file:
        parser = McDonaldsParser(file)
        
    parser.parse()
    print(parser.data)