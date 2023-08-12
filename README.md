# **CRUD Rental Cars App**

Hey Everyone! 

Before you dive into using this app or if you run into any trouble while using it, please take a quick read through this.

I made this app as part of my Data Science course at Purwadhika. It's my first capstone project and all about getting the hang of the CRUD concept. Think of it as a small practice app on my journey to becoming a data whiz😎

This app might not be flawless or represent the real deal of how rental cars work, but I tried my best. So let's cut it some slack, shall we?😆

I put this whole thing together using Python v3. The info you're seeing is all baked into the code, therefore it will be back to square one once you restart the app. Oh, and the data in here? Totally made up. Just playing pretend.

One more thing, this app runs using Bahasa Indonesia. So if you're cool with that, let's rock and roll! 🚀

---

## **Introduction to the App**

Welcome to Rental Cars Indonesia!
This app is your ticket to hassle-free car rentals across Indonesia!
Here's the main feature provided in the apps :
- Viewing list of cars available to rent
- Adding a new car to the List
- Delete car inside the list
- Update information within the list of cars
- Book and rent cars

Here's a preview of the main menu :
<img width="845" alt="Main Menu" src="https://github.com/almiradita/SIMPLE-APP-FOR-RENTAL-CARS/assets/142095969/4e169142-c613-4aba-b8e3-bf27f9ce0acd">

## **MENU 1: Viewing List of Cars**

<img width="827" alt="Menu 1-1" src="https://github.com/almiradita/SIMPLE-APP-FOR-RENTAL-CARS/assets/142095969/d7f3d926-eb96-4fb3-a670-92c886bb64fa">

The first menu is used when you want to check out the list of available cars for rent. 

In this menu, you can choose whether you want to see the complete list of cars or view car availability based on different regions. 

<img width="817" alt="Menu 1-2" src="https://github.com/almiradita/SIMPLE-APP-FOR-RENTAL-CARS/assets/142095969/6fd9d6dd-4de6-498a-bd76-73c4a0ef2177">

If you wish in viewing the car list by region, the app will prompt you to input the city you'd like to explore. It's important to note that **city names should be written just like the proper Indonesian language**, where the name of the city begins with a capital letter.

The car list includes license plate numbers, car brands, model types, capacity, options for chauffeur service, city, pricing, and the status indicating whether the car is still available for rental or not.

## **MENU 2: Adding New Car to the List**

<img width="835" alt="Menu 2" src="https://github.com/almiradita/SIMPLE-APP-FOR-RENTAL-CARS/assets/142095969/07d23012-d06f-4fcf-bad0-0508ecc97b10">

The second menu is designed to add new cars to the rental list. 

Adding a new car can be done by providing the necessary information and can only be carried out one by one. 

The required information will be displayed when this menu is accessed. It's important to note that filling out all the required information is mandatory. In case the information isn't filled out in the correct format, the app might not run smoothly.

## **MENU 3: Delete Car Inside the List**

<img width="846" alt="Menu 3" src="https://github.com/almiradita/SIMPLE-APP-FOR-RENTAL-CARS/assets/142095969/3e32571a-bb08-4035-ac23-0b7713cc933b">

The third menu is available when you want to delete some cars from the list. 

The action can be accomplished by simply entering the index number of the car you wish to delete. Once completed, the car along with all its information will be removed from the rental car list.

## **MENU 4: Update Car Information**

<img width="834" alt="Menu 4" src="https://github.com/almiradita/SIMPLE-APP-FOR-RENTAL-CARS/assets/142095969/3e6e441d-9f01-48cb-abb3-aa417d8004e5">

Not only you can add or delete some cars in the list, you can also modify the information of cars that are already present in the list. 

Note that not all information can be changed. Some of the information that can be altered includes the license plate number, the option for chauffeur service, the city, the pricing, and the status indicating whether the car can still be rented or not.

This menu, in particular, is highly useful when you intend to adjust rental prices and the availability status of the cars.

## **MENU 5: Book and Rent Cars**

<img width="837" alt="Menu 5-1" src="https://github.com/almiradita/SIMPLE-APP-FOR-RENTAL-CARS/assets/142095969/342e598f-22fb-4817-9101-b534c60ef24a">

Lastly, the fifth menu is utilized for making car reservations and rentals. 

Within this menu, you'll be asked to input which car you'd like to rent and for how long (in days) you intend to rent it. If you wish to rent more than one car, you can easily respond "ya" to the checker question as indicated in the above image.

<img width="810" alt="Menu 5-2" src="https://github.com/almiradita/SIMPLE-APP-FOR-RENTAL-CARS/assets/142095969/80173470-a622-4159-8a4d-9b0c92bb7580">

Upon completing your order, you'll be presented with a table containing the details of your car rental order, including necessary information and the total amount to be paid. Subsequently, during the payment process, you'll be asked to input the amount of money you'd like to pay. If your payment falls short, you'll be prompted to enter the appropriate amount again.

<img width="836" alt="Menu 5-3" src="https://github.com/almiradita/SIMPLE-APP-FOR-RENTAL-CARS/assets/142095969/499262fa-a9ce-4908-ad55-6c0676a7b058">

After a successful payment, your car will be immediately reserved, and automatically, the car that has been rented will change its status to "not available" in the rental car list.
