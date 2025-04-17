'''colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]
index = input("Enter index: ")
color = input("Enter new color: ")'''

colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]

index = int(input("Enter index 0-3: "))
new_color = input("Enter new color: ")
if index >= 0 and index <= 3:
    colors[index] = new_color
print(colors)