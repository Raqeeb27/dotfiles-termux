# <span style="vertical-align: middle;"><img src='assets/Readme-Images/Termux_Logo.png' alt="Termux_Logo" style="width:60px;height:auto; margin-bottom: -3px;"> dotfiles-termux</span>

### Configuration files and setup scripts for Termux.
A quick way to set up your Termux environment with custom dotfiles, aliases, and useful settings.

---

## ✨ Features
- Preconfigured shells (bash, fish, zsh) with useful aliases  
- Clean and organized prompt/environment setup  
- Automatic backup of your existing configuration before changes  
- Flexible: install permanently or roll back anytime  
- Simple to extend and customize  

---

## 📦 Requirements

Before installing, ensure your Termux packages are up to date:

```bash
apt update && apt upgrade -y
```

Install the required packages:

```bash
apt install git stow rsync -y
```

---

## 🚀 Initial Setup  
### Clone the Repository

First, clone the dotfiles repository to your Termux home directory:

```bash
git clone https://github.com/Raqeeb27/dotfiles-termux.git ~/dotfiles-termux
```

### Backup and Apply New Dotfiles

This step backs up your existing configuration and applies the new dotfiles from this repository. You can restore your previous setup later if needed:

```bash
cd ~/dotfiles-termux
git switch -c adopt-backup
stow --adopt -t ~ .
git add -A
git commit -m "chore: Backup existing configs"
git switch main
git restore .
```

---

## 🤩 User Interest
> 💡 Run these steps only after completing the Initial Setup section.

### Install dotfiles permanently
> ⚠️ Caution: Your previous configuration will be lost after this step.

If you are happy with the new configuration and want to make it your default:

```bash
cd ~/dotfiles-termux
stow -D -t ~ .
rm -rf ~/dotfiles-termux/.git ~/dotfiles-termux/README.md
rsync -av ~/dotfiles-termux/ ~
cd ~
rm -rf ~/dotfiles-termux
```

### Restore your previous configuration
Not a fan? No problem — you can roll back to your previous setup:

```bash
cd ~/dotfiles-termux
stow -D -t ~ .
git switch adopt-backup
rm -rf ~/dotfiles-termux/.git ~/dotfiles-termux/README.md
rsync -av ~/dotfiles-termux/ ~
cd ~
rm -rf ~/dotfiles-termux
```

---

## ⚙️ Customizing
- Add or edit aliases in `~/.termux_aliases`
- Adjust prompts, colors, and shell behavior in `~/.bashrc`, `~/.config/fish/config.fish`, or `~/.zshrc`

---

## 📝 Notes
- Designed specifically for Termux on Android  
- Existing configuration files are backed up before any changes  
- Permanent installation is optional; you can test the setup first  

---

## 🤝 Contributing
Contributions and suggestions are welcome.
Feel free to fork the repo, make changes, and open a pull request.
