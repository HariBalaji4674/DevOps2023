package main

import "fmt"

const name = "peddireddy"

func main() {
	fmt.Println("Peddireddy")
	sum(20, 30, 40)
	mul(10, 20)
	div(5, 2)

}

func sum(num1 int, num2 int, num3 int) {
	fmt.Println(num1 + num2 + num3)
}
func mul(num1 int, num2 int) {
	fmt.Println(num1 * num2)
}
func div(num1 int, num2 int) {
	fmt.Println(num1 / num2)
}
