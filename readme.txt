Here First Boiler Generator is for general/normal for creating using HTML, CSS, JS (plain) with file generated as:
    - index.HTML
    - style.CSS
    - script.JS
    along with this it also generate some boiler template to use it for.
Here the string are hard coded, it can also be configured from the file if needed.

Second is especially designed to work with react js library

ReactBoilerGenerator
Boiler are generated based on input, user is given chance to input filename/components name to create as:
    - input name of components
    - corresponding named compoents is generated with export deafult and respective css is also genereated
    - values here are also hard coded
    - import of css and uni css is done but if required more import change varibale correspondence name
    - uni is generated outside but the compoents are generated inisde compoents directory for organizing

newFileGenerator:
    specially desgined to serve the need to create the components files in react with corresponding css file
    - just type component name 
    - relative path is taken so program reside matter
    - while loop used and terminates if input is '0'

Here ReactBoilerGenerator is mostly for the purpose of creating already though components at the start of projects
and newFileGenerator can be used for creating new components on the way to add new ones with no worry with program running in background.