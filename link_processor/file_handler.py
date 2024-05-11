def save_links_to_file(urlslist):
    filename = "dedicated_links.txt"

    with open(filename, 'w') as file:
        for link in urlslist:
            file.write(f"{link}\n")  # Write each URL to the file

    print(f"Successfully written to {filename}")