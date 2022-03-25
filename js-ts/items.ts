const fs = require("fs")
const prompt = require("prompt-sync")()

export class MathGames {
  name: string;
  age: number;
  est_iq: number;
  iq: number;
  wrongMessage1: string;
  wrongMessage2: string;
  correctMessage: string;

  constructor(name, age, est_iq) {
    this.name = "";
    this.age = 0;
    this.est_iq = 0;
    this.iq = 0;
    this.wrongMessage1 =
      "{} You are incorrect. It's less than that. The answer is...{}";
    this.wrongMessage2 =
      "{} You are incorrect. It's more than that. The answer is...{}";
    this.correctMessage = "{} You are correct! The answer is...{}";
  }

  introduction() {
    let intro = {
      name: this.name,
      age: this.age,
      estimatediq: this.est_iq,
    };
    return (
      `
      Name: ${intro.name}
      Age: ${intro.age}
      Estimated-IQ: ${intro.estimatediq}
      Let's see your IQ skills.
      `
    );
  }

  check_iq() {
    fs.readFile("saved.yaml", "utf-8", (e, d) => {
      let i_q = parseInt(d.toString().slice(4, d.length));
      if (i_q >= 100) return `\nYour IQ Level is: ${i_q}! Congrats!`;
      else return `\nYour IQ Level is: ${i_q}.`;
    });
  }

  save_iq() {
    fs.readFile("score.yaml", { encoding: "UTF-8" }, (e: any, d: any) => {
      let iq = String(d).slice(4, String(d).length);
      fs.readFile("saved.yaml", { encoding: "UTF-8" }, (e: any, d: any) => {
        let i = String(d).slice(4, String(d).length);
        fs.writeFile("saved.yaml", `IQ: ${iq + i}`, (e: any, d: any) => {
          console.log("IQ saved successfully!");
          fs.writeFile("score.yaml", `IQ: 0`);
        });
      });
    });
  }

  clear_iq() {
    fs.writeFile("saved.yaml", `IQ: 0`);
    return "Successfully cleared all your IQ points.";
  }

  random(n1, n2) {
    return Math.floor(Math.random() * (n2 - n1) - n2);
  }

  check_iq_with_est_iq() {
    let msg1 = "Your Estimated IQ is lower than your actual IQ.";
    let msg2 = "Your Estimated IQ is higher than your actual IQ.";
    fs.readFile("saved.yaml", { encoding: "utf-8" }, (e: any, d: any) => {
      let iq = parseInt(String(d).slice(4, String(d).length));
      if (iq < this.est_iq) return msg1;
      else return msg2;
    });
  }

  playTheGame(run: boolean, op: string, sr: number, er: number) {
    function give_iq(op) {
      if (op == "+") this.iq += 5;
      else if (op == "-") this.iq += 8;
      else if (op == "*") this.iq += 12;
      else if (op == "/") this.iq += 18;
    }

    while (run) {
      let num1 = this.random(sr, er);
      let num2 = this.random(sr, er);
      let result = num1 + num2;

      let play = prompt(`\n${num1} + ${num2} = `);

      if (play == result) {
        console.log(this.correctMessage);
        give_iq(op);
        fs.writeFile("score.yaml", `IQ: ${this.iq}`);
      } else if (result < play) {
        console.log(this.wrongMessage1);
        break;
      } else if (result > play) {
        console.log(this.wrongMessage2);
        break;
      } else {
        console.log(`You are incorrect. The answer is ${result}.`);
        break;
      }
    }
  }
}
