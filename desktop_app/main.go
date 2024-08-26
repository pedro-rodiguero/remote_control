package main

import (
	"fmt"
	"image/png"
	"net"
	"net/http"
	"os"

	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/canvas"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
	"github.com/go-vgo/robotgo"
	"github.com/skip2/go-qrcode"
)

func main() {
	// Get local IP address
	ip, err := getLocalIP()
	if err != nil {
		panic(err)
	}

	// Generate QR code
	url := fmt.Sprintf("http://%s:8080", ip)
	err = generateQRCode(url, "qrcode.png")
	if err != nil {
		panic(err)
	}

	// Initialize GUI
	a := app.New()
	w := a.NewWindow("Slide Controller")

	img := canvas.NewImageFromFile("qrcode.png")
	img.FillMode = canvas.ImageFillOriginal

	w.SetContent(container.NewVBox(
		widget.NewLabel("Scan this QR code with your mobile app to connect:"),
		img,
	))

	// Start HTTP server
	http.HandleFunc("/next", nextSlideHandler)
	http.HandleFunc("/prev", prevSlideHandler)
	go http.ListenAndServe(":8080", nil)

	w.ShowAndRun()
}

func getLocalIP() (string, error) {
	addrs, err := net.InterfaceAddrs()
	if err != nil {
		return "", err
	}
	for _, addr := range addrs {
		if ipnet, ok := addr.(*net.IPNet); ok && !ipnet.IP.IsLoopback() {
			if ipnet.IP.To4() != nil {
				return ipnet.IP.String(), nil
			}
		}
	}
	return "", fmt.Errorf("no IP address found")
}

func generateQRCode(url, filepath string) error {
	qr, err := qrcode.New(url, qrcode.Medium)
	if err != nil {
		return err
	}
	file, err := os.Create(filepath)
	if err != nil {
		return err
	}
	defer file.Close()
	return png.Encode(file, qr.Image(256))
}

func nextSlideHandler(w http.ResponseWriter, r *http.Request) {
	robotgo.KeyTap("right")
	fmt.Fprintf(w, "Next slide")
}

func prevSlideHandler(w http.ResponseWriter, r *http.Request) {
	robotgo.KeyTap("left")
	fmt.Fprintf(w, "Previous slide")
}

func main() {
	// Get local IP address
	ip, err := getLocalIP()
	if err != nil {
		panic(err)
	}

	// Generate QR code
	url := fmt.Sprintf("http://%s:8080", ip)
	err = generateQRCode(url, "qrcode.png")
	if err != nil {
		panic(err)
	}

	// Initialize GUI
	a := app.New()
	w := a.NewWindow("Slide Controller")

	img := canvas.NewImageFromFile("qrcode.png")
	img.FillMode = canvas.ImageFillOriginal

	w.SetContent(container.NewVBox(
		widget.NewLabel("Scan this QR code with your mobile app to connect:"),
		img,
	))

	// Start HTTP server
	http.HandleFunc("/next", nextSlideHandler)
	http.HandleFunc("/prev", prevSlideHandler)
	go http.ListenAndServe(":8080", nil)

	w.ShowAndRun()
}

func getLocalIP() (string, error) {
	addrs, err := net.InterfaceAddrs()
	if err != nil {
		return "", err
	}
	for _, addr := range addrs {
		if ipnet, ok := addr.(*net.IPNet); ok && !ipnet.IP.IsLoopback() {
			if ipnet.IP.To4() != nil {
				return ipnet.IP.String(), nil
			}
		}
	}
	return "", fmt.Errorf("no IP address found")
}
