![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Plantarium

To visit the live website, click here (add link to the live website).

insert picture from  (is my website responsive)

# Introduction

This is my third project for Code Institute. I am really glad that I got to work on it because it gave me an opportunity to show my passions, which are gardening and storing information about plants - the flowers, shrubs, and other plants I alredy have in my own backyard and those I would like to have in the future. This is why I decided to create a plants database for small gardens.

# User Experience (UX)

This was probably the hardest part of my project. To make this project useful for my visitors, I needed to create an ideal visitor's profile.

I assumed that this person would:

 - love gardening,
 - live in their own or rented house with a small garden or a few plant pots on the balcony.
 - be between 20 - 50 years old
 - have a small or intermediate experience in gardening
 - want to read a little about plants before they decide to buy them
 - would like to take care of the plants in a natural way (without chemical fertilisers)

## First time Visitor's needs:

- they would like to know what the page is about, this means that the main topic is described clearly 
- easy and intuitive navigate through out the webpage (divided into proper sections)
- to find plant descriptions, their needs, photos and some advice on how to take care of them
- know where to find important information for them (FAQ and navigation bar)
- how to create own account to save items, which they found interesting 


## Returning visitors are very often interested in:

- reading more interesting descriptions of plants
- creating their own plant book
- sharing saved descriptions and pictures with others users
- adding their own advices about taking care of the plants
- adding pictures and descriptions of plants they alredy have
- adding pictures and descriptions of plants they would like to have in the future
- sorting the plants by type (flowes/shrubs etc.)
- sorting plants by the options "I have the plant" or "I want the plant"
- editing saved plants
- adding pictures from own gardens to inspire others  

# Design

## Global 

## Color Scheme

The webpage have white background color, the pages and plants hedings on the page have darkgreen color to correspond nicely with the white background, whole paragraphs are written in black color to give a good contrast and give people a chance to read content easily. The navigation bar, footer and buttons on the page have a the same darkgreen background color to keep consistently design White text is added to incerease the users experience. 


## Typography

## Imagery

Imagery is very important for this page, and is used throughout, the website so that it's visually appealing. It helps visitors to remember flowers and easly identify them.

## Wireframes

- [Mobile view ](https://madatoo.github.io/plantarium-ms3/static/wireframes/mobile_plantarium.docx)

- [Tablet view](https://madatoo.github.io/plantarium-ms3/static/wireframes/tablet_plantarium.docx)

- [Desctop view](https://madatoo.github.io/plantarium-ms3/static/wireframes/desktop_plantarium.docx)

# Features

## Home page

This page provide basic information about main purpose of this page and about that, who it aimed at.

## Plants page

Here are all plants added to plantarium database. To browse them you need choose one from available options and then selected category will be displayed on as the result. 

## Add plant page

That is probably most important page in whole project. Here you can add to plantarium database your plants. That part was for me most frustraiting and challenging. Especially part with plant pictures, plant type and plant place. I needed understand it very well to implement needet features.

### CRUD 

The most important thing in this project was design the application which meet whole CRUD criterias. 

1. Create - it was achived by creating a Add Yoyr plant page with form to add plant to a database.
2. Read - to implement this part All Plants page was created to allow visitors make a choose beetween available categories which will displayed when s/he decide which want to browse.
3. Update - from All Plants page visitors can go and read more about specific plant and edit all informations about plant.
4. Delete - simlar, like descripted above, visitors can remove data about specific plant using All Plants page.


# Technologies Used

- HTML5 - used for building the website
- CSS3 - for styling elements
- JavaScript.
- Python
- MongoDB
- Flask
- JQuery - to initialize Materialize CSS components.
- Google Fonts -  used for fonts on website
- Font Awesome - used for Icons.
- Materialize CSS - Used for elements, components and styling of the page.
- Balsamic - to creates of the Wireframes.
- GitHub - Used for hosting the code, and version control.
- Notion - for project management
 
# Testing

## User Stories testing

### First Time Visitor Goals

In this project FAQ wasen't implemented yet, but some informations about page functionallity were implemented. 

- main purpose of the webpage is described on the Home page below the carusel,
- how to add plant - each field in Add Plant form is described or intuitive (such us  switcher add to list wish field or plant place - you need only click on the correct place which have added icon, to help you decide about the correct place).
- how to browse plants - that is posibble on All Plants page. Here visitors can browse plants afrter choosing some categoty. 

- edit and delete  - this features are available on page All Plants Category, which is displayed after choosing plant about which visitors want to read more. Here are also available links to other sources implemented by users. (I am not sure they will be working properly now)

### Returning Visitors

Here not everythin was done yet.  I didn't add 

### Known bugs

I wanted create an app which will allows users add some info about favourite plants to databese. Unfortunatly not everything is going just like I intendent. 

First at all, my add plant form has a bug in filed choose category (it is a dropdown field with all categories which are  available in created database and saved in categories collection). Here Validation rule not working fine, the red color is not appered when the category is not selected. I tryied to solve it by adding the snippet of code from Tim Nelson materials which was showed in school project, but my skills wasent large, to fix it now. 


### Links

This time links are only to other subpages. Social Media links wasent added, but in future will be implemented to create a fanpage on Facebook and Discord, where visitors will have an opportunity to share own expirences, meet together or create some online events as well. 

### Responsive Design

To check the app is responsive I used:

- Dev Tools,
- 

### Validators
 
I walidated this app on :

1. [HTML Validator](https://validator.w3.org/)
2. [CSS Validator](https://jigsaw.w3.org/css-validator/)
3. [JavaScript Validator](https://jshint.com/)
4. [Python Validator](http://pep8online.com/)
5. [Autoprefixer](https://autoprefixer.github.io/)

I also used:

- Mozzilla and Google Chrom Dev Tools and
- LightHouse report to improve my app

### Browser Compatitbility

This app works fine on all browsers. I tested Plantarium on:

- Google Chrom,
- Mozzilla,
- Opera,

### Grammar and spelling

Was made during design process and after finished job.

### Lighthouse

My first report showed me this results (that was during my design process) 

--------------------------------------------------------------------
Criterion          |  Results 1   |   Results 2  |    Improved y/n
-------------------------------------------------------------------
Performance        |     63
-------------------------------------------------------------------- 
Accessibility      |     73
--------------------------------------------------------------------
Performance        |     87 
--------------------------------------------------------------------
SEO                |     92
--------------------------------------------------------------------

# Deployment
 
This project is stored on GitHub repository and hosted on Heroku.
 
## Github

To deploy this page to GitHub Pages from its GitHub repository, the following steps were taken:

1. Log into GitHub.
2. From the list of repositories on the screen, select madatoo/ms2-sligo
3. From the menu items near the top of the page, select Settings.
4. Scroll down to the GitHub Pages section.
5. Under Source click the drop-down menu labelled None and select Master Branch
6. On selecting Master Branch the page is automatically refreshed, the website is now deployed.
7. Scroll back down to the GitHub Pages section to retrieve the link to the deployed website.

Run this project locally (clone this project into Gitpod) you will need:

- a Github account. Create a Github account here
- use the browser with extention for gitpod Then follow these steps:

1. Install the Gitpod Browser Extentions for your browser
2. After installation, restart the browser
3. Log into Gitpod with your gitpod account.
4. Navigate to the Project GitHub repository
5. Click the green "Gitpod" button in the top right corner of the respository
6. This will trigger a new gitpod workspace to be created from the code in github where you can work locally.

## Heroku

1. Create a new application using the Heroku dashboard.
2. Go to settings tab, and then click on "reval config vars" and add:
- IP (0.0.0.0), 
- PORT (5000),
- MongoDB Name,
- MongoDB URI (URL with DB name and password)
3. Install Heroku via the console log using "npm install -g Heroku"
4. Log into Heroku via console using "heroku login" and follow on the screen instructions to log in. 
5. Create a requirements.txt file using the " pip3 freeze > requirements.txt " command.
6. Create a Procfile (remember it do not have any extentions) use the " echo web: python app.py > Procfile " command.
7. Push your code into Github repository
8. Connect GitHub to Heroku to do that go to Heroku page in Deply tab go to "App connected to GitHub" type your user name in Github and the repository name (which you want to connect with Heroku)
9. In Deploy Tab go to Automatic deploys section and click "Enable Automatic Deploys"
10. to see deployed app click "'Open App" on the top of the page
11. in Setting tab in Domains section will be link to your app.

### Run project on GitPod 
1. Select the Repository from the GitHub Dashboard
2. Click the green button labelled 'GitPod'
3. Install the necessary libraries specified in the requirements.txt
4. Set your environment variables by creating and adding them into a env.py file as showed below:

os.environ.setdefault("SECRET_KEY", <SECRET_KEY>) 
os.environ.setdefault("MONGO_URI", "mongodb+srv://marusroot:<PASWORD>@myfirstcluster.qk09g.mongodb.net/plantarium?retryWrites=true&w=majority") )
os.environ.setdefault("MONGO_DBNAME", <DB Name>)

Remember to replace the content inside <>  

5. Create a .gitignore file in the root directory and add the env.py file to avoid it being pushed to GitHub
6. Import the env.py file into the app.py file.
7. Runn the application.

# Credits

To prepare this project I took an ispirations from my own previous projects to create a READMEmd file. 

## Content 

To prepare valuable content I was using my own knowledge, experience, and  materials which are available on this websites:
 - [The Royal Horticultural Society](https://www.rhs.org.uk)
 - [Wikipedia](https://en.wikipedia.org)
 - [The Old Farmer's Almanac](https://www.almanac.com/)
 - [The Lakeland Horticultural Society](http://holehirdgardens.org.uk)
 - [ The BBC Gardeners' World Magazine ](https://www.gardenersworld.com)
 - [The Sunday Gardener](https://www.sundaygardener.co.uk)

## Images

In this project I used the free images available on [unsplash](https://unsplash.com)

The images authors are:

- Alexander Schimmeck
- Waldemar Brandt
- Zoe Schaeffer
- Darren Nunis
- Nicolette Meade

# Acknowledgements

I would lkke to thank you:

- my mentor Brian Maharia, for his tips and clarification about that what I need to include in this project,
- Tutor Support Team for advise how to solve some from my issue, which I had in this ptoject
- Student Care for support during whole course,
- Students in Code Institute on Slack channels, which gaved me support and some advices as well
- #women-in-tech Hackathon new freands from team-8 for opportunity to working in the same time with our project as well
- and finally to my family, which is the most important for me :)  
 
# Disclaimer

The content of this page is for educational purposes only.
