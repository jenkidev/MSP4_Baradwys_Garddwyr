# Baradwys Garddwyr E-Commerce Website

(by Morgan Jenkins)

[Live Project]

## Table of Contents

- [Baradwys Garddwyr E-Commerce Website](#baradwys-garddwyr-e-commerce-website)
  - [Table of Contents](#table-of-contents)
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Stories](#user-stories)
      - [First-time User](#first-time-user)
      - [Returning User](#returning-user)
      - [Site Owner](#site-owner)
  - [Scope](#scope)
  - [Design of Site](#design-of-site)
    - [Initial idea](#initial-idea)
    - [Wireframes](#wireframes)
    - [Site Layout](#site-layout)
    - [User Path](#user-path)
    - [Database Structure](#database-structure)
    - [Colour Choices](#colour-choices)
    - [Fonts](#fonts)
  - [Technologies Implemented](#technologies-implemented)
    - [Languages](#languages)
    - [Tools](#tools)
  - [Site Features](#site-features)
  - [Testing](#testing)
    - [Validation](#validation)
      - [HTML Validation- W3C markup validation service was used to assess the validity of my HTML code](#html-validation--w3c-markup-validation-service-was-used-to-assess-the-validity-of-my-html-code)
      - [CSS Validation- W3C CSS validation service was used to assess the validity of my CSS code](#css-validation--w3c-css-validation-service-was-used-to-assess-the-validity-of-my-css-code)
      - [JavaScript Validation- JS hint was used to assess the validity of my scripts](#javascript-validation--js-hint-was-used-to-assess-the-validity-of-my-scripts)
      - [Python Validation- The CI python linter was used to assess the the validity of my python file](#python-validation--the-ci-python-linter-was-used-to-assess-the-the-validity-of-my-python-file)
    - [Performance and Accessibility](#performance-and-accessibility)
    - [Device Tests](#device-tests)
    - [Responsiveness](#responsiveness)
    - [User Story Tests](#user-story-tests)
    - [First Time User](#first-time-user-1)
    - [Returning User](#returning-user-1)
    - [Site Owner](#site-owner-1)
  - [Bug Squashing](#bug-squashing)
  - [Deployment](#deployment)
    - [Project Creation](#project-creation)
    - [Deployment to Heroku](#deployment-to-heroku)
  - [Credits](#credits)
  - [Thank You](#thank-you)

## Project Goals

### User Goals



### Site Owner Goals


## User Experience

### Target Audience



### User Requirements and Expectations

* Easy to navigate site and intuitive design.


### User Stories

#### First-time User


#### Returning User


#### Site Owner


## Scope

The scope of the project in it’s first release is defined by the following features:


## Design of Site

### Initial idea



### Wireframes

To create the wireframes for this site I used the balsamiq cloud service. This allowed me to create a more basic wireframe. This was helpful as I have found in the past having a more complex and detailed wireframe to be quite restricting.


### Site Layout



### User Path



### Database Structure



### Colour Choices



### Fonts


## Technologies Implemented

### Languages

* HTML
* CSS
* JavaScript
* Python

### Tools



## Site Features

## Testing

### Validation

#### HTML Validation- W3C markup validation service was used to assess the validity of my HTML code



#### CSS Validation- W3C CSS validation service was used to assess the validity of my CSS code



#### JavaScript Validation- JS hint was used to assess the validity of my scripts



#### Python Validation- 
The CI python linter was used to assess the the validity of my python file whilst development of the site was underway and in progress. Upon project completion the command 'python3 -m flake8' was used to check for formatting and other issues.

`gitpod /workspace/MSP4_Baradwys_Garddwyr (main) $ python3 -m flake8
./.devcontainer/build-assets/http_server.py:22:80: E501 line too long (80 > 79 characters)
./.devcontainer/build-assets/make_url.py:10:39: E231 missing whitespace after ','
./.devcontainer/build-assets/make_url.py:11:36: E231 missing whitespace after ','
./.devcontainer/build-assets/make_url.py:12:39: E231 missing whitespace after ','
./.devcontainer/build-assets/make_url.py:14:59: W292 no newline at end of file
./articles/migrations/0001_initial.py:17:80: E501 line too long (117 > 79 characters)
./articles/migrations/0001_initial.py:21:80: E501 line too long (103 > 79 characters)
./articles/migrations/0001_initial.py:22:80: E501 line too long (82 > 79 characters)
./articles/migrations/0003_articlereview.py:19:80: E501 line too long (117 > 79 characters)
./articles/migrations/0003_articlereview.py:23:80: E501 line too long (147 > 79 characters)
./articles/migrations/0003_articlereview.py:24:80: E501 line too long (156 > 79 characters)
./baradwys_garddwyr/settings.py:142:80: E501 line too long (91 > 79 characters)
./baradwys_garddwyr/settings.py:145:80: E501 line too long (81 > 79 characters)
./baradwys_garddwyr/settings.py:148:80: E501 line too long (82 > 79 characters)
./baradwys_garddwyr/settings.py:151:80: E501 line too long (83 > 79 characters)
./checkout/apps.py:8:9: F401 'checkout.signals' imported but unused
./checkout/migrations/0001_initial.py:19:80: E501 line too long (117 > 79 characters)
./checkout/migrations/0001_initial.py:20:80: E501 line too long (82 > 79 characters)
./checkout/migrations/0001_initial.py:25:80: E501 line too long (85 > 79 characters)
./checkout/migrations/0001_initial.py:28:80: E501 line too long (92 > 79 characters)
./checkout/migrations/0001_initial.py:29:80: E501 line too long (83 > 79 characters)
./checkout/migrations/0001_initial.py:31:80: E501 line too long (98 > 79 characters)
./checkout/migrations/0001_initial.py:32:80: E501 line too long (97 > 79 characters)
./checkout/migrations/0001_initial.py:33:80: E501 line too long (97 > 79 characters)
./checkout/migrations/0001_initial.py:39:80: E501 line too long (117 > 79 characters)
./checkout/migrations/0001_initial.py:41:80: E501 line too long (104 > 79 characters)
./checkout/migrations/0001_initial.py:42:80: E501 line too long (137 > 79 characters)
./checkout/migrations/0001_initial.py:43:80: E501 line too long (115 > 79 characters)
./checkout/migrations/0004_order_user_profile.py:18:80: E501 line too long (155 > 79 characters)
./products/migrations/0001_initial.py:18:80: E501 line too long (117 > 79 characters)
./products/migrations/0001_initial.py:20:80: E501 line too long (91 > 79 characters)
./products/migrations/0001_initial.py:29:80: E501 line too long (117 > 79 characters)
./products/migrations/0001_initial.py:35:80: E501 line too long (103 > 79 characters)
./products/migrations/0001_initial.py:36:80: E501 line too long (89 > 79 characters)
./products/migrations/0001_initial.py:37:80: E501 line too long (82 > 79 characters)
./products/migrations/0001_initial.py:38:80: E501 line too long (141 > 79 characters)
./products/migrations/0002_alter_product_category.py:17:80: E501 line too long (141 > 79 characters)
./products/migrations/0003_review.py:18:80: E501 line too long (117 > 79 characters)
./products/migrations/0003_review.py:22:80: E501 line too long (146 > 79 characters)
./products/migrations/0003_review.py:23:80: E501 line too long (139 > 79 characters)
./products/migrations/0004_alter_review_created_by.py:19:80: E501 line too long (134 > 79 characters)
./products/widgets.py:9:80: E501 line too long (87 > 79 characters)
./profiles/migrations/0001_initial.py:21:80: E501 line too long (117 > 79 characters)
./profiles/migrations/0001_initial.py:22:80: E501 line too long (97 > 79 characters)
./profiles/migrations/0001_initial.py:23:80: E501 line too long (111 > 79 characters)
./profiles/migrations/0001_initial.py:24:80: E501 line too long (93 > 79 characters)
./profiles/migrations/0001_initial.py:25:80: E501 line too long (97 > 79 characters)
./profiles/migrations/0001_initial.py:26:80: E501 line too long (100 > 79 characters)
./profiles/migrations/0001_initial.py:27:80: E501 line too long (100 > 79 characters)
./profiles/migrations/0001_initial.py:28:80: E501 line too long (91 > 79 characters)
./profiles/migrations/0001_initial.py:29:80: E501 line too long (121 > 79 characters)` 

As can be seen above most issues raised are caused by lengthy migrations and the local env.


### Performance and Accessibility



### Device Tests

The website was tested on the following devices:

* Samsung Galaxy M31
* iPhone 12 Pro
* Ipad Pro 4th Gen
* Asus Vivobook laptop (X515JAB_X515JA)

### Responsiveness

[Responsinator]() was used to assess the responsiveness of the project.

### User Story Tests

### First Time User



### Returning User



### Site Owner


## Bug Squashing

| **Bug** | **Fix** |
|---------|---------|


## Deployment

### Project Creation



### Deployment to Heroku



## Credits

* Images for the site were acquired from [Pexels](https://www.pexels.com/)
* Majority of python code was adapted from the walkthorugh project (Task Manager).
* [Materialize](https://materializecss.com/) was used as the framework for this site aiding in components and responsiveness.

## Thank You

* My mentor Antonio Rodriguez for his help and advice in creating this project.
* To the team at [Code Institute](https://codeinstitute.net/) for the lessons and support.
* My Partner for helping with project testing and supporting me through it.
