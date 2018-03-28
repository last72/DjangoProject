# DjangoProject
Testing Django framework for python. Testing area for urver project that i'm working on now.
Following Turorial: https://docs.djangoproject.com/en/2.0/intro/


# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

# Urver
1. Clone this repository with `git clone https://github.com/esabunor/urver.git`
2. Then `cd` into the directory with `cd urver`
3. Ensure you have python3 installed on your device if you don't:
    1. ## Mac
        1. Install homebrew if you don't have it already. [How to install homebrew](https://www.howtogeek.com/211541/homebrew-for-os-x-easily-installs-desktop-apps-and-terminal-utilities/)
        you can check if you have it already by running `brew help`
        2. Install python3 with the command `brew install python3`
        3. Check that python3 is working by running `python3`

    2. ## Windows
        1. Download the windows executable installer for Python 3.6.4 at [Python Software Foundation](https://www.python.org/downloads/windows/)
        2. Follow the installation prompt.
        3. Ask google for the rest, if you run into problems, or me

4. Once you sure you've installed python3 on your device, you need to install `virtualenv`
    1. ## Mac
       1. Run the command `pip3 install virtualenv`
    2. ## Windows
       1. Not to sure. Google how to install pip on windows. (update) pip should come installed with python
       proceed to run the command `pip3 install virtualenv`

5. Create a virtual environment
    1. ## Mac
        1. I would suggest you create a directory called `environments` in the parent directory of the `urver` directory
        2. Go to the `environments` directory
        3. Run the command `virtualenv urver`
        4. Then run this command `source urver/bin/activate` your terminal should look like this `(urver)<your-username> $`
        5. Finally navigate to the project directory and run `pip install -r requirements.txt`
    2.  ## Windows
        1. Follow steps 1 - 3 of Mac
        2. Instead of `source urver/bin/activate` you run `source urver\Scripts\activate`
        3. Do step 5 of Mac

6. Run the project
    1. ## Mac
        1. Run the command `python3 manage.py migrate && python3 manage.py runserver`
    2.  ## Windows
        1. Run the command `python manage.py migrate && python manage.py runserver`

7. Go to http://127.0.0.1:8000/ on your browser if all goes well you should see page similar to this
![Sample page](media/sample.png)

## Python / Django Learning Resources
*   [The Django Book](https://djangobook.com/the-django-book/)
*   [Django Project](https://docs.djangoproject.com/en/1.11/)
*   [Python3 Programming](https://www.dropbox.com/s/an0i3xzbr2sfmkn/book.programming_in_python_3.summerfield.pdf?dl=0)

## DevOps
*   [Issue Tracking](http://218.214.104.207:8080/) Go to the url and Create an account, let me know when you've done so.
*   [Github repo](https://github.com/esabunor/urver.git/)
*   [Jenkins CI](http://218.214.104.207:9999/)

## Git Workflow
*  Whereever you pull from Github with the command `git pull origin master` always run source your virtualenv with
   `source environments/urver/bin/activate` for mac and `source environments\urver\Scripts\activate` for windows
   and your terminal or command prompt should look like `(urver)<your-username> $`.
*  After you've sourced your environment, run `pip install -r requirements.txt` to install any new requirements.
*  Run `python3 manage.py migrate && python3 manage.py runserver`. Voila it should work, call me if it doesn't.

   ## Commits
   * `git add <filename or filenames>` to add files that you've finished editing
    once you've added a file or files next step is to commit to files
   * `git commit -m "any simple but descriptive message"` then next step is to push your changes to the repository (github) run
   * `git push origin master` you might encounter and error message like this:

       ```
        To https://github.com/esabunor/urver.git
        ! [rejected]        master -> master (fetch first)
        error: failed to push some refs to 'https://github.com/esabunor/urver.git'
        hint: Updates were rejected because the remote contains work that you do
        hint: not have locally. This is usually caused by another repository pushing
        hint: to the same ref. You may want to first integrate the remote changes
        hint: (e.g., 'git pull ...') before pushing again.
        hint: See the 'Note about fast-forwards' in 'git push --help' for details.
        ```
       The solution is to run `git pull origin master` and push again with `git push origin master`

       After you run `git pull origin master` you might also encounter this
       ```
        Merge branch 'master' of https://github.com/esabunor/urver

        # Please enter a commit message to explain why this merge is necessary,
        # especially if it merges an updated upstream into a topic branch.
        #
        # Lines starting with '#' will be ignored, and an empty message aborts
        # the commit.
        ~
        ~
        ~
       ```

        click `esc` and type: `q!` and hit `enter`. You can proceed with you pushing.
        Disclaimer: If you ever encounter this error please let me know. This solution might only work for mac.

