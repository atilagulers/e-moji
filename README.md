# 🍭 🅴-🅼🅾🅹🅸

A Virtual Restaurant Reviewing App 🍔📱

### Description

[Demo Video](https://www.youtube.com/watch?v=bE0VatEfYLo)

## Distinctiveness and Complexity:

Welcome to E-Moji!

This is my Final Project for the course CS50’s Web Programming with Python and JavaScript.
It is built with Django, Hmtl, Css, Javascript, Python & Bootsrap.
The main concept of this app is to see ratings of restaurants before go there.
In addition, you can review restaurants and also you are able to add your own restaurant.

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

### Using Virtual Environments (venv):

Also, I employed Python's built-in venv module to create an isolated virtual environment.
This ensures that the project's environment is replicable and consistent across different machines and development stages.

### Responsive Design:

I've implemented a responsive design to ensure that it provides an optimal viewing experience across a wide range of devices.
This design approach makes the app mobile-friendly, adapting the layout to the viewing environment by using fluid, proportion-based grids and flexible images.

I figured out by myself all of them. When i start project i thought how can i make it more scalable
and i found all of the solutions. I think it was more complex then before we've done.

### File Structure

- `core/` Main app.
  - `templates/` Contains all the html of the core app.
    - `components/` Contains all the html components of core app.
    - `core/` Contains all local pages.
  - `views.py` Contains all views (backend functions).
  - `urls.py` Contains all routes.
  - `models.py` Contains all db models.
- `e-moji-venv/` Birtual environment.
- `static/` Stores static files like CSS, JavaScript, and image assets. Inside the images folder, restaurant-related images are kept.
- `templates/` Includes base HTML (base.html) and navigation bar template (navbar.html) which are extended by other templates.
- `emoji-project/` The main project directory with settings and root URL configurations.

### Pages

#### Main Page

<img width="1509" alt="image" src="https://github.com/me50/atilagulers/assets/128936466/4b29ee87-2dd0-4dc1-9689-8a7b7a0a3cc4">

## Restaurant Page

<img width="1496" alt="image" src="https://github.com/me50/atilagulers/assets/128936466/9914bd6e-0438-4d4b-9052-f527bcf1d9c8">

### Running the Application

#### To get the application up and running on your local machine, follow these steps:

1. Open the terminal and navigate to the root directory of the project.
2. Before running the server, activate the virtual environment to ensure that you are using the project's isolated dependency set. Depending on your operating system, use one of the following commands:

On Unix or macOS:

```
source e-moji-venv/bin/activate
```

On Windows:

```
.\e-moji-venv\Scripts\activate
```

3. Once the virtual environment is activated and you see (e-moji-venv) prefixed in your terminal, execute the following command to start the Django web server:

```
python manage.py runserver
```

4. After the server starts, open a web browser and navigate to localhost:8000 to access the application.
