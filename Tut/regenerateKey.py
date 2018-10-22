import APIKey as Consts

def main():
    file = open("APIKey.py", "w")
    key = raw_input("New API key: ")
    key = 'APIKey = "' + key + '"' 
    file.write(key)

if __name__ == "__main__":
    main()
