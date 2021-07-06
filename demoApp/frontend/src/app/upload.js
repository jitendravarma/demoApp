import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
import Select from 'react-select';
import DashboardHeader from '../components/DashboardHeader';

import { ToastContainer } from 'react-toastify';
import {
    Button, Form, Input
} from 'reactstrap';

import { WALLET_API_URL, UPLOAD_API_URL, TRANSFER_API_URL } from '../utils/constants';
import { getRequest, postRequest, getHeaders, fileUploadHeaders, notify } from '../utils/Utils';

class UploadJson extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            file: ""
        };
    }

    handleImageUpload = (data) => {
        if (data.header.status === "0") {
            notify("Something went wrong!", "error");
        } else {
            notify("File uploaded successfully!",);
        }
    };


    submitImage = () => {
        const image = this.state.file;
        if (image) {
            let form_data = new FormData();
            form_data.append('file', image, image.name);
            postRequest(UPLOAD_API_URL, form_data, this.handleImageUpload, "POST", fileUploadHeaders);
        } else {
            notify("Please upload json file!", "error");
        }
    };

    handleImageChange = (e) => {
        this.setState({
            file: e.target.files[0]
        });
    };

    render() {
        return (
            <React.Fragment>
                <ToastContainer />
                <DashboardHeader />
                <div className="row justify-content-center">
                    <div className="col-md-6 m-4 p-3">
                        <center>
                            <h4>Upload Json</h4>
                        </center>
                        <Form>
                            <div className="row mt-4">
                                <div className="col-4">
                                    Upload File:
                                </div>
                                <div className="col-5">
                                    <Input accept="application/JSON" type="file" onChange={this.handleImageChange} />
                                </div>
                            </div>
                            <div className="row mt-4">
                                <div className="col-4">
                                    <Button color="primary" size="md" onClick={this.submitImage}>Submit</Button>
                                </div>
                            </div>
                        </Form>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}

export default UploadJson;

ReactDOM.render(<UploadJson />, document.getElementById('root'));
