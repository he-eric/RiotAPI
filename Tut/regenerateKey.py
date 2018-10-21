import RiotConsts as Consts

def main():
    f = open("RiotConsts.py", "w")
    key = raw_input("New API key: ")
    f.write(key)

if __name__ == "__main__":
    main()
