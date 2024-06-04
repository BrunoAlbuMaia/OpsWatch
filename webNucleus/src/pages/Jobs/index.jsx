import React from 'react';
import JsonViewer from './TabelaJobs';

const App = () => {
  // Exemplo de JSON
  const jsonData = {
    abrir_exe: '! - Quando o cliente clica nisso aparece para que serve esse cara',
    // Adicione mais chaves e valores conforme necessário
  };

  return (
    <div>
      <h1>Visualizador e Editor de JSON</h1>
      {/* Passar o JSON para o componente JsonViewer */}
      <JsonViewer jsonData={jsonData} />
    </div>
  );
};

export default App;
