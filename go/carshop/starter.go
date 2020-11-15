package main

type Car struct {
	// Have fun!
}

type CarShop struct {
	// Have fun!
}

// Have fun!

func main() {
	carShop := CarShop{os.Args[1], make([]Car, 0)}

	for i := 0; i<3; i++ {
		var brand, model, year, odometer, color string
		fmt.Scanf("%s %s %s %s %s\n", &brand, &model, &year, &odometer, &color)
		carShop.AddCar(brand, model, year, odometer, color)
	}

	fmt.Printf("Welcome to %s's Car Shop!\n", carShop.name)
	fmt.Println("Available Cars:")
	fmt.Printf("%s\n", carShop.warehouse)

	if carShop.SearchCar(os.Args[2]) != nil {
		fmt.Println("This car is available!")
	} else {
		fmt.Println("This car is not available. :-(")
	}
}
