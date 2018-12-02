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

Anaconda,  Pillow==5.2.0, Django==2.1.2, Crispy forms of Django

# Steps to Run:
conda create -n venv

conda activate venv

python manage.py runserver 
