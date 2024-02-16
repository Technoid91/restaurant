#Pixel steak
<hr>
Pixel steak - is the restaurant booking application.
It allows customer to browse company news, restaurant menu
and provides functionality to book a table or few.

##Features

- ###Homepage
It introduces user the upcoming events and special offers.
Designed as moving slides with titles and description,
it also allows user to manipulate with slides by clicking on
news list items on the left sidebar.
The site owner can add, delete or edit slides to show,
using administration panel. The website fetch them automatically
from the cloud based data base


- ###Menu
Shows user available dishes, short description and pricing.
Also provides additional information about vegan and spicy
dishes using icons.
The site owner can add, edit or delete categories and dishes
in these categories. The web application show only categories
which have dishes. When adding a new dish, site owner can specify
is it vegan and hot spicy is it.

- ###Booking system
Provides customer the form to fill out and book a table.
Based on for how many people customer books places, the system 
automatically assign available tables. It tries to fit in everyone
and avoid wasting tables at the same time. The system also
checks the other reservations to prevent double booking.
To make booking the user should be registered and logged in.

- ###Responsive design
Using Bootstrap and custom CSS make the web application look good
both on mobile devices and desktop screens.

## Testing

<hr>

- ###HTML
No errors were returned when passing the official
[W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpixel-steak-5f7f6955f42e.herokuapp.com%2F)

- ###CSS
No errors were returned when passing the official
[Jigsaw validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fpixel-steak-5f7f6955f42e.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=ru)


- ###Python
All python files passed CI Python Linter with no issues.


## Deployment

<hr>

The web application was deployed on Heroku

## Improvement

<hr>
The project represents basic functionality however the structure
allows to scale it dramatically and add more features

- ### Booking from the news slides
On the homepage the button book a table can be placed on each
slide and redirect user to the booking page with the date filled
already. 

- ### Menu sorting and filters
The menu structure allows to add filters (e.g. "vegan only"), and
order by feature. It also can add special styling to highlight 
price drops

- ### Booking management
Ability for user to edit or cancel the reservation. It can be done
by creating user account web page or using reservation
reference number as a unique secure ID.