import os

fileNameList=input().split()

#here I am using boiler plate as the text itself without importing from file. 
#we can create the boiler page template and read and write to other coreeseponding file as well
def generateBoilerJS(title):
    importFile="import \"../"+f'uni.css'+"\"\n"+"import \"./"+f'{title}.css'+"\"\n\n"
    new_boiler=importFile+f'function {title}()\n'+"{\n\treturn(\n\t\t"+ f'<div>{title}</div>\n'+"\t)\n}\n\n"+f'export default {title}'
    return new_boiler

#Styling flex string creater (for universal)
def flexCreator(dir):
    temp=f'.flex-{dir}'+'-evenly{display:flex;flex-direction:'+f'{dir}'+';justify-content:space-evenly;align-items:center;}\n'
    return temp

#get current directory
currDirectory=os.getcwd()
offset="/src/"

#Check if the directory is already created or not
if not os.path.exists(currDirectory+offset+"./Components"):
    os.mkdir(currDirectory+offset+"./Components") 
else:
    print("Directory already exist so! Overwriting everthing!")


#create universal styling for everthing like common styling
with open(currDirectory+offset+"/uni.css","w") as nfuni:
    UniSelector='*{padding:0px;margin:0px;box-sizing:border-box;}\n'
    BaseStyling='html{font-size:1rem;scroll-behavior:smooth;}\n'
    UniFlexClass=flexCreator("row")+flexCreator("column")
    UniStyling=UniSelector+BaseStyling+UniFlexClass
    nfuni.write(UniStyling)

#new directory update
offset="/src/"
currDirectory=currDirectory+offset+"Components"

#create all the inputed files inside directory
for fileName in fileNameList:
    with open(currDirectory+"/"+fileName+".js",'w') as nfjs:
        boilerText=generateBoilerJS(fileName)
        nfjs.write(boilerText)
        nfjs.close()
    with open(currDirectory+"/"+fileName+".css","w") as nfcss:
        pass
        nfcss.close()






