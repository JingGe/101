# iTerm2 Env Setup in 10 min

If you like the following iTerm2 style, you are at the right place. I will show you how to get this setup in 10 min.

![](../.gitbook/assets/image%20%283%29.png)

## Install ohmyzsh

{% hint style="info" %}
sh -c "$\(curl -fsSL [https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh](https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\)"
{% endhint %}

Reference: [https://github.com/ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)

## Install Homebrew

{% hint style="info" %}
/bin/bash -c "$\(curl -fsSL [https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh](https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\)"
{% endhint %}

## Install iTerm2

The simplest way to install iTerm2 is to download and unzip it: [https://iterm2.com/downloads.html](https://iterm2.com/downloads.html)

## Install nerd-fonts \(optional\)

The simplest way is to clone the repo and run the install script:

{% hint style="info" %}
git clone [https://github.com/ryanoasis/nerd-fonts.git](https://github.com/ryanoasis/nerd-fonts.git)
{% endhint %}

switch to the nerd-fonts folder and run:

{% hint style="info" %}
./install.sh
{% endhint %}

## Install powerlevel10k

just clone the repo to the ohmyzsh themes folder:

{% hint style="info" %}
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH\_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
{% endhint %}

## Config .zshrc

change the theme to powerlevel10k:

{% hint style="info" %}
ZSH\_THEME="powerlevel10k/powerlevel10k"
{% endhint %}

setup the plugins:

{% hint style="info" %}
plugins=\(git gitignore autojump wd docker zsh-autosuggestions zsh-syntax-highlighting\)
{% endhint %}

### Install autojump

{% hint style="info" %}
brew install autojump
{% endhint %}

### Install zsh-autosuggestions

{% hint style="info" %}
git clone [https://github.com/zsh-users/zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions) ${ZSH\_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
{% endhint %}

### Install zsh-syntax-highlighting

{% hint style="info" %}
git clone [https://github.com/zsh-users/zsh-syntax-highlighting.git](https://github.com/zsh-users/zsh-syntax-highlighting.git) ${ZSH\_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
{% endhint %}

Don't forget to call

{% hint style="info" %}
source ~/.zshrc
{% endhint %}

## Configure Powerlevel10k

Now open a new iTerm and follow the wizard to configure the theme, if the wizard is not started automatically, type `p10k configure.`

![](../.gitbook/assets/configuration-wizard.gif)

Reference: [https://github.com/romkatv/powerlevel10k\#oh-my-zsh](https://github.com/romkatv/powerlevel10k#oh-my-zsh)

## Clone iTerm2-Color-Schemes

{% hint style="info" %}
`git clone`[`https://github.com/mbadolato/iTerm2-Color-Schemes.git`](https://github.com/mbadolato/iTerm2-Color-Schemes.git)\`\`
{% endhint %}

Go to iTerm-&gt;Preferences-&gt;Profiles-&gt;Colors, you can import color schemes from iTerm2-Color-Schemes/scheme. I personally recommend "Chester".

![](../.gitbook/assets/image%20%286%29.png)

![](../.gitbook/assets/image%20%284%29.png)

Go to iTerm-&gt;Preferences-&gt;Profiles-&gt;Text, you can change the font

![](../.gitbook/assets/image%20%282%29.png)

