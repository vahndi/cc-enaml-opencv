import subprocess

# activate environment and run app
commands = """
/anaconda3/bin/conda env create -f environment_{{cookiecutter.platform}}.yml
source activate {{cookiecutter.env_name}}
python ./{{cookiecutter.project_name}}/run_{{cookiecutter.project_name}}.py
"""
subprocess.run(
    args=commands, shell=True
)
