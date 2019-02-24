[![Build Status](https://travis-ci.org/Jagger81/h-consultants.svg?branch=master)](https://travis-ci.org/Jagger81/h-consultants)

# Djano Project

## Humanitarian Consultants

This is a basic online recipe book for various users.  Features include viewing, editing and adding recipes - additional features may be added in the future.  The full application can be viewed <a href="https://basic-recipe-book.herokuapp.com/" target="_blank" >here</a>.
 
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

The following are the initial mockups, based on the Materialize *Parallax* template that was used:

#### Index / Landing Page:



#### Recipes Page:



#### View Recipe Page <recipe_id>:



#### Edit Recipe Page <recipe_id>:



#### Add/Insert Recipe Page:



## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- 

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea


## Technologies used

Technologies used in this project include:

* Materialize: Materializecss was used for a basic HTML templates and styling.
* HTML5/CSS: Used for the layout and styling of the application.
* Python 3.4.3: The back end functionality of the application was written entirely in python 3.0.
  Was originally running on Python 2, following code was executed to upgrade:
  ~~~~
  jagger81:~/workspace (master) $ sudo mv /usr/bin/python /usr/bin/python2
  jagger81:~/workspace (master) $ sudo ln -s /usr/bin/python3 /usr/bin/python
  jagger81:~/workspace (master) $ python --version
  Python 3.4.3
  ~~~~
* Flask Microframework: Flask was used to extend pythons functionality to the frond end.
* Balsamiq: Used to create the below wireframes.
* Cloud9 IDE used as development environment workspace
* The project uses **JQuery** to simplify DOM manipulation.
* STRIPE is used for payment functionality
* TRAVIS CI is used for checking the application build
* Amazon S3 Bucket is used for storage of static files
* FormCarry is used for actioning the Contact Form (still to be fully implemented)


## Testing



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
