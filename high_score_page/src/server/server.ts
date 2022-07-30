import path from 'path';
import express, { Express } from 'express';
import cors from 'cors';
import { json } from 'body-parser';
const { Client } = require('pg');

const app: Express = express();
app.use(cors());
app.use(json());
const root: string = path.join(process.cwd(), 'dist');

app.use(express.static(root));


const client = new Client({
  connectionString: 'postgres://ivcbpotjixzvbn:6b543036367326181628fc4be6132b5c3518c2697016a6cc5f74f7ae94f1d15b@ec2-3-213-228-206.compute-1.amazonaws.com:5432/d264mbicdt4rcc',
  ssl: {
    rejectUnauthorized: false
  }
});

client.connect();

const port = process.env.PORT || 4000;
app.listen(port, () => {
  console.log('Hosted: http://localhost:' + port);
});

app.get('/scores', (_request: any, response: any) => {
  client.query('SELECT * FROM scores ORDER BY score DESC LIMIT 10', (err: Error, res: any) => {
    if (err) throw err;
    response.status(200).json(res.rows);
  });
});

// resets all the scores in the DB
// app.get('/clear', (_request: any, response: any) => {
//   console.log(typeof _request.body);
//   let sqlString = "DELETE FROM scores; "
//   let res = executeSQL(sqlString)
//   // let res = sqlString
//   response.send(res);

// });

app.post('/scores', (_request: any, response: any) => {
  console.log(typeof _request.body);
  let json = _request.body
  let sqlString = "INSERT INTO scores(name, score)VALUES( '"+json.name+"', "+json.score+")"
  let res = executeSQL(sqlString)
  // let res = sqlString
  response.send(res);

});

async function executeSQL(sqlString:string) {
  client.query(sqlString, (err: Error /*, res: any*/) => {
    if (err) throw err;
    return "successfuly uploaded"
  });
  return "something happened"
}




app.get('*', (_req, res) => {

  res.sendFile(path.join(root, 'index.html'));
});




