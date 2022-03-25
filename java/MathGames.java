import java.util.HashMap;
import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;

public class MathGames {
  public String name;
  public int age;
  public int est_iq;
  public int iq = 0;
  public String wrongMessage1 = "You are incorrect. It's less than that. The answer is...";
  public String wrongMessage2 = "You are incorrect. It's more than that. The answer is...";
  public String correctMessage = "You are correct! The answer is...";
  public Scanner scanFile;
  public BufferedWriter w;
  public final String file1 = "saved.yaml";
  public final String file2 = "score.yaml";
  public Random r = new Random();

  public MathGames() {
    this.name = name
    this.age = age
    this.st_iq = es
    this.iq = 0;
    this.wrongMessage1 = "You are incorrect. It's less than that. The answer is..."
    this.wrongMessage2 = "You are incorrect. It's more than that. The answer is..."
    this.correctMessage = "You are correct! The answer is..."
  }

  public String introduction() {
    HashMap<String, String> intro = new HashMap<>();
    intro.add("Name", this.name);
    intro.add("Age", this.age.toString());
    intro.add("Estimated-IQ", this.est_iq.toString());

    return (
      "Name: " + intro.get("Name") + "Age: " + intro.get("Age") + "Estimated-IQ: " + intro.get("Estimated-IQ") + "Let's see your IQ skills."
    )
  }

  public void checkIq() {
    scanFile = new Scanner(file1);
    w = new BufferedWriter(new FileWriter(file1));

    String line = scanFile.nextLine();
    
    System.out.println("Your IQ is: " + line);
  }

  public void saveIQ() {
    scanFile = new Scanner(file1);
    Scanner another = new Scanner(file2);

    int savedIq = (int) scanFile.nextLine().toString().slice(4);
    int scoreIq = (int) another.nextLine().toString().slice(4);

    w = new BufferedWriter(new FileWriter(file1));
    BufferedWriter wr = new BufferedWriter(new FileWriter(file2));
    w.write(savedIq + scoreIq);    
    wr.write("IQ: 0");
  }

  public void clearIQ() {
    w = new BufferedWriter(new FileWriter(file1));

    w.write("IQ: 0");

    System.out.println("Successfully cleared all your IQ points.");
  }

  public String checkIQWithEstIQ() {
    Scanner st = new Scanner(file1);
    
    String msg1 = "Your Estimated IQ is lower than your actual IQ.";
    String msg2 = "Your Estimated IQ is higher than your actual IQ.";

    int theIq = (int) st.nextLine().slice(4).toString();

    if (theIq < est_iq) {
      return msg1;
    } else if (theIq > est_iq) {
      return msg2;
    }
  }

  public void give_iq(String op) {
    if (op == '+')
      this.iq += 5

    if (op == '-')
      this.iq += 8

    if (op == '*')
      this.iq += 12

    if (op == '/')
      this.iq += 18
  }

  public void checkOp(int num1, String op, int num2) {
    if (op.equals('+'))
      return num1 + num2;

    if (op.equals("-"))
      return num1 - num2;

    if (op.equals("*"))
      return num1 * num2;

    if (op.equals("/"))
      return num1 / num2;
  }

  public void playTheGame(String operator, boolean run, int sr, int er) {
    Scanner input = new Scanner(System.in);
    while (run) {
      int num1 = random.randint(sr, er);
      int num2 = random.randint(sr, er);
      int result = checkOp(num1, operator, num2);

      System.out.println(num1 + " " + operator + " " + num2);
      String line = input.nextLine();

      if (play == result) {
        System.out.println(this.correctMessage.format(self.colors.GREEN, result))
        
      } else if (result < play) {
        System.out.println(this.wrongMessage1.format(self.colors.WARNING, result))
        break;
      } else if (result > play) {
        System.out.println(self.wrongMessage2.format(self.colors.WARNING, result))
        break;
      } else {
        System.out.println(f"You are incorrect. The answer is {result}.")
        break;
      }
    }
  }

  public static void main(String args[]) {
    MathGames game = new MathGames("Zamar", 14, 14921421848240);
    game.introduction();
  }
}