#!/bin/awk -f

/^([^ #]+)([ \t]+)([^ ]+)#?/ {
    #$2 -> conf name 
    #$1 -> path to conf
    
    #Nor file nor symlink exist
    if (system("test -e "$2$1) != 0) {
        system("sudo ln -s ~/.dotfiles/"$1" "$2)
    }

    #Symlink exists
    else if (system("test -L "$2$1) == 0) {
        print "The symlink "$2$1" already exists!"
        if (yn("Override it?")) {
            print "Old link pointed at:"
            system("readlink "$2$1)

            system("sudo rm "$2$1)
            system("sudo ln -s ~/.dotfiles/"$1" "$2)
    }
        
    #File/dir exist
    else if (system("test -e" $2$1) == 0) {
        print "The file/dir "$2$1" already exists!"
        if (yn("Override it?")) {
            system("copy -ar "$2$1" ~/.dotfiles/install/bak/")
            print "A copy has been made in ~/.dotfiles/install/bak/"
        }
    }
    
}

function yn(prompt) {
    print prompt" (y/N):"
    getline response < "-"
    return (response ~ /^(y|Y).*$/)
}

