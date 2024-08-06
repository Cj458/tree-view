import React from "react";

const EmployeeList = ({ employees, loadMore, hasMore }) => {
  return (
    <div className="employee-list">
      <ul>
        {employees.map(employee => (
          <li key={employee.id}>
            {employee.full_name} - {employee.position}
          </li>
        ))}
      </ul>
      {hasMore && (
        <button onClick={loadMore}>Load More...</button>
      )}
    </div>
  );
};

export default EmployeeList;
