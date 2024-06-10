import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCircleCheck, faCircleXmark } from '@fortawesome/free-solid-svg-icons';
import GenericTable from '../../components/Tabela/index';
import { Link } from 'react-router-dom';

function TabelaServidores({servers,columns}) {
  const renderRow = (server) => {
    return (
      <>
        <td className="py-3 px-6 text-left whitespace-nowrap">{server.nrServidorId}</td>
        <td className="py-3 px-6 text-left">{server.nmServidor}</td>
        <td className="py-3 px-6 text-left">{server.nmIpServidor}</td>
        <td className="py-3 px-6 text-left">{server.urlWebsocketServidor}</td>
        <td className="py-3 px-6 text-left">{server.urlWebSocketJobs}</td>
        <td className="py-3 px-6 text-center">
          <span
            className={`py-1 px-3 rounded-full text-xs ${
              server.flAtivo ? 'bg-green-200 text-green-600' : 'bg-red-200 text-red-600'
            }`}
          >
            {server.flAtivo ? 'Ativo' : 'Inativo'}
          </span>
        </td>
        <td className="py-3 px-6 text-center">
          <span
            className={`py-1 px-3 rounded-full text-xs ${
              server.statusJobs ? 'bg-green-200 text-green-600' : 'bg-red-200 text-red-600'
            } flex items-center justify-center`}
          >
            <FontAwesomeIcon icon={server.statusJobs ? faCircleCheck : faCircleXmark} className="mr-1" />
            {server.statusJobs ? 'Sucesso' : 'Falha'}
          </span>
        </td>
        <td className="py-3 px-6 text-left">
          <Link to={`/detalheServidor/${server.nmIpServidor}`}>
          <button className="py-2 px-4 bg-green-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75">
            Verificar
          </button>
          </Link>
        </td>
      </>
    );
  };

  return <GenericTable columns={columns} data={servers} renderRow={renderRow} />;
}

export default TabelaServidores;
