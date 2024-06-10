
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEdit,faTrash  } from '@fortawesome/free-solid-svg-icons';
import GenericTable from '../../components/Tabela/index';
import { useParams } from 'react-router-dom';
import React, { useState,useEffect } from 'react';
import { getJobsAll } from '../../service/Jobs';
import cronstrue from 'cronstrue';
import 'cronstrue/locales/pt_BR'; // Importa a tradução para português
import ResponsiveModal from '../../components/Modal'


function Jobs() {
  const { id } = useParams(); // Obtém o parâmetro 'id' da URL
  const [servers, setServers] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const resultado = await getJobsAll(id);
      setServers(resultado || []); // Garante que servers seja um array, mesmo em caso de erro.
      
    };
    fetchData();
  }, []);
  
  
    
    const columns = [
      { header: 'ID', accessor: 'nrServidorId' },
      { header: 'Nome Job', accessor: 'nomeJOB' },
      { header: 'Execução', accessor: 'cron_time' },  // Converte cron time para formato legível
      { header: 'Status', accessor: 'status' },
      { header: '', accessor: '' }
      
    ];
    // console.log(id)

    return (
      <>
        <TabelaJob columns={columns} servers={servers}></TabelaJob>
      </>
    );


}

export default Jobs;





function TabelaJob({servers,columns}) {
  const { id } = useParams(); // Obtém o parâmetro 'id' da URL



  const cronTimeToReadable = (cronTime) => {
    try {
      return cronstrue.toString(cronTime, { locale: 'pt_BR' }); // Usando a biblioteca cronstrue com a tradução para português
    } catch (err) {
      console.error('Erro ao analisar expressão cron:', err);
      return cronTime; // Retorna a expressão cron original em caso de erro
    }
  };
  const renderRow = (server) => {
    return (
      <>
        <td className="py-3 px-7 text-left whitespace-nowrap">{server.id}</td>
        <td className="py-3 px-6 text-left">{server.nomeJOB}</td>
        <td className="py-3 px-6 text-left">{cronTimeToReadable(server.cron_time)}</td>
        

        <td className="py-3 px-6 text-left">
          <span
            className={`py-1 px-4 rounded-full text-xs ${
              server.status ? 'bg-green-200 text-green-600' : 'bg-red-200 text-red-600'
            }`}
          >
            {server.status ? 'Ativo' : 'Inativo'}
          </span>
        </td>
        <td className="py-3 px-6 text-left">
        <button className="py-2 px-4 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75 mr-2">
            <FontAwesomeIcon icon={faEdit} /> Editar
          </button>
          <button className="py-2 px-4 bg-red-500 text-white font-semibold rounded-lg shadow-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-400 focus:ring-opacity-75">
            <FontAwesomeIcon icon={faTrash} /> Deletar
          </button>
        </td>
      </>
    );
  };

  return <GenericTable columns={columns} data={servers} renderRow={renderRow} />;
}


