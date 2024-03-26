def main():
    ft = input("Input file name: ").lower().strip().rsplit(".", 1)[-1] 
    get_ext(ft)


def get_ext(ft):
    match ft:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")



if __name__ == "__main__":
    main()
