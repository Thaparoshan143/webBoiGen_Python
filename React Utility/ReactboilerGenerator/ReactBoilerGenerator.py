import os

fileNameList=input().split()

#here I am using boiler plate as the text itself without importing from file. 
#we can create the boiler page template and read and write to other coreeseponding file as well
def generateBoilerJS(title):
    importFile="import \"../"+f'uni.css'+"\"\n"+"import \"./"+f'{title}.css'+"\"\n\n"
    new_boiler=importFile+f'function {title}()\n'+"{\n\treturn(\n\t\t"+ f'<div className="{title}">{title}</div>\n'+"\t)\n}\n\n"+f'export default {title}'
    return new_boiler

#get current directory
currDirectory=os.getcwd()
uniDirectory=os.getcwd()
uniDirectory=uniDirectory+'/React Utility/uni.css'
offset="/src/"

#Check if the directory is already created or not
if not os.path.exists(currDirectory+offset+"./Components"):
    os.mkdir(currDirectory+offset+"./Components") 
else:
    print("Directory already exist so! Overwriting everthing!")


#create universal styling for everthing like common styling
with open(currDirectory+offset+"/uni.css","w") as nfuni:
    uniFile=open(uniDirectory,"r")
    nfuni.write(uniFile.read())
    uniFile.close()

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






