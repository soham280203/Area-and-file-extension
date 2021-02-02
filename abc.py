input=input("Input your file: ") #takes input in format sample.__
fn=input.split(".") #split the  input name
file_exten=fn[-1]
if(file_exten=='py'):
    print("The extension of the file is 'python'")
else:
    print("The extension of the file is ",file_exten)
