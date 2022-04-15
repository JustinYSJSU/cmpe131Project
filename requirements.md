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

1. The user should be able to customize the color theme of the website.
2. 
3. non-functional
4. non-functional

## Use Cases

6. User profiles
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

