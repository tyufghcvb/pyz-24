from link_processor import LinkProcessor, url_base, is_valid_url
from file_handler import save_links_to_file
from test import test_url_type


def main():
    # while True:
    #     options = """What do you want to do?
    #      1 - transform urls
    #      2 - save links
    #      3 - close program
    #       Select -> """

    patterns_dict = {
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

    link = LinkProcessor(user_id, user_url, patterns_dict)
    url_type = link.recognize_url_type(patterns_dict)
    ident = link.get_url_ident()
    dedicated_url = link.generate_dedicated_link(url_type, ident)

    print(dedicated_url)

    if is_valid_url(dedicated_url):
        link.update_dedicated_links_list()

    link.show_dedicated_links_list()
    save_links_to_file(link.dedicated_links_list)

    # print(url_type)

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
