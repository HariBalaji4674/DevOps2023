package main

import (
	"fmt"
)

func main() {
	/*
		 Using user to give the input
		var userName string
		fmt.Print("Enter your first name : ")
		fmt.Scan(&userName)
		 fmt.Printf("My name is %v in my", userName)

				Arrays and Slices
				Arrays: Data Strutures where we store multiple values at a time
				Arrays in go has fixed size

				var bookings = [50]


			fmt.Println()

			var bookings = [50]string{"peddireddy", "hari", "vardhan", "reddy"}

			fmt.Println(bookings)

			 Arrays
			var books [4]string
			books[0] = "java"
			books[1] = "python"
			books[2] = "google"
			books[3] = "go lang"
			fmt.Scan(&books[3])
			fmt.Println(books)

			 Slices : An automatic increment for arrays we can increase the number by adding
			 Slice is an abstraction of an array
			 slices are more flexible and power ful
			 slices are insed-based and have a size and but is resized when needed
			var numbers []string
			 fmt.Scan(&numbers[0])
			 fmt.Scan(&numbers[1])
			 fmt.Scan(numbers = append(numbers, ))
			numbers = append(numbers, "peddireddy")
			fmt.Println(numbers)


	var name string
	for {
		fmt.Scan(&name)
		fmt.Println(name)
	}

	var names = []string{"peddireddy hari","annam pappu"}
	fmt.Println(names)
	for index,name := range names{
		fmt.Println(index)
		fmt.Println(name)
	}
	for _,nam := range names {
		var name = strings.Fields(nam)
		fmt.Println(name)
	}

	// user input validation

	var firstName string
	fmt.Println("Enter first name : ")
	fmt.Scan(&firstName)
	var secondName string
	fmt.Println("Enter Second Name : ")
	fmt.Scan(&secondName)
	isValidName := len(firstName) > 3 && len(secondName) > 4

	fmt.Println(isValidName)


// Switch Statement

city := "hyderabad"

switch city {
case "kadapa":
	fmt.Println("This is kadapa district")
case "andhra":
	fmt.Println("This is andhra")
case "ananthapur":
	fmt.Println("this is ananthapur")
default:
	fmt.Println("None is correct")
}
*/

// Functions:
// Same use of code can be re sued that code
// Packages in go
 // Map
 // Make map empty map
 // we cannot map different data types in go language

 var username = make(map[string]string)
 username["firstname"] = "peddireddy"
 fmt.Println(username)

 type userData struct {
	firstname string
	secondName string
	email string
	numberofTicket int
 }
}
