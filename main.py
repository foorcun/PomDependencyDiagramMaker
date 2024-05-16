
from FileService import FileService
from pomReader import find_pom_files
# from xmlToJson import xml_to_json
from pomXmlToJson import pomXmlToJson

#include json library
import json

def main():
    # print("hello world")

    projectDirectory = "C:\\DEV\\Mobile_projects\\coreservices"
    pomsArray = find_pom_files(projectDirectory)


    diagramContent= "```mermaid\n graph TD\n" # top

    for pomPath in pomsArray:
        # print(pom)
        # pomContent = FileService.readFile(pomsArray[0])
        pomContent = FileService.readFile(pomPath)
        diagramContent = diagramContent + itemBuilder(pomContent) + "\n"

    diagramContent = diagramContent + "```" # bottom
    FileService.writeFile(diagramContent)


def itemBuilder(pomContent):

    pomJson = pomXmlToJson(pomContent)

    # print(pomJson)

    #convert string to  object
    json_object = json.loads(pomJson)

    artifactId = json_object["project"]["artifactId"]
    parent = json_object["project"]["parent"]["artifactId"]
    print(artifactId)
    print(parent)


    diagramItem = artifactId + " --> " + parent
    return diagramItem
    # print(diagramItem)

    # diagramContent= "```mermaid\n graph TD\n" # top
    # diagramContent = diagramContent + diagramItem + "\n"
    # diagramContent = diagramContent + "```" # bottom
    
    # FileService.writeFile(diagramContent)






    # read file
    xml_string = FileService.readFile("C:\\DEV\\Mobile_projects\\coreservices\\servers\\coreServicesJBoss\\pom.xml")



if __name__ == "__main__":
    main()