# Roman Numerals CI/CD Kata

The goal of this kata is to practice setting up a continuous integration / continuous delivery system.

We start with my solution to the Roman Numerals kata (also known as theh Reverse Roman Numerals kata). We've added on a simple web UI.

You will take this simple web app and set up a continuous delivery pipeline to run it in "production."

Here are the steps:

## Fork this repository
You will need your own Roman Numerals repository. To fork this repository:
- Visit https://github.com/rkasper/roman-python.
- Click the `Fork` button.
- In your GitHub account, visit the forked repository you just created.

## Clone your Roman Numerals repository
- In PyCharm Professional, create a new project from VCS.
  - For `Version Control`, specify `Git`.
  - For the `URL`, copy-paste the URL of _your_ Roman Numerals repository
  - Click the `Clone` button.

## Make sure the app runs on your machine
- If you notice an error like _no such file or directory: venv/bin/python_, then install a new Python virtual environment. One way to do this is to select `Preferences / Project / Python Interpreter`. Click the gear icon, and add a new virtual environment. On my machine, PyCharm finds the `python3` executable.
- If you notice an error like _no such file or directory: venv/bin/behave_, then either:
  - Open file `requirements.txt` and follow the instructions at the top of the editor window, or
  - Type this inside a terminal in your project's root directory:
`$ venv/bin/pip install -r requirements.txt`
  - Run all the tests. In the Project browser at the top-left of the IDE, right-click `app / test`. Select `Run 'Python tests in test...'`. Confirm that all the tests are green.
    - __--> Open the files in the `test` directory. What does each file do?__
  - Run the web app. In the Project browser, right-click file `flask-app.py`. Select `Run flask-app`. Visit http://127.0.0.1:5000 and play with the web app.
    - __--> Open file `flask-app.py`. How does it work?__
    - __--> Where is the UI code for the web app?__
    - __--> Where is the Roman numerals business logic?__
    - __--> Is there any storage?__
    - __--> Are there any other files? What does each file do?__

## Set up your continuous delivery pipeline
We'll use [Digital Ocean App Platform](https://www.digitalocean.com/products/app-platform), a super-simple way to set up a continuous delivery pipeline and deploy an application.
- Login to Digital Ocean, either using your own account or using an account provided by your instructor.
- In the Digital Ocean UI, create your own Roman Python project.
  - Navigate to `Projects / New Project`. Name your project `Roman Python` and click `Create Project'.
  - In the `Move Resources` dialog, click `Skip for now`.
- Create your Roman Python app. Click `Create App`.
  - At the prompt, `Create Resource from Source Code / Service Provider`, select `GitHub`.
  - For `Repository`, login to your GitHub account and select _your_ Roman Python repo.
  - Notice that `Autodeploy` is checked.
    - __--> What do you think Autodeploy does?__
  - Click `Next`. 
- On the `Edit Plan` page, select these options:
  - `Plan`: `Basic`
  - `Size`: `$5/mo - Basic`
  - Click the `Back` button.
  - Click `Next`. 
- On the `Environment Variables` page, just take a look. Click `Next`.
  - __--> What might you use environment variables for?__
- On the `Info` page, select `App Info` to edit more project details.
  - Edit your app name. Rename it `roman-python`.
  - Choose your Roman Python project
  - Click `Save`, then `Next`.
- On the `Review` page, take a look the settings. Click `Create Resource`.
- Go to `Build Logs` and watch your app build.
- Your app is now running in a production environment. To run your app's web UI, click the `Live App` button.

## Continous delivery
One way we reduce risk is by reducing batch size: our CD pipeline automatically rebuilds and redeploys every time we introduce a code change. Remember that `Autodeploy` setting? We left it turned on. Whenever we push new code to the repository, our CD pipeline will notice, clone the repository, build it, and deploy it.
- __--> Try it: change some code on your machine, run the tests to make sure everything is "green", and commit and push to git.__
- __--> What did you change?__
- __--> Exactly what happened when you pushed to git?__
- __--> What are the risks of automatic deployment?__

## Safety: Add tests to your build pipeline
Another way we reduce risk is via test-driven development. We have a test suite that we run on our machine while writing code. We can enhance the safety of our deployments by also running these tests in the build & deploy environment.
- In `App Settings / Components`, select your `roman-python` app.
- In `Commands`, click `Edit`. 
- Add a `Build Command` to run your tests: `python app/test/tests.py`. Click `Save`.
- Notice that when we change our app's configuration, the CD pipeline rebuilds it. Go to `Build Logs` and watch the new build. Notice that the pipeline now runs tests, and that all the tests passed.

## Safety: blue/green deployments
- On your machine, intentionally introduce a test that fails. Commit and push your code to the repository.
- __-->What happens in the CD pipeline?__
- On your machine, make that test pass . Commit and push your code to the repository.
- __-->What happens in the CD pipeline?__