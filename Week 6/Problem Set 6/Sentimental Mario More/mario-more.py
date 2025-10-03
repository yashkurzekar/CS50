# mario_more.py
# Prints the "more comfortable" Mario double-pyramid

def get_height():
    while True:
        try:
            h = int(input("Height: "))
            if 1 <= h <= 8:
                return h
        except ValueError:
            pass

def main():
    height = get_height()

    for row in range(1, height + 1):
        # left padding, left blocks, gap, right blocks
        left_spaces = " " * (height - row)
        left_hashes = "#" * row
        gap = "  "
        right_hashes = "#" * row

        print(left_spaces + left_hashes + gap + right_hashes)

if __name__ == "__main__":
    main()
