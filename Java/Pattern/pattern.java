
import java.util.Scanner;

public class   demo{
    static void pattern1(int n){
        System.out.println("1");
        System.out.println();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print("* ");
            }
            System.out.println();

        }
    }

    static void pattern2(int n){
        System.out.println("2");
        System.out.println();
        for (int i = 0; i <=n; i++) {
            for (int j = 0; j <=i; j++) {
                System.out.print("* ");
            }
            System.out.println();

        }
    }
    static void pattern3(int n){
        System.out.println("3");
        System.out.println();
        for (int i = 1; i <=n; i++) {
            for (int j = 1; j <=n+1-i; j++) {
                System.out.print("* ");
            }
            System.out.println();

        }

    }

    static void pattern4(int n){
        System.out.println("4");
        System.out.println();
        for (int i = 1; i <=n; i++) {
            for (int j = 1; j <=i; j++) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }

    static void pattern5(int n){
        System.out.println("5 ");
        System.out.println();
        for (int i = 0; i < 2*n; i++) {
            int totalvalue = i > n ? 2*n - i : i;
            for (int j = 0; j < totalvalue; j++) {
                System.out.print("* ");
            }
            System.out.println();

        }
    }

    static void pattern6(int n){
        System.out.println("6");
        System.out.println();
        for (int row = 1; row <=n; row++) {
            for(int i = row; i < n; i++) {
                System.out.print("  ");
            }
            for (int j = 1; j <= row; j++) {
                System.out.print("* ");
            }
            System.out.println();

        }
    }
    static void pattern7(int n){
        System.out.println("7");
        System.out.println();
        for (int row = 1; row <=n*2; row++) {
            int totalvalue = row > n ? 2*n - row : row;

            for(int i = totalvalue; i < n; i++) {
                System.out.print("  ");
            }

            for (int j = 1; j <= totalvalue; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    static void pattern8(int n){
        System.out.println("8");
        System.out.println();
        for (int row = 1; row <=n; row++) {
            int totalvalue = row > n ? 2*n - row : row;

            for(int i = totalvalue; i < n; i++) {
                System.out.print(" ");
            }

            for (int j = 1; j <= totalvalue; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    static void pattern9(int n){
        System.out.println("9");
        System.out.println();
        for (int row = 0; row <=n; row++) {
            int totalvalue = row > n ? 2*n - row : row;

            for(int i = 0; i < totalvalue; i++) {
                System.out.print(" ");
            }

            for (int j = 1; j <= n-totalvalue; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
    static void pattern10(int n){
        System.out.println("10");
        System.out.println();
        for (int row = 1; row <=n*2; row++) {
            int totalvalue = row > n ? 2*n - row : row;

            for(int i = totalvalue; i < n; i++) {
                System.out.print(" ");
            }

            for (int j = 1; j <= totalvalue; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    static void pattern11(int n) {
        System.out.println("11");
        System.out.println();

        for (int i = 0; i < n ; i++) {
            int totalvalue = i > n ? 2*n - i : i;
            for (int s= 0; s < totalvalue; s++) {
                System.out.print(" ");
            }
            for (int j = 0; j < n-i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        for (int row = 1; row <=n; row++) {
            int totalvalue = row > n ? 2*n - row : row;

            for(int i = totalvalue; i < n; i++) {
                System.out.print(" ");
            }

            for (int j = 1; j <= totalvalue; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

    }
    static void pattern12(int n){
        System.out.println("12");
        System.out.println();
        for (int row = 0; row < n; row++) {
            for (int space = 0; space < n-row ; space++) {
                System.out.print("  ");
            }
            for (int i = row; i >=1 ; i--) {
                System.out.print(i+" ");
            }
            for (int j = 2; j <= row ; j++) {
                System.out.print(j+" ");
                
            }
            System.out.println();
        }
    }

    static void pattern13(int n){
        for (int row = 1; row <= 2*n; row++) {
            int totalvalue = row > n ? n*2 -row : row;
            for (int space = 0; space < n-totalvalue ; space++) {
                System.out.print("  ");
            }
            for (int i = totalvalue; i >=1; i--) {
                System.out.print(i+ " ");
            }
            for (int j = 2; j <=totalvalue ; j++) {
                System.out.print(j+ " ");
            }
            System.out.println();


        }
    }

    public static void main(String[] args){
        pattern1(5);
        System.out.println();
        pattern2(5);
        System.out.println();
        pattern3(5);
        System.out.println();
        pattern4(5);
        System.out.println();
        pattern5(5);
        System.out.println();
        pattern6(5);
        System.out.println();
        pattern7(5);
        System.out.println();
        pattern8(5);
        System.out.println();
        pattern9(5);
        System.out.println();
        pattern10(5);
        System.out.println();
        pattern11(5);
        System.out.println();
        pattern12(5);
        System.out.println();
        pattern13(5);
    }

}
