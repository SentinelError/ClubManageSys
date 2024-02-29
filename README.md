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

![MicrosoftTeams-image](https://github.com/SentinelError/ClubManageSys/assets/71810497/4bc345c3-aa3c-4d74-b46b-b37edbefcba1)


# Screenshots

The following Screenshots are various functions available to the SuperUser :




![00 Admin Homepage](https://github.com/SentinelError/ClubManageSys/assets/71810497/fa59b3da-8d24-4b46-b4b8-ae77933bfdf5)

![01 Admin Edit Profile](https://github.com/SentinelError/ClubManageSys/assets/71810497/b4271bea-ea04-47bd-b3c7-bf9876ed3e1f)

![02 Admin Edit Password](https://github.com/SentinelError/ClubManageSys/assets/71810497/600e2db8-afb2-409e-af9b-09d53f0c66de)

![03 Admin Available Venues](https://github.com/SentinelError/ClubManageSys/assets/71810497/444a50a8-2c7b-400e-9617-1cd1bad74c3c)

![04 Admin Add Venue](https://github.com/SentinelError/ClubManageSys/assets/71810497/4e509e2d-28bd-4169-a226-2426b76fccac)

![05 Admin View Club Users](https://github.com/SentinelError/ClubManageSys/assets/71810497/bdfe2183-312a-4b99-aac4-7de003e0d39f)

![06 Admin Available Events](https://github.com/SentinelError/ClubManageSys/assets/71810497/abb7b5cd-4993-4ed7-9859-31c5a9014900)

![07 Admin Add Events](https://github.com/SentinelError/ClubManageSys/assets/71810497/fdde23e2-c67f-41db-bedd-aed2beb90d77)

![08 Admin Update Events](https://github.com/SentinelError/ClubManageSys/assets/71810497/3a00b550-1ece-41c9-9bc7-2fb708dae41b)

![09 Admin Approve Events](https://github.com/SentinelError/ClubManageSys/assets/71810497/7dacbf2b-7e90-42a1-b198-f1ef906161b7)

![10 Admin Report Archive](https://github.com/SentinelError/ClubManageSys/assets/71810497/168661da-0a8f-4c77-9ac2-e65940805f69)

![11 Admin Update Report](https://github.com/SentinelError/ClubManageSys/assets/71810497/07cb7e50-15f6-4f6a-b2a1-31e63c22303d)

