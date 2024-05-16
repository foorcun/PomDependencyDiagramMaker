import os

def find_pom_files(directory):
    pom_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'pom.xml':
                pom_files.append(os.path.join(root, file))
    return pom_files

def print_pom_files(pom_files):
    for pom_file in pom_files:
        print(pom_file)

# Example usage:
if __name__ == "__main__":
    # directory = input("Enter the directory path: ")
    directory = "C:\DEV\Mobile_projects\coreservices"
    pom_files = find_pom_files(directory)
    print_pom_files(pom_files)