import os

fileList=["index.html","style.css","script.js"]

uniStyleFile = os.getcwd()
uniStyleFile += "/uni.css"

#Styling flex string creater (for universal)
def styleGenerator(dir):
    styleContent = ''
    with open(uniStyleFile)  as styleFile:
        styleContent = styleFile.read()
    return styleContent

boilerHTMLContent = "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\t<title>Boiler</title>\n</head>\n<body>\n\n</body>\n</html>"
boilerCSSContent = styleGenerator(uniStyleFile)
boilerJSContent = ""
fileContent=[boilerHTMLContent,boilerCSSContent,boilerJSContent]

targetFolder = "./WebFolder/"

for index,file in enumerate(fileList):
    if os.path.exists(targetFolder) == False:
        os.mkdir(targetFolder)

    with open(targetFolder+file,"w") as fn:
        fn.write(fileContent[index])

print("File Successively created!")
