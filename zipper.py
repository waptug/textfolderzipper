import os
import zipfile
import shutil

def get_all_folders(src_path):
    """ Get all folders in a nested structure """
    all_folders = []

    for root, dirs, files in os.walk(src_path):
        all_folders.append(root)

    return all_folders

def zip_txt_files(src_folder):
    """ Zip all .txt files in a folder and return the zip file path """
    zip_name = os.path.basename(src_folder) + '.zip'
    zip_path = os.path.join(src_folder, zip_name)

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in os.listdir(src_folder):
            if file.endswith('.txt'):
                zipf.write(os.path.join(src_folder, file), file)

    return zip_path

def copy_to_plrpacks(src_zip):
    """ Copy a zip file to plrpacks """
    if not os.path.exists('plrpacks'):
        os.mkdir('plrpacks')

    shutil.copy(src_zip, 'plrpacks')
    return os.path.join('plrpacks', os.path.basename(src_zip))

def create_html(zip_files):
    """ Create an HTML with links to the zip files """
    with open('plrpacks/links.html', 'w') as htmlf:
        htmlf.write('<html>\n<head>\n<title>Zip Links</title>\n</head>\n<body>\n')
        
        for zfile in zip_files:
            basename = os.path.basename(zfile)
            htmlf.write(f'<a href="{basename}">{basename}</a><br>\n')
        
        htmlf.write('</body>\n</html>')

def main():
    src_path = input("Enter the path of the source folder to process: ")

    all_folders = get_all_folders(src_path)
    zip_files = []

    for folder in reversed(all_folders):
        zip_path = zip_txt_files(folder)
        new_zip_path = copy_to_plrpacks(zip_path)
        zip_files.append(new_zip_path)

    create_html(zip_files)

if __name__ == "__main__":
    main()
