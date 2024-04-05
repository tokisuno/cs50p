
def main():
    print(float(eval(input("Expression: "))), end='')


# def math():
#     while True:
#         try:
#             x = input("Expression: ")
#             expr = re.findall(r'[0-9\.]+|[^0-9\.]+', x)
#             if expr[0] == "0":
#                 return 0/int(expr[2])
#             if int(expr[0]):
#                 if int(expr[2]):
#                     if expr[1] == "/" or expr[1] == "+" or expr[1] == "-" or expr[1] == "*":
#                         return eval(x)
#         except ValueError:
#             return

if __name__ == "__main__":
    main()
