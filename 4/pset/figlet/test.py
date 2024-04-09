from lxml import html
import requests as req


def main():
    resp = req.get("http://www.figlet.org/fontdb.cgi")
    tree = html.fromstring(resp.content)
    print(tree)


if __name__ == "__main__":
    main()
