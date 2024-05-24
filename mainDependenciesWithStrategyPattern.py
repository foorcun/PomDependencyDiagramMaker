
from FileService import FileService
from pomReader import find_pom_files
# from xmlToJson import xml_to_json
from pomXmlToJson import pomXmlToJson

#include json library
import json

from strategyPattern.MermaidStrategy import MermaidStrategy
from strategyPattern.Context import Context

from getParentFolder import getParentFolder

def main():
    # print("hello world")

    # parent = "mblService-server"
    # pomPath = "C:\\DEV\\Mobile_projects\\mobile_backend\\webapps\\mblService\\mblService-server\\pom.xml"

    # parent = "mblModule-api"
    # pomPath = "C:\DEV\Mobile_projects\mobile_backend\modules\mblModule\mblModule-api\pom.xml"


    parent = "mblService-api"
    pomPath = "C:\\DEV\\Mobile_projects\\mobile_backend\\webapps\\mblService\\mblService-api\\pom.xml"
    

    pomContent = FileService.readFile(pomPath)
    # print(pomContent)

    # print(itemBuilder(pomContent,parent))
    # itemBuilder(pomContent,parent)
    
    context = Context(MermaidStrategy())
    mermaidContent = context.execute_strategy(pomContent, getParentFolder(pomPath))
    print(mermaidContent)


    # writeMermaid(parent, pomContent)

def writeToFile(content):
    FileService.writeFile(content, "output/dependenciesDiagram.md")



if __name__ == "__main__":
    main()