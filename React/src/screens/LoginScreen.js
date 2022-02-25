import React, {useState} from 'react'
import {Navigate} from "react-router-dom";
import axios from "axios";


function LoginScreen({location, history}) {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const submitHandler = async (e) => {
        e.preventDefault()
        return await axios
            .post(
                "http://localhost:8000/v1/auth/login",
                {
                    login: username,
                    password: password,
                }
            )
            .then((response) => {
                localStorage.setItem('access_token', response.data.access_token);
                localStorage.setItem('refresh_token', response.data.refresh_token);
                setUsername('');
                return response;
            })
            .catch((error) => {
                console.log(error.message);
            });
    }

    return (
        <div>
            {(() => {
                if (localStorage.getItem('access_token')) {
                    return <Navigate to={'/'}/>
                }
            })()}
            <br/>
            <br/>
            <br/>

            <div className="card">
                <div className="card-body">
                    <div className="d-flex justify-content-center mb-3">
                        <h3 className="fw-bold">Sign In</h3>
                    </div>
                    <form onSubmit={submitHandler}>
                        <input
                            className="form-control mb-2"
                            type="text"
                            placeholder='Enter Username'
                            required={true}
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                        <input
                            className="form-control mb-3"
                            type="password"
                            placeholder='Enter Password'
                            required={true}
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <div className="d-flex justify-content-end mb-3">
                            <button type='submit' className='btn btn-primary'>
                                Sign In
                            </button>
                        </div>
                    </form>
                </div>
            </div>
            <br/>
            <div className="text-center small">
                No have account? <a href="#">Register</a>
            </div>
        </div>
    )
}

export default LoginScreen
