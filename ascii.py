def file_ascii(filename):
    with open(filename, 'r+', encoding='utf-8') as f:
        value = f.read()
        mas = []
        for i in value:
            mas.append(ord(i))
        print("Length text in the byte:", len(mas))
