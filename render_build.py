import subprocess

def run_command(command):
    try:
        subprocess.run(
            command,
            shell=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e)

def main():
    # Commands to run
    commands = [
        "docker-compose up -d",
        "python manage.py migrate",
        "python manage.py createsocial",
        "python manage.py createsuperuser",
        "python manage.py runserver"
    ]

    # Run each command
    for command in commands:
        run_command(command)

if __name__ == "__main__":
    main()
