import path from 'path';
import express, { Express } from 'express';
import cors from 'cors';
import { json } from 'body-parser';

const app: Express = express();
app.use(cors());
app.use(json());
const root: string = path.join(process.cwd(), 'dist');

app.use(express.static(root));

app.get('*', (_req, res) => {
  res.sendFile(path.join(root, 'index.html'));
});

app.post('/score', (_req, res) => {
  let obj = res.json({requestBody: _req.body})
  console.log(obj);
  
  res.sendFile(path.join(root, 'index.html'));
});
const port = process.env.PORT || 4000;
app.listen(port, () => {
  console.log('Hosted: http://localhost:' + port);
});
