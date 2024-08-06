import React, { useState } from "react";
import { useTreeState } from "./TreeContext";
import EmployeeList from "./EmployeeList";
import { fetchEmployees } from "../data";

const TreeNode = ({ node }) => {
  const { dispatch } = useTreeState();
  const [employees, setEmployees] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [hasMore, setHasMore] = useState(false);

  const handleToggle = async () => {
    dispatch({
      type: "TOGGLE_NODE",
      id: node.id,
      isExpanded: !node.isExpanded,
    });
    if (!node.isExpanded) {
      const data = await fetchEmployees(node.id, 1);
      setEmployees(data.results);
      setHasMore(data.next !== null);
      setCurrentPage(1);
    }
  };

  const loadMore = async () => {
    const data = await fetchEmployees(node.id, currentPage + 1);
    setEmployees((prev) => [...prev, ...data.results]);
    setHasMore(data.next !== null);
    setCurrentPage((prev) => prev + 1);
  };

  return (
    <div className="tree-node">
      {node.children && (
        <button
          onClick={handleToggle}
          className="toggle-icon"
        >
          {node.isExpanded ? "⮝" : "⮟"}
        </button>
      )}
      <span className={node.isHighlight ? "highlight" : ""}>{node.name}</span>
      {node.isExpanded && (
        <>
          <TreeView data={node.children} />
          <EmployeeList employees={employees} loadMore={loadMore} hasMore={hasMore} />
        </>
      )}
    </div>
  );
};

const TreeView = ({ data }) => {
  if (!Array.isArray(data)) {
    return null;
  }

  return (
    <div className="tree-view">
      {data.map((node) => (
        <TreeNode key={node.id} node={node} />
      ))}
    </div>
  );
};

export default TreeView;
