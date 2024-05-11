import re

url_base = r'^https://helion\.pl/'

site_pattern = r'^https?://[\w_]+\.(pl|com|edu|gov|mil|net|org|int|biz)$'

# patterns list

patterns_dict = {
    'url_base': f'url_base$',
    # `https://helion.pl/ksiazki/nazwa_ksiazki`
    'books': f'{url_base}ksiazki/[\w_]+$',
    # `https://helion.pl/kategorie/programowanie'
    'category': f'{url_base}kategorie/[\w]+$',
    # `https://helion.pl/kategorie/promocja-xyz`
    'sales': f'{url_base}kategorie/[\w]+-[\w]+$'
}


def is_valid_url(url):
    if re.match(site_pattern, url):
        return True


class LinkProcessor:
    def __init__(self, user_id, user_url, patterns_dict):
        self.user_id = user_id
        self.user_url = user_url
        self.patterns_dict = patterns_dict

    def recognize_url_type(self, patterns):
        print(f"URL: {self.user_url}")
        for key, value in patterns.items():
            if re.match(value, self.user_url):
                url_type = key
                print(f"URL: {self.user_url} is {key} type")
                return url_type

        print("Not recognized")
        return None

    # Strona główna
    # Strona produktu
    # Strona promocji
    # Link do kategorii

    def get_url_ident(self):
        data_pattern = r'/([^/]+)$'

        match = re.search(data_pattern, self.user_url)
        if match:
            ident = match.group(0)
            print("Urls ident: ", ident)
            return ident
        else:
            print("there is no ident")
            return ""

    def generate_dedicated_link(url_type, ident, user_id):
        url_base_dedicated_link = '{url_base}+view/user_id#'
        dedicated_link = ''
        # - Strona główna → `https: // helion.pl / ` → `https: // helion.pl / view / [ID klienta]#`
        if url_type == url_base:
            dedicated_link = url_base_dedicated_link
        # - Strona produktu →  `https: // helion.pl / view / [ID klienta] / nazwa_ksiazki `
        elif url_type == 'books':
            dedicated_link = '{url_base_dedicated_link}/view/{user_id}/{ident}'
        # Strona promocji → `https: // helion.pl / page / [ID klienta] / promocja / promocja - xyz `
        elif url_type == 'sales':
            dedicated_link = '{url_base_dedicated_link}/page/{user_id}/promocja/{ident}'
        # - Link do kategorii → `https: // helion.pl / page / [ID klienta] / kategorie / programowanie`
        elif url_type == 'category':
            dedicated_link = '{url_base_dedicated_link}/page/{user_id}/kategorie/{ident}'
        else:
            print("Something's wrong")
            dedicated_link = url_base_dedicated_link
