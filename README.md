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
 - live in their own or rented house with a small garden or have a few plant pots on the balcony.
 - be between 20-50 years old
 - have little to intermediate experience in gardening
 - want to read a little about plants before they decide to buy them
 - would like to take care of the plants in a natural way (without chemical fertilisers)

## First time Visitor's needs:

- they would like to know what the page is about, this means that the main topic is described clearly 
- easy and intuitive navigation throughout the webpage (divided into proper sections)
- to find plant descriptions, their needs, photos and some advice on how to take care of them
- know where to find important information for them (navigation bar) 


## Returning visitors are very often interested in:

- reading more interesting descriptions of plants
- sharing saved descriptions and pictures with others users
- adding their own advice about taking care of the plants
- adding pictures and descriptions of plants they alredy have
- adding pictures and descriptions of plants they would like to have in the future
- sorting the plants by place (Sun/Shade etc.)
- editing saved plants
- adding pictures from own gardens to inspire others  

# Design

## Global 

## Color Scheme

The webpage has a white background and the pages and plants headings on the page have dark green color, so that they correspond nicely with the white background. All paragraphs are written in black to give a good contrast and give people a chance to read content easily. The navigation bar, footer and buttons on the page have the same dark green background to keep consistent design. White text is added to incerease the users experience. 


## Typography

## Imagery

Imagery is very important for this page, and is used throughout the website, so that it's visually appealing. It helps visitors remember flowers and easily identify them.

## Wireframes

- ![Mobile view ](https://madatoo.github.io/plantarium-ms3/static/wireframes/mobile_plantarium.pdf)

- ![Tablet view](https://madatoo.github.io/plantarium-ms3/static/wireframes/tablet_plantarium.pdf)

- ![Desctop view](https://madatoo.github.io/plantarium-ms3/static/wireframes/desktop_plantarium.pdf)

# Features

## Home page

This page provides basic information about the main purpose of this page and about, who it's aimed at.

## Plants page

Here are all plants added to plantarium database. To browse them you need to choose one from available options and then select the category that will be displayed as the result. 

## Add plant page

That is probably the most important page in the whole project. Here you can add to plantarium database your plants. That part was the most frustraiting and challenging for me. Especially the part with plant pictures, plant type and plant place. I needed to understand it very well to implement needed features.

### CRUD 

The most important thing in this project was designing the application which meets all CRUD criterias. 

1. Create - it was achived by creating an Add Your Plant page with a form to add a plant to the database.
2. Read - to implement this part All Plants page was created to allow visitors make a choice beetween the available categories which will display when they decide which one they want to browse.
3. Update - from All Plants page visitors can go and read more about a specific plant and edit all information about the plant.
4. Delete - simlarly to what's above, visitors can remove data about a specific plant using All Plants page.


# Technologies Used

- HTML5 - used for building the website
- CSS3 - for styling elements
- JavaScript to improve users experience
- Python used as a “scripting language” for web applications
- MongoDB to store created data inside plantarium database
- Flask for developing web application 
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

In this project FAQ wasn't implemented yet, but some information about page functionallity was implemented. 

- main purpose of the webpage is described on the Home page below the carusel,
- how to add plants - each field in Add Plant form is described or intuitive.
- how to browse plants - that is posibble on All Plants page. Here visitors can browse plants afrter choosing some categoty. 
- edit and delete - those features are available on the All Plants Category page, which is displayed after choosing the plant about which visitors want to read more. Here are also available links to other sources implemented by users. (I am not sure if they will be working properly now)

### Returning Visitors

Most of teir needs is implemented, but not all. I didn't add an login and register function in this project (that will be done in future). This decision, bring me a lot od problems :). And didn't allow to create own (user) database. For now, this app allows each users add /edit and delate  each plant in this database -  and that is, because I did't created an admin or super-user. 

### Known bugs add challanges 

I wanted to create an app which will allow users to add some info about their favourite plants to the database. Unfortunately not everything is going just like I intended. 

First of all, my Add Plant form has a bug in the place to choose the category (it is a dropdown field with all categories that are available in the created database and saved in the categories collection). Here Validation rule is not working well, the red color does not appear when the category is not selected. I tried to solve it by adding a snippet of code from Tim Nelson's material which was showed in the school project, but my skills are not good enough to fix it, yet. 

The one from my biggest challanges in this project was understanding how the database works, and where I should write some conditions, to edit/display or delete some data.  

I had a lots troubles with adding images into database. To solve this issue I wanted : create an route to store my images to that I was whached an tutorials from Pretty Printed, then save them directly in project (pictures for carousel and categories), I also added images to the imgbb.com, where I created an album, and in github in different repositarium (lavener-iguana). Finally I addded the pictures using url for github repo.


### Links

This time links are only to other subpages. Social Media links weren't added, but in the future they will be implemented to create a fanpage on Facebook and Discord, where visitors will have an opportunity to share their own expirences, to meet together or to create some online events as well. 

### Responsive Design

To check if the app is responsive I used:

- Dev Tools,
- Am I responsive page

### Validators
 
I validated this app on :

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

My first report showed me these results (taken during my design process) 

--------------------------------------------------------------------
Criterion          |  Results 1   |   Results 2  |    Improved y/n
-------------------------------------------------------------------
Performance        |     63       |  98
-------------------------------------------------------------------- 
Accessibility      |     73       | 91
--------------------------------------------------------------------
Best Practices     |     87       | 87
--------------------------------------------------------------------
SEO                |     92       | 100
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

To prepare this project I took an ispiration from my own previous projects to create a READMEmd file. 
I also was watched project  from March Hackhaton (Happy Paddy Go, where I was one from contributors), to look how use Materialize. I needed also some idea how to create this app, and I watched some projects created by others students. Some solutions, I transform to my own idea. 

## Content 

To prepare valuable content I was using my own knowledge, experience, and  materials which are available on these websites:
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

I would lkke to thank:

- my mentor Brian Maharia, for his tips and clarification about what I need to include in this project,
- Tutor Support Team for advising me how to solve some of my issues, which I had in this project
- Student Care for support during the whole course,
- Students in Code Institute on Slack channels, which gave me support and some advice as well
- #women-in-tech Hackathon new friends from team-8 for the opportunity to work on our project at the same time
- and finally my family, which is the most important for me :)  
 
# Disclaimer

The content of this page is for educational purposes only.
