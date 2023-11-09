def main():
    x=input("File name: ")
    if x.endswith(".gif"):
        print("image/gif")
    elif x.endswith(".png"):
        print("image/png")
    elif x.endswith(".jpg"):
        print ("image/jpeg")
    elif x.endswith(".pdf"):
        print ("application/pdf")
    elif x.endswith(".zip"):
        print ("application/zip")
    elif x.endswith(".txt"):
        print ("application/octet-stream")
main()