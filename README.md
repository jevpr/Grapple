# Grapple

<br>


## Important Information
| Site              | Link |
|-------------------|------|
| Heroku Deployment | LINK | 
| Github Repository       | [LINK](https://github.com/jevpr/Grapple) |


## Grapple Login Details

| User type | Username | Password |
|-----------|----------|----------|
| Student   | student  | Testing123! |
| Content Creator | contentCreator | Testing123! |

<br>
<br>

# Contents

## Ideation and Design 
### 1. [Project Overview](#project-overview)
- [Description](#description)
- [Technologies Used](#technologies-used)

### 2. [Users](#users)
- [User Roles](#user-roles)
- [User Stories](#user-stories)
### 3. [Features](#features)
### 4. [Front End](#front-end)
- [Colour Scheme](#colour-scheme)
- [Fonts](#fonts)
- [Pixel Assets](#pixel-assets)
- [Wireframes and UI](#wireframes)

<br>
<br>

# Project Overview

## Description
Grapple is a VLE (virtual learning environment) designed for people studying English. 

It's aimed at users who want to benefit from an English learning site with a fun and playful interface. 

These users will be more advanced in the language already, and want access to articles that can help them develop  their skills further. 

The project takes inspiration from Duolingo in it's use of cute avatars and bright colours to inspire students and keep the learning environment energetic. 

Although Grapple is still in early stages of development, later iterations will include features like games, quizzes, advanced notes features, and progress tracking. 

Grapple keeps English learner's notes and materials in one place, making it easy for them to access annd keep track of their learning. A consistent and accessible style across the site removes barriers to learning, and ensures all information can be easily absorbed. 

## Technologies Used
| **Category**           | **Technologies Used** |
|-----------------------|----------------------|
| **Frontend**         | HTML, CSS, JavaScript |
| **Backend**          | Django (Python) |
| **Database**         | SQLite3 |
| **Version Control**  | Git & GitHub |
| **Deployment**       | Heroku
| **Libraries & Tools** | Django Authentication, CKEditor5 for rich text editing, Django Signals for user group management |



<br>
<br>

# Users

## User Roles
| User type | Permissions |
|-----------:|----------|
| Unauthenticated| Can browse some of the site but has limited access to functionality and materials. | Testing123! |
| Students | Can search, read, bookmark, and make notes / comments on lessons. Dashboard allows them to access bookmarked lessons quickly. | Testing123! |
| Content Creators | Can create, read, update, and delete (CRUD) lessons from their dashboard. lesson creator allows them to add title, tags, preview, and content.|

## User Stories 
### Students

<em>As a student, I want to be able to: </em>

- register an account, so that I can access lessons, bookmark important materials, and save notes. 
- securely log in and log out, so that my personal data is protected. 
- browse available lessons, so that I can learn new topics at my own pace. 
- search for lessons using a specific key word or tag name, so that I can quickly find relevant material.
- open a lesson and view its content, so that I can study the material in detail. 
 - add personal notes to a lesson, so that I can refer to key points later. 
 - comment on kessons, so that I can ask questions or discuss the topic with others.

<br>

 Grapple 2.0 (March 2025):
 - see my lesson progress, so that I can keep track of what I have completed. 
- take quizzes after completing lessons, so that I can assess my understanding.
- see my quiz scores and correct answers, so that I can improve my knowledge. 


### Content Creators

<em>As a content creator, I want to be able to: </em>

- navigate an intuitive dashboard, so that I can quickly manage me lessons. 
- log in securely so that my content cannot be edited by unauthorized users. 
- create new lessons, so that students have educational material to learn from. 
- format lessons content with headings, tables and lists, so that the material is engaging and readable (using a rich text editor).
- edit lessons, so that I can update content as needed. 
- delete lessons, so that I can remove outdated or incorrect content. 
- organize lessons by tags using relevant key words, so that students can find related content easily. 

Grapple 2.0 (March 2025): 
- view and respond to comments on my lessons, so that I can interact with students and keep up to date on the success of articles.
- view student progress and quiz scores for my lessons, so that i can assess how well students are learning.
- create quizzes for lessons, so that students can test their knowledge. 

<br>
<br>

## Features

Grapple features include: 
- User sign up, authentication, and authorization
- A fully-responsive, accessible, mobile-first UI 
- Role-based access control and functionalities
- Search and filtering functionalities for students looking through lesson materials
- Interactive elements (comments and notes for students, dynamic content updates for content creators)
- CRUD functionality for lesson materials (for content creators)
- Cloud deployment for live accessibility 

<br>
<br>


## Front End


## Colour Scheme

![Image showing the site colour scheme: black, white, cherry, dark red, pink, and light pink](docs/Grapple%20Colours.png)

The initial colour theme for this project was simple and playful. Although a more feminine colour like pink can limit a user base, I wanted users to associate the site with lightheartedness and playfulness. 

Pink therefore seemed an appropriate colour, making the learning interface cute and appealing. The aim with this colour scheme was to create an association between learning and enjoyment. 

Later versions of the UI will offer a theme toggle, allowing users to toggle between colour schemes. 

<br>
<br>


## Font

This project uses two major font types: 
1. Jersey 10
2. Atkinson Hyperlegible Classic 

Jersey 10 is a pixel font, used as part of the sites branding plan. For more information, see the [Pixel Assets section](#pixel-assets). This font was used for larger titles and form inputs. 

![An image of the Jersey 10 font saying 'Welcome to GRAPPLE!'](docs/Jersey10.png)

<em>An example of the Jersey 10 font</em>

<br>

Atkinson Hyperlegible Classic is a sans serif font that has been used for all learning content on the platform. This font was chosen for its excellent readability and professional look. 

![An image of the Atkinson Hyperlegible font saying 'Prepositions - like 'to', 'in', and 'over' - are used to talk about the relationship between two items.'](docs/Atkinson%20Hyperlegible.png)
<em>An example of Atkinson Hyperlegible</em></em>

<br>
<br>


## Pixel Assets

The pixel image reflects Grapples approach to learning: that it should be fun, simple, and modular. In other words, in the way pixel images are made up of lots of smaller parts, the most effective approach to learning breaks down the process into small, bitesize chunks. 

Pixels were also used in the inital design to evoke a sense of nostalgia and playfulness in the brand. In later versions of Grapple, the pixel theme can be further integrated into progress tracking, games, quizzes, animations and other parts of Grapple's brand.


<br>
<br>

## Wireframes and Layout

- [Nav Bar](#nav-bar)
- [Landing Page](#landing-page)
- [Sign Up Page](#sign-up-page)
- [Student Dashboard](#student-dashboard)
- [Lesson Search](#lesson-search)
- [Content Creator Dashboard](#content-creator-dashboard)
- [Lesson Management](#lesson-management)
- [Lesson Creation](#lesson-creation)


The initial wireframes design outlined the layout and navigation for the landing page and sign up page. Other html templates worked from this design, using a nav bar: main content layout. 
 
 ### Nav Bar
The logo is place in the top right corner to optimize interaction for right handed mobile users. This is the main point of navigation for users across the site, offering links to: Home, Sign Up, About, Login. 

Python elif script changes the content of this dropdown to respond to different user types after log in: a student dashboard or content creator dashboard, and log out.

#### Landing Page
![Image of the langing page, with 'Welcome to Grapple' text and a sign up button](docs/landing.png)
<em>Landing Pgae Wireframe</em>

![Image of the landing page, with dropdown nav](docs/landing%20with%20dropdown%20(1).png)
<em>Landing Page Wireframe with Dropdown</em>


![An image of the current landing page](docs/landing2.png)
<em>Above is a screetshot of Grapple's current landing page. The current version features previews of lessons with the tag 'grammar', to give students a taste of the materials available on the platform and to encourage potential users to sign up to the site. The CTA button to 'sign up' is clear and prominent. </em>

#### Sign Up Page
![Image of a sign up form with username, email, password and avatar selection fields](docs/Sign%20up.png)
<em>Above is the original design for the sign up form. As well as entering a username, email, and password, users have the option to choose from 1 of 5 avatars. </em>

![Image of the sign up form with drop down activated](docs/signup%20with%20dropdown.png)
<em>Sign Up Wireframe with Dropdown</em>


### Student Dashboard
![A screenshot of the current student dashboard](docs/student-dashboard.png)
<em>Above, is a screenshot of the current student dashboard. It features a button to take you to the lesson search page, and shows all the lessons a student has bookmarked. </em>

### Lesson Search 

![A screenshot of the student's lesson search page](docs/lesson-search.png)
<em>Above is a screenshot of the student lesson search page, where students can serach for lessons using a keyword, or select pre-ordained tags to filter through search results. They have the option to bookmark these lessons in the lesson search page, or from the main lesson view.</em>

### Content Creator Dashboard
![A screenshot of the content creator's dashboard, with drop down nav engaged](docs/creator-dashboard.png)
<em>Above is a screenshot of the content creator dashboard, where lesson creators can choose to manage their lesson content, or create a lesson.</em>

### Lesson Management
![A screenshot of the lesson management page for creators](docs/lesson-manager.png)
<em>Above is a screenshot of the lesson management page, where content creators can view, edit, and delete the lessons they have created. They have the option to arrange lessons in order of creation, recently edited, and name, to make it easier to find the lesson they're looking for.</em>

### Lesson Creation
![A screenshot of the lesson creator page for content creators](docs/create-lesson.png)
<em>Above is a screenshot of the lesson creation page. Here content creators can give their lesson a title, assign relevant tags, write a short preview, and enter the main content of the lesson. </em>

<br>
<br>
<br>


## Backend

## Database Design
