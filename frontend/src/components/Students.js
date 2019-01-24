import React, { Component } from 'react';
import {Link} from 'react-router-dom';
import {getStudents} from 'services/studentServices.js';

class Students extends Component {
  constructor() {
    super();
    this.state = {
      students: [],
    }
  }



  componentWillMount() {
    getStudents().then(students=> {
      this.setState({students, loading: false});
    });
  }

  render() {
    const {students} = this.state;
    return (
      <div>
        <h1>Students</h1>
        <table>
          <tbody>
          {students.map(student=>{
            const {id, name, school, birthdate} = student;
            return (<tr key={id}>
              <td><Link to={`student/${id}`}>{name}</Link></td>
              <td>{school}</td>
              <td>{birthdate}</td>
            </tr>)
          })}
          </tbody>
        </table>
      </div>
    )
  }
}

export default Students;
