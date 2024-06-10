import { Fragment,useState } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Servidores from '../pages/Servidores/index'
import DetalhesServidor from '../pages/DetalheServidor'
import EditeJobs from "../pages/Jobs/editarJobs";

const Private = ({ Item }) => {
  const { signed } = useAuth();
  const [signed1, setSigned] = useState();

  return signed ? (
    <Item setSigned={setSigned} />
    
  ) : (
    <Signin setSigned={setSigned} />
  );
};



const RoutesApp = () => {
  return (
    <BrowserRouter>
      <Fragment>
        <Routes>
          <Route path="/servidores" element={<Servidores/>} />
          <Route path="/detalheServidor/:id" element={<DetalhesServidor/>}/>
          <Route path="/teste" element={<EditeJobs/>}/>
          {/* <Route path="Home/" element={<Private Item={MainLayout} />}>
              <Route exact path="/servidores" element={<Servidores/>} />
          </Route> */}
          
        </Routes>
        
      </Fragment>
    </BrowserRouter>
  );
};



export default RoutesApp;