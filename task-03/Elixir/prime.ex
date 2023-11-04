defmodule PrimeNumbers do
  def check_prime(x) do
    check_prime(0, x)
  end

  defp check_prime(i, x) when i <= x do
    count = count_divisors(i, 1, 0)
    if count == 2 do
      IO.write("#{i} ")
    end
    check_prime(i + 1, x)
  end

  defp check_prime(x, x), do: IO.puts("")

  defp count_divisors(i, j, count) when j <= i do
    if rem(i, j) == 0 do
      count_divisors(i, j + 1, count + 1)
    else
      count_divisors(i, j + 1, count)
    end
  end

  defp count_divisors(i, j, count) when j > i, do: count
end

IO.write("Enter a number: ")
input = IO.gets("") |> String.trim() |> String.to_integer()

PrimeNumbers.check_prime(input)
