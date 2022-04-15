## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

1. Login
2. Logout
3. Create new account
4. delete account
5. Add to cart
6. Buy Item
7. Find items
8. Add item to seller store
9. See all items available from all of the sellers
10. User ratings
11. User profiles
12. Add pictures for items

## Non-functional Requirements

1. Only expeceted to work on FireFox
2. The user should be able to customize the color theme of the website.
3. non-functional
4. non-functional

## Use Cases

1. Find items (User is able to search for an item they want to buy)
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

2. Add item to seller store (User is able to put items out for sale)
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
field incorrectly (neagtive price, etc)
 1. System alerts user that certain fields have an error 
 2. User is prompted to fix those fields 
 3. User fixes the fields
 4. User submits changes

- **Alternate Postconditions:** The fields have been fixed and the item
has been put out for sale. 
