glb_name = "Sally"

print(glb_name)
def change_name():
    global glb_name
    glb_name = "Leke"

change_name()
print(glb_name)