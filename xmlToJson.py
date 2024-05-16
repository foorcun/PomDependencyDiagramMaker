import xml.etree.ElementTree as ET
import json

from FileService import FileService

def xml_to_json(xml_string):
    root = ET.fromstring(xml_string)
    def parse_element(element):
        parsed_data = {}
        if element.text:
            parsed_data["text"] = element.text.strip()
        parsed_data.update({k: v for k, v in element.attrib.items()})
        for child in element:
            child_data = parse_element(child)
            if child.tag in parsed_data:
                if not isinstance(parsed_data[child.tag], list):
                    parsed_data[child.tag] = [parsed_data[child.tag]]
                parsed_data[child.tag].append(child_data)
            else:
                parsed_data[child.tag] = child_data
        return parsed_data

    return json.dumps({root.tag: parse_element(root)}, indent=4)


def simplifyJson(jsonString):
    return json.dumps(json.loads(jsonString), indent=4)

# xml_string = '''<root><child name="value">text<   /child></root>'''
xml_string = FileService.readFile('example.xml')
xml_string = FileService.readFile("C:\\DEV\\Mobile_projects\\coreservices\\servers\\coreServicesJBoss\\pom.xml")

print(xml_to_json(xml_string))