import os
import subprocess
from pathlib import Path

# install dependecies for windows
def install():
    subprocess.run(['pip',  'install', 'winshell'], check=True, capture_output=True)
    subprocess.run(['pip',  'install', 'pypiwin32'], check=True, capture_output=True)
    print('please run the script again')


# create notebooks folder
def main():
    from winshell import folder

    path = Path().absolute()
    documents_path = Path(folder('CSIDL_PERSONAL'))
    folder_name = 'PythonProjects'
    os.chdir(documents_path)
    os.mkdir(folder_name)
    os.chdir(documents_path / folder_name)
    os.mkdir('notebooks')
    os.mkdir('scripts')

    # Create virtual environment
    subprocess.run(['python', '-m', 'venv', 'env'], check=True, capture_output=True)

    packages = [
        'numpy',
        'pandas',
        'jupyter',
        'jupyterlab',
         'unidecode',
         'openpyxl',
         'xlrd',
         'XlsxWriter',
        'winshell'
    ]

    for package in packages:
        print(package)
        subprocess.run(['env/Scripts/pip', 'install', package], check=True, capture_output=True)

    os.chdir(path)

    # create desktop shortcuts
    subprocess.run([documents_path / folder_name / 'env/Scripts/python', 'create_shortcut.py'], check=True, capture_output=True)


if __name__ == '__main__':
    
    try:
        main()

    except:
        install()