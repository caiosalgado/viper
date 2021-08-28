from pathlib import Path
import winshell


desktop = Path(winshell.desktop())
folder_name = 'PythonProjects'
documents_path = Path(winshell.folder('CSIDL_PERSONAL')) / folder_name
env_path = documents_path / 'env' 
venv_interpreter = Path(env_path / 'Scripts/jupyter-lab.exe').absolute()
link_filepath = desktop / "Jupyter Lab.lnk"
work = documents_path / 'notebooks'
icon = Path('./icon.ico').absolute()

with winshell.shortcut(str(link_filepath)) as link:
    link.path = str(venv_interpreter)
    link.description = "Launch Jupyter Lab with Python virtual environment"
    link.working_directory = str(work)
    link.icon_location = (str(icon), 0)

win32_cmd = str(Path(winshell.folder('CSIDL_SYSTEM')) / 'cmd.exe')
icon = Path('./terminal.ico').absolute()
link_filepath = desktop / "Python Env.lnk"
work = documents_path / 'scripts' 
arg_str = "/K " + str(env_path / "Scripts" / "activate.bat") + " " + str(env_path) 

with winshell.shortcut(str(link_filepath)) as link:
    link.path = win32_cmd
    link.description = "Launch Python with virtual environment"
    link.arguments = arg_str
    link.icon_location = (str(icon), 0)
    link.working_directory = str(work)

