###############################################################################
# Authour: Ben Haubrich                                                       #
# File: webapp.py                                                             #
# Data: January 2nd, 2025                                                     #
# Synopsis: Renders the web application from jinja templates to static html   #
#           files.                                                            #
###############################################################################
#Python Virtual Environment:
#https://docs.python.org/3/tutorial/venv.html
#Once activated, any pip install is local to the virtual environment

#Jinja rendering:
#https://atufashireen.medium.com/creating-templates-with-jinja-in-python-3ff3b87d6740

#htmx:
#https://htmx.org/
from jinja2 import FileSystemLoader, Environment, Template
import os
from pathlib import Path
from fileToArrayOfBytes import fileToArrayOfBytes

def listFilesFromDir(directory):
    files = []
    for file in os.listdir(directory, extension):
        if file.endswith(extension):
            files.append(file)
    return files

def loadTemplates(templateDirectory):

    templateFiles = listFilesFromDir(templateDirectory)

    loadedTemplates = []

    loader = FileSystemLoader(searchpath = templateDirectory)
    env = Environment(loader=loader)

    for jinjaTemplateFile in templateFiles:
        loadedTemplates.append(env.get_template(jinjaTemplateFile))

    return loadedTemplates

def renderTemplates(loadedTemplates):
   
    renderedTemplates = []

    for template in loadedTemplates:
        renderedTemplates.append((template.render(webAppName="Automatic Pet Feeder"), template.filename))

    return renderedTemplates

def publishHtmls(renderedHtmls):
   for renderedHtml in renderedHtmls:
       filename = Path(renderedHtml[1]).stem
       Template(renderedHtml[0]).stream(name="AutomaticPetFeederWebapp").dump("./Static/" + filename + ".html")

if __name__ == "__main__":
    jinjaTemplates = loadTemplates("./Templates")
    renderedHtmls = renderTemplates(jinjaTemplates)
    publishHtmls(renderedHtmls)

    htmls = listFilesFromDir("./Static", "html")
    for html in htmls:
        fileToArrayOfBytes("./Static" + html, "./Embed")

    javascripts = listFilesFromDir("./Static/Javascript", "html")
    for javascript in javascripts:
        fileToArrayOfBytes("./Static/Javascript" + javascript, "./Embed")
