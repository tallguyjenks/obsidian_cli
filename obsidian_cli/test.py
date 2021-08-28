with open('../templates/text.md', 'r') as f:
    Name = "world"
    text = f.read().replace('\n', ' ')
    text = text.replace('{Name}', Name)
    print(text)