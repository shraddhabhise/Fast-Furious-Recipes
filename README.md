# Fast & Furious Recipes
This is a website for searching and viewing recipes. Users can also register and then create and share their recipes.
This created recipes can be modified or deleted by the user if they want to.

# Website functionalities:

For any user:

  Home: Lists all the recipes.
  
  About: Describes about the website.
  
  Search: Recipes can be searched based on title of recipes.
  
For authorized user:

  In addition to functionalities of general user, after they register and login they can:
  create recipes: Create recipes by providing title, ingredients and contents
  
  update recipes: update any field of created recipes.
  
  delete recipes: delete recipes.
  
  create/update profile: can create and update user profile.
  
# Installation 

- pip install django (2.1 is installed)

- Download and install anaconda     (from https://www.anaconda.com/download/#macos, in order to use few anaconda features) and follow https://docs.anaconda.com/anaconda/install/mac-os/

- pip install pillow            (install pillow for image feature of user profile in python) 

- pip install django-crispy-forms       (Crispy forms of Django)

# Steps to Run:
conda create -n venv

conda activate venv

python manage.py runserver 
