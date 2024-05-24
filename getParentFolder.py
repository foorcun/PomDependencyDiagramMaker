import os


def getParentFolder(pomPath):
    # Extract the directory name
    directory = os.path.dirname(pomPath)

    # Extract the 'mblService-api' part
    parentFolder = os.path.basename(directory)

    return parentFolder



pomPath = "C:\\DEV\\Mobile_projects\\mobile_backend\\webapps\\mblService\\mblService-api\\pom.xml"

print(getParentFolder(pomPath))