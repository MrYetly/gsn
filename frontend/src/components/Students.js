import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { getStudents } from 'services/studentServices';

export default function Students(props) {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    console.log('useEffect ran in Students.js');
    getStudents().then((s) => {
      setStudents(s);
      setLoading(false);
    });
  }, []);

  if (loading) {
    return (
        <div>
            <h1>Students</h1>
            <h2>Loading...</h2>
        </div>
    );
  }
  return (
      <div>
          <h1>Students</h1>
          <table>
              <thead>
                  <tr>
                      <th>Name</th>
                      <th>School</th>
                      <th>Birthdate</th>
                  </tr>
              </thead>
              <tbody>
                  {students.map((student) => {
                    const {
                      studentId, name, school, schoolId, birthdate,
                    } = student;
                    return (
                        <tr key={studentId}>
                            <td><Link to={`/students/${studentId}`}>{name}</Link></td>
                            <td><Link to={`/schools/${schoolId}`}>{school}</Link></td>
                            <td>{birthdate}</td>
                        </tr>
                    );
                  })}
              </tbody>
          </table>
      </div>
  );
}
