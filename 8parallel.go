package main

import (
	"fmt"
	"os"
	"strconv"
	"sync"
)

func iterations_at_point(x, y float64, max int, iterChan chan int) {
	x0 := x
	y0 := y
	var iter int = 0
	for (x*x+y*y <= 4) && iter < max {
		xt := x*x - y*y + x0
		yt := 2*x*y + y0
		x = xt
		y = yt
		iter++
	}
	iterChan <- iter
}

var wg sync.WaitGroup

func receiver(iterChan chan int, numCalcs chan int) {
	max := 0
	i := 0
	sum := 0
	for max == 0 || i < max {
		if max == 0 {
			select {
			case msg := <-numCalcs:
				max = msg
				//fmt.Println("max: %d\n", max)
				close(numCalcs)
			default:
			}
		}
		select {
		case iter := <-iterChan:
			sum += iter
			i++
		default:
		}
	}
	fmt.Println(sum)
	wg.Done()
}

func mandelbrot(x0, y0, x1, y1, dx, dy float64, maxIter int) {
	iterChan := make(chan int, 50)
	numCalcChan := make(chan int)

	wg.Add(1)
	go receiver(iterChan, numCalcChan)
	numCalcs := 0
	for y := y0; y < y1; y += dy {
		for x := x0; x < x1; x += dx {
			go iterations_at_point(x, y, maxIter, iterChan)
			numCalcs++
		}
	}
	numCalcChan <- numCalcs
	wg.Wait()
}

func main() {
	args := os.Args[1:]
	x0, err := strconv.ParseFloat(args[0], 64)
	y0, err := strconv.ParseFloat(args[1], 64)
	x1, err := strconv.ParseFloat(args[2], 64)
	y1, err := strconv.ParseFloat(args[3], 64)
	dx, err := strconv.ParseFloat(args[4], 64)
	dy, err := strconv.ParseFloat(args[5], 64)
	maxIter, err := strconv.Atoi(args[6])
	if err != nil {

	}
	mandelbrot(x0, y0, x1, y1, dx, dy, maxIter)
	//fmt.Printf("%d\n", result)
}
