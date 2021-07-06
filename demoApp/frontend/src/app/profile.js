import React from 'react';
import ReactDOM from 'react-dom';

import { ToastContainer } from 'react-toastify';
import { Button, Form, Input } from 'reactstrap';

import DashboardHeader from '../components/DashboardHeader';

import { USER_API } from '../utils/constants';
import { getRequest, postRequest, getHeaders, postHeaders, notify } from '../utils/Utils';


class ProfilePage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            id: "",
            email: "",
            first_name: "",
            last_name: "",
            profile_pic: "",
            fileData: '',
        }
    }

    // get logged in users profile
    getUserProfile = () => {
        getRequest(USER_API, this.setUserProfile, getHeaders);
    }

    // callback function to set profile
    setUserProfile = (data) => {
        if (data) {
            var result = data.body.results;
            this.setState({
                "id": result.id,
                "email": result.email,
                "first_name": result.first_name,
                "last_name": result.last_name,
            })
        }
    }

    // handles form validation and notifies the user for the same
    handleValidation = () => {
        if (!this.state.first_name) {
            notify("First name cannot be empty!", 'error');
            return false;
        }
        if (!this.state.last_name) {
            notify("Last name cannot be empty!", 'error');
            return false;
        }
        return true;
    }

    // event handler for on submit of profile form
    onSubmit = () => {
        var isValid = this.handleValidation();
        if (isValid) {
            var post_data = {
                "id": this.state.id,
                "first_name": this.state.first_name,
                "last_name": this.state.last_name,
                "email": this.state.email,
                "profile_pic": this.state.fileData,
            }
            var body = JSON.stringify(post_data)
            postRequest(USER_API, body, this.handleSubmitResponse, "POST", postHeaders);
        }
    }

    // callback event for profile form submit
    handleSubmitResponse = (data) => {
        if (data.header.status == 1) {
            notify(data.body.msg)
        } else {
            notify(data.body.msg, 'error')
        }
    }

    // as soon as the component mounts get the user profile
    componentDidMount() {
        this.getUserProfile();
    }

    // handle input text change 
    handleTextChange = (e) => {
        if (e.target.name == 'first_name') {
            this.setState({ first_name: e.target.value })
        }
        if (e.target.name == 'last_name') {
            this.setState({ last_name: e.target.value })
        }
    }

    render() {
        return (
            <React.Fragment>
                <DashboardHeader />
                <ToastContainer />
                <div className="row justify-content-center">
                    <div className="col-md-4 m-4 p-3">
                        <center>
                            <h4>Profile</h4>
                        </center>
                        <Form>
                            <div className="form-group">
                                <label >Email</label>
                                <Input type="email" className="form-control" name="email" aria-describedby="emailHelp"
                                    placeholder="Enter email" value={`${this.state.email}`} disabled />
                            </div>
                            <div className="form-group">
                                <label>First Name</label>
                                <Input type="text" className="form-control" name="first_name" aria-describedby="firstNameHelp"
                                    placeholder="John" value={`${this.state.first_name}`}
                                    onChange={this.handleTextChange} />
                            </div>
                            <div className="form-group">
                                <label>Last Name</label>
                                <Input type="text" className="form-control" name="last_name" aria-describedby="lastNameHelp"
                                    placeholder="Doe" value={`${this.state.last_name}`}
                                    onChange={this.handleTextChange} />
                            </div>
                            <div>
                                <Button color="primary" size="md" onClick={this.onSubmit}>Submit</Button>
                            </div>
                        </Form>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}

export default ProfilePage;

ReactDOM.render(<ProfilePage />, document.getElementById('root'));
