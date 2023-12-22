with open("file.txt", "r") as f:
    line_count = sum(1 for line in f)
    f.seek(0)
    word_count = sum(len(line.split()) for line in f)

print(f"Количество строк: {line_count}")
print((f"Количество слов: {word_count}"))