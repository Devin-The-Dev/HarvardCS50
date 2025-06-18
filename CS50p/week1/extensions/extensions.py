### This is very similar to the "Bank" problem set ###
# Get user input
# Set letters to lowercase and strip spaces for easier conditionals
fileName = input("File name: ").lower().strip(" ")

# Does "." exist between the string, and not at the end?
if "." in fileName and not fileName.endswith("."):
    # Run a match statement
    # Convert string to list and collect the last element
    match fileName.split(".").pop():
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")
