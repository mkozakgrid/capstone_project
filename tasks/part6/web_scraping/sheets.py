def print_sheet(title, headers, rows):
    col_widths = [
        max(len(str(headers[i])), max(len(str(row[i])) for row in rows))
        for i in range(len(headers))
    ]

    header_row = "| " + " | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers)) + " |"
    total_width = len(header_row)

    print(title.center(total_width, "="))

    print(header_row)
    print("-" * total_width)

    for row in rows:
        print("| " + " | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(headers))) + " |")

    print()