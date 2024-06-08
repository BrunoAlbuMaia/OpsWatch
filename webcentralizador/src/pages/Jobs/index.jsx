
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCircleCheck, faCircleXmark } from '@fortawesome/free-solid-svg-icons';
import GenericTable from '../../components/Tabela/index';
import { Link } from 'react-router-dom';
import React, { useState,useEffect } from 'react';


function Jobs() {
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
      { header: 'Nome Job', accessor: 'nome_job' },
      { header: 'Horário de execução', accessor: 'cron_time' },
      { header: 'Status', accessor: 'status' },
      
    ];
  

    return (
      <>
        <TabelaJob columns={columns} servers={servers}></TabelaJob>
      </>
    );


}

export default Jobs;





function TabelaJob({servers,columns}) {
  const renderRow = (server) => {
    return (
      <>
        <td className="py-3 px-6 text-left whitespace-nowrap">{server.id}</td>
        <td className="py-3 px-6 text-left">{server.nome_job}</td>
        <td className="py-3 px-6 text-left">{server.cron_time}</td>

        <td className="py-3 px-6 text-center">
          <span
            className={`py-1 px-3 rounded-full text-xs ${
              server.status ? 'bg-green-200 text-green-600' : 'bg-red-200 text-red-600'
            }`}
          >
            {server.status ? 'Ativo' : 'Inativo'}
          </span>
        </td>
        <td className="py-3 px-6 text-left">
          <button className="py-2 px-4 bg-green-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75">
            Editar
          </button>
        </td>
      </>
    );
  };

  return <GenericTable columns={columns} data={servers} renderRow={renderRow} />;
}


