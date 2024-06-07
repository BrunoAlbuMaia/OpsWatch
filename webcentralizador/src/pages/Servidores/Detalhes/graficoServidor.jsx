import React, { useEffect, useRef, useState } from 'react';
import Chart from 'chart.js/auto';

const GraficosServidor = () => {
  const cpuChartRef = useRef(null);
  const ramChartRef = useRef(null);
  const diskChartRef = useRef(null);
  const [selectedYear, setSelectedYear] = useState('2022'); // Valor inicial do filtro de ano

  useEffect(() => {
    const createChart = (chartRef, label, data) => {
      const ctx = chartRef.current.getContext('2d');

      // Inicializar o gráfico
      return new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'],
          datasets: [
            {
              label: label,
              data: data,
              fill: false,
              borderColor: 'rgb(75, 192, 192)',
              tension: 0.1,
            },
          ],
        },
      });
    };

    const cpuChart = createChart(cpuChartRef, 'Uso de CPU', [65, 59, 80, 81, 56, 55]);
    const ramChart = createChart(ramChartRef, 'Uso de Memória RAM', [35, 50, 60, 70, 45, 55]);
    const diskChart = createChart(diskChartRef, 'Uso do Disco', [20, 40, 50, 100, 30, 45]);

    // Retornar uma função de limpeza para destruir os gráficos ao desmontar o componente
    return () => {
      cpuChart.destroy();
      ramChart.destroy();
      diskChart.destroy();
    };
  }, [selectedYear]); // Atualizar os gráficos sempre que o ano selecionado mudar

  // Função para lidar com a mudança no seletor de ano
  const handleYearChange = (e) => {
    setSelectedYear(e.target.value);
  };

  return (
    <div className="container mx-auto mt-8 p-4">
      {/* Seletor de ano */}
      
      <div className="mb-4">
        <label htmlFor="year" className="mr-2">Selecione o ano:</label>
        <select id="year" value={selectedYear} onChange={handleYearChange}>
          <option value="2022">2022</option>
          <option value="2021">2021</option>
          {/* Adicione mais opções de ano conforme necessário */}
        </select>
      </div>

      {/* Gráficos */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div>
          <canvas ref={cpuChartRef} className="w-full" style={{ maxWidth: '400px', margin: '0 auto' }} />
        </div>
        <div>
          <canvas ref={ramChartRef} className="w-full" style={{ maxWidth: '400px', margin: '0 auto' }} />
        </div>
        <div>
          <canvas ref={diskChartRef} className="w-full" style={{ maxWidth: '400px', margin: '0 auto' }} />
        </div>
      </div>
    </div>
  );
};

export default GraficosServidor;
