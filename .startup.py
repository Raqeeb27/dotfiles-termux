import os
import sys
from random import choice
from subprocess import run
try:
    from colorama import Fore, Style
except ImportError:
    print("\nERROR!\nThis startup script requires 'colorama' module.\nPlease install it with 'pip install colorama' commamd and try again.")
    sys.exit(1)


RED = Fore.RED
DIM = Style.DIM
BLUE = Fore.BLUE
CYAN = Fore.CYAN
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
BRIGHT = Style.BRIGHT
RESET = Style.RESET_ALL


USERNAME = os.getenv("DOTFILES_USERNAME")
HOME = os.getenv("HOME", "home")
BASHRC = os.path.join(HOME, ".bashrc")
ZSHRC = os.path.join(HOME, ".zshrc")
FISH_CONFIG = os.path.join(HOME, ".config", "fish", "config.fish")
SHELL_FILES = [BASHRC, FISH_CONFIG, ZSHRC]


def startup_setup():
    from shlex import quote
    try:
        print(f"\n{BRIGHT}{YELLOW} " + " Shell Startup Setup ".center(31, "-"))
        input_username = input(f"\nEnter your USERNAME to display on startup of the shell: {CYAN}").strip()
    except (KeyboardInterrupt, EOFError):
        print(f"{RED}{BRIGHT}\n\nKeyboard Interrupt !!!\n\nExiting without setting up the required environment variable....{RESET}\n")
        sys.exit(1)

    if len(input_username) == 0:
        print(f"\n{RED}{BRIGHT}Please input a valid Username.\nExiting without setting up the required environment variable....\n{RESET}")
        sys.exit(1)

    run(f'export DOTFILES_USERNAME="{input_username}"', shell=True)
    os.environ["DOTFILES_USERNAME"] = input_username

    for shell_file in SHELL_FILES:
        if os.path.exists(shell_file):
            os.system(f"sed -i '/^export DOTFILES_USERNAME=/d' {shell_file}")
            os.system(f"sed -i '/python ~\\/.startup.py/i export DOTFILES_USERNAME={quote(input_username)}' {shell_file}")

    print(f"\n\n{GREEN}{BRIGHT}DOTFILES_USERNAME variable set as \"{MAGENTA}{input_username}{GREEN}\" in {BLUE}{[os.path.basename(i) for i in SHELL_FILES if os.path.exists(i)]}{GREEN}.\n\n{YELLOW}Please restart your shell.\n{RESET}")
    sys.exit(0)


def check_username():
    if not USERNAME:
        os.system("clear")
        print(f"\n{RED}{BRIGHT}Startup Error: 'DOTFILES_USERNAME' variable not set!{RESET}\n")
        print(f"{CYAN}{BRIGHT}python ~/.startup.py --setup{RESET}\n")
        print(f"{YELLOW}Run the above command to perform the required setup.\n{RED}(OR)\n{YELLOW}Manually add the below command before the {BLUE}'python ~/.startup.py'{YELLOW} line to your {GREEN}Shell startup file.{RESET}\n")
        print(f"{BLUE}export DOTFILES_USERNAME=\"YOUR_USERNAME\"{RESET}\n\n")
        sys.exit(1)


def startup_display():
    # Get parent PID (the shell that launched Python)
    ppid = os.getppid()

    result = run(
        ["ps", "-p", str(ppid), "-o", "comm="],
        capture_output=True,
        text=True,
        check=True
    )

    shell = os.path.basename(result.stdout.strip())
    welcome_commands = f"clear; \
    date +\"%A, %d %B %Y, %I:%M:%S %p\" | lolcat; \
    echo; \
    echo \"Welcome back, {USERNAME.upper()} @ Termux.{shell.lower()}\" | lolcat"

    COWS = [
        "default",
        "moose",
        "tux",
        "sus"
    ]

    COMMANDS = [
        "echo; pokemon-colorscripts -r --no-title",
        "echo; fastfetch --pipe false",
        f"fortune | cowsay -f {choice(COWS)} | lolcat",
        "echo; figlet ASSALAMU | lolcat; figlet ALAIKUM | lolcat",
        f"echo; figlet ASSALAMU | lolcat; figlet ALAIKUM | lolcat; figlet {USERNAME.upper()} | lolcat",
    ]

    os.system(welcome_commands)

    random_command = choice(COMMANDS)
    os.system(random_command)

    os.system(f"figlet -f small '   MY {shell.upper()}' | lolcat; echo")

    os.system(f"python {HOME}/.update_termux.py > /dev/null 2>&1 &")


if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == "--setup":
        startup_setup()

    check_username()
    startup_display()

