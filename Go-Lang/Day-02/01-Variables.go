package main

import (
	"bufio"
	"fmt"
	"os"
)

func funtask () {
	var number = 254
	fmt.Println("Peddireddy Vardhan Reddy")
	fmt.Println(number)

	reader := bufio.NewReader(os.Stdin)
	userInput, _ := reader.ReadString('\n')
	fmt.Println(userInput)

}