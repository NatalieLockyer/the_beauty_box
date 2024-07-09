# [The Beauty Box](https://the-beauty-box-9dcfa44a254a.herokuapp.com/)

A fictional E-commerce Beauty Store using Django and Stripe, developed by Natalie Lockyer.

***

![Image of sie on devices](media/readme_images/site-image.png)

[Please click here to view my live website](https://the-beauty-box-9dcfa44a254a.herokuapp.com/)

# Contents
+ [Purpose of the Project](#purpose-of-the-project)
    + [Checkout Details](#checkout-details)
+ [User Experience](#user-experience)
    + [Key Project Goals](#key-project-goals)
    + [Target Audience](#target-audience)
    + [User Requirements and Expectations](#user-requirements-and-expectations)
    + [User Stories](#user-stories)
+ [Website Information](#website-information)
    + [Website Menus](#website-menus)
    + [Wireframes](#wireframes)
      + [Mobile Wireframes](#mobile-wireframes)
      + [Desktop Wireframes](#desktop-wireframes)
    + [Entity Relationship Diagram (ERD)](#entity-relationship-diagrams-erd)
      + [Product ERD](#product-erd)
      + [Checkout ERD](#checkout-erd)
      + [Tutorials ERD](#tutorial-erd)
      + [Blogs ERD](#blog-erd)
      + [Profile ERD](#profile-erd)
      + [Contact ERD](#contact-erd)
    + [Design](#design)
      + [Typography ](#typography)
    + [Features](#features)
      + [Main Homepage](#homepage)
      + [Products Page](#products-page)
      + [Product Detail Page](#product-detail-page)
      + [Shopping Basket Page](#shopping-basket-page)
      + [Checkout Page](#checkout-page)
      + [Tutorial Page](#tutorial-page)
      + [Tutorial Detail Page](#tutorial-detail-page)
      + [Blog Page](#blog-page)
      + [Blog Detail Page](#blog-detail-page)
      + [Blog Comment Section](#blog-comment-section)
      + [Sign Up Page](#sign-up-page)
      + [Login Page](#login-page)
      + [Profile Page](#profile-page)
      + [Managment Pages](#management-pages-superusers-only)
      + [Help Page](#help-page)
      + [Contact Page](#contact-page)
      + [404 Error Page](#404-error-page)
+ [Future Features](#future-features)
+ [Technologies Used](#technologies-used)
    + [Languages Used](#language)
    + [Frameworks Used](#frameworks-and-tools)
+ [Testing](#testing)
  + [Code Validation](#code-validation)
  + [Full Testing](#full-testing)
  + [Fixed Bugs](#fixed-bugs)
  + [Supported Browsers](#supported-browsers)
  + [Deployment and Local Deployment](#deployment-and-local-deployment)
  + [Deployment](#deployment)
  + [Local Deployment](#local-deployment)
  + [How to Clone](#how-to-clone)
+ [Credits](#credits)
+ [Acknowledgement](#acknowledgements)

***
***

# Purpose of the Project
The Beauty Box is a ficticious E-Commerce website that sells beauty products and accessories. The website also has make-up tutorial videos and make-up blogs. 
The website has been designed to give the user a great experience, from an attractive and eyecatching website, to filtering our products to see the newly listed items, tips and tricks in our make-up tutorials and blogs containing up to date and intresting information.  

This full stack frame work has been built using the Django framework. 

The Beauty Box, provides its users with 
* A registration page, which will give the user a profile page once complete. The profile page will allow the user to  update their contact/delivery and payment details and also see their previous orders (if any).
* A product page, detailing all our items we have for sale, which can be filtered into many different categories.
* A checkout page, listing the items in their basket and a secure checkout.
* A tutorial page were users can get the latest tips and tricks and instructions on how to apply their make-up.
* A blog page, again with all the lastest tips and tricks, and the most up to date and interesting information.
* A contact page, where users can get in touch, join our mailing list or ask questions.
* A help page, where users can see our returns policy, delivery costs and our privacy policy.

For Superusers it provides all of the above and in addition -
* A Product management page, where the superuser can add new products directly on the webpage, edit, update and delete products.
* A Tutorial management page, where the superuser can add new tutorials directly on the webpage, edit, update and delete them.
* A Blog management page, where the superuser can add new blogs directly on the webpage, edit, update and delete them.

### Checkout Details

In order to make an example purchase a specific card number is required:
|Card Number|Date|CVC|Postal Code|
|---|---|---|---|
|4242 4242 4242 4242|any date|any 3 numbers|any 5 numbers|



# User Experience

### Key Project Goals

* To write and develop an E-commerce website that is an eyecatching, informative, interactive, and enjoyable website that users will want to return to.
* The user will be able to navigate around the website with ease, either on a mobile or desktop device. 
* The main homepage is clear as to what the website is about and have accessible menus taking the user to the different pages of the website. 
* Users that register for a Beauty Box account will be able to see their own profile, which will have up to date contact/delivery and payment details. Users will also be able to see their order history (if any). 
* Users will be able to see a products page that lists all the items that Beauty Box has for sale. Users will be able to filter the items into categories of their choosing.
* Users will be able to add products to a basket, go to checkout and pay for the items through a secure checkout.
* Users can view make up tutorials via video and a text column
* Users can view blog posts which provide intereting and up to date information, users can add comments, edit them and delete them. 
* Users can get in touch with our team if required via a contact page.
* Users can see returns policy, delivery information a site policy. 

### Target Audience

* Anyone over the age of 12, that wears or has an interest in make-up.
* Anyone who is looking for gift ideas or want to make a purchase for themselves. 
* Users that want to learn how to apply make up via an online tutorial.
* Users who like to keep up to date with the latest tips and tricks blogs. 

### User Requirements and Expectations 

* An accessable website, that is clear and easy to navigate and understand.
* The ability to register for a Beauty Box account
* The ability to view products, and view them in more detail, before they add them to their basket.
* The ability to filter products into categories.
* The ability to take the products to a checkout and pay for the products securely. 
* The ability to view, add, edit & delete any comments they have made.
* The ability to get in touch.
* The ability to see the return policy, delievery information and the sites privacy policy. 

### User Stories

As a site user:

* I am able to view a list of products
* I am able to view individual products, which contain an image, description, price, shades, quantity and an add to basket button if I wish. 
* I want to be able to identify any products that are in the sale. 
* I want to be able to view the products in my bag, amend them if required, see the total of the products and be able to make a secure payment. 
* I want to be able to register for an account. I want to be able to easily login and out. I am then able to see my personal information, previous orders if any, make changes to my personal information or payment details and view order confirmations. I also want to be able to reset my password if I forget it.
* I want to be able to sort and filter the available products, so that I can quickly identify the best rated and best priced items.
* I want to be able to search for a product by its name.
* I want to be able to add my payment details quickly and be confident that this is a safe and secure process. 
* I want to see confirmation of the products in my basket before purchase and I want an email confirmation once the products have been paid for. 

As a store owner:

* I can add new products, tutorials and blogs to my store
* I can edit and update products/tutorials and blogs. I want to be able to change the product description, prices, images and any other detail that I wish. 
* I can delete products, tutorials and blogs when they are no longer for sale/available to watch. 

# Website Information

### Website Menus
* Homepage
* Index
* Registration/Sign Up Page
* Login Page
* Logout Page
* Products Page
* Basket Page
* Checkout Page
* Tutorials Page
* Blogs Page
* Help Page
* Contact Page
* Privacy Policy Page
* Error Page
* User Profile Page
* Product Management Page (Add/edit and delete Products)
* Tutorial Management Page (Add/edit and delete Tutorials)
* Blog Management Page (Add/edit and delete Products)

### Wireframes

#### Mobile wireframes

![Mobile Wireframes of main pages](media/readme_images/mobile_wireframes.png)

#### Desktop wireframes 
![Desktop Wireframes of main pages](media/readme_images/desktop_wireframes.png)

### Entity Relationship Diagrams (ERD) 

##### Product ERD
![Product ERD](media/readme_images/products_erd.png)

#### Checkout ERD
![Checkout ERD](media/readme_images/checkout_erd.png)

#### Tutorial ERD
![Tutorial ERD](media/readme_images/tutorials_erd.png)

#### Blog ERD
![Blog ERD](media/readme_images/blog_erd.png)

#### Profile ERD
![Profile ERD](media/readme_images/profiles_erd.png)

#### Contact ERD
![Contact ERD](media/readme_images/contact_erd.png)


### Design

#### Typography 

For my website I used a font called Raleway. For the main headings and subtitles I used this font in uppercase. For everything else, I used the same font but with a font-weight of 400

![Typography](media/readme_images/raleway.png)


### Features

#### Homepage
* The homepage contains a fully responsive navigation bar used to navigate throughout the site. 
* It displays a profile icon linking to the users profile, or a login menu if the user isnt logged in. 
* A basket icon where the user can see what items (if any) are in the basket. 
* A search bar to find specific items within the site.
* A scrolling banner with messages to the users
* Links to other pages of the website (Shop Now, Tutorials and Beauty Blogs)
* A footer that links the user to social media pages, and in particular our 'Beauty Box' Facebook page.

![Homepage Screenshot](media/readme_images/homepage_screenshot.png)

#### Products Page
* The products page is fully responsive, altering the layout depending on the size of the device that is used to view it. 
* The navigation bar is also fully reponsive allowing the user to navigate around the store easily
* It displays all the products available within the store
* There is a filtering option that allows users to sort by a specific category, e.g. Price low to high. 
* There is an arrow in the bottom right corner which when pressed takes the user to the top of the page.

![Product Page Screenshot](media/readme_images/product_screenshot.png)

#### Product Detail Page
* The product detail page is fully responsive, altering the layout depending on the size of the device that is used to view it. 
* The navigation bar is also fully reponsive allowing the user to navigate around the store easily
* This page shows the individual product, with details about the product
* If the product has shades the user is able to select a colour.
* The user is able to select the quantity of the item
* A keep shopping button that takes the user back to the products page
* Add to basket button which adds the product to the users shopping Basket

![Product Detail Screenshot](media/readme_images/product_detail_screenshot.png)

#### Shopping Basket Page
* The Shopping Basket page is fully responsive, altering the layout depending on the size of the device that is used to view it. 
* The navigation bar is also fully reponsive allowing the user to navigate around the store easily
* This page shows all the items that the user has added to basket
* This shows an image of the product, the title, the price, the quantity, the subtotal, delivery cost (if applicable) the grand total and the amount the user needs to spend to qualify for free delivery.
* There is also an option for the user to update the quantity or remove the item from the basket.
* A keep shopping button that takes the user back to the products page
* A secure checkout button which takes the user to the secure checkout page
* A homepage button which takes the user back to the homepage
* When a user add an item to the basket / updates the basket or removes the item from the basket the user will get a message.

![Basket Page](media/readme_images/basket_screenshot.png)

Example Success Message

![Success Message](media/readme_images/added_to_basket_screenshot.png)


#### Checkout Page
* The Checkout Basket page is fully responsive, altering the layout depending on the size of the device that is used to view it. 
* The navigation bar is also fully reponsive allowing the user to navigate around the store easily
* If the user is logged into their account, their email and delivery address will be pre-populated. However, users will still need to enter their full name.
* User can see an order summary containing items within their order, an order total, delivery total and a grand total.
* Once all the form is complete and the user is happy with the order summary, the user is able to input their card details before clicking the complete order button.
* Alternativly they can amend their order using the 'adjust basket' button. 
* When the user selects the complete order button, a confirmation message will appear and the user will recieve a confirmation email.

![Checkout Page](media/readme_images/checkout_screenshot.png)

Confirmation Message

![Confirmation Message](media/readme_images/confirmation_message.png)

Confirmation Page

![Confirmation Page](media/readme_images/confirmation_page.png)

Confirmation Email 

![Confirmation Email](media/readme_images/confirmation_email.png)


#### Tutorial Page
* The Tutorial page is fully responsive, altering the layout depending on the size of the device that is used to view it. 
* The navigation bar is also fully reponsive allowing the user to navigate around the store easily
* It displays all the tutorials available on the site
* There is a homepage button to return the user to the homepage
* You will see on the image that there is an edit|delete button. This is only visible to the superuser which will be covered later.
* When the user clicks on a tutorial image they will be taken to the individual tutorial detail page.

![Tutorial Page Screenshot](media/readme_images/tutorial_screenshot.png)

#### Tutorial Detail Page
* The tutorial detail page is fully responsive, altering the layout depending on the size of the device that is used to view it. 
* The navigation bar is also fully reponsive allowing the user to navigate around the store easily
* This page shows the individual tutorial, a tutorial video and a small section of text.
* Users can press the play button to start the video
* The user can see a rating of the video
* There is a return to tutorials button which will take the user back to the tutorial page. 

![Tutorial Detail Page](media/readme_images/tutorial_detail_screenshot.png)


#### Blog Page
* The blog page is fully responsive, altering the layout depending on the size of the device that is used to view it. 
* The navigation bar is also fully reponsive allowing the user to navigate around the store easily
* It displays all the blogs available on the site
* There is a homepage button to return the user to the homepage
* When the user clicks on the blog image they will be taken to the individual blog detail page.

![Blog Page Screenshot](media/readme_images/blog_screenshot.png)

#### Blog Detail Page
* The blog detail page is fully responsive, altering the layout depending on the size of the device that is used to view it. 
* The navigation bar is also fully reponsive allowing the user to navigate around the store easily
* This page shows the blog image and the content of the blog itself. 
* The user can see a rating of the blog
* There is a return to blog button which will take the user back to the blog page. 
* As the user gets to the bottom of the blog, there is a section where they can add / edit and delete comments.

![Blog Detail Screenshot](media/readme_images/blog_detail_screenshot.png)

#### Blog Comment Section
* Logged in users are able to add comments to blogs. 
* They can also make changed to their own comment and delete them if they wish. 
* Comments will only appear on the website once they have been approved by the superuser. 

![Blog Comment Section](media/readme_images/blog_comments_screenshot.png)


#### Sign Up Page
* Users can navigate to this page by selecting the Register link on the 'My Account' drop down menu. 
* The sign up page is fully responsive, altering the layout depending on the size of the device that is used to view it. 
* The navigation bar is also fully reponsive allowing the user to navigate around the store easily
* Users are required to input the fields within the form before selecting the 'Sign Up' button. 
* Once done, the user will recieve a message to confirm that a verification email will be sent to them. Users will need to approve this before they get full access to the site. 

![Sign Up Page](media/readme_images/signup_screenshot.png)

Sign Up Verification Message

![Sign Up Verification Message](media/readme_images/verify_email_screenshot.png)

Sign Up Verification Email

![Sign Up Verification Email](media/readme_images/verification_email.png)


#### Login Page
* Users can navigate to this page by selecting the Login link on the 'My Account' drop down menu. 
* The Login page is fully responsive, altering the layout depending on the size of the device that is used to view it. 
* The navigation bar is also fully reponsive allowing the user to navigate around the store easily
* Users are required to input the fields within the form before selecting the 'Sign In' button. 
* If users forget their password they can select the forgot password link.
* Users also have the option of the 'remember me' button. 

![Login Page](media/readme_images/login_screenshot.png)


#### Profile Page
* Users can navigate to this page by selecting the My Profile link on the 'My Account' drop down menu. 
* The Profile page is fully responsive, altering the layout depending on the size of the device that is used to view it. 
* The navigation bar is also fully reponsive allowing the user to navigate around the store easily
* On this page, users are able to update their delivery information and contact number. 
* User can also see any previous orders, and click on the link to see them. 

![Profile Page](media/readme_images/profile_screenshot.png)


#### Management Pages (Superusers ONLY)
* Superusers can navigate to this page by selecting the relevant management link on the 'My Account' drop down menu. 
* The superusers are able to add / edit and delete products once logged into the site. 
* Superuser are required to fill in the necessary fields before submitting. 
* On this site, the superuser can manage products, tutorials and the blog pages. 

![Management Link](media/readme_images/management_links.png)

Management Pages for the superuser 

![Managment Pages](media/readme_images/management_screenshot.png)


#### Help Page
* Users can navigate to this page by selecting the Help link on the 'My Account' drop down menu. 
* The Help page is fully responsive, altering the layout depending on the size of the device that is used to view it. 
* The navigation bar is also fully reponsive allowing the user to navigate around the store easily
* On this page, users will see information relating to returns, delivery information and the site's privacy policy.
* There is a homepage button to return the user to the homepage
* There is also a link that that the user directly to the contact page.

![Help Page](media/readme_images/help_screenshot.png)


#### Contact Page
* Users can navigate to this page by selecting the Contact link on the 'My Account' drop down menu. 
* The Contact page is fully responsive, altering the layout depending on the size of the device that is used to view it. 
* The navigation bar is also fully reponsive allowing the user to navigate around the store easily
* On this page, users can enter their name, email address and a message which when submitted will be sent to the admin.
* Users will see a message to confirm that their message was sent. 
* There is a homepage button to return the user to the homepage


![Contact Page](media/readme_images/contact_screenshot.png)

Contact Confirmation message

![Contact Confirmation Message](media/readme_images/contact_message.png)


### 404 Error Page
* Users will be directed to this page if there is a broken link within the website. 
* Users have the option to return to the homepage by selecting the homepage button. 

![404 Error Page](media/readme_images/error_screenshot.png)
