def isBlack(url):
    with open("blacklisted.txt", "r") as file:
        blacklisted_links = [line.strip() for line in file.readlines()]
    print(blacklisted_links)

    return True if url in blacklisted_links else False

if __name__ == '__main__':
    url = "https://instagram.com"
    print(isBlack(url))
