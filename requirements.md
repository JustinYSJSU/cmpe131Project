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

1. non-functional
2. non-functional
3. non-functional
4. non-functional

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
