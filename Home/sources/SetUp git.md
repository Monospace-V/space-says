Git gh setup on Windows
Using git with gh cli on Windows


**Note some useful tips:**

*To open a command line in a specific folder:*

To open the command line in a specific folder, one may generally run the command line and run ```cd [DIRECTORY PATH]```. If your directory is in a different drive, eg G:/ drive, and your command line opens in C:/ drive, you also have to run the command ```G:``` (replace "G" with whichever other directory you wish to navigate to). You may do this before or after running cd.

The following method, however, is simpler:
You may navigate to the folder you wish to run the command line on in Windows Explorer. Now select the address bar (or press the key combination of ```Ctrl-L```). This selects the address of your directory. In this place, type ```cmd``` instead.
Basically navigate to your directory in the file explorer, hit ```Ctrl-L``` and type ```cmd```.
This opens a command line instance in your directory itself. Note that this command line instance does not have administrator privilges.

**Setting up git and gh:**

Install git.
In the event the git bin directory is not in your filesystem path, add it. This tends to happen in the case of portable install. If available, ensure you check the option to add it to your path.

Get gh cli.

In the command line, run ```gh auth login```. This will authenticate a login with a GitHub host and store your credentials, enabling you to use git from your computer.

Now when working with repositories, when creating commits (which are logs and details of specific changes), you need a username and email address to "sign" these commits. I recommend using a username and email you are comfortable showing to the world. A real name or personal email can be traced back to you and those around you regardless of whether this is what you want.
You can configure this either globally, or individually at each repository. I tend to do the latter.
Note that setting global configuration is not something I typically prefer. In the event I use my personal data, I can forget, and my data can be traced back to me. In the event I'm supposed to use my personal data, I am now linked to my separate one. I configure them on a per-repository basis.

To globally configure them, in your cli run ```git config --global user.name [YOUR USERNAME]``` and ```git config --global user.email [YOUR EMAIL ADDRESS]```
These are now the data git uses to sign commits.

You may configure this on a per-repository basis as:
You can do this by navigating to the repository folder and running ```git config user.name [YOUR USERNAME]``` and ```git config user.email [YOUR EMAIL ADDRESS]```


**Now we need to get used to some terminology real quick.**

A _repository is a collection of data and files.

A _commit is a (set of) changes to a repository. A commit contains data of the precise change, the files modified, and the before and after states. It is "signed" with your username and email to record data of who made a change. It also contains a *commit message*, a short descriptor that may be used to explain the purpose of the commit.

A _branch is a version of a repository in a certain state. Most repositories have a "master" branch, which contains the code as it is developed, and create separate branches for versions to save the state of the repository associated with that version. Branches can be used for several reasons, including versions, specific features major enough you want to test them separate from the master of the repository, or even features at all. It is common to create a branch each time you want to make modifications, test the branch, and merge it into master only if found satisfactory. This means your master is never broken or partial.
The working source branch is commonly called "main" or "master".

A _fork is a branch made by anyone other than the original repository owner.

A _remote is a reference to an external version of the repository. It is not local. In the event you are working with git alongside github, you will have a remote for github to push and pull. If you are running a website on a server, you may have this server's address set as a remote.
Setting up a remote requires authentication, and the steps mentioned here are one way to enable this authentication in the case of github.

_Push means to send commit data to a remote. If you have modified your code and commited these modifications locally, you may "push" this branch to the corresponding remote so the changes reflect there too.

_Pull means to get data, branch state, and commits from a remote. If the code has been modified on a remote, you may- in the event there aren't conflicting modifications on your local repository- perform a pull to update your local repository.

A *pull request* is an attempt to merge changes recorded in one branch or fork (the one you created the feature on) into another parent branch or repository (typically the master). It allows you to record your creation of the branch, and review any changes in a neater organization.

_Merge means to update a parent branch with the commits of a separate branch. It is the next step to creating and finalising a branch as complete, and commonly used to update the master branch with the contents of a pull request.

_Tracking is the state of a file to be included under the purview of the repository. It means that git is capable of saving states on this file in commits, and if a file is tracked then git can keep a track of whether it has been changed at all (with respect to the previous committed state) or not.

Now, in the event you want to make a change to a website by adding a new article (name.html) and adding a link to a navigator (homepage.html), this is what you do.
You either create a branch to work on or you work on the master itself. One would want to avoid the latter for organizational purposes.
You make your changes locally and save the modified files.
You add these changes to a record of new changes for your next commit. You do this by using git to add the modified file(s). You can add both files, and commit with a message of "Add new article [name]". The commit now contains the details of the files changed and the message which describes the change
Alternatively, you can add the first file, commit it with the message "add article [name] html page", and add the second file, comitting it with the message "add link to article [name] on home page".
You may push your repository from your branch to a remote alongside creating commits. If you are pushing to a live version of the webpage, you may perform the push to its remote after finishing all your changes.

If you have created a Python calculator project in ```C:/John/Documents/Python/calculator/``` and the filepaths are ```C:/John/Documents/Python/calculator/UI.py```, ```C:/John/Documents/Python/calculator/calculator.py```, and ```C:/John/Documents/Python/calculator/rules.dat```, then your repository directory is ```C:/John/Documents/Python/calculator/``` and *this is where you will run your command line instance.*
The *repository directory* is the main directory containing all your files that are a part of your repository. So the ```/calculator/``` directory is the repository directory in this case.
One may save their repository directory within C itself. Eg, ```C:/calculator/```, ```C:/Project1/```, and ```C:/DataRepo/``` just means your calculator, Project1, and DataRepo repositories are all in the C drive directly, not in a subdirectory. Each of these are repository directories for different repositories.

I keep my repositories in a directory called ```G:/Projects/```. But this itself isn't the repository directory. I place them in one place.
It is also likely for repositories to be set up and initialized wherever convenient. Your repositories may be in different places rather than organized in one folder.

**Understand**:
Git is simply a version control system. It allows you to track and manage your repository's history and changes if you use it. It even allows you to track and manage the changes in an organized fashion if you use it better. It enables multiple programmers to work on the same code.
Additionally, all the commands mentioned below are, UNLESS OTHERWISE SPECIFIED, TO BE RUN FROM THE REPOSITORY DIRECTORY AS EXPLAINED ABOVE.

**Creating your repository:**

*To initialize and set up a git repository to manage your code:*

In your repository directory, open the command line.
The command ```git init``` initializes a repository with the default branch name "master". To initialize a repository with the default branch "main" you may run ```git init -b main```. To set its name as "primary" you may run ```git init -b primary```. I use ```git init -b main``` because I want my working branch to be named "main".
It is convenient to stick to "main" or "master" since a lot of projects follow this convention. It is ideal to have your own standard preference so that, if you are managing multiple repositories, you do not need to remember your primary branch's name.

Now to add all your files from the directory to your git repository you may run ```git add .``` which marks all your files to be a part of the commit.

To commit these changes (you have just put files in your repository) you may run ```git commit```. This opens an editor window where you may write your commit message (Create repository!) detailing what you've done. This view also allows you to see what files are in this commit.
A simpler way to commit is to run ```git commit -m "[YOUR COMMIT MESSAGE]"``` (include the quotes around the commit message) so the commit is made with this commit message without opening a separate window.

If your email and username are not set up, this will not work.

*To push your own nearly-created locally hosted repository to github:*

In your repository directory, with your git set up, you may run ```gh repo create``` to create a github repository.
Follow the steps as the interactive prompting guides you. You may use your arrow keys to select options.

You are pushing your locally-hosted code to github. You want this directory to be pushed.
When asked if you want to create a remote object/reference, select "Yes".
This creates a remote object called "origin" that enables push and pull to work alongside github.

When asked if you want to push all commits to your github remote repository, click yes. (if this does not show up, just type ```git push origin [NAME OF YOUR MASTER BRANCH]``` after you are finished.)
This pushes your commit of adding all the initial files, so the repository on github now contains your files.

*To fork someone else's code from github:*

You may create a fork using these instructions: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository
Simply put, fork the repository on github to your own account.
Then follow the instructions given below to work on code from github. Since you have forked the repository, you are to clone your fork of the repository under your username, not the original owner's username.

If you wish to do so from the command line, these are useful instructions: https://cli.github.com/manual/gh_repo_fork
Note that I haven't had an opportunity to test this myself. But this is capable of cloning a repository too.

*To work on code from github:*

Go to the directory ABOVE your repository directory. If you want to clone your repository into ```C:/Documents/Projects/repoProj``` then navigate to ```C:/Documents/Projects```.

Open the command line here. Run ```gh repo clone [YOUR-USERNAME]/[NAME-OF-REPO]```.

This will _clone the repository, setting the "origin" remote to your repository on git.
If you are working on a forked repository this will also a remote called "upstream" referencing the parent project this was forked from (so you may base and update your fork alongside it).

**Modifying a repository:**

*Creating a branch to work on changes:*

You may create a branch using these instructions: https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github#create-a-new-branch
A branch can be created ```git branch [branch-name]```, and use it by running ```git checkout [branch-name]``` or ```git switch [branch-name]``` to use that branch.

It is recommended, when making changes, to create a branch, ideally with a name that describes the purpose of the specific branch, for the sake of convenience.

To push this branch so it shows up on github, look at the "Pushing branches" section below.

*Making and comitting changes:*

Understand that a commit is necessarily simply a collection of data about modified files and their modifications. Your commit may modify several files.
When creating or modifying a file ```filename.ext```, you may add this file to the next commit using ```git add filename.ext```.
You may commit right now or modify more files and add them to the commit by running the ```git add``` command again.
Any git commands are to be run from the repository directory only, and file paths are to be referenced as relative within it. In a repository directory at ```C:/John/calculator```, where file ```C:/John/calculator/documentation/img.png``` has been changed, you may run FROM THE REPOSITORY DIRECTORY the command ```git add documentation/img.png```. If your filepath has a space in it, surround it in quotes.
If you are making a collection of changes on several files, especially if they are related changes, you may place all these modifications in a single commit instead of separating them.

You may add all files in a repository by running ```git add .``` but I DO NOT recommend doing this. This allows for disorganization and accidents. For the love of God, just add the files you know to have changed.

You may commit by running ```git commit```. This opens an editor window where you may write your commit message and observe the files your commit affects. Alternatively, you _may run ```git commit -m "[YOUR MESSAGE HERE]"``` (include the quotes around the commit message), which commits directly with the given commit message.
If your commit does not work, scroll back up. You may configure the username and email used to sign commits for the repository on a per-repository basis by running these commands right here in the repository directory.

Once you have commited, the commit is now a part of your branch. Any further files you add now go to your next commit.

Do not mistake consecutive commits to affect each other: they are separate commits, and adding files simply means adding them to your NEXT commit. Commits that have been made are done and dusted.
Commits are the equivalent adding balls to a basket and labelling the basket. The second you label the basket, it moves on, replaced by another empty basket. Adding modified files is the equivalent of adding balls. The second you commit, your commit is done, and any balls (modifications) you add now go into a fresh basket waiting to be labelled.
Once your commits are made, you may merge them into your master branch if you have been working on a separate branch.

*Pushing branches:*

You may push a branch to a remote using ```git push```. This is assuming your remote is called origin, which it probably is if you followed these instructions.
Run it as ```git push origin [branch-name]```.


**Keeping a repository up-to-date:**

If you are working on a repository that other people may work on and change, there are several ways to keep your repository up to date with the latest master. I have a tendency to use all forms of pull and fetch.

*Sync a fork:*
Run ```git fetch upstream``` to get the latest repo from the source. Your remote for the source is probably 
Switch to your fork's default branch on your local repository: ```git checkout [branch-name]```. In this case it's probably main.