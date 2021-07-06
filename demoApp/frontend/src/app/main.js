import React from 'react';
import ReactDOM from 'react-dom';
import Cookies from 'universal-cookie';

import { ToastContainer } from 'react-toastify';
import DashboardHeader from '../components/DashboardHeader';
// import { getRequest, postRequest, authHeaders } from '../../utils/Utils';
// import { Button, Form, Input, Row, Col, Table } from 'reactstrap';

const cookies = new Cookies();

class Dashboard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fullName: FULLNAME ? FULLNAME : '',
            profilePic: PROFILE_PIC ? PROFILE_PIC : '/static/images/default-profile.png',
        };
    }

    render() {
        return (
            <React.Fragment>
                <ToastContainer />
                <DashboardHeader
                    fullName={this.state.fullName}
                    profilePic={this.state.profilePic}
                />
                <div className="row justify-content-center">
                    <div className="col-md-6 m-6 p-3">
                        <p>Welcome To DemoApp, {`${this.state.fullName}`}</p>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}

export default Dashboard;

ReactDOM.render(<Dashboard />, document.getElementById('root'));
