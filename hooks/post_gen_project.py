import subprocess
from os import listdir, getcwd
from os.path import isdir, isfile

project_dir_name = [d for d in listdir(getcwd()) if isdir(d)][0]
env_file_name = [f for f in listdir(getcwd()) if isfile(f)
                 and f.startswith('environment_')][0]

# set up environment
subprocess.run(
    args=[
        '/anaconda3/bin/conda',
        'env',
        'create',
        '-f',
        'environment_osx.yml'
    ]
)

# activate environment and run app
commands = """
conda activate %s
python ./%s/run_%s.py
""" % (
    env_file_name,
    project_dir_name,
    project_dir_name
)
subprocess.run(
    args=commands, shell=True
)
