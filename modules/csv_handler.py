import csv


def write_csv(filename: str, headers, rows):
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
