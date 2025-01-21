#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
import os

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

print(f"Current working directory is: {os.getcwd()}")

with open("Input/Names/invited_names.txt") as i_name:
    invited_names = i_name.readlines()

for n in invited_names:
    name = n.strip("\n")
    with open(f"Output/ReadyToSend/letter_to_{name}.txt",mode="w") as output_file:
        with open("Input/Letters/starting_letter.txt") as f:
            contents = f.readlines()

        new_var1 = contents[0].replace("name",name)
        new_var2 = new_var1.replace("[", "")
        new_var = new_var2.replace("]", "")

        contents[0] = new_var
        for line in contents:
            output_file.write(line)

