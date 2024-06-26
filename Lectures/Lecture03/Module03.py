# Reading from a file
"""
FILENAME = "hashes.txt"

in_file = open(FILENAME, "r")
for line in in_file:
    if line.startswith("# "):
        line = line.rstrip("\n")
        print(line)
in_file.close()
"""

# Reading a csv-like file
# with open("guitars.txt", "r") as in_file:
#     in_file.readline()  # Ignore header
#     for line in in_file:
#         parts = line.strip().split(",")
#         brand = parts[0]
#         model = parts[1]
#         year_released = parts[2]
#         cost = float(parts[3].strip("\\n"))
#         print(f"The {model} was released by {brand} in {year_released}, and it costs ${cost:.2f}¢.")

# Next section
