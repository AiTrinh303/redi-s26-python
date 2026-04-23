from pathlib import Path

verse = "Somewhere over the rainbow\n" \
        "Way up high\n" \
        "There's a land that I heard of\n" \
        "Once in a lullaby\n\n"

path= Path.cwd() / "ClassFiles" / "Song.txt"
if path.exists():
    print("Adding more lyrics to the song.")
else:
    print("Writing the song for the first time.")

with path.open(mode="a") as file: #append
    file.write(verse)       

exit(0)

pathhome = Path.home()
# print (f"Home directory: {pathhome}")
path = Path.cwd() / "ClassFiles" / "Story.txt"
# print (f"Path to file: {path}")

if path.exists():
    with path.open(mode="r") as file: #read, w write, a append, rb read binary, wb write binary, ab append binary
        print(f"File {path.name} is now open.")
        contents = file.read()
        # contents = file.readlines()
        # while True:
        #     line = file.readline()
        #     if not line:
        #         break
        #     modified_line = line.replace(" ", ":")
        #     print(f"{modified_line}", end="")

    # print(f"{contents}")
    # print(f"File {path.name} is now closed.")
# else:
#     print(f"File {path.name} does not exist.")


output = Path.cwd() / "ClassFiles" / "Output.txt"
if output.exists():
    print(f"WARNING: File {output.name} already exists.")
    
with output.open(mode="w") as file:
    # cs = file.write(contents)  
    # print(f"{cs} characters were written to {output.name}.")
    file.writelines(contents)
    print(f"Characters were written to {output.name}.")


