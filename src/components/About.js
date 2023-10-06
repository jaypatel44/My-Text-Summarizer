import React from 'react'
// import { useHistory } from 'react-router-dom'
import bg from './Book_Shelf.jpg'
import { Link } from "react-router-dom";
import './About.css'
import Typewriter from "typewriter-effect";
import { FaHandPointRight } from 'react-icons/fa';
import summary from './summary.png'

const About = () => {
    return (
        <>
            <div className='w-100 main' style={{ "backgroundImage": `url(${bg})`, "opacity": "0.83", "backgroundRepeat": "no-repeat", "height": "500px", "backgroundPosition": "center", "backgroundSize": "cover", "width": "100%", }}>
                <div className='left' style={{ "opacity": "1", "width": "75%" }}>
                    <div className='heading'>
                        <h3>TextUtils TEXT ANALYSIS IN NEW AVATAR</h3>
                    </div>
                    <div className="App">
                        <Typewriter
                            options={{
                                strings: ['Summarize your Text...', 'Take Notes...!!'],
                                autoStart: true,
                                loop: true,
                            }}
                        />
                    </div>
                    <div className='services'>
                        <p style={{ "color": "white", "fontSize": "22px", "fontWeight": "600","marginTop":"30px","marginBottom":"0px" }}>Register account with Definedge Securities and get acces to the below features:</p>
                        <p style={{ "fontSize": "20px", "fontWeight": "400","marginTop":"0px","marginBottom":"0px" }}><FaHandPointRight />  Get Summary of your large texts</p>
                        <p style={{ "fontSize": "20px", "fontWeight": "400","marginTop":"0px","marginBottom":"0px" }}><FaHandPointRight />  Take unlimited notes and access 24 * 7</p>
                    </div>
                    <div style={{"marginTop":"30px"}}>
                        <Link to="/signup">
                        <button className='batan2' style={{"marginRight":"15px"}} >Know More</button>
                        </Link>
                        <Link to="/login">
                        <button className='batan3' >Continue with Login</button>
                        </Link>
                    </div>
                </div>

                <div className='right'>
                    <img src={summary} alt={'hello'}></img>
                </div>


            </div>
        </>
    )
}

export default About
