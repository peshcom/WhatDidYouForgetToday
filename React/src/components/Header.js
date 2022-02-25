import React, {useState} from 'react'


function Header() {
    let [logged, setLogged] = useState(localStorage.getItem('access_token') && localStorage.getItem('access_token').length > 0)

    const logout = () => {
        localStorage.clear();
        setLogged(false);
        window.location.reload();
    }

    return (
        <header>
            <div className="navbar bg-dark">
                <div className="w-100 mx-3">
                    <div className="d-flex justify-content-between">
                        <div className="brand my-auto">
                            <a href='/' className="text-white text-decoration-none">
                                <h1 className="fw-bold" title="What did you forget today?">WDYFT</h1>
                            </a>
                        </div>
                        {logged ? <a className="my-auto text-white" onClick={logout} href="#">Logout</a> : ""}
                    </div>
                </div>
            </div>
        </header>
    )
}

export default Header
