import { Say } from './shared/say.service';
import { Dialog } from './shared/dialog';

class Module {
  title = 'Heroku Wakka';
  say = new Say();
  select = 'Dialog';



  onload() {

    // const h1 = document.getElementsByTagName('h1')[0] as HTMLHeadingElement;
    // h1.innerText = this.title;
  }

  updateSelect(): void {
    const select = document.getElementById('select') as HTMLSelectElement;
    this.select = select.value;
  }

  updateDisplay(msg: string): void {
    const display = document.getElementById('display') as HTMLDivElement;
    display.innerText = msg;
  }

  shout(): void {
    const input = document.getElementById('msg') as HTMLInputElement;
    switch (this.select) {
      case 'Alert': this.say.alert(input.value); break;
      case 'Console': this.say.console(input.value); break;
      case 'UI': this.updateDisplay(input.value); break;
      case 'Dialog': dialog.open(input.value); break;
    }
  }
}
export const module = new Module();
export const dialog = new Dialog();

window.addEventListener('load', () => {
  getScores()
  document.getElementById('postButton')?.addEventListener('click',
  ()=>{ setScore({ 'name': 'yaniv', 'score': Math.random()*2000 })} )
});



async function getScores() {
  let obj = await (await fetch("https://invaders-page.herokuapp.com/scores")).json()
  console.log(obj);
  console.log("count ", typeof obj);
  obj.sort((a: number, b: number) => a - b)
  for (const data of obj) {
    let scores_div = document.getElementById('scores_div');
    let new_score = document.createElement('div')
    new_score.classList.add('single_score_div')
    let name_span = document.createElement('span')
    name_span.innerText = data.name + ":"
    let score_span = document.createElement('span')
    score_span.innerText = data.score
    new_score.append(name_span)
    new_score.append(score_span)
    scores_div?.append(new_score)
  }


  console.log("creating ", "gggfsfds");

  return obj
}



function setScore(obj: any) {
  console.log("creating ", obj);

  const dataString = JSON.stringify(obj);
  console.log(obj);

  fetch('https://invaders-page.herokuapp.com/scores', {
    method: 'POST', // or 'PUT'
    headers: {
      'Content-Type': 'application/json',
    },
    body: dataString,
  })
    .then((response) => response)
    .then((data) => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}
