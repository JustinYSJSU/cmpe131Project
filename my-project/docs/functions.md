##Functions/Featues 

```
def login():

Location
-----
- routes.py

Author
-----
- Justin

Parameters
-----
- None

Function
-----
- Logs the specified user into their account from the given username and
  password, if an account with the username/password combination exists

Returns
-----
- Returns the render_template function with the following parameters
  - 'login.html', login_form
  - 'login.html' is the corresponding .html file to display the login page
  - login_form is the web form that takes username and password to log the
    user in (see user_login.py)
```


```
def home():

Location
-----
- routes.py

Author 
-----
- Justin

Parameters
-----
- None

Function
-----
- Serves as the home page for the site. Displays a welcome message, item
  search bar, as well as options to sell an item or delete user account
- If the user searches for an item that exists, they will be brought to a 
  page with seach results for the item. 
- If the users searches for an item that doesn't exist, they will receive 
  a message alerting them that the item does not exist in the store

Returns
-----
- returns the render_template function with the following parameters:
  - 'home.html'
  - search_form
  - 'home.html' is the corresponding .html file to display the home page.
     It also contains the option to sell an item or delete their account. 
  - serach_form is the web form to take in an item search results
    (see item_search.py)

- If the user searches for an existing item
  - returns the render_template function with the following parameters:
    - 'display_item.html', item_list, search_form.item_name.data)
    - 'display_item.html' is the .html the corresponds to displaying an 
       item. 
    - item_list is the list of items that match the user's input (the item
      they searched for). 
    - search_form.item_name.data is the item that user searched for (what
      they entered in the web form). 
```


```
def sell_item():

Location
-----
- routes.py

Author
-----
- Justin

Parameters
-----
- None

Function
-----
- Allows users to put their own item up for sale
- Users are required to enter an item name, positive price value, 
  description, and an image of the item
- If any of these are missing, their item will not be published for sale

Returns
-----
- returns the render_template function with the following parameters
  - 'sell_item.html'
  - sell_form
  - 'sell_item.html' is the corresponding .html file that displays the 
    option to sell an item
  - sell_form is the web form used to take in the item name, price, 
    image, and description (see item_sale.py)
```

```
def createAccount():

Location
-----
- routes.py

Author
-----
- Joe

Parameters
-----
- None

Function
- Allows the user to create an account. 
- The user enters a username and password. 
- After their account has been created, they 
  are redirected to the login page

Returns
-----
- returns the render_template function with the following parameters:
  - 'createAccount.html'
  - accountForm
  - 'createAccount.html' is the corresponding .html file that corresponds
    to creating an account
  - accountForm is the web form that takes information to create an account
    (see createAccount.py)

- After the user has created an account
  - returns 'redirect('/')', which is a redirect to 
    the login page

```

```
def view_profile():

Location
-----
- routes.py

Author
-----
- Zach / Justin

Parameters
-----
- None

Function
-----
- Allows the current user to see their account information 
  (username, email, payment info)

Returns
-----
- Returns the render_template function with the following parameters
  - 'user_profiles.html', user
  - 'user_profiles.html' is the .html file corresponding to displaying the user profile
  - user is the current user
```

```
def landingPage(itemId):

Location
-----
- routes.py

Author
-----
- Joe

Parameters
-----
- itemID: The ID of the item being added to a users cart

Function
-----
- Allows a user to add an item to their online cart

Returns
-----
- Returns the render_template function with the following parameters
  - 'landing.html', itemID, selectedItem[0], cartOption
  - 'landing.html' is the .html file to display adding to cart 
  - itemID is the id of the item being added
  - selectedItem[0] is the specfiic item being selected from the list of possible items
  - cartOption is the web form that allows users to submit their add to cart 
  
- After the user has added an item
  - returns a redirect to ('/cart'), the page that displays the users cart 

Location
-----
- routes.py

Author
-----
- Joe

Parameters
-----
- None

Function
-----
- Allows a user to view their cart

Returns
-----
- Returns the render_template function with the following parameters
  - 'displayCart.html', temp, checkout
  - 'displayCart.html' is the .html file to display viewing a cart
  - temp is the current cart (the user's cart)
  - checkout is the web form that allows users to view their cart
  
- After the user has finished viewing
  - returns a redirect to ('/checkout'), the page that displays allows users to buy


Location
-----
- routes.py

Author
-----
- Joe

Parameters
-----
- None

Function
-----
- Allows a user to checkout and pay

Returns
-----
- Returns the render_template function with the following parameters
  - 'checkout.html', orders
  - 'checkout.html' is the .html that corresponds to displaying the checkout
  - orders is the order of the current user


  
- After the user has added an item
  - returns a redirect to ('/cart'), the page that displays the users cart 
