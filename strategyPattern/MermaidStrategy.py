from strategyPattern.Strategy import Strategy
from pomXmlToJson import pomXmlToJson
import json


class MermaidStrategy(Strategy):
    def doOperation(self,pomContent, parent):
        diagramContent= "```mermaid\n graph TD\n" # top

        diagramContent = diagramContent + itemBuilderMermaid(pomContent, parent) + "\n"

        diagramContent = diagramContent.rstrip("\n")
    
        diagramContent = diagramContent + "\n```" # bottom
        return diagramContent
    


def itemBuilderMermaid(pomContent, parent):

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