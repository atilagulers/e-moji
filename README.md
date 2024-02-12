# 🍭 🅴-🅼🅾🅹🅸

A Virtual Restaurant Reviewing App 🍔📱

## Distinctiveness and Complexity:

### Global Templates:
This project is different from before projects because i used global templates.
For example: i created a templates folder which is in the root of the project not only app.
Inside of the templates folder there is a "base.html" file, every page inherits from this layout.
In addition i created navbar.html inside of global templates folder. I did this to prevent code repetition.

### Components:
Again to prevent code repetition and clean code purposes i created "components" folder.
Then i created "restaurant_list.html" and "restaurant_card.html" inside of this folder.
i did this to prevent code repetition and centralized control. I highly used these compenents
and i could use it just by writing one line code to include whole component.


### Filter System:
I used a filter system by using get queries. Users are able to select filters and
able to apply it. Then the client sends a request by get method. Server gets the query
and filter the restaurants according to this query. As i remember we've never done that.

I figured out by myself all of them. When i start project i thought how can i make it more scalable
and i found all of the solutions. I think it was more complex then before we've done.

### File Structure
* components/: Contains HTML templates for different components of the app such as the restaurant list (my_restaurants.html), the individual restaurant view (restaurant.html), and review submissions (reviews.html). 
* core/: Houses the main Django app with views (views.py), URL dispatchers (urls.py), models (models.py), forms, and tests (tests.py). 
* static/: Stores static files like CSS, JavaScript, and image assets. Inside the images folder, restaurant-related images are kept. 
* templates/: Includes base HTML (base.html) and navigation bar template (navbar.html) which are extended by other templates. 
* emoji-project/: The main project directory with settings and root URL configurations. 

### Running the Application

1. Execute python manage.py runserver from the terminal in the project directory. 
2. Open a web browser and navigate to localhost:8000 to access the application.
