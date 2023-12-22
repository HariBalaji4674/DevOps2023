package main

import "fmt"
const age = 19
// var s1 string
// var s2 string
func main() {
	fmt.Println("adding new lines")
	conditi()
	fmt.Println(concat("peddireddy","annapureddy"))
}
func conditi() {
	if age>18 {
		fmt.Println("My age is 18 i am eligible for vote")
	}
}
func concat(s1 string, s2 string) string {
	return s1 + s2
}

