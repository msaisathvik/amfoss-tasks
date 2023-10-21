x = gets.to_i
for i in 2..x do
    count = 0
    for j in 1..i do
        if i%j==0
            count+=1
        end
    end
    if count==2
        puts i
      end
    end