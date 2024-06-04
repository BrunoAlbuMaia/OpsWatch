import React, { useState } from 'react';
import ReactJson from 'react-json-view';
import Modal from '../../components/Modal'; // Importe o componente Modal customizado aqui
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faInfoCircle } from '@fortawesome/free-solid-svg-icons';

const JsonViewer = ({ jsonData }) => {
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [selectedKey, setSelectedKey] = useState('');
  const [selectedValue, setSelectedValue] = useState('');

  const handleKeyClick = (key, value) => {
    setSelectedKey(key);
    setSelectedValue(value);
    setModalIsOpen(true);
  };

  const customKeyRenderer = (keyProps) => {
    const handleClick = () => handleKeyClick(keyProps.name, keyProps.value);
    const isSpecialKey = keyProps.name === 'abrir_exe'; // Defina suas chaves especiais aqui
    return (
      <div style={{ display: 'flex', alignItems: 'center' }}>
        {isSpecialKey && (
          <FontAwesomeIcon
            icon={faInfoCircle}
            style={{ marginRight: '4px', color: 'blue', cursor: 'pointer' }}
            onClick={handleClick}
          />
        )}
        <span>{keyProps.name}</span>
      </div>
    );
  };

  return (
    <div>
      {/* Exibir o JSON usando react-json-view com a renderização personalizada de chave */}
      <ReactJson
        src={jsonData}
        icon={false}
        name={false}
        enableClipboard={false}
        displayObjectSize={false}
        displayDataTypes={false}
        collapsed={false}
        groupArraysAfterLength={10}
        indentWidth={4}
        keyRenderer={customKeyRenderer}
      />

      {/* Modal para exibir informações sobre a chave selecionada */}
      <Modal isOpen={modalIsOpen} onRequestClose={() => setModalIsOpen(false)} title="Informações da Chave">
        <h2 className="text-xl font-bold mb-2">Informações adicionais</h2>
        <p>Chave: {selectedKey}</p>
        <p>Valor: {selectedValue}</p>
        {/* Aqui você pode adicionar mais informações conforme necessário */}
        <button onClick={() => setModalIsOpen(false)} className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 focus:outline-none">
          Fechar
        </button>
      </Modal>
    </div>
  );
};

export default JsonViewer;
