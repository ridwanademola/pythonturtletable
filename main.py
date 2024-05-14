from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokeman Name", ["Pikacthu", "Squiretle", "Chamande"])
table.add_column("Type", ["Electric", "water", "fire"])

table.align = "l"

print(table)
