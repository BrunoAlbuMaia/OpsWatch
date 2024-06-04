import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCircleCheck, faCircleXmark } from '@fortawesome/free-solid-svg-icons';
import GenericTable from '../../components/Tabela/index';

const servers = [
  { nrServidorId: 2, nmServidor: 'OFBNB043859', nmIpServidor: '10.2.60.112', nmDescricao: '', urlWebsocketServidor: 'ws://10.2.60.112:9001/Servidor/ws', urlWebsocketJobs: 'ws://10.2.60.112:9001/Jobs/ws', flAtivo: false, statusJobs: false },
  { nrServidorId: 3, nmServidor: 'SRVDS01', nmIpServidor: '110.1.0.250', nmDescricao: '', urlWebsocketServidor: 'ws://10.1.0.250:9001/Servidor/ws', urlWebsocketJobs: 'ws://10.1.0.250:9001/Jobs/ws', flAtivo: true, statusJobs: true },
  // Adicione mais servidores conforme necessário
];

const columns = [
  { header: 'ID', accessor: 'nrServidorId' },
  { header: 'Nome', accessor: 'nmServidor' },
  { header: 'IP', accessor: 'nmIpServidor' },
  { header: 'URL WebSocket Servidor', accessor: 'urlWebsocketServidor' },
  { header: 'URL WebSocket Jobs', accessor: 'urlWebsocketJobs' },
  { header: 'Status', accessor: 'flAtivo' },
  { header: 'StatusJob', accessor: 'statusJobs' },
];

function TabelaServidores() {
  const renderRow = (server) => {
    return (
      <>
        <td className="py-3 px-6 text-left whitespace-nowrap">{server.nrServidorId}</td>
        <td className="py-3 px-6 text-left">{server.nmServidor}</td>
        <td className="py-3 px-6 text-left">{server.nmIpServidor}</td>
        <td className="py-3 px-6 text-left">{server.urlWebsocketServidor}</td>
        <td className="py-3 px-6 text-left">{server.urlWebsocketJobs}</td>
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
      </>
    );
  };

  return <GenericTable columns={columns} data={servers} renderRow={renderRow} />;
}

export default TabelaServidores;
