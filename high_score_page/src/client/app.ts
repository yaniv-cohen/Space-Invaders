window.addEventListener('load', () => {
  getScores()
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
  console.log("creating ", obj);
  console.log(obj);
  return obj
}