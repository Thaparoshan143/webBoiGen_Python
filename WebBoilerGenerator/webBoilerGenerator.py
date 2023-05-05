
fileList=["index.html","style.css","script.js"]


#Styling flex string creater (for universal)
def flexCreator(dir):
    temp=f'.flex-{dir}'+'-evenly{display:flex;flex-direction:'+f'{dir}'+';justify-content:space-evenly;align-items:center;}\n'
    return temp

#create universal styling for everthing like common styling
def generateCSS():
    UniSelector='*{padding:0px;margin:0px;box-sizing:border-box;}\n'
    BaseStyling='html{font-size:1rem;scroll-behavior:smooth;}\n'
    UniFlexClass=flexCreator("row")+flexCreator("column")
    UniStyling=UniSelector+BaseStyling+UniFlexClass
    return UniStyling    

boilerHTML="<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\t<title>Boiler</title>\n</head>\n<body>\n\n</body>\n</html>"
boilerCSS=generateCSS()
boilerJS=""
fileContent=[boilerHTML,boilerCSS,boilerJS]


for index,file in enumerate(fileList):
    with open("./"+file,"w") as fn:
        fn.write(fileContent[index])

print("File Successively created!")
