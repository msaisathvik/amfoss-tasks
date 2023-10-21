package main
import "fmt"

func main() {
  var num int
  fmt.Print("Enter a number: ")
  fmt.Scan(&num)
  for i:=2; i < num+1; i++ {
    count:=0
    for j:=1;j<i+1;j++ {
        if i%j==0 {
            count+=1
        }
    }
    if count==2 {
        fmt.Print(i," ")
    }
  }
  
}