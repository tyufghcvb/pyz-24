from link_processor import LinkProcessor, url_base
from test import test_url_type


def main():

    patterns_list = {
        'url_base': f'url_base$',
        # `https://helion.pl/ksiazki/nazwa_ksiazki`
        'books': f'{url_base}ksiazki/[\w_]+$',
        # `https://helion.pl/kategorie/programowanie'
        'category': f'{url_base}kategorie/[\w]+$',
        # `https://helion.pl/kategorie/promocja-xyz`
        'sales': f'{url_base}kategorie/[\w]+-[\w]+$'
    }

    user_id = input("please put your user_id ")
    # user_url = input("please put your url")
    # user_url = "https://helion.pl/kategorie/promocja-xyz"
    # user_url = "https://helion.pl/ksiazki/nazwa_ksiazki"
    # user_url = "https://helion.pl/kategorie/programowanie"
    user_url = "https://helion.pl/ksiazki/inna_ksiazka"


    link = LinkProcessor(user_id, user_url)
    url_type = link.recognize_url_type(patterns_list)
    ident = link.get_url_ident()

    #print(url_type)

    urls_test_set = [
        "https://helion.pl/ksiazki/nazwa_ksiazki",
        "https://helion.pl/kategorie/promocja-xyz",
        "https://helion.pl/kategorie/programowanie",
        "https://helion.pl/ksiazki/inna_ksiazka"
    ]

    # results = test_url_type(link.recognize_url_type(patterns_list), urls_test_set, patterns_list)
    # for url, type in results.items():
    #     print(f"URL: {url}, Type: {type}")


if __name__ == "__main__":
    main()
