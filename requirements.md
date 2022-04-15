
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
field incorrectly (neagtive price, etc)
 1. System alerts user that certain fields have an error 
 2. User is prompted to fix those fields 
 3. User fixes the fields
 4. User submits changes

- **Alternate Postconditions:** The fields have been fixed and the item
has been put out for sale. 
