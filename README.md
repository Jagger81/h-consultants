[![Build Status](https://travis-ci.org/Jagger81/h-consultants.svg?branch=master)](https://travis-ci.org/Jagger81/h-consultants)

# Django Project

## Humanitarian Consultants

This is a basic online recipe book for various users.  Features include viewing, editing and adding recipes - additional features may be added in the future.  The full application can be viewed <a href="https://humanitarian-consultants.herokuapp.com/" target="_blank" >here</a>.
 
## UX

This web application is aimed at Humanitarian professionals that work on providing dedicated support to Overseas Programmes in the capacity of Finance, Human Resources, Logisitics & Supply Chain and Child Protection.  As well providing access to a dedicated team of humanitarian professionals with extensive experience in the field, users can request remote support/advice, request trainings/workshops, system reviews/audits, and purchase useful materials such as Manuauls/Policy Documents, Documents Templates.

### User Stories:

![hc_user_story_1](https://user-images.githubusercontent.com/28737216/53301320-2d94b800-3849-11e9-9cc8-543438e3353c.PNG)

![hc_user_story_2](https://user-images.githubusercontent.com/28737216/53301321-2d94b800-3849-11e9-8eb6-58af18d99df1.PNG)

![hc_user_story_3](https://user-images.githubusercontent.com/28737216/53301322-2d94b800-3849-11e9-8dd5-3585441aafba.PNG)

![hc_user_story_4](https://user-images.githubusercontent.com/28737216/53301323-2d94b800-3849-11e9-8d84-d858a6e59a48.PNG)

![hc_user_story_5](https://user-images.githubusercontent.com/28737216/53301324-2e2d4e80-3849-11e9-9116-98691394300e.PNG)

### Data Schema:



### Wireframes / Mockups:

The following are the initial mockups, based on the *BizPage* template available from <a href="https://bootstrapmade.com/bizpage-bootstrap-business-template/" target="_blank" >bootstrapmade.com</a>:

#### Index / Landing Page:

![hc_index](https://user-images.githubusercontent.com/28737216/53301771-dbef2c00-384e-11e9-863b-da7b2ae4176c.PNG)

The index page will also include the following sections when the user scrolls down through the page:
- About Us
- Services/Portfolio of Services
- Testimonials
- Team details
- Contact Form (design only - not fully initiated)

#### Products Page:

![hc_products](https://user-images.githubusercontent.com/28737216/53301772-dbef2c00-384e-11e9-9650-6e0aa43525d2.PNG)

There are identical pages established for each Category of Products (Workshops/Trainings, Manuals/Guidelines, Templates, System Audits)

#### Shopping Cart:

![hc_cart](https://user-images.githubusercontent.com/28737216/53301769-dbef2c00-384e-11e9-9300-fbe24c8f06f9.PNG)

#### Checkout:

![hc_checkout](https://user-images.githubusercontent.com/28737216/53301770-dbef2c00-384e-11e9-98c2-8d0180a54096.PNG)

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Filter on Portfolio of Services section
- User Registration
- User authentication (login and log out)
- Authentication messages
- Shopping Cart
- Checkout (using Stripe for payment authentication)


### Features Left to Implement

The following are features that required futher work and would be implemented in subsequent real-life implementation

- Contact form
- Quantity field for Products not being allows to remain as zero
- Portfolio images link would ideally open a modal to provide more info on the respective service


## Technologies used

Technologies used in this project include:

* Bootstrap: *BizPage* template available from <a href="https://bootstrapmade.com/bizpage-bootstrap-business-template/" target="_blank" >bootstrapmade.com</a> was used for HTML and CSS styling.
* HTML5/CSS: Used for the layout and styling of the application.
* Python 3.4.3: The back end functionality of the application was written entirely in python 3.0.
  Was originally running on Python 2, following code was executed to upgrade:
  ~~~~
  jagger81:~/workspace (master) $ sudo mv /usr/bin/python /usr/bin/python2
  jagger81:~/workspace (master) $ sudo ln -s /usr/bin/python3 /usr/bin/python
  jagger81:~/workspace (master) $ python --version
  Python 3.4.3
  ~~~~
* Django framework: used to expedite the clean design and devlopment of the application.
* Balsamiq: Used to create the below wireframes.
* Cloud9 IDE used as development environment workspace
* The project uses **JQuery** to simplify DOM manipulation.
* STRIPE is used for payment functionality.
* TRAVIS CI is used for checking the application build.
* Amazon S3 Bucket is used for storage of static files.
* FormCarry is used for actioning the Contact Form (still to be fully implemented).
* PostgresSQL connection via Heroku


## Testing

Mainly manual testing used throughout - for routing and checking if data is properly rendered in the correct template and format.

Basic testing included:

DB Connection
SuperUser login working correctly
Adding new records to the database
Editing database records
Ensuring the "settings.py" is configured correctly
Rendering data / images
Many GitHub commits will contain the prefix TESTING

Pep 8 was used to assist with cleaning the data - indentation, whitespaces, non-spaces, 2 lines expected

http://pep8online.com/

Stripe test payment received successfully:

![payment_success](https://user-images.githubusercontent.com/28737216/53303942-24671380-3868-11e9-8b49-ea812625dec4.PNG)

Test builds were consistently checked also, via both Travis CI and Heroku:

![build_passed1](https://user-images.githubusercontent.com/28737216/53303959-57110c00-3868-11e9-9505-7389bca984c5.PNG)

![build_passed2](https://user-images.githubusercontent.com/28737216/53303960-57110c00-3868-11e9-9d56-baaeb8f26c80.PNG)


Basic testing of Products was also performed:

PASS:
![test products](https://user-images.githubusercontent.com/28737216/53303988-79a32500-3868-11e9-81b3-3d74471178e7.PNG)

FAIL:
![test products_fail](https://user-images.githubusercontent.com/28737216/53303989-7a3bbb80-3868-11e9-9ea3-ff5bf8c19da8.PNG)



## Deployment



In addition, you can clone or download the code from this GitHub repository.


## Credits

### Content
- 

### Media
- 

### Acknowledgements

- I received inspiration for this project from https://myfoodbook.com.au and https://www.bbcgoodfood.com
- I would also like to acknowledge the help received from the Slack Community in helping solve some of the issues realted to this project.
