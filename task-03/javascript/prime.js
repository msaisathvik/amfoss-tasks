var x = parseInt(prompt("Enter a number: "));
for (let i = 2; i<x+1;i++){
    var count = 0;
    for (let j=1;j<i+1;j++){
        if (i%j==0) count++;
    }
    if (count == 2) {
        console.log(i);
    }
}