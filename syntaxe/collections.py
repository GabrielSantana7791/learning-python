#Setting global variable inside a method
"""comments
"""
def settingGlobalVariable():
    global name, number
    name = "Gabriel"
    number = 2

def main():
    """settingGlobalVariable()

    print(f"{name},{type(name)}")
    print(f"{number},{type(number)}")"""

    #List
    names = ["Gabriel", "Fernando"]
    
    #Tuple (Cannot be changed)
    fruits = ("Banana", "apple")

    #Dictionary
    users = {"gabcbq123": "123"}
    
    users["gabcbq123"] = "321"
    users["neo12"] = "ab"
    users.update({"masterOfLc": "123123"})

    print("Hello" + " " + str(2))

main()