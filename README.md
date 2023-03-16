# QA Toolkit

This is a base project with the structure needed to run any QA automation in any project.

## Project Structure

- core: Here is the base class and the urls for the tests.
- models: Here you can add all the models that you are going to need to your tests. For this base project we have added a user model in order to generate fake users.
- objects: Inside this folder you will find 2 more folders:
    - components: Here you will add your component classes with their elements.
    - pages: Here you will add your pages classes with their elements and related components.
- reports: Here you will see the data used to generate allure reports.
- tests: There are 3 main folders and 2 files in this directory:
    - Folders:
        - test_components: Here you will create the tests for all your components
        - test_flows: Here you will create all the tests that use more than one component or page.
        - test_suites: Here you will create all the tests that uses other tests functionalities. (In other words, you can combine tests here).
    - Files:
        - conftest: This is the file where the driver is configured for all the tests.
        - test_main: Here you will need to import all your tests so that all of them can run in order using pytest.
- utils: Here you will find some files that have all utilities you may need to create a test divided by funtionality (simple_actions, wait_events...). Also, you can find a file called custom; you can add all the custom functions you may need in your tests.

## Run Tests

First, install all the requirements running this command:

```pip install -r requirements.txt```

After you have finished developing your tests you can run them using this command:

```pytest tests/test_main.py --alluredir=./reports```

Something to take into consideration is that you can add allure settings to your tests and define them as: features, stories, and epics. If you want to run only an specific feature or story or epic you can run this command:

- For feature:
```pytest tests/test_main.py --alluredir=./reports --allure-features feature_name```

- For story:
```pytest tests/test_main.py --alluredir=./reports --allure-stories story_name```

- For epic:
```pytest tests/test_main.py --alluredir=./reports --allure-epics epic_name```

You can also combine them:

```pytest tests/test_main.py --alluredir=./reports --allure-features feature_name_1, feature_name_2 --allure-stories story_name```

Also, you can specify the browser for the tests by using this command:

```pytest tests/test_main.py --alluredir=./reports --browser_name <browser>```

The browser can be: chrome, firefox, edge.

Finally, you can also run tests in parallel by using ```-n <num>``` like in this command used to run 3 tests in parallel.

```pytest tests/test_main.py --alluredir=./reports -n 3```

If you want to run all tests in parallel you will need to send ```-n auto```

## Create Allure Report

First, you need to have allure installed in your computer. [Here is a guide to install it.](https://docs.qameta.io/allure/#_manual_installation) You will need to follow these steps:
- download a maven package from [here](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/). Just select the most recent package and then download the .zip archive. 
- Unpack it and save the folder in any folder in your computer (recommended in C:\Program Files\Allure).
- Go to the bin folder and copy the path (C:\Program Files\Allure\allure-your-version\bin)
- Add that path to your system PATH.
- Open a terminal and run allure --version to make sure that you have allure installed correctly.

As this is a maven package you will need to have java jdk in your computer and the JAVA_HOME variable setted in your system varaibles.

Now that you have allure installed you can generate the reports. After running the tests you may notice that there is no html file with the report. To generate the report you need to run this command:

```allure serve ./reports```

This will search for all the files created in the reports folder and create a temp html file with all that information.