Title: Supercharging the shell
Date: 2019-02-11 11:00
Category: shell, 
Tags: rust, cli, go, fuzzy finder
Slug: Supercharging-shell
Summary: 
Status: Published

I'm not a real power user of the command line in Linux, but I tend to use it quite regularly and is my intention to improve on that. My first step to become more proficient and increase its use was to start enhancing shell experience. The first action on this regard was to move from `bash` to `zsh`. With that change I also started useing `oh-my-zsh` to manage some goodies like themes, where I tend to gravitate to use something like `agnoster` or `powerline9k` with very few customizations.

Recently, I've discovered new "clones" of old tools: `find`, `cat`, `ls`, and `grep`. They tend to be reimagined tools and not a complete simple clone, considering the changes of computing technology and development "culture". From removed IO constrains, to the pervasive `.gitignore` file. And most importantly, in my opinion, with sane defaults providing  aready to use tool out of the box. Also, these four tools are available for Linux, Windows, and macOS.

For the four commands mentioned before, there is something in common, they're implemented in `rust`. Personally, I have a strong bias in favor of `rust` and I'd like to learn more of it and eventually become proficient (but that's a topic for another time).

## Replacements

I want to quickly and succintly review the tools that *replace* the ones already mentioned.

- [`fd`](https://github.com/sharkdp/fd) replaces `find`. This wasn't a tool that I really used, because I never managed to understand and learn how to use it. Now, `fd` has quite some advantages, for example being faster (in most cases) and easier to use by making `find`'s most common use pattern the default one.

- [`bat`](https://github.com/sharkdp/bat) is a rather modest reinterpretation of `cat`. It automatically highlights the content of the file given as input, integrates with git, and shows line numbers. Not much to say, but just a nice improvement.

- [`exa`](https://the.exa.website) replaces `ls`. In the website they very clearly exaplain how constraing from 1970 don't apply anymore and a reimagined tool could be build. Again, saner default like showing human readable file sizes in the long format and has optinal git awareness.

- [`ripgrep`](https://github.com/BurntSushi/ripgrep) is a replacement to `grep`. When compared with similar tools in benchmarks it is consistently at the top of the pack. Ignores files based on `.gitignore` out of the box.

## Fuzzy "finders" (filter)

Now, what really can supercharge the command line experience is the use of fuzzy finders. The two I've tried are ['fzf'](https://github.com/junegunn/fzf) and ['skim'](https://github.com/lotabout/skim). Both feel very similar, but `fzf` feels much more mature and works very well right out of the box where the installation already sets useful keybindings (`ctrl+R` to search the history, `ctrl+T` to recursively search and filter from the current directory). Plus it has [fuzzy completion for the comand line](https://github.com/junegunn/fzf#fuzzy-completion-for-bash-and-zsh). Moreover, `fzf` provides an extensive [library of examples](https://github.com/junegunn/fzf/wiki/examples) which can be extremely useful.

Here is when the previous set of tools start to shine, since we can combine them. For example, `fzf` and `skim` can be configured to use `fd` to do the finding and then use `bat` to do highlighted previews.

## Customizations
To finish, I'll share how all of this plays out in my `.zshrc` file

```shell
# aliases
alias ls="exa --group-directories-first"
alias cat="bat"

# fzf config
# Default command to use when input is tty
export FZF_DEFAULT_COMMAND="fd --type f --color=always"
# Use ctrl+o to open selected file(s) in VS Code
export FZF_DEFAULT_OPTS="--bind='ctrl-o:execute(code {})+abort'"
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
# Using bat as previewer 
export FZF_CTRL_T_OPTS="--preview-window 'right:60%' --preview 'bat --color=always --style=header,grid --line-range :300 {}'"
# Changing from ** to ~~ the trigger for autocompletion in shell
export FZF_COMPLETION_TRIGGER='~~'

export SKIM_DEFAULT_COMMAND="rg --files || fd || find ."

# modified from mitsuhiko dotfiles to use bat as a previewer
alias skvi='f(){ x="$(sk --bind "ctrl-p:toggle-preview" --ansi --preview="bat {} --color=always" --preview-window=right:60%:hidden)"; [[ $? -eq 0 ]] && vim "$x" || true }; f'
# doing the same for VSCode
alias skvs='f(){ x="$(sk --bind "ctrl-p:toggle-preview" --ansi --preview="bat {} --color=always" --preview-window=right:60%:hidden)"; [[ $? -eq 0 ]] && code :w "$x" || true }; f'

# Use fd (https://github.com/sharkdp/fd) instead of the default find
# command for listing path candidates.
_fzf_compgen_path() {
  fd --hidden --follow --exclude ".git" . "$1"
}

# Use fd to generate the list for directory completion
_fzf_compgen_dir() {
  fd --type d --hidden --follow --exclude ".git" . "$1"
}
```

I'm still experimenting on options and further tweaks, but this provided me already with a nicely working experience. Feel free to get inspired! And there are plenty of other tools out there, try them out and keep improving.