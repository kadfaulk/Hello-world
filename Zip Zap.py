#kadari faulkner 3/12/2021

def ZipZap(n):
    if n%5 == 0 and n%7 == 0:
        print("ZipZap")
    elif n%5 == 0:
        print("Zip")
    elif n%7 == 0:
        print("Zap")
    else:
        print(n)
