# 🍭 🅴-🅼🅾🅹🅸

A Virtual Restaurant Reviewing App 🍔📱

## Distinctiveness and Complexity:

### Global Templates:
This project differs from previous projects because I utilized global templates. 
For instance, I created a 'templates' folder at the root of the project, not just within the app. 
Inside the 'templates' folder, there's a 'base.html' file, which serves as the layout for every page. 
Additionally, I created 'navbar.html' within the global templates folder to avoid code repetition.

### Components:
To maintain clean code and prevent repetition, I established a 'components' folder. 
Within this folder, I created 'restaurant_list.html' and 'restaurant_card.html'. 
This approach allowed for centralized control and easy inclusion of these components with just a single line of code.

### Filter System:
I implemented a filter system using GET queries. Users can select filters and apply them. 
The client then sends a GET request, and the server filters the restaurants based on this query. 
As far as I remember, we haven't implemented this before.

I came up with all of these solutions on my own. When I started the project, 
I brainstormed ways to make it more scalable, and I found these solutions. 
I believe it was more complex than anything we've done before.

### File Structure
* components/: Contains HTML templates for different components of the app such as the restaurant list (my_restaurants.html), the individual restaurant view (restaurant.html), and review submissions (reviews.html). 
* core/: Houses the main Django app with views (views.py), URL dispatchers (urls.py), models (models.py), forms, and tests (tests.py). 
* static/: Stores static files like CSS, JavaScript, and image assets. Inside the images folder, restaurant-related images are kept. 
* templates/: Includes base HTML (base.html) and navigation bar template (navbar.html) which are extended by other templates. 
* emoji-project/: The main project directory with settings and root URL configurations. 

### Running the Application
```
1. Execute 'python manage.py runserver' from the terminal in the project directory.
2. Open a web browser and navigate to localhost:8000 to access the application.
```
