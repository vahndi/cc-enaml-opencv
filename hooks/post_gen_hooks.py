import subprocess

subprocess.run(
    args=['conda', 'env', 'create', '-f', 'environment_{{cookiecutter.platform}}.yml'],
    shell=True
)
