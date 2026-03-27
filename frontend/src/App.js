import {useState} from 'react';
import axios from 'axios';

function App(){
 const [q,setQ]=useState('');
 const [r,setR]=useState([]);

 const search=async()=>{
  const res=await axios.get(`http://localhost:8000/search?q=${q}`);
  setR(res.data.results);
 }

 return(
  <div>
   <h2>AI Search</h2>
   <input onChange={e=>setQ(e.target.value)} />
   <button onClick={search}>Search</button>
   {r.map((x,i)=><p key={i}>{x}</p>)}
  </div>
 )
}

export default App;
