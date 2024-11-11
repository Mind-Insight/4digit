import React from "react"
import '../../styles/basicUser/Header.css'

import logo from "../../images/logo_name.svg"

function Header() {
    return (
        <div className="Header">
            <img src={logo} className="Header_Logo" alt="Header_Logo" />
            <div className="Header_left">
            </div>
        </div>
    )
}

export default Header