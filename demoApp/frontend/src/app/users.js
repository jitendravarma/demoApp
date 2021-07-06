import React from 'react';
import ReactDOM from 'react-dom';
import Select from 'react-select';
import DashboardHeader from '../components/DashboardHeader';

import { ToastContainer } from 'react-toastify';
import { Button, Form, Input, Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';

import { TEXT_API_URL } from '../utils/constants';
import { getRequest, postRequest, putRequest, getHeaders, postHeaders, notify } from '../utils/Utils';

import '../css/App.css';

class TextPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            text: [],
            fullName: FULLNAME ? FULLNAME : '',
        };
    }

    // get wallet details for the logged in user
    getText = () => {
        getRequest(TEXT_API_URL, this.setWallet, getHeaders);
    };

    // call back for get wallet and set it in the state
    setWallet = (data) => {
        if (data.header.status === '1') {
            this.setState({ text: data.body.results });
        }
    };

    // as soon as the component mount, set the state of the wallet
    componentDidMount() { this.getText(); }

    render() {
        const { text } = this.state;
        const table = text.map(item => {
            return (<>
                <tr>
                    <th scope="row">{item.user_id}</th>
                    <td>{item.data_id}</td>
                    <td>{item.title}</td>
                    <td>{item.body}</td>
                </tr>
            </>);
        });
        return (
            <React.Fragment>
                <ToastContainer />
                <DashboardHeader />
                <div className="row justify-content-center">
                    <div className="col-md-10 m-4 p-3">
                        <center>
                            <h4>Text</h4>
                        </center>
                        {table ? <table class="table">
                            <thead>
                                <tr>
                                    <th scope="col">User Id</th>
                                    <th scope="col">Data Id</th>
                                    <th scope="col">Title</th>
                                    <th scope="col">Body</th>
                                </tr>
                            </thead>
                            <tbody>
                                {table}
                            </tbody>
                        </table> : <p>"Please upload text"</p>}
                    </div>
                </div>
            </React.Fragment>
        );
    }
}

export default TextPage;

ReactDOM.render(<TextPage />, document.getElementById('root'));
