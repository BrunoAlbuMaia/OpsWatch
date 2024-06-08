import React, { useState, useEffect } from 'react';
import { getDocumentacao_chave } from '../../service/Documentacao';
import JSONPretty from 'react-json-prettify';


const PluginInfo = ({ pluginName }) => {
  const [pluginData, setPluginData] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const resultado = await getDocumentacao_chave(pluginName);
        setPluginData(resultado || {}); // Garante que pluginData seja um objeto, mesmo em caso de erro.
        console.log(resultado);
      } catch (err) {
        setError('Erro ao buscar os dados do plugin.');
        setPluginData({});
      }
    };

    if (pluginName) {
      fetchData();
    }
  }, [pluginName]);


  

  return (
    <div className="container mx-auto p-4">
      {/* <h1 className="text-2xl font-bold mb-4">Informações do Plugin: {pluginName}</h1> */}
      {error && <p className="text-red-500">{error}</p>}
      {pluginData && Object.keys(pluginData).length > 0 ? (
        <div className="bg-gray-100 p-4 rounded">
          <p className="mb-2"><strong>Nome da Chave:</strong> {pluginData.nmChavePlugin}</p>
          <div className="mb-4">
            <p><strong>Estrutura:</strong></p>
            <div className="bg-white p-2 rounded border overflow-auto">
              {pluginData.nmJsonPlugin ? (
                <JSONPretty json={pluginData.nmJsonPlugin}></JSONPretty>
              ) : (
                <p>Nenhuma estrutura disponível</p>
              )}
            </div>
          </div>
          <div className="mb-4">
            <p><strong>Descrição:</strong></p>
            <p>{pluginData.descricao}</p>
          </div>
        </div>
      ) : (
        <p>Carregando informações...</p>
      )}
    </div>
  );
};

export default PluginInfo;
