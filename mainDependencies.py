
from FileService import FileService
from pomReader import find_pom_files
# from xmlToJson import xml_to_json
from pomXmlToJson import pomXmlToJson

#include json library
import json


def main():
    # print("hello world")

    # projectDirectory = "C:\\DEV\\Mobile_projects\\coreservices"
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


    writeMermaid(parent, pomContent)

def writeMermaid(parent, pomContent):
    diagramContent= "```mermaid\n graph TD\n" # top

    diagramContent = diagramContent + itemBuilderMermaid(pomContent, parent) + "\n"
    
    diagramContent = diagramContent + "```" # bottom
    FileService.writeFile(diagramContent, "dependenciesDiagram.md")


def itemBuilderMermaid(pomContent,parent):

    pomJson = pomXmlToJson(pomContent)

    # print(pomJson)

    #convert string to  object
    json_object = json.loads(pomJson)

    # print(json_object)

    dependenciesArr = json_object["project"]["dependencies"]["dependency"]
    # print(dependenciesArr)

    diagramItem = ""

    for dependency in dependenciesArr:
        # print(dependency["artifactId"])
        artifactId =  dependency["artifactId"]


        diagramItem = diagramItem + artifactId + " --> " + parent + "\n"
    return diagramItem
    # print(diagramItem)

    # diagramContent= "```mermaid\n graph TD\n" # top
    # diagramContent = diagramContent + diagramItem + "\n"
    # diagramContent = diagramContent + "```" # bottom
    
    # FileService.writeFile(diagramContent)



def itemBuilderUml(pomContent,parent):

    pomJson = pomXmlToJson(pomContent)

    # print(pomJson)

    #convert string to  object
    json_object = json.loads(pomJson)

    # print(json_object)

    dependenciesArr = json_object["project"]["dependencies"]["dependency"]
    # print(dependenciesArr)

    diagramItem = ""

    for dependency in dependenciesArr:
        # print(dependency["artifactId"])
        artifactId =  dependency["artifactId"]


        diagramItem = diagramItem + artifactId + " -- " + parent + "\n"
    return diagramItem
    # print(diagramItem)

    # diagramContent= "```mermaid\n graph TD\n" # top
    # diagramContent = diagramContent + diagramItem + "\n"
    # diagramContent = diagramContent + "```" # bottom
    
    # FileService.writeFile(diagramContent)



if __name__ == "__main__":
    main()