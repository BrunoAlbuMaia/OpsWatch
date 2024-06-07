import React from 'react';
import Servidores from './pages/Servidores/index';
import Container from './components/Headers/container';
import Navbar from './components/Headers/NavBar'; // Importando o componente Navbar
import RoutesApp from './routes';
function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <header>
        <Navbar />
      </header>

      {/* Container para o conteúdo principal */}
      <Container>
        <RoutesApp/>
      </Container>
    </div>
  );
}

export default App;
