# Club Manager with Django

## Introduction

This project is a fully fuunctional Club Management Website for any Education Institute. I had originally built this as my institution at the time did not have a efficient process for Club Members to manage their clubs and activities. This app covers everything from Account Creation all the way to report submission on various activities. In this ReadMe, I will cover everything from app functions to various levels of authorization. There will be some images at the end to showcase the application. [The images are a placeholder till I find someplace to host this app.]

## Table of Contents [Updating]

### 1. Description
### 2. Usage
### 3. Screenshots

# Description

During my 6th semester of college, I was tasked with building a functional website to manage club affairs and provide a centralized platform for club members to access information about activities and important dates. I decided to use Django for this project because of its robust support for Python and its seamless integration with HTML, CSS, and JavaScript.

Django's beginner-friendly layout and the intuitive way in which templates are structured and linked through URLs made it an ideal choice for me. After submitting the initial assignment, I continued to enhance the project by adding new functionalities and refining existing features. As the Web Application came together, **I built various levels of _user authorization_** :

_The Highest Level of authorization_ : **The SuperUser**

The SuperUser role was assigned to the Club Managers. [The teacher assigned to club] They had control over almost all of the functionalties the App provided from Venue creation to editing User data. They could assign new events as well as competetion events. However they weren't allowed to write reports of events as that functionality was explicitly reserved for the Student Representatives of the clubs.

_The Middleman_ : **The StaffUser**

The StaffUser role was assigned to the Club Student Representatives. They had access to limited functionalities such as creation of **_training events only_** and **_the creation of event reports._**

_The Clubber_ : **The User**

The User role was assigned to the club members. They could login and view the events for the day and upcoming events for their club and that was it.

_Who are you?_ : **The Non-User**

This role was created so that new people coming to the Application wouldn't be kicked out immediately and instead ended up on the landing page.

# Usage

The Following is a Use-Case Diagram at the inception of the project :




# Screenshots


![MicrosoftTeams-image](https://github.com/SentinelError/ClubManageSys/assets/71810497/4bc345c3-aa3c-4d74-b46b-b37edbefcba1)
