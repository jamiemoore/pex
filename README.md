# pex
Python EXample Project

An excuse to write some python and play with some fun tech.  Marvel not at the amazing service, but rather the technologies and practices used :).

## Architecture Overview

Simple service to produce some dummy output.

todo: Arch Diagram goes here.





## Tech and Process Overview

Listing of the technology and processes used in the project.  If you haven't come accross one of these technologies before, just click the link and learn something new!  Know a technology with a better fit, please open an issue.

| Requirement                 | Tech or Process                                              |
| --------------------------- | ------------------------------------------------------------ |
| Language                    | [Python](https://www.python.org/)                            |
| Language Version Management | [pyenv](https://github.com/pyenv/pyenv)                      |
| Linters                     | [pylint](https://www.pylint.org/) [flake8](https://flake8.pycqa.org/en/latest/) [bandit](https://bandit.readthedocs.io/en/latest/) |
| Formatter                   | [Black](https://github.com/psf/black)                        |
| Web Framework               | [Flask](https://flask.palletsprojects.com/en/1.1.x/)         |
| Web Server                  | [Gunicorn](https://gunicorn.org/)                            |
| Testing Framework           | [pytest](https://docs.pytest.org/en/stable/) [pytest-sugar](https://github.com/Teemu/pytest-sugar/) |
| SCM                         | [Github](https://github.com/)                                |
| Branching Model             | [Trunk Based Development](https://trunkbaseddevelopment.com/) |
| Integration Model           | [Continuous Integration](https://www.thoughtworks.com/continuous-integration) |
| Dependency Management       | [Poetry](https://python-poetry.org/)                         |
| Packaging                   | [Docker](https://www.docker.com/)                            |
| Container OS                | [python:3.9.1-alpine3.13](https://hub.docker.com/layers/python/library/python/3.9.1-alpine3.13/images/sha256-d67bb897163cd15791acae189ba1bacef82017b4d2d0c36623f55a3eb0c8e989?context=explore) |
| Versioning                  | [Semantic Versioning](https://semver.org/) [bump2version](https://pypi.org/project/bump2version/) |
| Pre-Commit Pipeline         | [pre-commit](https://pre-commit.com/)                        |
| CI Pipeline                 | [Github Actions](https://github.com/features/actions)        |
| CI Environment              | [Google Cloud Run](https://cloud.google.com/run)             |
|                             |                                                              |
|                             |                                                              |
|                             |                                                              |



## Development Overview

Before starting development.  Configure your environment.  This is an example of Mac OS X, please add your own OS if different.



### Configure Development Environment

1. Install Docker - https://docs.docker.com/get-docker/

2. Install an editor - https://code.visualstudio.com/

3. Install homebrew - https://brew.sh/

4. Install homebrew packages

   ```
   brew update && brew install git pyenv pipx poetry
   ```

5. Add the following to `.zshrc` for pyenv

   ```
   eval "$(pyenv init -)"
   ```

6. Add the following to you `.zshrc` for pipx

   ```
   export PATH="$PATH:${HOME}/.local/bin"
   ```

7. Install pre-commit using pipx

   ```
   pipx install pre-commit bump2version
   ```

1. Install the pre-commit hook

   ```
   pre-commit install
   ```

9. Clone repository

   ```
   git clone
   ```

10. Set correct python version

   ```
   pyenv local
   ```

11. Configure the python virtual environment

    ```
    poetry env use 3.9.1
    poetry install
    ```

12. Launch editor

    ```
    code .
    ```

13. Select the appropriate virtual environment in your editor

14. You are now ready for the development workflow



## Deployment and Development workflow

The deployment process is descibed only to the the continuous integration environment.

1. Check out latest version of code

   ```
   git pull
   ```

2. Write tests for any acceptence criteria

3. Develop (The magic happens here)

4. Confirm tests pass

   ```
   pytest
   ```

5. Commit code (Please see the pre-commit hook)

   ```
   git commit -a -m "my new amazing feature"
   ```

6. Push code

   ```
   git push
   ```

7. Pipeline will now run and deploy to the CI environment



## Pipeline

The pipeline is using github actions and does the following on a new commit.

* Run the pre-commit hooks
* Build the docker container
* Deploy to the CI Environment



## Pre-commit hook

There is a pre-commit hook configured for this project that will:

* Check for security issues such as aws creds and private keys
* Remove trailing whitespace and bad line endings
* Check for python debug statements
* Check for large files
* Check for merge conflicts
* Check listing using
  * pylint
  * flake8
  * bandit
* Check Formatting using black
* and run the tests

Install the git hook with

```
pre-commit install
```

If the above passes when you try to commit you will be able to commit.  If you would like to run the command manually

```
pre-commit run --all-files
```



## Versioning

We are using Simantec Versioning and the tool bumpversion.  We are not only updating the files we are also adding a git tag.

* Bump the version (minor) i.e. 0.1.0

  ```
  bumpversion minor
  ```

* Bump the version (major)  i.e. 1.0.0

  ```
  bumpversion major
  ```

* Bump the version (patch)  i.e. 0.0.1

  ```
  bumpversion patch
  ```

* Check the git tags

  ```
  git tag
  ```

* Push the changes once you have bumped the version and added the tag

  ```
  git push
  git push --tags
  ```

* If you want to bump the version even though the git working directory is dirty, not usually a good idea

  ```
  bumpversion minor --allow-dirty
  ```



### Initial project setup

The initial repo setup only needs to be done once, but handy for reference.

1. Specify python version

   ```
   pyenv local 3.9.1
   ```

2. Init poetry

   ```
   poetry init
   poetry env use 3.9.1
   ```

3. Add deps

   ```
   poetry init
   poetry add -D poetry add -D pytest pytest-sugar pylint flake8 bandit black
   poetry add flask gunicorn
   ```

4. The first time you run the deployment it will not allow you to connect unauthenticated.

### Testing

Tests can be run using the pytest command

```
pytest
```



## Packaging

Packaging is done using docker.  It is automated in the pipeline but if you wish to build or run the image manually you can use the following commands.

* Build docker image

  ```
  docker build -t pex:$(cat VERSION) --build-arg COMMIT_SHA=$(git rev-parse --short HEAD) .
  ```

* Run the container

  ```
  docker run --rm -p 8080:4040 pex:$(cat VERSION)
  ```

* Debug container

  ```
  docker run --rm -it -p 8080:80 pex:$(cat VERSION) /bin/sh
  ```




## Risks

* Deployment is a CI deployment and should not be used for production for the following reason
  * No monitoring and alerting
  * No health checks and auto healing
  * No automated scaling or elasticity
* TBD is almost always a good practice for a single developer but as teams get bigger Github Flow may be a better fit.



## Notes

* https://testdriven.io/blog/flask-pytest/
* https://github.com/actions/starter-workflows/blob/main/ci/google.yml
* https://github.com/marketplace?type=actions
* https://github.com/marketplace/actions/deploy-to-cloud-run