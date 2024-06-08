import React, { useState,useEffect } from 'react';
import TabelaServidores from './TabelaServidores';
import { getServidoresAll } from '../../service/Servidor';

function Servidores() {
  const [servers, setServers] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const resultado = await getServidoresAll();
      setServers(resultado || []); // Garante que servers seja um array, mesmo em caso de erro.
      console.log(resultado)
    };
    fetchData();
  }, []);
  

    
    const columns = [
      { header: 'ID', accessor: 'nrServidorId' },
      { header: 'Nome', accessor: 'nmServidor' },
      { header: 'IP', accessor: 'nmIpServidor' },
      { header: 'URL WebSocket Servidor', accessor: 'urlWebsocketServidor' },
      { header: 'URL WebSocket Jobs', accessor: 'urlWebsocketJobs' },
      { header: 'Status', accessor: 'flAtivo' },
      { header: 'StatusJob', accessor: 'statusJobs' },
      { header: '', accessor: '' }
    ];
  

    return (
      <>
        <TabelaServidores columns={columns} servers={servers}></TabelaServidores>
      </>
    );


}

export default Servidores;
