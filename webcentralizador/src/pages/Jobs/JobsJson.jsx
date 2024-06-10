import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faInfoCircle } from '@fortawesome/free-solid-svg-icons';
import JSONPretty from 'react-json-prettify';
import ResponsiveModal from '../../components/Modal'
import PluginInfo from './pluginInfo';

const JobJson = () => {
  const [modalOpen, setModalOpen] = useState(false); // Estado para controlar se o modal está aberto
  const [selectedPluginKey,setSelectedPluginKey] = useState()
  
  function openModal(pluginKey) {
    // Set modalOpen state with the received pluginKey
    setModalOpen(true);
    setSelectedPluginKey(pluginKey); // Add a state variable to store the selected plugin key
  }

  const closeModal = () => {
    setModalOpen(false);
  };


  const data = {
    jobs: [
      {
        id: 1,
        nomeJOB: "Abrir e fechar monitoramento chrome",
        cron_time: "* * * * *",
        status: false,
        plugins: {
          fechar_exe: {
            nome_arquivo_plugin: "openClose",
            nome_arquivo_hooks: "openClose_hooks",
            config: {
              nome_exe: "chrome.exe",
              description: "Esse é o nome do executável que ele vai fechar, pela tela de GERENCIADOR DE TAREFAS"
            }
          },
          abrir_exe: {
            nome_arquivo_plugin: "openClose",
            nome_arquivo_hooks: "openClose_hooks",
            config: {
              caminho_exe: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
              description: "Caminho executável para o arquivo google.exe"
            }
          },
          call_api: {
            nome_arquivo_plugin: "http",
            nome_arquivo_hooks: "http_hooks",
            config: {
              method: "GET",
              url: "https://viacep.com.br/ws/60532560/json/",
              description: "Consumindo API para buscar dados de um CEP"
            }
          }
        }
      },
      {
        id: 1,
        nomeJOB: "Abrir e fechar monitoramento chrome",
        cron_time: "* * * * *",
        status: false,
        plugins: {
          fechar_exe: {
            nome_arquivo_plugin: "openClose",
            nome_arquivo_hooks: "openClose_hooks",
            config: {
              nome_exe: "chrome.exe",
              description: "Esse é o nome do executável que ele vai fechar, pela tela de GERENCIADOR DE TAREFAS"
            }
          },
          abrir_exe: {
            nome_arquivo_plugin: "openClose",
            nome_arquivo_hooks: "openClose_hooks",
            config: {
              caminho_exe: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
              description: "Caminho executável para o arquivo google.exe"
            }
          },
          call_api: {
            nome_arquivo_plugin: "http",
            nome_arquivo_hooks: "http_hooks",
            config: {
              method: "GET",
              url: "https://viacep.com.br/ws/60532560/json/",
              description: "Consumindo API para buscar dados de um CEP"
            }
          }
        }
      }
    ]
  };

  return (
    <div className="container mx-auto p-4">
      {data.jobs.map((job) => (
        <div key={job.id} className="mb-4 bg-gray-100 p-4 rounded">
          <p className="font-bold">{`{`}</p>
          <div className="ml-4">
            <p className="font-bold">"id": {job.id},</p>
            <p className="font-bold">"nome_job": "{job.nomeJOB}",</p>
            <p className="font-bold">"cron_time": "{job.cron_time}",</p>
            <p className="font-bold">"status": "{job.status ? 'Ativo' : 'Inativo'}",</p>
            <p className="font-bold">"plugins": {`{`}</p>
            <div className="ml-4">
              {Object.keys(job.plugins).map((pluginKey, index) => {
                const plugin = job.plugins[pluginKey];
                return (
                  <div key={pluginKey} className="mb-2">
                    <div className="flex items-center">
                      <FontAwesomeIcon
                        icon={faInfoCircle}
                        onClick={()=> openModal(pluginKey)}
                        className="text-blue-500 cursor-pointer"
                        data-plugin-name={pluginKey}
                      />
                      <p className="font-bold ml-2">{`"${pluginKey}": {`}</p>
                    </div>
                    <div className="ml-4">
                      <p className="font-bold">"nome_plugin": "{plugin.nome_arquivo_plugin}",</p>
                      <p className="font-bold">"nome_hooks": "{plugin.nome_arquivo_hooks}",</p>
                      <p className="font-bold">"config": </p>
                      <div className="ml-4">
                        <JSONPretty json={plugin.config} />
                      </div>
                    </div>
                    <p className="font-bold ml-2">{index === Object.keys(job.plugins).length - 1 ? `}` : `},`}</p>
                  </div>
                );
              })}
            </div>
            <p className="font-bold"> {`}`}</p>
          </div>
          <p className="font-bold">{`}`}</p>
          <hr></hr>
        </div>
      ))}

        <ResponsiveModal
        isOpen={modalOpen}
        onRequestClose={closeModal}
        title="Informações do Plugin"
        >
          <PluginInfo pluginName={selectedPluginKey}/>
      </ResponsiveModal>

    </div>
  );
};

export default JobJson;
