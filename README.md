# Automation-Project
E-commerce web application, smoke tests performed

## CONTENTS OF THIS FILE
* Introduction
* Motivation
* Requirements
* Technology/Frameworks
* Tests
* Installation
* Configuration
* Troubleshooting
* Maintainers


# Introduction

This is e-commece demo web application http://automationpractice.com/index.php. Main goal of this project is to do automation on main functionality for this site. Smoke test is applyed to several test cases using Python3 and Selenium webdriver. Impertive is an actual user workflow.


## Motiovation

I was always passionate about web testing and finding defects on the application. Quality assurance is so interesting, you get involved in the development of the application, also finding defects helps developers and the customer to get quality software. There are so many ways to test features, from manual to automation, there are so many different types of tests.


## Requirements

* Windows 11
* MacOS Monterey (Slightly mods needed)
* Python3(Recommended)
* Python2
* Pip3

## Technology/Frameworks

All smoke tests were automated throught Selenium webdriver. I used Python3 to write the tests and hybrid framework for this project. Page object model where all logics are based in the objects classes. Pytest which means pytest is a command-line tool that automatically finds tests you've written, runs the tests, and reports the results. Package pytest-html is used to generate HTML reports for test results with clear UI, pytest-xdist can run tests parallel on several different browsers.


## Tests
* All tests fall into a Smoke test category.
* Validation of home page title.
* Log in test for check crutial login funcionallity.
* Logout test for check crutial logout funcionallity.
* Register test from adding and validation of email, to various inputs from firstname, lastname, password, city, state exc.
* Shopping tests to run whether basic funcionallity of e-commerce site is working, such as look for dress in a certaing category, pick a size, color ,price, buying a   dress and put in the cart, go to checkout, and finally buy the product.


## Installation

Use the package manager pip to install foobar.

To execute all test in a Smoke category, type following command in PyCharm terminal:

```
pytest -s -v -m "smoke" --html=.Reports\report_smoke.html testCases/ --browser chrome
```


Execute following commands for install library:
```
selenium webdriver
pytest
pytest-html - PyTest HTML reports
pytest-xdist - Run test parallel
allure-pytest - Generate allure reports
```


# Install(Clone) software

https://github.com/davud-gobeljic/Automation-Project.git
Troubleshooting
Please consider that this is a demo e-commerce website, it is high possillity to crash down due limited resource usage. If so, re-run the test for hopefully better site performance.



# Maintainers
`
Davud Gobeljic - Quality Assurance (QA) Engineer
`
