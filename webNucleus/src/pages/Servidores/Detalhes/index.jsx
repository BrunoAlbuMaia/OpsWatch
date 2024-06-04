import React, { useState, useEffect } from 'react';
import GraficosServidor from './graficoServidor';

const DetalhesServidor = () => {
    const [activeTab, setActiveTab] = useState('informacoesGerais');
    const [isSmallScreen, setIsSmallScreen] = useState(window.innerWidth <= 600);

    useEffect(() => {
        const handleResize = () => {
        setIsSmallScreen(window.innerWidth <= 600);
        };

        window.addEventListener('resize', handleResize);

        return () => {
        window.removeEventListener('resize', handleResize);
        };
    }, []);

    const handleTabChange = (tab) => {
        setActiveTab(tab);
    };

    return (
        <div className="container mx-auto mt-8 p-4">
            <div className="bg-white border rounded shadow-lg p-4">
                <ul className="flex mb-4">
                    <li
                    className={`mr-4 cursor-pointer ${
                    activeTab === 'informacoesGerais' ? 'border-b-2 border-blue-500' : ''
                    }`}
                    onClick={() => handleTabChange('informacoesGerais')}
                    >
                        Informações Gerais
                    </li>
                    <li
                        className={`mr-4 cursor-pointer ${
                        activeTab === 'graficomediarecuroso' ? 'border-b-2 border-blue-500' : ''
                        }`}
                        onClick={() => handleTabChange('graficomediarecuroso')}
                    >
                        Gráficos média de recursos
                    </li>
                    <li
                        className={`mr-4 cursor-pointer ${
                        activeTab === 'graficotemporeal' ? 'border-b-2 border-blue-500' : ''
                        }`}
                        onClick={() => handleTabChange('graficotemporeal')}
                    >
                        Gráficos em tempo real
                    </li>
                    <li
                        className={`mr-4 cursor-pointer ${
                        activeTab === 'logsEventos' ? 'border-b-2 border-blue-500' : ''
                        }`}
                        onClick={() => handleTabChange('logsEventos')}
                    >
                        Logs e Eventos
                    </li>
                    
                    <li
                        className={`mr-4 cursor-pointer ${
                        activeTab === 'servicosagendados' ? 'border-b-2 border-blue-500' : ''
                        }`}
                        onClick={() => handleTabChange('servicosagendados')}
                    >
                        Serviços agendados
                    </li>
                </ul>

                {activeTab === 'informacoesGerais' && <GraficosServidor/>}
                {activeTab === 'graficomediarecuroso' && <GraficosServidor />}
                {/* {activeTab === 'logsEventos' && <LogsEventos />} */}
                {/* {activeTab === 'aplicacoesServicos' && <AplicacoesServicos />} */}
            </div>
        </div>
    );
};

export default DetalhesServidor;
