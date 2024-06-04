
// export default GenericTable;
import React from 'react';

function GenericTable({ columns, data, renderRow }) {
  return (
    <div className="bg-white shadow-md rounded my-6 overflow-x-auto">
      <table className="min-w-max w-full table-auto">
        <thead>
          <tr className="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
            {columns.map((column, index) => (
              <th key={index} className="py-3 px-6 text-left">{column.header}</th>
            ))}
          </tr>
        </thead>
        <tbody className="text-gray-600 text-sm font-light">
          {data.map((item, index) => (
            <tr key={index} className="border-b border-gray-200 hover:bg-gray-100">
              {renderRow(item)}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default GenericTable;
