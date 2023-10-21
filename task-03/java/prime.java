import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner obj = new Scanner(System.in);
    System.out.println("Enter a number: ");
    int num = obj.nextInt();
    for (int i=2;i<num+1;i++){
        int count = 0;
        for (int j=1;j<i+1;j++){
            if (i%j==0){
                count+=1;
            }
        }
        if (count==2){
            System.out.println(i + " ");
        }
    }
  }
}