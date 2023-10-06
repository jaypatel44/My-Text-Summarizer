import React from 'react'
import { Link, useLocation, useHistory } from "react-router-dom";
import { ImHome } from 'react-icons/im';
import { BiSolidNotepad,BiLockOpen } from 'react-icons/bi';
import { MdSummarize } from 'react-icons/md';
import { FiLogIn,FiLogOut } from 'react-icons/fi';
import './Navbar.css'



const Navbar = (props) => {
    let history = useHistory();
    const handleLogout = () => {
        localStorage.removeItem('token');
        history.push('/about');
    }
    let location = useLocation();
    return (
        <nav className="navbar navbar-expand-lg navbar-dark " style={{"backgroundColor":"#411f1f"}}>
            <div className="container-fluid">
                <Link className="navbar-brand" to="/about"><div style={{"fontSize":"1.6rem", "marginRight":"1.2rem"}}>TextUtils</div></Link>
                
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse mr-7" id="navbarSupportedContent">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">

                        <li className="nav-item" style={{"display":"flex","alignItems":"center", "justifyContent":"center"}}>
                            <Link className={`nav-link ${location.pathname === "/about" ? "active" : ""}`} to="/about"><ImHome size={22}/> Home</Link>
                        </li>
                        {localStorage.getItem('token') ?
                            <li className="nav-item" style={{"display":"flex","alignItems":"center", "justifyContent":"center"}}>
                                <Link className={`nav-link ${location.pathname === "/" ? "active" : ""}`} aria-current="page" to="/"><BiSolidNotepad size={23}/> Notes</Link>
                            </li>:
                            <p></p>
                        }
                        {localStorage.getItem('token') ?
                            <li className="nav-item" style={{"display":"flex","alignItems":"center", "justifyContent":"center"}}>
                                <Link className={`nav-link ${location.pathname === "/summarizer" ? "active" : ""}`} to="/summarizer"><MdSummarize size={23}/> Summarizer</Link>
                            </li>:
                            <p></p>
                        }

                    </ul>
                    {!localStorage.getItem('token') ? <form className="d-flex">
                        <Link className="mx-1 batan1" to="/login" role="button"><FiLogIn/> Login</Link>
                        <Link className="mx-1 batan1" to="/signup" role="button"><BiLockOpen size={19}/> Signup</Link>
                    </form> : <button onClick={handleLogout} className='mx-1 batan1'><FiLogOut size={19}/> LogOut</button>}


                </div>
            </div>
        </nav>
    )
}

export default Navbar
