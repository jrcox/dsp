# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > grep:  search for a specific string within a file /n
    find:  looks for a file /n
    pwd: print working directory, tell you where you are
    mkdir:  make a new directory
    cd:  change directory
    ls:  list everything within current directory
    rmdir:  remove directory
    pushd:  takes current directory and pushes into a list for later, then changes to another directory ("save where i am and go to this new place")
    popd:  takes last directory you pushed and "pops" it off, taking you back to where you were
    touch:  makes an empty file
    cp:  copy a file
    mv:  moves a file
    less:  displays a file within the terminal, need to press 'q' to exit file display
    cat:  streams a file, no paging or stopping required
    rm:  remove a file
    pipes:  |  command on left is piped to command on right
    < :  send input from file on right to program on the left
    > :  takes output of command on left and writes to file on the right
    >> :  takes output of command on left, appends it to file on right
    wildcard matching:  use * to say 'anything'
    man:  will find information on command
    apropos:  will try to find relevant commands/info if you dont know the command
    sudo:  the magic word!  runs a command with elevated privelages, requires a user password
    chmod:  "change mode"  will change the permissions of files or directories
    chown:  "change ownder"  will change the ownder and group of files, directories and links
    

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > 'ls' will list the contents of a directory.  
    'ls -a' will list the contents including hidden files.
    'ls -l' will list the contents of the directory in longform.  This includes details such as filename, permissions, file owner, date, etc.
    'ls -lh' will list content sizes in long form.
    'ls -la' will list the long form of hidden files.
    'ls -lah' will list the size in the long form of all files, including hidden.

---


---

What does `xargs` do? Give an example of how to use it.

> > 'xargs' is used to build and execute command lines from standard input.  It can be used to remove or do some operation on a long list of file names which were produced by using the find and/or grep commands.

Example:   find ./documents -print | xargs grep "data"   Will find files in the documents folder, pipe thorugh to the grep command to look for files with the word "data" within them.

---

