# iTerm2 in 10 min

If you like the following iTerm2 style, you are at the right place. I will show you how to get this setup in 10 min.

![](../.gitbook/assets/image%20%282%29.png)

## Install ohmyzsh

{% hint style="info" %}
sh -c "$\(curl -fsSL [https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh](https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\)"
{% endhint %}

For reference: [https://github.com/ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)

## Install iTerm2

The simplest way to install iTerm2 is to download and unzip it: [https://iterm2.com/downloads.html](https://iterm2.com/downloads.html)

## Install the nerd-fonts

The simplest way is to clone the repo and run the install script:

{% hint style="info" %}
git clone [https://github.com/ryanoasis/nerd-fonts.git](https://github.com/ryanoasis/nerd-fonts.git)
{% endhint %}

switch to the nerd-fonts folder and run:

{% hint style="info" %}
./install.sh
{% endhint %}

## Install the powerlevel10k

just clone the repo to the ohmyzsh themes folder:

{% hint style="info" %}
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH\_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
{% endhint %}

## Config .zshrc



