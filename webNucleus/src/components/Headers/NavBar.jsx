import React, { useState } from 'react';
import logoEmpresa from "../../assets/logoEmpresa.png";

const navigation = [
  {
    name: 'Home',
    href: '',
    current: false,
    submenu: [
      { name: 'Dashboard', href: '/dashboard' },
      { name: 'Vendas', href: '/vendas' }
    ]
  },
  { name: 'Servidores', href: 'servidores', current: false }
];

function Navbar() {
  const [showMenu, setShowMenu] = useState(false);
  const [showSubmenu, setShowSubmenu] = useState({});

  const toggleSubmenu = (index) => {
    setShowSubmenu((prev) => ({
      ...prev,
      [index]: !prev[index]
    }));
  };

  return (
    <nav className="bg-green-800 p-1">
      <div className="container mx-auto flex justify-between items-center">
        {/* Logo */}
        <div className="flex items-center">
          <img src={logoEmpresa} alt="Logo" className="w-24 h-20 mr-2" />
        </div>

        {/* Links da Navbar - Visíveis em telas maiores */}
        <ul className="hidden md:flex space-x-4">
          {navigation.map((item, index) => (
            <li key={item.name} className="relative">
              <a
                href={item.href}
                className="flex items-center text-white hover:text-gray-300"
                onClick={(e) => {
                  if (item.submenu) {
                    e.preventDefault();
                    toggleSubmenu(index);
                  }
                }}
              >
                {item.name}
                {item.submenu && (
                  <svg
                    className="ml-2 h-4 w-4 fill-current"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" />
                  </svg>
                )}
              </a>
              {item.submenu && showSubmenu[index] && (
                <ul className="absolute left-0 mt-2 w-40 bg-white rounded shadow-lg">
                  {item.submenu.map((subItem) => (
                    <li key={subItem.name}>
                      <a
                        href={subItem.href}
                        className="block px-4 py-2 text-black hover:text-green-800"
                      >
                        {subItem.name}
                      </a>
                    </li>
                  ))}
                </ul>
              )}
            </li>
          ))}
        </ul>

        {/* Ícone de menu para telas menores */}
        <div className="md:hidden">
          <button className="text-white" onClick={() => setShowMenu(!showMenu)}>
            <svg
              className="h-6 w-6 fill-current"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
            >
              <path
                fillRule="evenodd"
                d="M3 18a1 1 0 0 1 0-2h18a1 1 0 0 1 0 2H3zm0-5a1 1 0 1 1 0-2h18a1 1 0 1 1 0 2H3zm0-5a1 1 0 1 1 0-2h18a1 1 0 1 1 0 2H3z"
              />
            </svg>
          </button>
        </div>
      </div>

      {/* Lista de Links - Dropdown para telas menores */}
      <div className={`md:hidden ${showMenu ? 'block' : 'hidden'}`}>
        <ul className="bg-green-800 py-2 px-4">
          {navigation.map((item, index) => (
            <li key={item.name}>
              <a
                href={item.href}
                className="flex items-center text-white hover:text-gray-300"
                onClick={(e) => {
                  if (item.submenu) {
                    e.preventDefault();
                    toggleSubmenu(index);
                  }
                }}
              >
                {item.name}
                {item.submenu && (
                  <svg
                    className="ml-2 h-4 w-4 fill-current"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" />
                  </svg>
                )}
              </a>
              {item.submenu && showSubmenu[index] && (
                <ul className="pl-4 mt-2 bg-white rounded">
                  {item.submenu.map((subItem) => (
                    <li key={subItem.name}>
                      <a
                        href={subItem.href}
                        className="block py-1 text-black hover:text-green-800"
                      >
                        {subItem.name}
                      </a>
                    </li>
                  ))}
                </ul>
              )}
            </li>
          ))}
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
