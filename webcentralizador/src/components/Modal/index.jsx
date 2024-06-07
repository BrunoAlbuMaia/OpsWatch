import React from 'react';
import { AiOutlineClose } from 'react-icons/ai';

const ResponsiveModal = ({ isOpen, onRequestClose, title, children }) => {
  const modalClasses = isOpen
    ? 'fixed top-0 left-0 w-full h-full flex items-center justify-center overflow-auto'
    : 'hidden';

  const modalContentClasses = 'bg-white w-full md:w-1/2 lg:w-2/3 xl:w-1/3 p-4 rounded shadow-lg';

  return (
    <div className={modalClasses}>
      <div className={modalContentClasses}>
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-semibold">{title}</h2>
          <button
            className="text-gray-500 hover:text-gray-700 focus:outline-none"
            onClick={onRequestClose}
          >
            <AiOutlineClose/>
          </button>
        </div>
        <div>{children}</div>
      </div>
    </div>
  );
};

export default ResponsiveModal;