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

The django administration panel was used to add items to the Products and Orders tables.  The following code was used to establish the required models:

Products (products app / models.py):

~~~
class Product(models.Model):
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='static/img')
~~~

Orders (checkout app / models.py):

~~~
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
        
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)
~~~

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

The following steps are how this application was deployed, using Cloud 9 IDE:

1.	Set-up new workspace in C9
2.	Using the bash terminal install the relevant version of Django:
   * Sudo pip3 install django==1.11
3.	Create a django project: “django-admin startproject hconsultants .”
4.	Open the “settings.py” file and add C9 as an allowed host [(os.environ.get(‘C9_HOSTNAME’)]
5.	Run the server: “python3 manage.py runserver $IP:$C9_PORT” 
6.	Show Hidden Files in C9 settings and open the “.bash_aliases” file and insert the following text;  run=” python3 ~/workspace/manage.py runserver $IP:$C9_PORT”, this means you don’t need to type the full string in step 3 above each time you want to run the server (instead, you just type the word “run”)
7.	Close the terminal and reopen it to make this alias available.
8.	Initiate a GIT Repo (git init)
9.	echo ‘*.sqlite3’ >> .gitignore
10.	git add --all
11.	git remote add origin https://github.com/Jagger81/h-consultants.git
12.	git push origin master
13.	Add “accounts” folder and import app_authentication files (File>Upload Local Files)
14.	Add “templates” folder, same as above (from “templates folder”)
15.	Create top level “static” folder, then “css” and create a “custom.css” file
16.	Update settings:  wire it all up.  Add ‘accounts’ as an installed app in the “settings.py” file
    * Add “AUTHENTICATION_BACKENDS” and “MESSAGE_STORAGE”
17.	Run “python3 manage.py makemigrations”
18.	Run “python3 manage.py makemigrations accounts” (no changes noted in either app)
19.	Run “python3 manage.py migrate”
20.	Changes made to urls.py (see git commits)
21.	Run “sudo pip3 install django-forms-bootstrap”
22.	Create a super user; “python3 manage.py createsuperuser” (call them ‘admin’ and create a password)
23.	Add “django_forms_bootstrap” to installed apps in the settings.py file
24.	Need to specify that all directories called “templates” essentially contain templates; “[os.path.join(BASE_DIR, ‘templates’)]” Line 59
25.	Create a Home and Products app:
    * Python3 manage.py startapp home (run again and replace with “products”)
26.	To allow the upload of images install Pillow: sudo pip3 install Pillow
27.	Make migrations, etc.
28.	Setup product URL’s / Views / Models and perform some styling
29.	Ensure that STATIC has been added to the settings.py file
30.	Sudo pip3 install stripe
31.	Set up free Stripe account online (stripe.com)
32.	Get API Keys (reveal secret key)
33.	Insert STRIPE details in setting.py and create env.py file
34.	Copy key details from Stripe website to env.py
35.	Hide env.py file so it doesn’t get uploaded to GitHub;
    * Echo env.py >> .gitignore
36.	To use this file, be sure to insert “import env” to your settings.py file
37.	Python3 manage.py startapp checkout
38.	Add ‘checkout’ to list of apps in setting.py file
39.	Create models.py file under checkout app
40.	Update admin.py file of the account app, add those models
41.	Create STRIPE settings and Checkout.html
42.	Create Heroku app and go to “Resources” > Add-ons to create a database:
    * Postgres database (free-hobby)
    * Copy key from Config_Vars
43.	Return to C9 and run:
    * ‘sudo pip3 install dj-database-url’ 
    * ‘sudo pip3 install psycopg2’ (package for connect two postgres databases)
    * ‘pip3 freeze > requirements.txt’  (heroku will need these dependancies to build the app)
44.	Update settings.py and env.py (with database details and secret_key)
45.	Run ‘python3 manage.py migrate’ (to migrate existing migrations to our new postgres database)
46.	Because it’s totally new and blank database we need to create a superuser:
    * ‘python3 manage.py createsuperuser’
47.	Set up AWS Account and S3 bucket
48.	Run ‘sudo pip3 install django-storages’
49.	Run ‘sudo pip3 install boto3’ (these allow Django to connect to AWS S3)
50.	Change settings.py and env.py files (to include any Secret Keys, et.)
51.	Run ‘python3 manage.py collectstatic’
52.	Create ‘custom.storages.py’ and update settings.py file
53.	Set up Travis CI and change settings.py file
54.	Set Config Vars Heroku and connect to Git Hub repo
55.	Run ‘sudo pip3 install gunicorn’ (package required to connect to Heroku)
56.	Update requirements.txt and add Procfile
57. Deploy application via Heroku

In addition, you can clone or download the code from this GitHub repository.


## Credits

The template used in this project is the *BizPage* template available from <a href="https://bootstrapmade.com/bizpage-bootstrap-business-template/" target="_blank" >bootstrapmade.com</a>.  Testimonial / Team and Portfolio images are supplied with the template.


### Acknowledgements

- I would also like to acknowledge the help received from the Slack Community in helping solve some of the issues realted to this project.
