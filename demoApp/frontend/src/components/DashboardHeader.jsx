import React from 'react';
import { Button, Input, Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';
import { putRequest, notify, fileUploadHeaders } from '../utils/Utils';
import { USER_API } from '../utils/constants';

// import common css file
import '../css/App.css';

class DashboardHeader extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            profilePic: PROFILE_PIC,
            fullName: FULLNAME,
            modal: false,
            fileData: '',
        };
    }

    // toggle file upload modal
    toggleModal = () => {
        this.setState({ modal: !this.state.modal });
    };

    // handle file change, as the user uploads it
    handleFileChange = (e) => {
        this.setState({
            fileData: e.target.files[0],
        });
    };

    // submit reponse for file upload
    handleFileUpload = (e) => {
        if (this.state.fileData) {
            let formData = new FormData();
            formData.set('image_file', this.state.fileData);
            putRequest(USER_API, formData, this.profileImageUpdateSuccess,
                "PUT", fileUploadHeaders);
        }
    };

    // call back function for file upload
    profileImageUpdateSuccess = (data) => {
        if (data.header.status == 1) {
            this.setState({
                profilePic: URL.createObjectURL(this.state.fileData)
            });
        }
        notify(data.body.msg);
    };

    render() {
        return (
            <div className="body-section border">
                <nav className="navbar navbar-expand-lg navbar-light bg-light">
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav">
                            <li className="nav-item active">
                                <a className="nav-link" href="/">DemoApp <span
                                    className="sr-only">(current)</span></a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="/users">Users</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="/upload">Upload</a>
                            </li>
                        </ul>
                        <ul className="navbar-nav dropdown ml-auto">
                            <li className="nav-item">
                                <img src={`${this.state.profilePic}`}
                                    className="rounded-circle" width="50px"
                                    onClick={this.toggleModal}
                                />
                            </li>
                            <li className="nav-item">
                                <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    {this.state.fullName}
                                </a>
                                <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                                    <a className="dropdown-item" href="/profile">Profile</a>
                                    <div className="dropdown-divider"></div>
                                    <a className="dropdown-item" href="/logout">Logout</a>
                                </div>
                            </li>
                        </ul>
                    </div>
                </nav>
                <Modal isOpen={this.state.modal} toggle={this.toggleModal}>
                    <ModalHeader toggle={this.toggleModal}>Edit your profile image</ModalHeader>
                    <ModalBody>
                        <div className="text-center">
                            <img src={`${this.state.profilePic}`}
                                className="rounded-circle" width="200px"
                                onClick={this.toggleModal}
                            />
                        </div>
                        <Input type="file" className="form-control btn" name="profile_pic"
                            aria-describedby="lastNameHelp"
                            onChange={this.handleFileChange}
                        />
                    </ModalBody>
                    <ModalFooter>
                        <Button color="success" onClick={this.handleFileUpload}>Submit</Button>
                        <Button color="secondary" onClick={this.toggleModal}>Cancel</Button>
                    </ModalFooter>
                </Modal>
            </div>
        );
    }
}

export default DashboardHeader;