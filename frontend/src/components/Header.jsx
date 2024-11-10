import React from "react"
import './../styles/Header.css'

import logo from "./../images/logo.svg"
import theme from "./../images/moon.svg"
import profile from './../images/profile.png'
import arrow from './../images/arrow.svg'

function Header() {

    return (
        <div className="Header">
            <img src={logo} className="Header_Logo" alt="Header_Logo" />
            <div className="Header_right">
                <div className="Header_Theme">
                    <img className="Header_ThemeMoon" src={theme} alt="Theme" />
                </div>
                <div className="profile">
                    <img className="Header_ProfilePhoto" src={profile} alt="profile_photo" />
                    <img className="Header_Arrow" src={arrow} alt="down_click" />
                </div>
            </div>
        </div>
    )
}

export default Header