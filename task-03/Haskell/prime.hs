import System.IO

isPrime :: Int -> Bool
isPrime x = length [d | d <- [1..x], x `mod` d == 0] == 2

printPrimes :: Int -> IO ()
printPrimes x = do
    mapM_ (putStr . (++ " ") . show) [n | n <- [0..x], isPrime n]
    putStrLn ""

main :: IO ()
main = do
    putStr "Enter a number: "
    hFlush stdout
    input <- getLine
    let x = read input :: Int
    printPrimes x
