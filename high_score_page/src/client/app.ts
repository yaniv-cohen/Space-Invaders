window.addEventListener('load', () => {
  getScores()

  //manually enter a score -  geet good
//   document.getElementById('postButton')?.addEventListener('click',
//   ()=>{ setScore({ 'name': 'yaniv', 'score': Math.random()*2000 })
// fetch('http://localhost:4000/clear')
// } )
});


// fetches the scores from the server, which makes a query in the DB
// then, add to the HTML a score_div for each score
async function getScores() {
  let obj = await (await fetch("https://invaders-page.herokuapp.com/scores")).json()
  console.log(obj);
  console.log("count ", typeof obj);
  // obj.sort((a: number, b: number) => a - b)
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


// manual score insertion
// function setScore(obj: any) {
//   console.log("creating ", obj);

//   const dataString = JSON.stringify(obj);
//   console.log(obj);

//   fetch('https://invaders-page.herokuapp.com/scores', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: dataString,
//   })
//     .then((response) => response)
//     .then((data) => {
//       console.log('Success:', data);
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//     });
// }
