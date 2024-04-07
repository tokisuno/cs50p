import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

month_num = list(range(1, 12))

STATIC_MONTHS = 12
STATIC_DAYS = 31


def main():
    month_dict = dict(zip(months, month_num))
    while True:
        try:
            x = input("Date: ").strip()
            expr = re.findall(r'[0-9\.]+|[^0-9\.]+', x)
            m = expr[0].strip()
            d_num = expr[1].strip()
            d = expr[2].strip()
            y = expr[-1].strip()
            if m in months:
                if d == ",":
                    if int(d_num) <= STATIC_DAYS:
                        if m in months[0:9]:
                            print(f"{y}-0{month_dict.get(m)}-{d_num.zfill(2)}", end='')
                        else:
                            print(f"{y}-{month_dict.get(m)}-{d_num.zfill(2)}", end='')
                        return
                    else:
                        pass
                else:
                    pass
            elif int(m) <= STATIC_MONTHS:
                if int(d) <= STATIC_DAYS:
                    print(f"{y}-{m.zfill(2)}-{d.zfill(2)}", end='')
                    return
                else:
                    pass
            else:
                pass
        except TypeError:
            pass
        except ValueError:
            pass


if __name__ == "__main__":
    main()
