# filename: initproject.py

import os
import argparse

def create_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def read_file_content(filename):
    # Get the absolute path of the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the file
    file_path = os.path.join(script_dir, filename)
    with open(file_path, 'r') as f:
        return f.read()

def main(project_name):
    os.makedirs(project_name, exist_ok=True)

    settings_content = read_file_content('settings.py')
    create_file(os.path.join(project_name, 'settings.py'), settings_content)

    main_test_content = read_file_content('run.py')
    create_file(os.path.join(project_name, 'run.py'), main_test_content)

    print(f"Project {project_name} has been created.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Initialize a new project.')
    parser.add_argument('project_name', help='The name of the project to initialize')

    args = parser.parse_args()
    main(args.project_name)