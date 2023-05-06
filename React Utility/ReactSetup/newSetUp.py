import os

fileNamesPublic=["favicon.ico","logo192.png","logo512.png"]
fileNamesSrc=["App.test.js","logo.svg","reportWebVitals.js","setupTests.js"]
fileNamesSrcEmpty=["App.css","index.css"]
fileNamesSrcJSModify=["index.js","App.js"]

indexTemplateContent="import React from 'react';\nimport ReactDOM from 'react-dom/client';\nimport './index.css';\nimport App from './App';\n\nconst root = ReactDOM.createRoot(document.getElementById('root'));\nroot.render(\n\t<React.StrictMode>\n\t\t<App />\n\t</React.StrictMode>\n);"
appTemplateContent="import './App.css';\n\nfunction App() {\n\treturn (\n\t\t<div className=\"App\">\n\n\t\t</div>\n\t);\n}\n\nexport default App;"

modifyContent=[indexTemplateContent,appTemplateContent]

currDir=os.getcwd()

#remove the public files from above list
for file in fileNamesPublic:
    os.remove(currDir+"/public/"+file)

# remove file from src
for file in fileNamesSrc:
    os.remove(currDir+"/src/"+file)

# removing the content without removing file
for file in fileNamesSrcEmpty:
    with open(currDir+"/src/"+file,"w") as nf:
        pass

# modifying the content for use
for index,file in enumerate(fileNamesSrcJSModify):
    with open(currDir+"/src/"+file,"w") as nf:
        nf.write(modifyContent[index])

