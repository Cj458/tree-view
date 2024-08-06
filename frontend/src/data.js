const REACT_APP_BACKEND_PREFIX = process.env.REACT_APP_BACKEND_PREFIX

export async function fetchData() {
  try {
    const response = await fetch(`${REACT_APP_BACKEND_PREFIX}/api/departments/`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();

    return data.results;
  } catch (error) {
    console.error('Fetch data failed:', error);
    return [];
  }
}

export async function fetchEmployees(departmentId, page = 1) {
  try {
    const response = await fetch(`${REACT_APP_BACKEND_PREFIX}/api/departments/${departmentId}/employees/?page=${page}`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Fetch employees failed:', error);
    return { results: [], next: null };
  }
}
