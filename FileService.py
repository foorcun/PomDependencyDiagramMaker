import json

class FileService:
    @staticmethod
    def read_json_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
    @staticmethod
    def readFile(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        
    @staticmethod
    def writeFile(data, file_path):
        # file_path = 'projectDiagram.md'
        with open(file_path, 'w') as file:
            file.write(data)
        print(f"Data written to '{file_path}'")

# # Example usage
# file_path = './configs/mobile_required_version.json'  # Assuming the file is named 'data.json' and located in the same directory as the script

# data = JsonUtil.read_json_from_file(file_path)
# if data:
#     print(data)  # Output: The content of the JSON file as a Python dictionary



import xml.etree.ElementTree as ET

def read_xml(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Print root element
    print(f"Root element: {root.tag}")
    
    # Iterate through child elements
    for child in root:
        print(f"Child element: {child.tag}")
        for subchild in child:
            print(f"Subchild element: {subchild.tag}, Attribute: {subchild.attrib}, Text: {subchild.text}")

if __name__ == "__main__":
    file_path = 'example.xml'
    read_xml(file_path)



