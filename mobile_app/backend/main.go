package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/next", nextSlideHandler)
	http.HandleFunc("/prev", prevSlideHandler)
	http.HandleFunc("/menu", showMenuHandler)

	fmt.Println("Server is running on port 5000")
	log.Fatal(http.ListenAndServe(":5000", nil))
}

func nextSlideHandler(w http.ResponseWriter, r *http.Request) {
	// Logic to move to the next slide
	fmt.Fprintln(w, "Next Slide")
}

func prevSlideHandler(w http.ResponseWriter, r *http.Request) {
	// Logic to move to the previous slide
	fmt.Fprintln(w, "Previous Slide")
}

func showMenuHandler(w http.ResponseWriter, r *http.Request) {
	// Logic to show the menu
	fmt.Fprintln(w, "Show Menu")
}
