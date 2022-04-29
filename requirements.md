
## Functional Requirements

1. Login (Justin)
2. Logout (Trung)
3. Create new account (Joe)
4. delete account (Zach)
5. Add to cart (Joe)
6. Buy Item (Joe) 
7. Find items (Justin)
8. Add item to seller store (Justin)
9. See all items available from all of the sellers (Zach)
10. User ratings (Trung)
11. User profiles (Zach)
12. Add pictures for items (Trung)

## Non-functional Requirements

1. The website is expected to be fully functional on FireFox.
2. The user should be able to customize the color theme of the website.
3. Finding items shall take no longer than 5 seconds to display search results.
4. Price of items are to be displayed in USD (United States Dollars).


## Use Cases

5. Add to cart
- **Pre-condition:** User is viewing an item

- **Trigger** User selects "Add to Cart" option

- **Primary Sequence:**

  1. System verifies item availability
  2. System adds item to a list of items that have been added to the cart
  3. System adjusts price total of items in shopping cart 
  4. System prompts user with the option to checkout or continue shopping

- **Alternate Sequence:** Item is out of stock

  1. System notifies user that the item is out of stock
  2. The item is not added to cart and the user's subtotal is not modified

- **Alternate Sequence:** User proceeds to checkout

  1. User proceeds to buy items (See use case "Buy Items")

- **Alternate Sequence:** User continues to shop

  1. User is returned to item page

- **Postconditions:** The user will have the item added to their shopping cart with an adjusted subtotal if the item is in stock or they will be returned to the item page with their shopping cart remaining unmodified

6. Buy item
- **Pre-condition:** User has items in their shopping cart

- **Trigger:** User chooses to checkout

- ** Primary Sequence:** 

  1. System prompts user to enter their shipping address
  2. User enters their shipping address
  3. System calculates the total cost given the shopping cart subtotal, shipping, and taxes in the user's region
  4. System prompts user to enter payment details
  5. User enters their payment information
  6. System verifies method of payment
  7. System sends items ordered and shipping details to seller

- **alternate sequence:** Payment information is not valid

  1. System notifies user that there is an error in the payment information provided
  2. System prompts user to enter payment information again

- **Postconditions:** The user will have their order placed and the seller will be notified that they have to deliver the item


7. Find items (User is able to search for an item they want to buy)
- **Pre-condition:** User must be logged in

- **Trigger:** User clicks the search bar 

- **Primary Sequence:**
  
  1. User is promoted to enter the name of the item
  2. User enters the name
  3. User clicks submit
  4. System displays items that match the name entered

- **Primary Postconditions:** User sees all items that matched entered name 

- **Alternate Sequence:** No items match entered name
  
  1. System displays a message telling user no items match name
  2. Propmts user to enter a new name 

- **Alternative Postconditions:** User can enter a new name

8. Add item to seller store (User is able to put items out for sale)
- **Pre-condition**: User must be logged in

- **Trigger:** User clicks "Sell" button

- **Primary Sequence:**
  1. User is prompted to enter the name of the item they wish to sell
  2. User enters name
  3. User is promoted to attach images of the item (see use case "add pictures for items")
  4. User attches images
  5. User is promoted to enter a price for the item (price is positive non zero)
  6. User enters price 

- **Primary Postconditions:** The item the user wishes to sell has been 
put out for sale

- **Alternate Sequence:** The user has left a field blank or filled out a 
field incorrectly (negative price, etc)
 1. System alerts user that certain fields have an error 
 2. User is prompted to fix those fields 
 3. User fixes the fields
 4. User submits changes

- **Alternate Postconditions:** The fields have been fixed and the item
has been put out for sale. 

11. User profiles
- **Pre-condition:** 
  The user is logged in to their account.

- **Trigger:** 
  The user left-clicks their name at the top-right corner of the website.

- **Primary Sequence:**

  1. Website opens a seperate window with the URL (/profile).
  2. Page loads and displays user's name, profile picture, and description. 
  3. If changes are made, the user can choose to save them.

- **Primary Postconditions:** 

  Any changes made to the user's profile are saved or discarded, profile window is closed, and the user may continue browsing the website.

- **Alternate Sequence:** User changes their profile without clicking "Save changes".

  1. Ask the user via a message at the top of the page whether they would like to discard their changes.
  2. If they click "Save", changes are saved.
  3. Otherwise, if they click "Discard changes", then the profile is unchanged and the user may return to browsing the website.

- **Alternate Sequence:** Profile is edited such that user's name is blank
  
  1. Display at top of profile page that a name cannot be blank and is a required field.
  2. Allow the user to re-enter a valid name.

12. Add pictures for items
- **Pre-condition:** 
The user is logged in to their account.

- **Trigger:**
The user left-clicks the "Add picture for item" button below an item label"

- **Primary Sequence:**

1. Website opens up a file explorer window on user's PC that only shows PNG/JPEG files
2. User selects one or more PNG/JPEG file(s)
3. User left-clicks the "Open" button on the file explorer window

- **Primary Postconditions:**
Website displays the PNG/JPEG file(s) as images on the item's individual product page.

- **Alternative Sequence:** User doesn't select a PNG/JPEG file and left-clicks "Open" on the file explorer window

- **Trigger:**
The user left-clicks the "Add picture for item" button below an item label
   
- **Primary Sequence:**

1. Website opens up a file explorer window on user's PC that only shows PNG/JPEG files
2. User selects one or more PNG/JPEG file(s)
3. User left-clicks the "Open" button on the file explorer window

- **Primary Postconditions:**
  
Website displays the PNG/JPEG file(s) as images on the item's individual product page.
  
- **Alternative Sequence:** User doesn't select a PNG/JPEG file and left-clicks "Open" on the file explorer window
 
1. A error popup appears in the center of the user's screen asking the user to choose a PNG/JPEG file
2. User presses "OK" on error popup
3. Error popup closes
4. User selects PNG/JPEG file(s)
5. User left-clicks the "Open" button

- **Alternative Postconditions:**

Website displays the PNG/JPEG file(s) as images on the item's individual product page.
  
