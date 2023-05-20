
<h2>How to use:</h1>

1. Open the react project in Vscode (Open directory react created i.e react name directory)
2. clone it in the same dir (i.e react project dir)
3. if it is fresh new project
    i. run the newSetUp.py
    ii. run ReactBoilerGenerator for the known component creation (know more from below..)
    iii. uni.css is imported for all file and have common styling (change if not required)

<h3>If already existing project:</h3>
<li> run newFileGenerator.py, write component name to create</li>
    i. js file and css will be created of respective name
    ii. export default used and uni.css imported


<h3>More Details:</h3>

Here First Boiler Generator is for general/normal for creating using HTML, CSS, JS (plain) with file generated as:
#weBoilerGenerator
    <li> index.html</li>
    <li> style.css</li>
    <li> script.js</li>
    along with this it also generate some boiler template to use it for.
Here the string are hard coded, it can also be configured from the file if needed.
(#Note : Linking of css is missing. Watch out for that)

Second is especially designed to work with React js library

#ReactBoilerGenerator
Boiler are generated based on input, user is given chance to input filename/components name to create as:
    <li> input name of components</li>
    <li> corresponding named compoents is generated with export deafult and respective css is also genereated</li>
    <li> values here are also hard coded</li>
    <li> import of css and uni css is done but if required more import change varibale correspondence name</li>
    <li> uni is generated outside but the compoents are generated inisde compoents directory for organizing</li>
    (#Note: uni.css generated is the copy of the file uni.css residing inside React Utility Folder, if any changes in uni.css is required, just insert/update the required changes and save the file.)

#newFileGenerator:
    specially desgined to serve the need to create the components files in react with corresponding css file
    <li> just type component name </li>
    <li> relative path is taken so program reside matter</li>
    <li> while loop used and terminates if input is '0'</li>

Here ReactBoilerGenerator is mostly for the purpose of creating already though components at the start of projects
and newFileGenerator can be used for creating new components on the way to add new ones with no worry with program running in background.

#newSetUp:
    specialy designed to serve the purpose of :
    <li> remove the unnecessary files</li>
    <li> clear the content of few file</li>
    <li> modify the files for the required content</li>

all the file list are in the list, they are seperated by the folder and the way they are add, modify, erase ...

#all the code base can be update as per required after downloading! 

