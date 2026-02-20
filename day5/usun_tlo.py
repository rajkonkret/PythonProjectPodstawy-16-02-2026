from rembg import remove

# pip install "rembg[cpu]"
# pip install pillow

# source .venv/bin/activate - aktywacja wirtualnego srodowiska

input_path = 'input1.png'
outpu_path = "output.png"

with open(input_path, "rb") as f:
    input_data = f.read()

# print(input_data)

output_data = remove(input_data)
# print(output_data)

with open(outpu_path, 'wb') as f:
    f.write(output_data)

print("Tło usunięte")
