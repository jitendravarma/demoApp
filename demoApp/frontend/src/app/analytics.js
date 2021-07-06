import React from 'react';
import ReactDOM from 'react-dom';
import Datetime from 'react-datetime';
import DashboardHeader from '../components/DashboardHeader';

import { ToastContainer } from 'react-toastify';
import {
    Button, Col, Form, Label, FormGroup
} from 'reactstrap';

import { TRANSFER_HISTORY_API_URL } from '../utils/constants'
import { postRequest, postHeaders, notify } from '../utils/Utils';

class AnalyticsPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            convertModal: false,
            balanceModal: false,
            fullName: FULLNAME ? FULLNAME : '',
            profilePic: PROFILE_PIC ? PROFILE_PIC : '/static/images/default-profile.png',
            endDate: new Date(),
            history: [],
        }
    }


    handleFileUpload = (e) => {
        this.setState({
            profilePic: URL.createObjectURL(e.target.files[0])
        })
    }

    toggleConvertModal = () => {
        this.setState({ convertModal: !this.state.convertModal })
    }

    isValidDate = (current) => {
        var d = new Date();
        if (current > d) {
            return false;
        } return true;
    }

    handleDateChange = (current) => {
        var state = this.state;
        if (current < this.state.endDate) {
            state.startDate = current
            this.setState(state);
        } else {
            notify("Start date should be less than enddate", "error")
        }
    }

    generateHistory = () => {
        if (!this.state.startDate) {
            notify("Please select start date first", "error")
        } else {
            var startDate = this.state.startDate.format('YYYY-MM-DD');
            var endDate = this.state.endDate.toISOString().slice(0, 10);
            var post_data = { "start_date": startDate, "end_date": endDate }
            var body = JSON.stringify(post_data);
            postRequest(TRANSFER_HISTORY_API_URL, body, this.handleHistory,
                "POST", postHeaders);
        }
    }

    handleHistory = (data) => {
        if (data.body.results.length > 0) {
            this.setState({ history: data.body.results })
        } else {
            notify("No results found", "info")
        }
    }

    render() {
        var table = "";
        if (this.state.history.length > 0) {
            table = <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Amount</th>
                        <th>From</th>
                        <th>To</th>
                        <th>Sent Rate</th>
                        <th>Current Rate</th>
                        <th>Difference</th>
                        <th>Sent Date</th>
                    </tr>
                </thead>
                <tbody>
                    {this.state.history.map((item, index) => {
                        return (
                            <tr key={index}>
                                <td>{item.amount}</td>
                                <td>{item.sender.first_name} {item.sender.last_name}</td>
                                <td>{item.receiver.first_name} {item.receiver.last_name}</td>
                                <td>{item.difference.sent_rate}</td>
                                <td>{item.difference.current_rate}</td>
                                <td>{item.difference.diff}</td>
                                <td>{item.date_added}</td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>
        }
        return (
            <React.Fragment>
                <ToastContainer />
                <DashboardHeader
                    fullName={this.state.fullName}
                    profilePic={this.state.profilePic}
                />
                <div className="row justify-content-center">
                    <div className="col-md-6 m-4 p-3">
                        <center>
                            <h4>Analytics</h4>
                            <p>Enter start date to generate order history</p>
                        </center>
                        <Form>
                            <FormGroup row>
                                <Label for="" className="d-block">Start Date</Label>
                                <Col sm={6}>
                                    <Datetime refs="start_date" dateFormat="YYYY-MM-DD" timeFormat={false}
                                        placeholder="YYYY-MM-DD" id="start_date" onChange={(e) => this.handleDateChange(e)}
                                        inputProps={{ placeholder: 'Start date' }}
                                        value={this.state.startDate}
                                    />
                                </Col>
                            </FormGroup>
                            <FormGroup row>
                                <Label for="" className="d-block">End Date</Label>
                                <Col sm={6}>
                                    <Datetime refs="end_date"
                                        dateFormat="YYYY-MM-DD" timeFormat={false}
                                        placeholder="YYYY-MM-DD" id="end_date"
                                        inputProps={{ placeholder: 'N/A', 'disabled': true }} value={this.state.endDate} />
                                </Col>
                            </FormGroup>
                            <FormGroup>
                                <Button color="primary" size="md" onClick={this.generateHistory}>Get History</Button>
                            </FormGroup>
                        </Form>
                    </div>
                    <div className="row">
                        <div className="col-md-12 m-4">
                            {table}
                        </div>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}

export default AnalyticsPage;

ReactDOM.render(<AnalyticsPage />, document.getElementById('root'));
