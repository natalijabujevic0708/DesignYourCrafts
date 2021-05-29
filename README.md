![](media/readme_images/hero_image.png)

View the project on Heroku [here](https://design-your-crafts.herokuapp.com/)

# Overview

## Purpose of the application
Have you ever wanted to make your own craft but didn't have the time or material?
**Design Your Craft** is a page where you can design an item and have it handcrafted for you. 


## How does it work?

### First step: Choose an item you want to design  
Choose between jewlery boxes, christmas decoration or bottles.

### Second step: Design your product 
Choose between different patterns, decorations or customised messages

### Third step: Order a handcrafted item 
After you desiged an item, it will be handcrafted by one of our team members and send out to you!

Users can create a handcrafted item with the **Design Your Craft** application upon their first use of the application. No registration is necessary to design and order an item.


Users who are interested can sign up and have their past designs and orders info saved in the profile page. Users details can be saved on their profile to make the order quicker and the information can be edited or deleted easily.

# Features
The following are the features provided in the **Design Your Craft** application. 

## Navigation bar and Footer
* Each page features a **navigation bar** that has 3 navigation links - Home, About Us and Start the design. On a screen size smaller than a tablet the navbar becomes a collapsible element. In the right corner there are Profile and Shopping list icons.


* Each page features **social media links**  at the bottom. They redirect a user to the social media platform opening it in a new window. 

## Home & About page
* Users can learn about the purpose of the site on the Home and About page.
<img src="media//readme_images/home_example.png" alt="Home page" style="max-height:200px">
<p>&nbsp;</p>
<img src="media/readme_images/about us.gif" alt="About page" style="max-height:200px">
<p>&nbsp;</p>

## Start the design
* The user is presented with 3 categories of the products - Jewlery boxes, Christmas decorations and Bottles.

    <img src="media/readme_images/categories_example.png" alt="Product categories" style="max-height:200px">
    <p>&nbsp;</p>

* After deciding about a category, the user can choose a specific product to design.

    <img src="media/readme_images/product_example.png" alt="Products" style="max-height:200px">
    <p>&nbsp;</p>

* There are many options for the design:
 - colors
 - patterns
 - text
 - decoration

    <img src="media/demo.gif" alt="Design demo" style="max-height:250px">
    <p>&nbsp;</p>
* After the design is finished, the user can add it to the bag and complete the checkout to buy the product:



## User Login and Registration
* Registering users are asked to create a username, provide an email address and create a password.
* Users have to log in in order to have their order and design saved in their profile.  



## User Profile
* Users profile page contains a list of all of the customers personal details, past orders and designs.

    <img src="static/images/readme_images/profile.png" alt="Profile" style="max-height:200px">
    <p>&nbsp;</p>


 






# Wireframes

1. Home:
- [Desktop](media/readme_images/home.png)
- [Tablet](media/readme_images/home_tablet.png)
- [Mobile](media/readme_images/home_mobile.png)

2. About page:
- [Desktop](media/readme_images/about.png)
- [Tablet](media/readme_images/about_tablet.png)
- [Mobile](media/readme_images/about_mobile.png)

3. Start the Design:
- [Desktop](media/readme_images/design.png)
- [Tablet](media/readme_images/design_talet.png)
- [Mobile](media/readme_images/design_mobile.png)

4. Shopping bag:
- [Desktop](media/readme_images/bag.png)
- [Tablet](media/readme_images/bag_tablet.png)
- [Mobile](media/readme_images/bag_mobile.png)

5. Profile:
- [Desktop](media/readme_images/profile.png)
- [Tablet](media/readme_images/profile_tablet.png)
- [Mobile](media/readme_images/profile_mobile.png)



# Site Users 
### Who is the site focused on?
People who want to buy or gift a unique item that they design but don't have the skills/time/materials to create them.


### The following user stories were used to design the website:
1. Mel, “I would love to create something for my mom, but I was never good and arts and crafts and honesly, I don't have the time with work and everyday chores to learn a new skill."


# Testing
Testing information can be found in the separate testing file that can be accessed [here](https://github.com/natalijabujevic0708/.../TESTING.md).


# Database Organisation
Database information can be found in the separate file that can be accessed [here](https://github.com/natalijabujevic0708/..../DATABASE.md).


## Bugs/ Features Left to Implement


# Technologies 

## Languages

* HTML5
* CSS3
* JavaScript  
* Python (3.6)


## Libraries, frameworks and API's
- [BootStrap4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) to assist with the structuring and responsiveness of the site
- [Django](https://www.djangoproject.com/) - Python framework for building the project.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - to style Django forms.
- [Fontawesome (4.7.0)](https://fontawesome.com/v4.7.0/) library for custom icons
- [Google Fonts](https://fonts.google.com/) for the fonts used throughout the page
- [Gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server to enable deployment to Heroku.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - templating language for Python
- [JQuery](https://jquery.com/) for DOM manipulation.
- [jscolor.js](https://jscolor.com/docs/) - jscolor.js is a JavaScript color picker with opacity channel
- [Psycopg2](https://pypi.org/project/psycopg2/) - to enable the PostgreSQL database to function with Django.
- [Stripe](https://stripe.com/ie) - to handle financial transactions.

### Tools
- [Vectr](https://vectr.com/) - for creating the Vector Shape / SVG Markup.
- [Balsamiq](https://balsamiq.com/) - to create wireframes.
- [xiconeditor](http://www.xiconeditor.com/) - to create icons

### Databases
- [SQlite3](https://www.sqlite.org/index.html) - a development database.
- [PostgreSQL](https://www.postgresql.org/) - a production database.
## Hosting and deployment 

- [Git](https://git-scm.com/) for version control
- [Github](https://github.com/) to store repositories of the project
- [Heroku](https://www.heroku.com/) for hosting the deployed app
- [AWS S3 Bucket](https://aws.amazon.com/) -  to store static and media files in production.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for compatibility with AWS.


# Deployment
This project has been pushed and deployed to the cloud application platform [Heroku](https://www.heroku.com/).



## Credits
### Code 
*[boutique_ado_v1](https://github.com/ckz8780/boutique_ado_v1): Project that was followed to create most of the layount and the functionality for the project Design your Crafts (Products, Shopping bag, Checkout, Profile...)
* [ Dynamically Change the Colors ](https://tympanus.net/codrops/2019/09/03/how-to-dynamically-change-the-colors-of-product-images-using-css-blend-mode-and-svg/): Tutorial used to dynamically change the colors and patterns of product images using CSS Blend Mode and SVG
* [ Auto-Playing Slideshow ](https://css-tricks.com/snippets/jquery/simple-auto-playing-slideshow/): Tutorial used to create the slideshow in the About Us section
* [ How to create tabs]https://www.w3schools.com/howto/howto_js_tabs.asp): Tutorial used to create tabs in the Start the Design section
* Example code to add dynamic text to canvas image found on Codepen - [link](https://codepen.io/ahebler/pen/KzyQBZ)
* Example code to create a draggable text box in canvas found on Stack Overflow - [link](https://stackoverflow.com/questions/59828371/draggable-text-box-on-top-of-canvas-image)
* Example code to add, resize, position and color change text inside a div using jquery
 found on Stack Overflow - [link](https://stackoverflow.com/questions/40103239/add-resize-position-color-change-text-inside-a-div-using-jquery)
* Example code to allow a user to resize a image on the page found on Stack Overflow - [link](https://stackoverflow.com/questions/31545041/allowing-a-user-to-resize-a-image-on-the-page)
* Example code to rotate images with slider found on Codepen - [link](https://codepen.io/companionstudio/pen/ewxboE)


### Content

* Inspiration for the README.md came from [trisdauvergne/milestone-project-03](https://github.com/trisdauvergne/milestone-project-03) and [taikatta/Milestone3-Konyvkucko](https://github.com/taikatta/Milestone3-Konyvkucko)


### Media
* Paintbrush icon was taken from the [depositphotos.com](https://depositphotos.com/289261084/stock-illustration-paintbrush-line-icon-colorful-paint.html)

## Acknowledgements
I would like to thank my mentor Brian Macharia for his advice and help with this project.




