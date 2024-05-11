def save_links_to_file(urlslist):
    filename = "dedicated_links.txt"

    with open(filename, 'w') as file:
        # Write urls list to file
        for link in urlslist:
            file.write(f"{link}\n")

    print(f"Successfully written to  {filename}")
