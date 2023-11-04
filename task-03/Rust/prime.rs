use std::io;

fn main() {
    let mut input = String::new();

    println!("Enter a number: ");
    io::stdin().read_line(&mut input).expect("Failed to read input");

    let x: u32 = input.trim().parse().expect("Invalid input. Please enter a valid number.");

    for i in 0..=x {
        let mut count = 0;
        for j in 1..=i {
            if i % j == 0 {
                count += 1;
            }
        }
        if count == 2 {
            print!("{} ", i);
        }
    }
}