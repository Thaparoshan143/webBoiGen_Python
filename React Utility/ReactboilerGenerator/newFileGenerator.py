import os

def generateBoilerJSContent(title):
    importFile="import \"../"+f'uni.css'+"\"\n"+"import \"./"+f'{title}.css'+"\"\n\n"
    new_boiler=importFile+f'function {title}()\n'+"{\n\treturn(\n\t\t"+ f'<div>{title}</div>\n'+"\t)\n}\n\n"+f'export default {title}'
    return new_boiler

offset="/src/"
fileType = ".js"
# fileType = ".tsx"

# determines if we need to produce the styling file of same name i.e css file 
includeStylingFile = True

while True:
    fileName=input().split()

    currDir=os.getcwd()
        
    if fileName[0]=='0':
        print("Program Exited")
        break

    for file in fileName:
        with open(currDir + offset + file + fileType, "w") as nfjs:
            nfjs.write(generateBoilerJSContent(file))
        if includeStylingFile:
            with open(currDir + offset + file + ".css", "w") as nfcss:
                pass
        print(file + fileType + "and " + file + ".css " + "file Created!")
