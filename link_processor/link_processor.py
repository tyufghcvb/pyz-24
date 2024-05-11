import re

url_base = r'^https://helion\.pl/'


def is_valid_url():
    pass


class LinkProcessor:
    def __init__(self, user_id, user_url):
        self.user_id = user_id
        self.user_url = user_url

    def generate_dedicated_link(url_type):
        pass

    # patterns list

    # patterns_list = {
    #     'url_base': url_base,
    #     # `https://helion.pl/ksiazki/nazwa_ksiazki`
    #     'books': f'{url_base}ksiazki/[\w_]+$',
    #     # `https://helion.pl/kategorie/programowanie'
    #     'category': f'{url_base}kategorie/[\w]+$',
    #     # `https://helion.pl/kategorie/promocja-xyz`
    #     'sales': f'{url_base}kategorie/[\w]+-[\w]+$'
    # }

    def recognize_url_type(self, patterns):
        print(f"URL: {self.user_url}")
        for key, value in patterns.items():
            if re.match(value, self.user_url):
                url_type = key
                print(f"URL: {self.user_url} is {key} type")
                return url_type

        print("poza kategorią")
        return None

    # Strona główna
    # Strona produktu
    # Strona promocji
    # Link do kategorii
