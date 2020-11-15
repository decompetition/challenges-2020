package main

import (
	"fmt"
	"os"
	"strconv"
)

type Color int

const (
	Aurora Color = iota
	Indigo
	Charcoal
	Jade
	Platinum
)

func (c Color) String() string {
	return []string{"Aurora", "Indigo", "Charcoal", "Jade", "Platinum"}[c]
}

func StringToColor(s string) Color {
	return map[string]Color{
		"Aurora":   Aurora,
		"Indigo":   Indigo,
		"Charcoal": Charcoal,
		"Jade":     Jade,
		"Platinum": Platinum,
	}[s]
}

type Car struct {
	brand    string
	model    string
	year     int
	odometer int
	color    Color
}

func (c Car) String() string {
	return fmt.Sprintf("{%d %s %s (%s, %d miles)}", c.year, c.brand, c.model, c.color, c.odometer)
}

type CarShop struct {
	name      string
	warehouse []Car
}

func (carShop *CarShop) AddCar(brand string, model string, year string, odometer string, color string) {
	var car Car
	var y int
	var o int
	var c Color
	y, _ = strconv.Atoi(year)
	o, _ = strconv.Atoi(odometer)
	c = StringToColor(color)
	car = Car{brand, model, y, o, c}
	carShop.warehouse = append(carShop.warehouse, car)
}

func (carShop CarShop) SearchCar(name string) *Car {
	for _, element := range carShop.warehouse {
		if name == element.model {
			return &element
		}
	}
	return nil
}

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
